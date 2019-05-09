from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/begin", methods = ['POST'])
def begin():
    player1 = request.form['player1']
    player2 = request.form['player2']

    logfile = open("./logs/logs.csv", "w+")
    logfile.write("Player One: %s | Player Two: %s\r\n" % (player1, player2))

    # TODO:
    # Add page for mod to send data to
    # Add logging for each death
    # Add ability to toggle pumps on / off

    logfile.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
