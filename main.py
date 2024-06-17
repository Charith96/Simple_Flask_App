from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])

def handle_post():
    # Get data from the POST request
    data = request.get_json()

    # Pass the body of the request as the response data
    response_data = data or 'Invalid Request!'

    # Send a JSON response back to the requestor
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)