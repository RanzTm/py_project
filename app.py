import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request

app = Flask(__name__)


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    user = "vastseliinaabi@gmail.com"
    msg["from"] = user
    password = "punqzhlfzwulstnr"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


@app.route("/")  # http://127.0.0.1:5000/ töötaks serveris
def index():
    return render_template("index.html")


# http://127.0.0.1:5000/success töötkas serveris
# ilma methods= ita tule teade - Method Not Allowed
@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        problem = request.form["problem_name"]
        room = request.form["room_name"]
        email = request.form["email_name"]
        print(problem, room, email)  # Tuleks konsoolis ühele reale
        email_alert(room, problem, email)
        return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()

##############################################
'''
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")  # http://127.0.0.1:5000/ töötaks serveris
def index():
    return render_template("index.html")


# http://127.0.0.1:5000/success töötkas serveris
# ilma methods= ita tule teade - Method Not Allowed
@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        problem = request.form["problem_name"]
        room = request.form["room_name"]
        email = request.form["email_name"]
        print(problem, room, email)  # Tuleks konsoolis ühele reale
        return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
'''
