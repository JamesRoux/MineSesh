from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/begin", methods = ['POST'])

# TODO:
# Add ability to edit the blower time for players
# Easy, medium, hard?
# Actual times?

def begin():
    player1 = request.form['player1']
    player2 = request.form['player2']

    logtime = datetime.now()
    logtime = logtime.strftime("%m.%d.%Y.%H.%M.%S")
    print(logtime)
    logfile = open("./logs/%s" % logtime, "w+")
    logfile.write("Player One: %s | Player Two: %s\r\n" % (player1, player2))

    logfile.close()
    return redirect('/gametime')

@app.route("/gametime")
def gametime():
    # This will be where the users see their scores, total time inhaled, and basic things like that
    return redirect("/")

@app.route("/modhandler")
def modhandler():
    # This will handle all data from the game itself
    # TODO:
    # Add logging for each death / inhale
    # Add backend for activating the GPIO
    # Add catch for mod data
    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True)
