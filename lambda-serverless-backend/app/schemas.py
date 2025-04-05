from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    created_at: str

class FunctionCreate(BaseModel):
    name: str
    description: str
    route: str
    runtime: str
    timeout: int = 5000  # Default value
    memory: int = 128    # Default value
    is_active: bool = True  # Default value

    @validator("runtime")
    def check_runtime(cls, value):
        allowed_values = {"python", "javascript"}
        if value not in allowed_values:
            raise ValueError("Runtime must be 'python' or 'javascript'")
        return value