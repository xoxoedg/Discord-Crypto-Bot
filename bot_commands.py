import discord
from binance_prices import get_bid_price
from Mapping import commands, crypto_list



client = discord.Client()

@client.event
async def on_ready():
    pass


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!atakantreppe"):
        my_embed = discord.Embed(title="Wuff", description="Ab auf die ruhige Treppe du kek")
        member = await message.guild.fetch_member(517766546387501063)
        channel = client.get_channel(838076458994761738)
        await message.channel.send(embed=my_embed)
        await member.move_to(channel)

    if message.content.startswith("!emretreppe"):
        my_embed = discord.Embed(title="Wuff", description="Ab auf die ruhige Treppe du kek")
        member = await message.guild.fetch_member(156871051689721856)
        channel = client.get_channel(838076458994761738)
        await message.channel.send(embed=my_embed)
        await member.move_to(channel)

    if message.content.startswith("!antontreppe"):
        my_embed = discord.Embed(title="Wuff", description="Ab auf die ruhige Treppe du kek")
        member = await message.guild.fetch_member(395371925704278026)
        channel = client.get_channel(838076458994761738)
        await message.channel.send(embed=my_embed)
        await member.move_to(channel)

    if message.content.startswith("!riadtreppe"):
        my_embed = discord.Embed(title="Wuff", description="Ab auf die ruhige Treppe du kek")
        member = await message.guild.fetch_member(286216180140736533)
        channel = client.get_channel(838076458994761738)
        await message.channel.send(embed=my_embed)
        await member.move_to(channel)


    #if message.author.id == 395371925704278026:
    #    url = "https://i1.wp.com/futter.kleinezeitung.at/wp-content/uploads/2019/11/76189804_420045602262230_4868106857467609088_n.jpg?fit=740%2C389&ssl=1"
    #    my_embed = discord.Embed(title="QUITTER👺👺👺👺👺👺")

    #    my_embed.set_image(url=url)
    #    await message.channel.send(embed=my_embed)
    #
    # if message.author.id == 517766546387501063:
    #     url = "https://media.giphy.com/media/jpft0FdIKRqFO/giphy.gif"
    #     my_embed = discord.Embed(title="ok MR VERLUST 👺👺👺👺👺👺")
    #
    #     my_embed.set_image(url=url)
    #     await message.channel.send(embed=my_embed)

    if message.content.startswith("!crypto"):
        url = "https://media.giphy.com/media/AGovZiAB941Ww/giphy.gif"
        my_embed = discord.Embed(title=message.content[1:6].upper())

        my_embed.set_image(url=url)
        await message.channel.send(embed=my_embed)

    if message.content.startswith("!hapi"):
        url = "https://i.ytimg.com/vi/-2yiWIo3lGE/maxresdefault.jpg"
        my_embed = discord.Embed(title=message.content.upper())

        my_embed.set_image(url=url)
        await message.channel.send(embed=my_embed)


    if message.content.startswith("!karen"):
        url = "https://img-9gag-fun.9cache.com/photo/anQ2wMn_460s.jpg"
        my_embed = discord.Embed(title=message.content.upper())

        my_embed.set_image(url=url)
        await message.channel.send(embed=my_embed)

    if message.content.startswith("!anton"):
        url = "https://i1.wp.com/futter.kleinezeitung.at/wp-content/uploads/2019/11/76189804_420045602262230_4868106857467609088_n.jpg?fit=740%2C389&ssl=1"
        my_embed = discord.Embed(title=message.content[1:6].upper())

        my_embed.set_image(url=url)
        await message.channel.send(embed=my_embed)

    if message.content.startswith("!crypto"):
        my_embed = discord.Embed(title="Crypto", description="You can check the price for the following coins\n"
                                                             "ADA\nETH\nDOT\nDENT\nBTC\n"
                                                             "LTC\nBTT\nCHZ\nLINK\nALGO\n"
                                                             "NEO\nTHETA\nDOGE\nBNB", color=0x00FF66)

        my_embed.set_footer(text="Just Type in !coin")
        await message.channel.send(embed=my_embed)

    if message.content.startswith("!atakan"):
        url = "https://i.ytimg.com/vi/EsRXXUWuENQ/maxresdefault.jpg"
        my_embed = discord.Embed(title="QUITTER")

        my_embed.set_image(url=url)
        await message.channel.send(embed=my_embed)


    command = commands.get(message.content[1:6].upper())

    if command:
        response = get_bid_price(command["symbol"])
        price = response.json()[("bidPrice")]
        my_embed = discord.Embed(title=message.content[1:6].upper(), description=command["message_to_user"] + str(price) + " USDT",
                                 color=0x00FF66)
        my_embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP9xf3QhFhrwvUPvEuHx5cRIsOIDoQCB7H0g&usqp=CAU")

        my_embed.set_footer(text="Crypto to the Mooooooon ....Wufff")
        await message.channel.send(embed=my_embed)


        if message.content[0] == "!" and message.content[1:6].upper() not in crypto_list:
            return await message.channel.send("Sorry Crypto Dogey could not find that Coin 🙀🙀🙀🙀")

    if message.content.startswith("!moon"):
        my_embed = discord.Embed(title=message.content[1:6].upper())

        my_embed.set_image(url="https://media3.giphy.com/media/Ogak8XuKHLs6PYcqlp/giphy.gif?cid=ecf05e47afxx0vihat3yfaqsig82brss8czzcsj2q3rwiyfy&rid=giphy.gif&ct=g")

        await message.channel.send(embed=my_embed)


