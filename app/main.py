from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import user, auth, test, expense, category, analytics
from app.dependencies.auth import get_current_user


app = FastAPI(title = "FinTrack API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now (we’ll restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(test.router, prefix="/test", tags=["Tests"])
app.include_router(expense.router, prefix="/expense", tags=["Expenses"])
app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])


# test routes
@app.get("/")
def root():
    return {"message": "FinTrack API is running"}


