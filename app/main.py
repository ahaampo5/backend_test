from fastapi import FastAPI
from app.representation.routers.user_router import router as user_router

app = FastAPI()

# 엔드포인트 등록
app.include_router(user_router)

# 예: uvicorn으로 실행할 수 있음
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)