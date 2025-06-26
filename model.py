from pydantic import BaseModel, EmailStr, Field, validator

class UserRegistration(BaseModel):
    name: str = Field(..., min_length=1, description="Name must be provided")
    email_id: EmailStr = Field(..., description="Enter a valid email ID")
    age: int = Field(..., ge=16, le=60, description="This age is not suitable for any event")
    event: str = Field(..., min_length=1, description="Event must be provided")

    @validator("name")
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        return value

    @validator("event")
    def validate_event(cls, value):
        if not value.strip():
            raise ValueError("Event name can't be empty")
        return value