# Testing Guidelines and Best Practices 🧪

    ## Table of Contents
    1. [Testing Agents](#testing-agents)
    2. [Database Testing](#database-testing)
    3. [API Error Handling](#api-error-handling)
    4. [Sample Test Structures](#sample-test-structures)
    5. [Best Practices](#best-practices)

    ## Testing Agents

    ### Isolated Agent Testing
    To test agents in isolation, use `agent.run_sync` with test data:

    ```python
    def test_director_agent():
        test_data = {
            "user_id": "test123",
            "topic": "AI in Healthcare",
            "keywords": ["AI", "healthcare"],
            "content_type": "blog",
            "publish": False
        }
        
        result = director_agent.run_sync(
            "Create test content",
            deps=test_data
        )
        
        assert result.data.status == "success"
        assert "content_id" in result.data
    ```

    ### Mocking Dependencies
    Use `unittest.mock` to mock dependencies:

    ```python
    from unittest.mock import AsyncMock, patch

    @patch('agents.director_agent.director_agent.run_sync')
    def test_director_agent_mock(mock_run):
        mock_run.return_value = AsyncMock(data={"status": "success"})
        
        result = director_agent.run_sync("test")
        assert result.data["status"] == "success"
    ```

    ## Database Testing

    ### Supabase Operations
    Test database operations by:
    1. Creating test records
    2. Verifying insertion
    3. Cleaning up

    ```python
    async def test_supabase_insert():
        test_data = {"title": "Test", "content": "Test content"}
        
        # Insert test data
        insert_result = await supabase_tools.save_content(test_data)
        assert insert_result["status"] == "success"
        
        # Verify insertion
        content_id = insert_result["content_id"]
        fetch_result = await supabase_tools.get_content(content_id)
        assert fetch_result["title"] == "Test"
        
        # Clean up
        await supabase_tools.delete_content(content_id)
    ```

    ### Mocking Database Calls
    Use `unittest.mock` to mock database operations:

    ```python
    @patch('tools.supabase_tools.save_content')
    async def test_save_content_mock(mock_save):
        mock_save.return_value = {"status": "success", "content_id": "test123"}
        
        result = await supabase_tools.save_content({})
        assert result["status"] == "success"
    ```

    ## API Error Handling

    ### Using ModelRetry
    Implement fallback logic with `ModelRetry`:

    ```python
    from pydantic_ai import ModelRetry

    @weather_agent.tool
    async def get_weather(ctx, lat, lng):
        try:
            response = await ctx.deps.client.get(weather_url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise ModelRetry(f"Weather API failed: {str(e)}")
    ```

    ### Testing Error Handling
    Test error scenarios:

    ```python
    @patch('tools.weather_tools.get_weather')
    async def test_weather_error(mock_weather):
        mock_weather.side_effect = Exception("API Error")
        
        with pytest.raises(ModelRetry):
            await weather_agent.run_sync("Get weather")
    ```

    ## Sample Test Structures

    ### Unit Test Example
    ```python
    import pytest
    from unittest.mock import AsyncMock, patch
    from agents.director_agent import director_agent

    class TestDirectorAgent:
        @pytest.mark.asyncio
        @patch('agents.director_agent.director_agent.run_sync')
        async def test_content_creation(self, mock_run):
            mock_run.return_value = AsyncMock(data={"status": "success"})
            
            result = await director_agent.run_sync("test")
            assert result.data["status"] == "success"
    ```

    ### Integration Test Example
    ```python
    @pytest.mark.integration
    async def test_full_workflow():
        test_data = {
            "user_id": "test123",
            "topic": "AI Testing",
            "keywords": ["testing", "AI"],
            "content_type": "article"
        }
        
        result = await director_agent.run_sync(
            "Create test content",
            deps=test_data
        )
        
        assert result.data.status == "success"
        assert result.data.content_id is not None
    ```

    ## Best Practices

    1. **Isolation**: Test each component in isolation
    2. **Mocking**: Use mocks for external dependencies
    3. **Error Scenarios**: Test all error cases
    4. **Data Cleanup**: Always clean up test data
    5. **CI Integration**: Add tests to CI pipeline
    6. **Test Coverage**: Aim for 80%+ coverage
    7. **Documentation**: Document test cases
    8. **Performance**: Include performance tests
    9. **Security**: Test for security vulnerabilities
    10. **Maintenance**: Regularly update tests

    ## Running Tests

    ### Unit Tests
    ```bash
    pytest tests/unit -v
    ```

    ### Integration Tests
    ```bash
    pytest tests/integration -v
    ```

    ### Coverage Report
    ```bash
    pytest --cov=src --cov-report=html
    ```

    ## Troubleshooting

    - **Database Issues**: Ensure test database is separate
    - **API Limits**: Use mocks for rate-limited APIs
    - **Flaky Tests**: Use retries for intermittent failures
    - **Environment**: Keep test environment consistent

    ---

    Made with ❤️ by Quality Assurance Team
