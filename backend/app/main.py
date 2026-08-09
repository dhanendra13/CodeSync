from fastapi import FastAPI


app = FastAPI(
    title="CodeSync API",
    description="Backend API for the CodeSync LeetCode automation platform.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "codesync-api",
    }