import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "main:create_app",
        host="localhost",
    )
