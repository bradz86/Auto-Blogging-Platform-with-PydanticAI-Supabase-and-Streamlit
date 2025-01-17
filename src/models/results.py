"""
    Result Models and Validation
    Follows PydanticAI's results documentation
    """
    from typing import Union, Optional
    from pydantic import BaseModel, Field, ValidationError
    from datetime import datetime

    class ContentSuccess(BaseModel):
        content_id: str = Field(description="ID of the created content")
        content_url: Optional[str] = Field(None, description="URL of published content")
        created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")

    class ContentError(BaseModel):
        error_code: str = Field(description="Error code")
        error_message: str = Field(description="Detailed error message")
        retryable: bool = Field(False, description="Whether the operation can be retried")

    ContentResult = Union[ContentSuccess, ContentError]

    class StreamedContentProfile(TypedDict, total=False):
        title: str
        status: str
        progress: float
        warnings: list[str]
