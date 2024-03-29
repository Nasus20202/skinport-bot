# Skinport Bot

Simple bot for Skinport API, includes WEB UI (default port: 5000). It also supports Discord Webhooks.

Start as Python script:

```bash
python3 src/main.py
```

or a Docker container:

```bash
docker compose up
```

App will be available at port 5000 (http://localhost:5000/).

### Configuration

You can set the following environment variables:

```
WEBHOOK_URLS=https://discord.com/api/webhooks/...;https://discord.com/api/webhooks/...
MINIMUM_DISCOUNT=10
MIN_PRICE=0
MAX_PRICE=1000
CURRENCY=EUR
TAGS=Knifel;Pistol;Rifle
```

You can use a `.env` file, shell environment variables or `docker-compose.yml` file.

| Variable         | Description                                                                                                                               | Example                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| WEBHOOK_URLS     | Discord Webhook URLs separated by semicolon                                                                                               | https://discord.com/api/webhooks/...;https://discord.com/api/webhooks/... |
| MINIMUM_DISCOUNT | Minimum discount for items                                                                                                                | 10                                                                        |
| MIN_PRICE        | Minimum price for items                                                                                                                   | 0                                                                         |
| MAX_PRICE        | Maximum price for items                                                                                                                   | 1000                                                                      |
| CURRENCY         | Currency for items                                                                                                                        | EUR                                                                       |
| TAGS             | Tags for items, separated by semicolon, at least one tag must be matched for the sale to be approved, if empty all sales will be approved | Knifel;Pistol;Rifle                                                       |
