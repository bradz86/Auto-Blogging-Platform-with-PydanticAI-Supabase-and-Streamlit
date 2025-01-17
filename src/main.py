"""
    Main Application Entry Point
    """
    import uvicorn
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from src.config.production import settings
    from src.middleware.security import JWTBearer
    from src.utils.rate_limiter import limiter, rate_limit_exceeded_handler
    from src.monitoring.logging import setup_logging
    from src.interfaces.streamlit_app import create_ui

    # Initialize logging
    setup_logging()

    # Create FastAPI app
    app = FastAPI(
        title="Content Creation System",
        description="AI-powered content creation platform",
        version="1.0.0",
        docs_url="/docs",
        redoc_url=None
    )

    # Add middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add rate limiting
    app.state.limiter = limiter
    app.add_exception_handler(429, rate_limit_exceeded_handler)

    # Include routers
    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    # Run Streamlit app
    if __name__ == "__main__":
        # Start FastAPI server
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            log_level=settings.LOG_LEVEL.lower(),
            reload=settings.DEBUG
        )
        
        # Start Streamlit UI
        create_ui()
