from fastapi import FastAPI

from routers import sector_routers, type_routers, user_routers

app = FastAPI()

app.include_router(user_routers.router, tags=["Users"])
app.include_router(sector_routers.router, tags=['Sectors'])
app.include_router(type_routers.router, tags=["Type"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
