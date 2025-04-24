from fastapi import FastAPI
from api import router

app = FastAPI(
    title="Email Classification API",
    description="Mask PII and Classify Email",
    version="1.0"
)

# Include API routes
app.include_router(router,prefix="/predict")
