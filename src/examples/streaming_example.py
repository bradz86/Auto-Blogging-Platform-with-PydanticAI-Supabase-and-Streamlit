"""
    Streaming Example Implementation
    """
    import asyncio
    from ..config.dependencies import AppDependencies
    from ..agents.director_agent import (
        create_content_streaming,
        create_content_structured_streaming
    )

    async def main():
        deps = AppDependencies(
            supabase_url='your-supabase-url',
            supabase_key='your-supabase-key',
            openai_api_key='your-openai-api-key'
        )

        # Text streaming example
        print("Starting text streaming example...")
        await create_content_streaming(
            deps,
            "Create content about AI in content creation"
        )

        # Structured streaming example
        print("\nStarting structured streaming example...")
        await create_content_structured_streaming(
            deps,
            "Create structured content about AI trends"
        )

        # Clean up resources
        await deps.close()

    if __name__ == "__main__":
        asyncio.run(main())
