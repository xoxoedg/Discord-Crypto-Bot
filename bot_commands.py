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
        await message.channel.send("")

    if message.content.startswith("!crypto"):
        my_embed = discord.Embed(title="Crypto", description="You can check the price for the following coins\n"
                                                             "ADA\nETH\nDOT\nDENT\nBTC\n"
                                                             "LTC\nBTT\nCHZ\nLINK\nALGO\n"
                                                             "NEO\nTHETA\nDOGE\nBNB", color=0x00FF66)
        my_embed.set_footer(text="Just Type in !coin")
        await message.channel.send(embed=my_embed)

    command = commands.get(message.content[1:6].upper())

    if command:
        response = get_bid_price(command["symbol"])
        price = response.json()[("bidPrice")]
        my_embed = discord.Embed(title=message.content[1:6].upper(), description=command["message_to_user"] + str(price) + " USDT",
                                 color=0x00FF66)
        my_embed.set_image(url="https://specials-images.forbesimg.com/imageserve"
                               "/5dc8af63ea103f0006522230/960x0.jpg?fit=scale")
        my_embed.set_footer(text="Crypto to the Mooooooon ....Wufff")
        await message.channel.send(embed=my_embed)
        crypto_list = ["ADA","ETH", "DOT", "DENT","BTC", "LTC",
                       "BTT", "CHZ", "LINK", "ALGO", "NEO", "THETA", "DOGE", "BNB"]

        if "!" in message.content[0:1] and message.content[1:6].upper() not in crypto_list:
            await message.channel.send("Sorry Crypto Dogey could not find that Coin 🙀🙀🙀🙀")


