from flask import Flask, render_template, request
from mario import build_pyramid

app = Flask(__name__)
# “Start a web server, ready to receive HTTP requests from a browser.”


@app.route("/", methods=["GET", "POST"])
#"When the browser visits /, run the function below."It connects a URL on the web → to a Python function.
def index():
#This Python function is the web endpoint.Whatever this function returns, Flask sends back to the browser.
    pyramid = None
    error = None

    if request.method == "POST":
        try:
            h = int(request.form.get("height", 0))
            #This is Flask reading what the browser sent through the HTML <form>.Browser → sends height → Flask receives it → Python reads it. This is what servers do: receive data from clients.
            if 1 <= h <= 8:
                pyramid = build_pyramid(h)
            else:
                error = "Height must be between 1 and 8."
        except ValueError:
            error = "Please enter a valid number."

    return render_template("index.html", pyramid=pyramid, error=error)


if __name__ == "__main__":
    app.run(debug=True)
