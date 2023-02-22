# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "24236993"))
    API_HASH = os.environ.get("API_HASH", "0a56df2f25eefcace1c2e8948106dd66")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6194982121:AAGlpR1mqSScLMjemnhpaEOK1PNbzu5pSHM")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQA0weH32a1zhBHQBCGM6JPAe2aEXEac2jOUVY6zNkxKat4fpvIKskJ8IMQt6bxpF8yjg7iDVX1JwmAFAklNpv1mZp9d92hP3RJItUzzvBvkNcZOIqAkuRI2uqQbqHmZZs6yePJuuEY4b4OglNacshTdgs3gjBKjletHoeYjXgWTCCH7vLcZILOcUbSumxXAV3RF4M5LjS-2mk-i4BApI1YnCpXEkdK3WK5gre4kxwmMnl0XCU78lfXaxy14Twd0QV4rrsnk8oOzy48B6xWsBXo6LR4MLVwEPcLpLp0E-fjjgs6wKT1JO7n1cQDOmIbrPG6eLMD4oQ4agehMsA4XRQV1AAAAAUqdLycA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001893750015"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Movie_ab_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1324432518"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/cyniteofficial'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/cyniteofficial'>Cynite</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/cyniteofficial'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Cyniteofficial</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Cyniteofficial</a></b>
"""


