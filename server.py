"""Flask application for emotion detection using sentiment analyzer."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import sentiment_analyzer

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the index HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def analyze_emotion():
    """Analyze the emotion of the input text using sentiment analyzer."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."
    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
