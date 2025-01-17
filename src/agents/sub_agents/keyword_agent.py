"""
    Keyword Research Sub-Agent
    Handles keyword research and analysis
    """
    from pydantic import BaseModel
    from pydantic_ai import Agent

    class KeywordAnalysis(BaseModel):
      primary_keyword: str
      secondary_keywords: list[str]
      difficulty_score: float
      search_volume: int

    keyword_agent = Agent(
      'openai:gpt-4',
      result_type=KeywordAnalysis,
      system_prompt='Analyze and suggest keywords for content optimization.'
    )
