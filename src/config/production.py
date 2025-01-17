"""
    Production Configuration
    """
    import os
    from dotenv import load_dotenv
    from pydantic import BaseSettings

    # Load environment variables
    load_dotenv()

    class Settings(BaseSettings):
        # Application settings
        ENV: str = "production"
        DEBUG: bool = False
        LOG_LEVEL: str = "INFO"
        
        # Supabase configuration
        SUPABASE_URL: str
        SUPABASE_KEY: str
        
        # OpenAI configuration
        OPENAI_API_KEY: str
        
        # Rate limiting
        RATE_LIMIT: int = 100  # Requests per minute
        
        # Security
        SECRET_KEY: str = os.urandom(32).hex()
        CORS_ORIGINS: list = ["https://yourdomain.com"]
        
        class Config:
            env_file = ".env"
            case_sensitive = True

    settings = Settings()
