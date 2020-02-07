from flask import Flask
app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    return "Hello, world!"

@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return f"Hello, {name}"

@app.route('/interesting/<name>', methods=['GET'])
def serve_html(name):
    return f"""
    <html>
    <body>
    <h1>Hello {name}</h1>
    <p>This is my fancy webpage</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
