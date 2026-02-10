from flask import Flask, jsonify
import random

app = Flask(__name__)

def sample_metrics(name):
    return {
        "name": name,
        "status": "UP",
        "cpu": round(random.uniform(5, 75), 2),
        "memory": round(random.uniform(100, 2048), 2)
    }

@app.route('/metrics/app1')
def app1():
    return jsonify(sample_metrics('App 1'))

@app.route('/metrics/app2')
def app2():
    return jsonify(sample_metrics('App 2'))

@app.route('/')
def root():
    return jsonify({"message": "Python metrics simulator running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
