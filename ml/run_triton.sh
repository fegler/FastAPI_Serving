#!/bin/bash
docker run --gpus all --rm -d -it \
  --name triton_layoutlmv3 \
  -p 8000:8000 \
  -p 8001:8001 \
  -p 8002:8002 \
  -v $(pwd)/model_repository:/models \
  nvcr.io/nvidia/tritonserver:24.06-py3 \
  tritonserver \
  --model-repository=/models \
  --strict-model-config=false \
  --log-verbose=1 \
  --allow-http=true \
  --allow-grpc=true \
  --allow-metrics=true