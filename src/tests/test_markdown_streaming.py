"""
    Test Cases for Markdown Streaming
    """
    import pytest
    from unittest.mock import AsyncMock, patch
    from ..examples.markdown_streaming import stream_markdown_response

    @pytest.mark.asyncio
    async def test_markdown_streaming():
        mock_console = AsyncMock()
        mock_agent = AsyncMock()

        # Mock the stream response
        mock_stream = AsyncMock()
        mock_stream.stream.return_value = [
            "```python\n# Example code\n```",
            "Some **markdown** text"
        ]
        mock_stream.usage.return_value = {'tokens': 100}

        with patch('pydantic_ai.Agent', return_value=mock_agent):
            mock_agent.run_stream.return_value = mock_stream

            await stream_markdown_response(
                "Test prompt",
                "openai:gpt-4o",
                mock_console
            )

            # Verify the stream was processed
            mock_console.log.assert_called_with({'tokens': 100})
