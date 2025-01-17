"""
    Test Cases for Result Handling
    """
    import pytest
    from ..models.results import ContentSuccess, ContentError
    from ..agents.director_agent import director_agent
    from ..config.dependencies import AppDependencies

    @pytest.mark.asyncio
    async def test_successful_result():
        test_deps = AppDependencies(
            supabase_url='test-url',
            supabase_key='test-key',
            openai_api_key='test-key'
        )

        with director_agent.override(deps=test_deps):
            result = await director_agent.run(
                "Create test content",
                deps=test_deps
            )

            assert isinstance(result.data, ContentSuccess)
            assert result.data.content_id is not None
            assert result.usage().total_tokens > 0

    @pytest.mark.asyncio
    async def test_error_result():
        test_deps = AppDependencies(
            supabase_url='test-url',
            supabase_key='test-key',
            openai_api_key='test-key'
        )

        with director_agent.override(deps=test_deps):
            result = await director_agent.run(
                "Create invalid content",
                deps=test_deps
            )

            assert isinstance(result.data, ContentError)
            assert result.data.error_code is not None
            assert result.data.error_message is not None
