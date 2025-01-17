"""
    Content Writer Agent
    Finalizes and polishes content drafts
    """
    from typing import List, Optional
    from pydantic import BaseModel, Field
    from pydantic_ai import Agent, RunContext

    class SEOData(BaseModel):
        meta_title: str = Field(description="SEO title")
        meta_description: str = Field(description="SEO description")
        focus_keywords: List[str] = Field(description="Target keywords")

    class FinalContent(BaseModel):
        title: str = Field(description="Final title")
        content: str = Field(description="Final content in markdown")
        seo: SEOData = Field(description="SEO metadata")
        references: List[str] = Field(description="List of references")

    content_writer = Agent(
        'openai:gpt-4o',
        result_type=FinalContent,
        system_prompt=(
            "You are the Content Writer. Finalize and polish content drafts. "
            "Add SEO enhancements, proper formatting, and references. "
            "Ensure the content is ready for publication."
        )
    )

    @content_writer.tool
    async def validate_content(
        ctx: RunContext[None],
        content: str
    ) -> Optional[str]:
        """
        Validate content structure and quality

        Args:
            ctx: Run context
            content: Content to validate

        Returns:
            Validation errors or None if valid
        """
        # Implementation for content validation
        # Could check for:
        # - Proper heading structure
        # - SEO requirements
        # - Readability metrics
        return None

    # Example of streaming implementation (commented out)
    # async def stream_final_content(content: str):
    #     """
    #     Stream final content with incremental validation
    #     """
    #     async with content_writer.run_stream("Finalize content") as result:
    #         async for chunk in result.stream_text():
    #             # Validate each chunk
    #             errors = await validate_content(None, chunk)
    #             if errors:
    #                 raise ModelRetry(f"Content validation failed: {errors}")
    #             yield chunk
