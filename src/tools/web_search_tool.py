"""
    Web Search Tool following PydanticAI patterns
    """
    from dataclasses import dataclass
    from typing import List, Dict, Optional
    from pydantic_ai import RunContext, Tool, ModelRetry
    import httpx

    @dataclass
    class WebSearchDeps:
      brave_api_key: Optional[str] = None

    @Tool(retries=2)
    async def search_web(ctx: RunContext[WebSearchDeps], query: str) -> List[Dict[str, str]]:
      """
      Search the web using Brave Search API

      Args:
        ctx: Run context with API key
        query: Search query string

      Returns:
        List of search results with title, URL, and snippet
      """
      if ctx.deps.brave_api_key is None:
        # Fallback to dummy data
        return [{
          'title': 'Example Result',
          'url': 'https://example.com',
          'snippet': 'This is a dummy result'
        }]

      try:
        async with httpx.AsyncClient() as client:
          headers = {
            'Accept': 'application/json',
            'X-Subscription-Token': ctx.deps.brave_api_key
          }
          params = {'q': query}
          response = await client.get(
            'https://api.search.brave.com/res/v1/web/search',
            headers=headers,
            params=params
          )
          response.raise_for_status()
          data = response.json()
          
          if not data.get('web', {}).get('results'):
            raise ModelRetry("No search results found, please try different query")
          
          return [{
            'title': result.get('title', ''),
            'url': result.get('url', ''),
            'snippet': result.get('description', '')
          } for result in data.get('web', {}).get('results', [])]
      except Exception as e:
        return [{
          'title': 'Error',
          'url': '',
          'snippet': str(e)
        }]
