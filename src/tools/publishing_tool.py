"""
    Content Publishing Tool following PydanticAI patterns
    """
    from dataclasses import dataclass
    from typing import Dict, Any
    from pydantic_ai import RunContext, Tool, ModelRetry
    import httpx

    @dataclass
    class PublishingDeps:
      wordpress_url: str
      wordpress_username: str
      wordpress_password: str

    @Tool(retries=2)
    async def publish_to_wordpress(ctx: RunContext[PublishingDeps], content: Dict[str, Any]) -> Dict[str, Any]:
      """
      Publish content to WordPress

      Args:
        ctx: Run context with WordPress credentials
        content: Content to publish, must include:
          - title: str
          - content: str
          - status: str
          - categories: List[int]

      Returns:
        Dictionary with operation status and post ID
      """
      try:
        auth = (ctx.deps.wordpress_username, ctx.deps.wordpress_password)
        endpoint = f"{ctx.deps.wordpress_url}/wp-json/wp/v2/posts"
        
        async with httpx.AsyncClient() as client:
          response = await client.post(endpoint, json=content, auth=auth)
          response.raise_for_status()
          
          if not response.json().get('id'):
            raise ModelRetry("Failed to publish content, no post ID returned")
          
          return {
            'status': 'success',
            'post_id': response.json().get('id')
          }
      except httpx.HTTPStatusError as e:
        return {
          'status': 'error',
          'error': f"HTTP error: {e.response.status_code}",
          'details': e.response.json()
        }
      except Exception as e:
        return {
          'status': 'error',
          'error': str(e)
        }
