"""
    Centralized Logging Configuration
    """
    import logging
    from logging.handlers import RotatingFileHandler
    from src.config.production import settings

    def setup_logging():
        logging.basicConfig(
            level=settings.LOG_LEVEL,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                RotatingFileHandler(
                    "app.log",
                    maxBytes=10485760,  # 10MB
                    backupCount=5
                ),
                logging.StreamHandler()
            ]
        )

        # Configure third-party loggers
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("openai").setLevel(logging.INFO)
