from flask import Flask, render_template, request, redirect
import sqlite3

from datetime import datetime

from discordwebhook import Discord





app = Flask(__name__)

discord = Discord(url="https://discordapp.com/api/webhooks/1288490670201245747/rjzj733T5IO5ITcshODT6t4nbK31vcHQmY__y_09DrssieZP6mhDItY1JSqHaIAx4LEC")
#discord.post(content="Testttt")



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/update", methods = ["POST"])
def checkAndUpdate():
    user_message = request.form["textBox"] #getting the message from the text box which called "textBox"

    #check if it the message is valid - only letters and numbers
    for char in user_message:
        if char.isnumeric() or char.isalpha():
            message_is_valid = True
        else:
            message_is_valid = False
            break

    if message_is_valid:
        current_time = datetime.now()
        print (current_time)

        discord.post(content=user_message)

        conn = sqlite3.connect("discordDB")
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO messages (message, time) VALUES ('{user_message}', '{current_time}')")
        conn.commit()
        conn.close()


        return f"{user_message} | {current_time}"

    else:
        return "not valid message"


@app.route("/showLast30")
def showLast30Messages():
    conn = sqlite3.connect("discordDB")
    cursor = conn.cursor()

    #show all messages from last 30 minutes
    cursor.execute("SELECT * FROM messages")

    allMessages = cursor.fetchall()
    conn.close()

    last30Messages = {}

    current_time = datetime.now()

    for message in reversed(allMessages):
        time_then = datetime.fromisoformat(message[2])
        time_passed = str(current_time - time_then)

        if time_passed[0] == "0":
            minutes_passed = int(time_passed.split(":")[1])

            if minutes_passed < 30:
                last30Messages[str(time_then)] = message[1]

    return last30Messages



if __name__ == "__main__":
    app.run()
