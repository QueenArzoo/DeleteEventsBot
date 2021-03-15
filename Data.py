from delevents import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nI can delete telegram service messages. Add me to your group with delete messages right and leave rest to me. "

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @HEROGAMERS1 ♥"

    # About Message
    ABOUT = "**About This Bot** \n\nThis is an open source delete events bot by @HEROGAMERS1 \n\nSource : [Click Here](https://github.com/QueenArzoo/DeleterRobot) \n\nFramework : [Pyrogram](docs.pyrogram.org) \n\nLanguage : [Python](www.python.org) \n\nDeveloper : [Hero](https://t.me/HEROGAMERS)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Deploy Message
    DEPLOY = '**Clone This Bot??** \n\nThis is simple and open source bot. \nJust click below on source code and tap on "Deploy to Heroku" to create your own bot. \n\nClick Here for [Source Code](https://github.com/QueenArzoo/DeleterRobot)'

    HELP = '**Need Help?** \n\nJust Add me in your group as admin with atleast "Delete Messages" permission and leave rest to me. '

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("Create your own bot", callback_data="deploy")],
        [InlineKeyboardButton("🙋 Support Group ", url="https://t.me/LaylaSupport")],
    ]
