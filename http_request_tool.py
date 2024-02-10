# http_request_tool.py
import os
import requests
import concurrent.futures


# HTTP 요청을 보낼 함수
def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from {url}: {response.status_code}")
    except Exception as e:
        print(f"Failed to send request to {url}: {str(e)}")


# 한 URL에 대해 N 개의 HTTP 요청을 동시에 보내는 함수
def send_multiple_requests(url, num_requests):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda _: send_request(url), range(num_requests))


def main():
    # Set the number of concurrent requests (N)
    num_requests_str = os.getenv("NUM_REQUESTS")
    if not num_requests_str:
        print("NUM_REQUESTS environment variable is not set.")
        return
    num_requests = int(num_requests_str)

    # Set the target URL
    target_url = os.getenv("TARGET_URL")
    if not target_url:
        print("TARGET_URL environment variable is not set.")
        return

    # HTTP 요청 보내기
    send_multiple_requests(target_url, num_requests)


if __name__ == "__main__":
    main()
