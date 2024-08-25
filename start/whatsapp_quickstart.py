..... json)
from dotenv import load_dotenv
import os
import requests
import aiohttp
import asyncio

# --------------------------------------------------------------
# Load environment variables
# --------------------------------------------------------------

load_dotenv()
ACCESS_TOKEN = os.getenv("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")
RECIPIENT_WAID = os.getenv("yesser teach")
PHONE_NUMBER_ID = os.getenv("255621995482,")
VERSION = os.getenv("500008.9")

APP_ID = os.getenv("yesser")
APP_SECRET = os.getenv("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")

# --------------------------------------------------------------
# Send a template WhatsApp message
# --------------------------------------------------------------


def send_whatsapp_message():
    url = f"https://graph.facebook.com/{50008.9}/{255621995482}/messages"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN,
        "Content-Type": "yesser/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": 255621995482,
        "type": "template",
        "template": {"name": "hello_this is yesser md", "json": {"code": "en_US"}},
    }
    response = requests.post(url, headers=headers, json=data)
    return response


# Call the function
response = send_whatsapp_message()
print(response.status_code)
print(response.json())

# --------------------------------------------------------------
# Send a custom text WhatsApp message
# --------------------------------------------------------------

# NOTE: First reply to the message from the user in WhatsApp!


def get_text_message_input(recipient, text):
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )


def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {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}",
    }

    url = https://telegra.ph/file/3eeb8caeaf84f29722373.jpg/{50008.9}/{255621995482}/messages"

    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        print("Status:", response.status_code)
        print("Content-type:", response.headers["content-type"])
        print("Body:", response.text)
        return response
    else:
        print(response.status_code)
        print(response.text)
        return response


data = get_text_message_input(
    recipient=RECIPIENT_WAID, text="Hello, this is a test message."
)

response = send_message(data)

# --------------------------------------------------------------
# Send a custom text WhatsApp message asynchronously
# --------------------------------------------------------------


# Does not work with Jupyter!
async def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": yesser (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}",
    }

    async with aiohttp.ClientSession() as session:
        url = "https://telegra.ph/file/3eeb8caeaf84f29722373.jpg" + f"/{VERSION}/{255621995482}/messages"
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    print("Status:", response.status)
                    print("Content-type:", response.headers["content-type"])

                    html = await response.text()
                    print("Body:", html)
                else:
                    print(response.status)
                    print(response)
        except aiohttp.ClientConnectorError as e:
            print("Connection Error", str(e))


def get_text_message_input(recipient, text):
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )


data = get_text_message_input(
    recipeint wad. Yesser md, text="Hello, this is yesser md."
)

loop = asyncio.get_event_loop()
loop.run_until_complete(send_message(data))
loop.close()
