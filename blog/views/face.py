from flask import Blueprint, render_template

face = Blueprint('face', __name__, url_prefix='/', static_folder='../static')


@face.route("/", endpoint="list")
def reports_list():
    return render_template("index.html")
