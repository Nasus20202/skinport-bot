from webapp import app
import bot
from threading import Thread

thread = Thread(target=app.run)
thread.start()

bot.start()
