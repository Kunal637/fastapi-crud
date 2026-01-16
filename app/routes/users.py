from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserSchema

router = APIRouter(prefix="/users", tags=["Users"])

# In-memory "database"
fake_users_db = {}
user_id_counter = 1

# Create User
@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate):
    global user_id_counter
    user_data = user.dict()
    user_data["id"] = user_id_counter
    fake_users_db[user_id_counter] = user_data
    user_id_counter += 1
    return user_data

# Read All Users
@router.get("/", response_model=list[UserSchema])
def get_users():
    return list(fake_users_db.values())

# Read Single User
@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int):
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update User
@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserCreate):
    existing_user = fake_users_db.get(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.update(user.dict())
    return existing_user

# Delete User
@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_users_db[user_id]
    return {"message": f"User {user_id} deleted successfully"}
