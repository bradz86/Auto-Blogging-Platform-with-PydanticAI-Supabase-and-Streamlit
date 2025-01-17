from pydantic_ai import Agent
    from pydantic import BaseModel

    class DraftContent(BaseModel):
      title: str
      content: str
      seo_optimized: bool

    drafting_agent = Agent(
      'openai:gpt-4',
      result_type=DraftContent,
      system_prompt='You are a content writer. Create high-quality blog posts.'
    )

    class FinalContent(BaseModel):
      html_content: str
      metadata: dict

    finalizing_agent = Agent(
      'openai:gpt-4',
      result_type=FinalContent,
      system_prompt='You are an editor. Finalize content for publishing.'
    )
