import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "22451456"))
    API_HASH = os.environ.get("API_HASH", "1f271f22b947cdfa712a9e37afe34223")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5749450997:AAHicjMZNtFaK_p6iyont5Rfhv-Ph8hMe8Q")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKYBux-PZ9LSiHjSu8bnTEyqUMUBXjECyQQZJNDxR4Lwfucg4m4kwykWPy_z6IN8ghe034mSvfoOVcJ0E3qR8yorXwfU0w96Rjd9RgBTiVRbvEoNTYbYaIvvHI2GXVFvlbqd2PM27eOinbCxZU0r-badRsUhuI005AwU6K4N8OMzvJg-H4vtl3l1U9E755dwTmxHrOjufpXS1gC60CDZLEHEjkl9Vrm9APCkE2L77Zg-HBg9gSiiSoHXu15N-TRZzq8d4rhdgdKipJUzJwnFkAv5Z-fiMp6_vetmCjSJ9sMDFdZbM0EbNy2A6dYW20SUjNhqQAvLerw6-pWGDitDumfRALc=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
