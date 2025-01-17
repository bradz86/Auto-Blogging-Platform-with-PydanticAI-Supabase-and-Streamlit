"""
    OpenAI Configuration Module
    Follows PydanticAI's OpenAI documentation
    """
    from pydantic_ai.models.openai import OpenAIModel
    from openai import AsyncOpenAI

    def create_openai_model(api_key: str, model_name: str = 'gpt-4o') -> OpenAIModel:
        """
        Create OpenAI model with proper configuration

        Args:
            api_key: OpenAI API key
            model_name: Model name (default: 'gpt-4o')

        Returns:
            Configured OpenAIModel instance
        """
        return OpenAIModel(
            model_name,
            api_key=api_key,
            openai_client=AsyncOpenAI(api_key=api_key)
        )
