
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kidcarematch_backend.api.v1.admin import router as admin_router
from kidcarematch_backend.api.v1.centres import router as centres_router
from kidcarematch_backend.api.v1.profile import router as profile_router
from kidcarematch_backend.api.v1.reviews import router as reviews_router
from kidcarematch_backend.api.v1.users import router as users_router
from kidcarematch_backend.api.v1.watchlist import router as watchlist_router

app = FastAPI()

# Allow the React frontend to communicate with the backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://kidscare-match-sg.web.app",
        "https://kidscare-match-sg.firebaseapp.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(centres_router)
app.include_router(reviews_router)
app.include_router(watchlist_router)
app.include_router(profile_router)
app.include_router(admin_router, prefix="/api/v1/admin")


@app.get("/")
def read_root():
    return {"Hello": "World"}
