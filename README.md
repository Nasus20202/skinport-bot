# Skinport Bot
Simple bot for Skinport API, includes WEB UI (default port: 5000). It also supports Discord Webhooks. 

Start with:
```bash
python3 main.py
```

### Configuration

Place your Discord Webhook URLs in `.env` file or set it as environment variable:
```
WEBHOOK_URLS=https://discord.com/api/webhooks/...;https://discord.com/api/webhooks/...
```
You can add more than one URL, separate them with `;`.

In `config.py` file, you can set the following variables:
- currency
- min_price (minimum price for items)
- max_price (maximum price for items)
- tags (list of tags to search for, at least one tag is required on sale to be notified, if empty, all items will be notified)
- history_size (size of history of items)