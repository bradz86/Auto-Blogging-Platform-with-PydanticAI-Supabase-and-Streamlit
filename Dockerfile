"""
    Production Dockerfile
    """
    FROM python:3.9-slim

    WORKDIR /app

    # Install system dependencies
    RUN apt-get update && apt-get install -y \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

    # Install Python dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy application code
    COPY . .

    # Environment variables
    ENV PYTHONUNBUFFERED=1
    ENV PYTHONPATH=/app

    # Expose ports
    EXPOSE 8000
    EXPOSE 8501

    # Health check
    HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
        CMD curl -f http://localhost:8000/health || exit 1

    # Run application
    CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port 8000 & streamlit run src/interfaces/streamlit_app.py"]
