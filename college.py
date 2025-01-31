from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

Sample college data
colleges = [
    {"name": "College A", "fees": 100000, "courses": ["B.Tech", "M.Tech"]},
    {"name": "College B", "fees": 150000, "courses": ["BBA", "MBA"]},
    {"name": "College C", "fees": 200000, "courses": ["B.Sc", "M.Sc"]},
]

Chatbot responses
responses = {
    "hello": "Hi! How can I assist you with college admissions?",
    "fees": "The fees for {} is {}.",
    "courses": "The courses offered by {} are {}.",
    "apply": "You can apply to {} through our website.",
}

Chatbot intents
intents = {
    "hello": ["hi", "hello", "hey"],
    "fees": ["fees", "fee structure"],
    "courses": ["courses", "programs"],
    "apply": ["apply", "admission"],
}

Chatbot function
def chatbot(message):
    message = message.lower()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in message:
                if intent == "fees":
                    for college in colleges:
                        if college["name"].lower() in message:
                            return responses["fees"].format(college["name"], college["fees"])
                elif intent == "courses":
                    for college in colleges:
                        if college["name"].lower() in message:
                            return responses["courses"].format(college["name"], ", ".join(college["courses"]))
                elif intent == "apply":
                    for college in colleges:
                        if college["name"].lower() in message:
                            return responses["apply"].format(college["name"])
                else:
                    return responses[intent]
    return "Sorry, I didn't understand that."

API endpoint
@app.route("/chatbot", methods=["POST"])
def chatbot_api():
    message = request.json["message"]
    response = chatbot(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
