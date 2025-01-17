"""
    Markdown Streaming Example
    Follows PydanticAI's documentation for streaming markdown
    """
    import asyncio
    import os
    from typing import List, Tuple

    import logfire
    from rich.console import Console, ConsoleOptions, RenderResult
    from rich.live import Live
    from rich.markdown import CodeBlock, Markdown
    from rich.syntax import Syntax
    from rich.text import Text

    from pydantic_ai import Agent
    from pydantic_ai.models import KnownModelName

    # Configure logfire
    logfire.configure(send_to_logfire='if-token-present')

    # Initialize agent
    markdown_agent = Agent()

    # Supported models and their required environment variables
    MODELS: List[Tuple[KnownModelName, str]] = [
        ('google-gla:gemini-1.5-flash', 'GEMINI_API_KEY'),
        ('openai:gpt-4o', 'OPENAI_API_KEY'),
        ('groq:llama-3.1-70b-versatile', 'GROQ_API_KEY'),
    ]

    class SimpleCodeBlock(CodeBlock):
        """
        Custom code block renderer for better markdown display
        """
        def __rich_console__(
            self, console: Console, options: ConsoleOptions
        ) -> RenderResult:
            code = str(self.text).rstrip()
            yield Text(self.lexer_name, style='dim')
            yield Syntax(
                code,
                self.lexer_name,
                theme='monokai',
                background_color='default',
                word_wrap=True,
            )
            yield Text(f'/{self.lexer_name}', style='dim')

    def prettier_code_blocks():
        """
        Configure rich to use our custom code block renderer
        """
        Markdown.elements['fence'] = SimpleCodeBlock

    async def stream_markdown_response(prompt: str, model: KnownModelName, console: Console):
        """
        Stream markdown response from the agent

        Args:
            prompt: The prompt to send to the agent
            model: The model to use
            console: Rich console for output
        """
        with Live('', console=console, vertical_overflow='visible') as live:
            async with markdown_agent.run_stream(prompt, model=model) as result:
                async for message in result.stream():
                    live.update(Markdown(message))
                console.log(result.usage())

    async def main():
        """
        Main function to demonstrate markdown streaming
        """
        prettier_code_blocks()
        console = Console()
        prompt = 'Show me a short example of using Pydantic with FastAPI.'

        console.log(f'Asking: {prompt}...', style='cyan')

        for model, env_var in MODELS:
            if env_var in os.environ:
                console.log(f'Using model: {model}')
                await stream_markdown_response(prompt, model, console)
            else:
                console.log(f'{model} requires {env_var} to be set.', style='yellow')

    if __name__ == '__main__':
        asyncio.run(main())
