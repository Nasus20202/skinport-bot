import skinport
import os
from dotenv import load_dotenv

load_dotenv()

currency = skinport.Currency[os.getenv("CURRENCY", "EUR").lower()]

minimum_discount = int(os.getenv("MINIMUM_DISCOUNT", "0"))
min_price = int(os.getenv("MIN_PRICE", "0"))
max_price = int(os.getenv("MAX_PRICE", "1000000"))

tags = [x for x in os.getenv("TAGS", "").split(";") if x]
discord_webhook_urls = [x for x in os.getenv("WEBHOOK_URLS", "").split(";") if x]
history_size = int(os.getenv("HISTORY_SIZE", "1000"))