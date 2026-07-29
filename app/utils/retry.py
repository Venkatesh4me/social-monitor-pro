from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_fixed

retry_request = retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(5)
)