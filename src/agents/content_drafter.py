"""
    Content Drafter Agent
    Creates initial drafts from content briefs
    """
    from typing import List
    from pydantic import BaseModel, Field
    from pydantic_ai import Agent, RunContext

    class DraftSection(BaseModel):
        heading: str = Field(description="Section heading")
        content: str = Field(description="Draft content")
        placeholders: List[str] = Field(description="Missing information")

    class ContentDraft(BaseModel):
        title: str = Field(description="Draft title")
        introduction: str = Field(description="Opening paragraph")
        sections: List[DraftSection] = Field(description="Draft sections")
        conclusion: str = Field(description="Closing paragraph")

    content_drafter = Agent(
        'openai:gpt-4o',
        result_type=ContentDraft,
        system_prompt=(
            "You are the Content Drafter. Create initial drafts based on content briefs. "
            "Use markdown formatting and clearly mark any placeholders for missing information."
        )
    )

    @content_drafter.tool
    async def format_section(
        ctx: RunContext[None],
        section: DraftSection
    ) -> str:
        """
        Format a draft section with proper markdown

        Args:
            ctx: Run context
            section: Section to format

        Returns:
            Formatted markdown content
        """
        formatted = f"## {section.heading}\n\n{section.content}\n"
        if section.placeholders:
            formatted += "\n**Placeholders:**\n"
            formatted += "\n".join(f"- {ph}" for ph in section.placeholders)
        return formatted
