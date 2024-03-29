import datetime
import skinport
import aiohttp
import discord

import config
from bargain import Bargain

client = skinport.Client()
client.bargains = []


async def get_item_from_sales_history(market_hash_name: str) -> skinport.ItemWithSales:
    sales_history = await client.get_sales_history(currency=config.currency)
    return next(
        item for item in sales_history if item.market_hash_name == market_hash_name
    )


@client.listen("saleFeed")
async def on_sale_feed(data):
    embeds = []
    sale_feed = skinport.SaleFeed(data=data)

    if sale_feed.event_type == "sold":  # skip if sold
        return

    for sale in sale_feed.sales:
        if sale.sale_price < config.min_price or sale.sale_price > config.max_price:
            continue

        if config.tags and not any(tag in sale.tags for tag in config.tags):
            continue

        item = await get_item_from_sales_history(sale.market_hash_name)
        if item is None:
            continue

        discount = (sale.suggested_price - sale.sale_price) / sale.suggested_price * 100
        if discount < config.minimum_discount:
            continue

        print(
            f"Found item: {sale.market_hash_name} ({sale.sale_price} {config.currency})"
        )

        bargain = Bargain(
            market_name=item.market_hash_name,
            name=sale.name,
            url=sale.url,
            image=sale.image,
            rarity_color=int(sale.rarity_color),
            wear=sale.wear,
            exterior=sale.exterior,
            lock=sale.lock if sale._lock else None,
            price=sale.sale_price,
            suggested_price=sale.suggested_price,
            discount=discount,
            last_7_days=item.last_7_days,
            last_30_days=item.last_30_days,
            last_90_days=item.last_90_days,
        )

        client.bargains.insert(0, bargain)
        client.bargains = client.bargains[: config.history_size]

        embeds.append(create_embed(bargain))

    if not embeds:
        return

    async with aiohttp.ClientSession() as session:
        for webhook_url in config.discord_webhook_urls:
            webhook = discord.Webhook.from_url(webhook_url, session=session)
            for embed in embeds:
                await webhook.send(embed=embed)


def start():
    print(
        f"Starting... (currency: {config.currency}, tags: {config.tags}, min price: {config.min_price}, max price: {config.max_price}, min discount: {config.minimum_discount}%)"
    )
    client.run(currency=config.currency)


def get_bargains():
    return client.bargains


def create_embed(bargain: Bargain):
    return (
        discord.Embed(title=bargain.market_name, color=bargain.rarity_color)
        .add_field(name="Link", value=f"[{bargain.name}]({bargain.url})")
        .add_field(name="Wear", value=bargain.get_wear_str())
        .add_field(name="Lock", value=bargain.get_lock_str())
        .add_field(name="Price", value=f"{bargain.price} {config.currency}")
        .add_field(
            name="Suggested price",
            value=f"{bargain.suggested_price} {config.currency}",
        )
        .add_field(name="Discount", value=f"-{bargain.discount:.1f}%")
        .add_field(
            name="7d",
            value=bargain.get_7d_str(),
        )
        .add_field(
            name="30d",
            value=bargain.get_30d_str(),
        )
        .add_field(
            name="90d",
            value=bargain.get_90d_str(),
        )
        .set_thumbnail(url=bargain.image)
    )
