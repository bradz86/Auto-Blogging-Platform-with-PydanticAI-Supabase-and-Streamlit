"""
    Dependency Configuration Module
    Follows PydanticAI's dependency injection documentation
    """
    from dataclasses import dataclass
    import httpx
    from supabase import create_client

    @dataclass
    class AppDependencies:
        """
        Main application dependencies container
        """
        supabase_url: str
        supabase_key: str
        openai_api_key: str
        wordpress_url: Optional[str] = None
        wordpress_username: Optional[str] = None
        wordpress_password: Optional[str] = None
        http_client: httpx.AsyncClient = httpx.AsyncClient()

        @property
        def supabase_client(self):
            """Lazy initialization of Supabase client"""
            return create_client(self.supabase_url, self.supabase_key)

        async def close(self):
            """Clean up resources"""
            await self.http_client.aclose()
