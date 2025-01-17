from dataclasses import dataclass
    from pydantic import BaseModel
    from pydantic_ai import Agent, RunContext
    from ..db import supabase_client

    @dataclass
    class DirectorDependencies:
      user_id: str
      db: supabase_client

    class BlogPlan(BaseModel):
      title: str
      outline: list[str]
      keywords: list[str]
      tone: str

    director_agent = Agent(
      'openai:gpt-4',
      deps_type=DirectorDependencies,
      result_type=BlogPlan,
      system_prompt='You are a content director. Create blog plans based on user input.'
    )

    @director_agent.tool
    async def get_user_preferences(ctx: RunContext[DirectorDependencies]) -> dict:
      """Get user preferences from database"""
      return await ctx.deps.db.table('preferences').select('*').eq('user_id', ctx.deps.user_id).single()
