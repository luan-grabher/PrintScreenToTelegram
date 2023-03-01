import requests
from PIL import ImageGrab
import json

configFilePath = "config.json"
config = json.load(open(configFilePath))

apiToken = config["apiToken"]
chatID = config["chatID"]

botApi = f"https://api.telegram.org/bot{apiToken}/"

def sendMessageToTelegram(message):
    url = botApi + "sendMessage"
    data = {
        "chat_id": chatID,
        "text": message
    }
    response = requests.post(url, data=data)
    return response

def sendImageToTelegram(imagePath):
    url = botApi + "sendPhoto"
    files = {
        "photo": open(imagePath, "rb")
    }
    data = {
        "chat_id": chatID
    }
    response = requests.post(url, files=files, data=data)
    return response

def takeScreenshot():
    image = ImageGrab.grab()
    imagePath = "screenshot.png"
    image.save(imagePath)
    return imagePath

def main():
    imagePath = takeScreenshot()
    response = sendImageToTelegram(imagePath)
    print(response.text)

if __name__ == "__main__":
    error = True

    while error:
        try:
            main()
            error = False
        except Exception as e:
            print(e)
