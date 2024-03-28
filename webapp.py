from flask import Flask, render_template, request
import bot
import config

app = Flask(__name__)


@app.route("/")
def bergains():
    limit = request.args.get("limit", type=int, default=100)
    sort = request.args.get("sort", type=str, default="none")
    bargains = bot.get_bargains()[:limit]
    match (sort):
        case "discount":
            bargains.sort(key=lambda bargain: bargain.discount, reverse=True)

    return render_template("bargains.html", bargains=bargains, config=config)
