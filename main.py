from fastapi import FastAPI

from routers import sector_routers, user_routers

app = FastAPI()

app.include_router(user_routers.router, tags=["users"])
app.include_router(sector_routers.router, tags=['sectors'])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
