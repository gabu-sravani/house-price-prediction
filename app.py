from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    predicted_price = None

    if request.method == "POST":
        try:
            # Form Inputs
            size = float(request.form.get("size"))
            rooms = int(request.form.get("rooms"))

            condition = request.form.get("condition")
            material = request.form.get("material")
            quality = request.form.get("quality")

            location = request.form.get("location")
            age = int(request.form.get("age"))
            floor = int(request.form.get("floor"))
            parking_slots = int(request.form.get("parking_slots"))

            furnished = request.form.get("furnished")

            features = request.form.getlist("features")

            # Base Price
            price = size * 1000 + rooms * 5000

            # Condition
            if condition == "Good":
                price *= 1.10

            # Material
            if material == "High":
                price *= 1.20
            elif material == "Medium":
                price *= 1.10

            # Quality
            if quality == "High":
                price *= 1.30
            elif quality == "Medium":
                price *= 1.15

            # Location
            if location == "Urban":
                price *= 1.25
            elif location == "SemiUrban":
                price *= 1.10

            # Floor Bonus
            price += floor * 10000

            # Parking Slots
            price += parking_slots * 50000

            # Furnished
            if furnished == "Yes":
                price += 300000
            elif furnished == "Semi":
                price += 150000

            # House Age Depreciation
            price -= age * 5000

            # Features
            if "Parking" in features:
                price += 100000

            if "Balcony" in features:
                price += 50000

            if "Garden" in features:
                price += 150000

            if "Swimming Pool" in features:
                price += 300000

            if "Lift" in features:
                price += 100000

            if "Security" in features:
                price += 80000

            if "Gym" in features:
                price += 120000

            if "Power Backup" in features:
                price += 70000

            predicted_price = round(price, 2)

        except Exception as e:
            predicted_price = f"Error: {str(e)}"

    return render_template(
        "home.html",
        predicted_price=predicted_price
    )


if __name__ == "__main__":
    print("Starting Flask App...")
    app.run(debug=True)