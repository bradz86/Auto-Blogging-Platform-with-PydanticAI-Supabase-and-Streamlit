"""
    Supabase Tools with Dependency Injection
    """
    from typing import Dict, Any, Optional
    from pydantic_ai import RunContext, Tool, ModelRetry
    from ..config.dependencies import AppDependencies

    @Tool(retries=1)
    async def save_content(ctx: RunContext[AppDependencies], content: Dict[str, Any]) -> Dict[str, Any]:
        """
        Save content to Supabase database

        Args:
            ctx: Run context with dependencies
            content: Content to save, must include:
                - title: str
                - body: str
                - author_id: str
                - status: str

        Returns:
            Dictionary with operation status and content ID
        """
        try:
            client = ctx.deps.supabase_client
            result = client.table('content').insert(content).execute()
            if not result.data:
                raise ModelRetry("Failed to save content, no data returned")
            return {
                'status': 'success',
                'content_id': result.data[0]['id']
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e)
            }
