"""
    Test Director Agent with Dependency Override
    """
    from dataclasses import dataclass
    from ..config.dependencies import AppDependencies
    from ..agents.director_agent import director_agent, ContentRequest

    @dataclass
    class TestDependencies(AppDependencies):
        """
        Test dependencies with overridden behavior
        """
        def __post_init__(self):
            # Override Supabase client behavior for testing
            self._supabase_client = None

        @property
        def supabase_client(self):
            class MockSupabase:
                def table(self, *args, **kwargs):
                    class MockTable:
                        def insert(self, *args, **kwargs):
                            class MockResult:
                                data = [{'id': 'test-id'}]
                            return MockResult()
                    return MockTable()
            return MockSupabase()

    async def test_director_agent():
        test_deps = TestDependencies(
            supabase_url='test-url',
            supabase_key='test-key',
            openai_api_key='test-key'
        )

        with director_agent.override(deps=test_deps):
            result = await director_agent.run(
                "Create test content",
                deps=test_deps,
                request=ContentRequest(
                    user_id='test-user',
                    topic='Test Topic',
                    keywords=['test'],
                    publish=False
                )
            )

            assert result.data.status == 'success'
            assert result.data.content_id == 'test-id'
