"""
    Content Brief Manager Agent
    Creates detailed content briefs from research
    """
    from pydantic import BaseModel
    from pydantic_ai import Agent

    class ContentBrief(BaseModel):
      title: str
      target_audience: str
      key_messages: list[str]
      tone: str
      seo_keywords: list[str]

    content_brief_manager = Agent(
      'openai:gpt-4',
      result_type=ContentBrief,
      system_prompt='Create detailed content briefs from research data.'
    )
