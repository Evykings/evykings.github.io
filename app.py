from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Projects page route
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
