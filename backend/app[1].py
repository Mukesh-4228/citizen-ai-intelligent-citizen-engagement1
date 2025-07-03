from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/message', methods=['POST'])
def message():
    data = request.json
    return jsonify({'reply': 'This is a dummy response'})
if __name__ == '__main__':
    app.run(debug=True)