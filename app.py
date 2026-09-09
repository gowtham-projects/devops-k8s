from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Demo Application</title>
        </head>
        <body>
            <h1>Hello from DevOps CI/CD!</h1>
            <h2>Version: 1.0</h2>
            <p>Environment: Development</p>
            <h2> Deployed Application using CI/CD Pipeline </h2>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
