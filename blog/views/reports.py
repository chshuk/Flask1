from flask import Blueprint, render_template

reports = Blueprint('reports', __name__, url_prefix='/reports', static_folder='../static')


@reports.route("/", endpoint="list")
def reports_list():
    return render_template("reports/list.html", reports=[1, 2, 3, 4, 5])
