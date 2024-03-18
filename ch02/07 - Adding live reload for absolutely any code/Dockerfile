# "slim" 버전은 다른 경량의 파이썬 기반 이미지들을
# 시작하기 위한 좋은 지점이다.
FROM python:3.9-slim
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY echo.py .
CMD ["python", "echo.py"]
