"""
    Research Manager Agent
    Handles high-level research tasks and coordinates sub-agents
    """
    from dataclasses import dataclass
    from pydantic import BaseModel
    from pydantic_ai import Agent, RunContext
    from ..tools.web_search import search_web

    @dataclass
    class ResearchDependencies:
      topic: str
      user_id: str

    class ResearchPlan(BaseModel):
      sources: list[str]
      key_points: list[str]
      competitor_analysis: str

    research_manager = Agent(
      'openai:gpt-4',
      deps_type=ResearchDependencies,
      result_type=ResearchPlan,
      system_prompt='You are a research manager. Analyze topics and competitors.'
    )

    @research_manager.tool
    async def find_relevant_sources(ctx: RunContext[ResearchDependencies]) -> list[str]:
      """Find relevant sources for research"""
      return await search_web(ctx.deps.topic)
