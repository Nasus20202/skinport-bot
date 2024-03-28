from webapp import app
import bot
from threading import Thread

thread = Thread(target=app.run, args=('0.0.0.0', 5000))
thread.daemon = True
thread.start()

bot.start()
