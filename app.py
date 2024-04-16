from flask import Flask, render_template, request, jsonify
import bot

doc ="files/attention-is-all-you-need-Paper.pdf"

def beutify(name):

    name = name.replace("files/", "")
    name = name.replace(".pdf", "")
    words = name.split("-")
    camel_case = ' '.join(word.capitalize() for word in words[0:])
    
    return camel_case


bot = bot.chatbot(doc)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html', doc_name = beutify(doc))


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    result = bot.qa_chain({"query": msg})
    return result["result"]


def get_Chat_response(text):
    pass

if __name__ == '__main__':
    app.run()
