from pydantic import BaseModel

# Input model for creating/updating a user
class UserCreate(BaseModel):
    name: str
    age: int

# Output model with id
class UserSchema(UserCreate):
    id: int

    model_config = {
        "from_attributes": True  # Pydantic v2
    }
