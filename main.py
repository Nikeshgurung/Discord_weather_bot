
import nextcord
from nextcord.ext import commands
from config import DISCORD_TOKEN, WEATHER_API_KEY
from responses import get_response
import aiohttp

# Initialize the bot
intents = nextcord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")

# Command: Fetch weather data
@bot.command()
async def weather(ctx: commands.Context, *, city: str):
    """
    Fetches and displays the current weather for a specified city.
    Usage: !weather <city>
    """
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as res:
            if res.status == 200:
                data = await res.json()

                # Extract weather data
                location = data["location"]["name"]
                temp_c = data["current"]["temp_c"]
                temp_f = data["current"]["temp_f"]
                humidity = data["current"]["humidity"]
                wind_kph = data["current"]["wind_kph"]
                wind_mph = data["current"]["wind_mph"]
                condition = data["current"]["condition"]["text"]
                image_url = "http:" + data["current"]["condition"]["icon"]

                # Create an embed to display the weather information
                embed = nextcord.Embed(
                    title=f"Weather for {location}",
                    description=f"The condition in {location} is {condition}."
                )
                embed.add_field(name="Temperature", value=f"C: {temp_c} || F: {temp_f}")
                embed.add_field(name="Humidity", value=f"{humidity}%")
                embed.add_field(name="Wind Speeds", value=f"KPH: {wind_kph} || MPH: {wind_mph}")
                embed.set_thumbnail(url=image_url)

                await ctx.send(embed=embed)
            else:
                await ctx.send("Failed to fetch weather data. Please try again later.")

# Event: Handle incoming messages
@bot.event
async def on_message(message: nextcord.Message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message starts with the bot's prefix
    if message.content.startswith("!"):
        await bot.process_commands(message)  # Process commands
        return

    # Handle non-command messages
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')

    # Get a response from responses.py
    response: str = get_response(user_message)
    await message.channel.send(response)

# Run the bot
bot.run(DISCORD_TOKEN)