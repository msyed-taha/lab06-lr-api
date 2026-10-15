import random
from flask import Flask, request, jsonify

REG_NO = "SP23-BAI-049"
# Seed = student roll number. If instructor says numeric, change to: SEED = 49
SEED = REG_NO

random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)
app.json.sort_keys = False  # keep "registration number" first, like the example


@app.route("/")
def home():
    return jsonify({"status": "running", "usage": "/predict?x1=2&x2=3&x3=1"})


@app.route("/predict", methods=["GET", "POST"])
def predict():
    src = request.args if request.args else (request.get_json(silent=True) or {})
    try:
        x1 = float(src.get("x1"))
        x2 = float(src.get("x2"))
        x3 = float(src.get("x3"))
    except (TypeError, ValueError):
        return jsonify({"error": "Provide numeric x1, x2, x3 e.g. /predict?x1=2&x2=3&x3=1"}), 400

    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({"registration number": REG_NO, "prediction": round(y, 2)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
