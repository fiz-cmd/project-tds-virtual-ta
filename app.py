from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/", methods=["POST"])
def answer_question():
    data = request.get_json()
    q = data.get("question", "")
    # TODO: load your knowledge base / scraped data here
    # For now, always return a placeholder answer:
    return jsonify({
        "answer": f"Sorry, I haven't learned that yet: '{q}'",
        "links": []
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
