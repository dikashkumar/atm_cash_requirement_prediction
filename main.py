from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
data = pd.read_csv("atm_data.csv")

# Input Features
X = data[["Total_Cash", "Withdrawal"]]

# Output
y = data["Required_Cash"]

# Train Model
model = LinearRegression()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    balance = None

    if request.method == "POST":

        atm_id = request.form["atm_id"]

        total_cash = float(
            request.form["total_cash"]
        )

        withdrawal = float(
            request.form["withdrawal"]
        )

        balance = total_cash - withdrawal

        prediction = model.predict(
            [[total_cash, withdrawal]]
        )[0]

        return render_template(
            "index.html",
            atm_id=atm_id,
            total_cash=total_cash,
            withdrawal=withdrawal,
            balance=balance,
            prediction=round(prediction, 2)
        )

    return render_template(
        "index.html",
        prediction=None
    )

if __name__ == "__main__":
    app.run(debug=True)