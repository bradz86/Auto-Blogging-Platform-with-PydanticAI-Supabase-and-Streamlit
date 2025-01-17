"""
    Content Writer Sub-Agent
    Generates draft content based on briefs
    """
    from pydantic import BaseModel
    from pydantic_ai import Agent

    class DraftContent(BaseModel):
      title: str
      introduction: str
      body: list[str]
      conclusion: str

    content_writer = Agent(
      'openai:gpt-4',
      result_type=DraftContent,
      system_prompt='Write high-quality blog content based on provided briefs.'
    )
