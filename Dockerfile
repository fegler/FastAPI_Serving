FROM ubuntu:22.04

# 기본 패키지 설치
RUN apt-get update && apt-get install -y \
    python3.10 python3-pip \
    libgl1-mesa-glx libglib2.0-0 \
    git wget curl && \
    rm -rf /var/lib/apt/lists/*

# 파이썬 기본 설정
RUN ln -s /usr/bin/python3.10 /usr/bin/python
RUN python -m pip install --upgrade pip

# Paddle 및 기타 의존성 설치
RUN pip install paddlepaddle==2.5.2 -i https://mirror.baidu.com/pypi/simple
RUN pip install paddleocr transformers fastapi uvicorn python-multipart torchvision

# 작업 디렉토리 설정
WORKDIR /app
COPY . /app

# FastAPI 실행
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]