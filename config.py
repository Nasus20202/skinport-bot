import skinport
import os
from dotenv import load_dotenv

load_dotenv()

currency = skinport.Currency.pln
minimum_discount = 10
min_price = 0
max_price = 1000
tags = ["Knife"]
discord_webhook_urls = os.getenv("WEBHOOK_URLS", "").split(";")
history_size = 1000
