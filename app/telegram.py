import httpx
from app.config import BOT_TOKEN, CHAT_ID
from app.logger import log

API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_message(text: str):

    try:

        with httpx.Client(timeout=30) as client:

            response = client.post(
                API,
                data={
                    "chat_id": CHAT_ID,
                    "text": text,
                    "parse_mode": "HTML",
                    "disable_web_page_preview": True
                }
            )

        response.raise_for_status()

        log.success("Telegram message sent")

        return True

    except Exception as e:

        log.error(f"Telegram Error: {e}")

        return False