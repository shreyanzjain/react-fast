from ticker import app, routes, models
from ticker.database import engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

origins = [
        "http://localhost:3000",  # React app address
        # "http://localhost:8000",  # Uncomment this if testing FastAPI's docs
        # "http://localhost:8080",  # Uncomment this if testing Swagger UI
    ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)