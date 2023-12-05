from flask import Flask

app = Flask(__name__)


@app.route('/<number>')
def hello_world(number):
    if int(number)>8:
        return '<h1 style="text-align: center">The number is too high!</h1>' \
               '<img src="https://i.gifer.com/WTw.gif">'
    elif int(number)<8:
        return '<h1 style="text-align: center">The number is too low!</h1>' \
               '<img src="https://humorpoint.com/wp-content/uploads/2022/10/d62447_e7860809264b4bd89d3d9c63d6df5b9c_mv2.gif">'
    else:
        return '<h1 style="text-align: center">You found the nunmber!!</h1>' \
               '<iframe src="https://giphy.com/embed/Xf8D9Qf8OCKnMvNnru" width="480" height="470" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/kitten-choreography-a-chorus-line-Xf8D9Qf8OCKnMvNnru">via GIPHY</a></p>'




@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/<name>")
def user_say(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run()
