from flask import Flask, render_template, request
from translator import translate_to_english, generate_auto_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    auto_response = ""
    if request.method == "POST":
        user_query = request.form["query"]
        translated_text = translate_to_english(user_query)
        auto_response = generate_auto_response(translated_text)
    return render_template("index.html", translated=translated_text, response=auto_response)

if __name__ == "__main__":
    app.run(debug=True)
