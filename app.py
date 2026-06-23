from flask import Flask, render_template, request, redirect, flash, session, url_for

app = Flask(__name__)
app.secret_key = "hillfields_ultra_secure"

# In-memory admin state
admin_profiles = {
    "deputy_principal": {
        "name": "Daniel Hernandez",
        "role": "Deputy Principal & CBC Coordinator"
    },
    "head_junior": {
        "name": "Kevin Nyambega Mongare",
        "role": "Head of Junior School Learning Areas"
    }
}


@app.route("/")
def home():
    return render_template("index.html", profiles=admin_profiles)


@app.route("/cbc-framework")
def cbc():
    return render_template("cbc_framework.html")


@app.route("/enroll")
def enroll():
    return render_template("enroll.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form.get("role")
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Please complete all login fields.", "error")
            return redirect(url_for("login"))

        session["role"] = role

        if role == "Parent":
            flash("Welcome to CBC Parent Portfolio Portal.", "success")
            return redirect(url_for("home"))

        elif role == "Teacher":
            flash("Welcome to Assessment Submission Desk.", "success")
            return redirect(url_for("home"))

        elif role == "Administrator":
            return redirect(url_for("admin"))

    return render_template("login.html")


@app.route("/admin")
def admin():
    if session.get("role") != "Administrator":
        flash("Unauthorized access.", "error")
        return redirect(url_for("login"))

    return render_template("admin.html", profiles=admin_profiles)


@app.route("/admin/update-profile", methods=["POST"])
def update_profile():
    deputy_name = request.form.get("deputy_name")
    head_name = request.form.get("head_name")

    admin_profiles["deputy_principal"]["name"] = deputy_name
    admin_profiles["head_junior"]["name"] = head_name

    flash("Leadership profiles updated successfully.", "success")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
