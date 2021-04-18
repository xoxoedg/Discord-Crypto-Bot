import discord
from binance_prices import get_bid_price
from Mapping import commands


client = discord.Client()

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!anton"):
        await message.channel.send("Hello Anton")

    if message.content.startswith("!crypto"):
        await message.channel.send("You can get live prices for\n"
                                   "!ADA\n!BTC\n!DOGE\n!BNB\n!CHT")
    command = commands.get(message.content[1:6].upper())

    if command:
        response = get_bid_price(command["symbol"])
        price = response.json()[("bidPrice")]
        await message.channel.send(command["message_to_user"] + str(price) + "💲.....wuffff")
    else:
        if "!" in message.content[0:1]:
            await message.channel.send("Sorry Crypto Dogey could not find that Coin 🙀🙀🙀🙀")


