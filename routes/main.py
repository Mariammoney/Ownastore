from flask import Blueprint, render_template

main = Blueprint("main", __name__)



@main.route("/")
def homepage():
    return render_template("index.html")

@main.route("/how-it-works")
def How_It_Works():
    return render_template("howitworks/howitworks.html")

@main.route("/why-us")
def Why_Us():
    return render_template("whyus/whyus.html")

@main.route("/pricing")
def Pricing():
    return render_template("pricing/pricing.html")

@main.route("/gurantees")
def Gurantees():
    return render_template("gurantees/gurantees.html")

@main.route("/testimonials")
def Testimonials():
    return render_template("testimonials/testimonials.html")