from flask import Flask, render_template
from data import tours, departures
app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template("index.html")


@app.route('/depature/<depature>')
def route_depature(depature):
    return render_template("depature.html", depature=depature, tours=tours, title=departures[depature])


@app.route('/tour/<id>')
def route_tour(id):
    return render_template("tour_1.html", id=id)

@app.route('/test/')
def route_test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run()
