from decouple import config
from bot import InstaFollower

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
TARGET_ACCOUNT = "golfviewmag"

bot = InstaFollower()

bot.login(EMAIL, PASSWORD)
bot.find_followers(TARGET_ACCOUNT)
bot.follow()