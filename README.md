# http-request-tool
Tool that can send HTTP REQUESTs simultaneously using docker\
도커를 사용해 여러 HTTP REQUEST를 동시에 보내는 툴

## 🔍 Usage

Follow these steps to use the tool:

1. Build a docker image.
```bash
docker build -t http_request_tool .
```
2. Execute the docker image.
```bash
docker run -e TARGET_URL="https://example.com" -e NUM_REQUESTS=10 http_request_tool
```


## 🔍 사용법

툴을 사용하기 위해 아래 단계를 따라주세요:

1. 도커 이미지 빌드하기
```bash
docker build -t http_request_tool .
```
2. 도커 이미지 실행하기
```bash
docker run -e TARGET_URL="https://example.com" -e NUM_REQUESTS=10 http_request_tool
```