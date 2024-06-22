from flask import Flask, request

app = Flask(__name__)

@app.route('/pirsensor/data', methods=['POST'])
def post():
    motion = request.form.get("motion")
    print(f"Received motion: {motion}")
    if motion == "detected":
        return 'PIR sensor detected motion', 200
    else:
        return 'Failed to receive data', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
