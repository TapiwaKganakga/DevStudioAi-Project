from flask import Flask, request, jsonify, send_from_directory
from ai_agent import build_prompt, call_llm
from static_analysis import run_flake8
import tempfile, os

app = Flask(__name__, static_folder='../frontend', static_url_path='/')


@app.route("/analyze", methods=["POST"])
def analyze():
    payload = request.json
    filename = payload.get("filename", "code.py")
    code = payload.get("code", "")
    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Run linter: write temp file
    fd, tmp = tempfile.mkstemp(suffix=os.path.splitext(filename)[1])
    try:
        with os.fdopen(fd, "w") as f:
            f.write(code)
        linter_output = run_flake8(tmp)
    finally:
        try:
            os.remove(tmp)
        except:
            pass

    prompt = build_prompt(filename, code, linter_output)
    ai_resp = call_llm(prompt)
    return jsonify({"ai": ai_resp, "linter": linter_output})


# Serve frontend index
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
