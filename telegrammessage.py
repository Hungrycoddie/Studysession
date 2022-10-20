import requests

def send_message(message):
    """
    send message to telegram
    """
    url = "https://api.telegram.org/bot<token>/sendMessage"
    data = {
        "chat_id": "<chat_id>",
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()

if __name__ == "__main__":
    send_message("Hello World")