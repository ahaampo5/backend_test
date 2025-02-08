FROM python:3.9

# 작업 디렉터리 생성
WORKDIR /app

# requirements.txt 복사 후 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 실제 코드 복사
COPY . .

# FastAPI + Uvicorn 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]