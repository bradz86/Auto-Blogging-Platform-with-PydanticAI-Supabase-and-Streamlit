from dataclasses import dataclass
    from pydantic import BaseModel
    from pydantic_ai import Agent, RunContext
    from ..db import supabase_client

    @dataclass
    class ManagerDependencies:
      blog_plan: dict
      db: supabase_client

    class ResearchReport(BaseModel):
      sources: list[str]
      key_points: list[str]
      competitor_analysis: str

    research_agent = Agent(
      'openai:gpt-4',
      deps_type=ManagerDependencies,
      result_type=ResearchReport,
      system_prompt='You are a research manager. Analyze topics and competitors.'
    )

    @research_agent.tool
    async def search_web(ctx: RunContext[ManagerDependencies], query: str) -> list[str]:
      """Search the web for relevant information"""
      # Implement web search logic
      return []
