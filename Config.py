import os


class Config:
    API_ID = int(os.environ.get("API_ID", 1095886)  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", (f8bd562b2e0d5de5b55b294ed4405566))  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", (1811559815:AAFGyDSbOK5qi2beZHtlKEE33COLeGuMi8U))  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 830872779)  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", (Mugen Rao))  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
