"""
    Content Brief Manager Agent
    Creates structured content briefs from research data
    """
    from typing import List
    from pydantic import BaseModel, Field
    from pydantic_ai import Agent

    class ContentSection(BaseModel):
        title: str = Field(description="Section title")
        key_points: List[str] = Field(description="Main points to cover")
        tone: str = Field("neutral", description="Desired tone for section")

    class ContentBrief(BaseModel):
        title: str = Field(description="Content title")
        target_audience: str = Field(description="Intended audience")
        sections: List[ContentSection] = Field(description="Content structure")
        seo_keywords: List[str] = Field(description="Target keywords")

    content_brief_manager = Agent(
        'openai:gpt-4o',
        result_type=ContentBrief,
        system_prompt=(
            "You are the Content Brief Manager. Create detailed content briefs "
            "based on research data and content type. Ensure the brief includes "
            "clear structure, target audience, and SEO considerations."
        )
    )
