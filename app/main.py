from fastapi import FastAPI, Depends

from app.api.routes import user, auth, test
from app.dependencies.auth import get_current_user

app = FastAPI(title = "FinTrack API")

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(test.router, prefix="/test", tags=["Tests"])


# test routes
@app.get("/")
def root():
    return {"message": "FinTrack API is running"}


