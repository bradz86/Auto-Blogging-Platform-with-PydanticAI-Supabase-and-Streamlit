"""
    Director Agent with Proper Result Handling
    """
    from typing import Union
    from pydantic_ai import Agent, RunContext, ModelRetry
    from ..models.results import ContentResult, ContentSuccess, ContentError
    from ..config.dependencies import AppDependencies

    # Initialize Director Agent with Union result type
    director_agent: Agent[AppDependencies, ContentResult] = Agent(
        'openai:gpt-4o',
        deps_type=AppDependencies,
        result_type=ContentResult,  # type: ignore
        system_prompt=(
            "You are an expert SEO Director AI agent. Your role is to orchestrate the "
            "entire content creation workflow, from research to publication."
        )
    )

    @director_agent.result_validator
    async def validate_content_result(
        ctx: RunContext[AppDependencies], 
        result: ContentResult
    ) -> ContentResult:
        """
        Validate content creation result

        Args:
            ctx: Run context with dependencies
            result: Content creation result to validate

        Returns:
            Validated content result
        """
        if isinstance(result, ContentError):
            if result.retryable:
                raise ModelRetry(result.error_message)
            return result

        # Additional validation for successful results
        if not result.content_id:
            return ContentError(
                error_code="INVALID_RESULT",
                error_message="Missing content ID",
                retryable=True
            )

        return result

    async def create_content_streaming(deps: AppDependencies, prompt: str):
        """
        Example of streaming content creation
        """
        async with director_agent.run_stream(prompt, deps=deps) as result:
            async for message in result.stream_text():
                print(f"Streaming update: {message}")

            final_result = await result.get_data()
            print(f"Final result: {final_result}")

    async def create_content_structured_streaming(deps: AppDependencies, prompt: str):
        """
        Example of structured streaming content creation
        """
        async with director_agent.run_stream(prompt, deps=deps) as result:
            async for profile, last in result.stream_structured(debounce_by=0.01):
                try:
                    validated = await result.validate_structured_result(
                        profile,
                        allow_partial=not last
                    )
                    print(f"Partial result: {validated}")
                except ValidationError:
                    continue

            final_result = await result.get_data()
            print(f"Final structured result: {final_result}")
