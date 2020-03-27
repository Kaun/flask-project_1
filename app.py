from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template("index.html")


@app.route('/depature/<depature>')
def route_depature(depature):
    return render_template("depature.html", depature=depature)


@app.route('/tour/<id>')
def route_tour(id):
    return render_template("tour_1.html", id=id)

@app.route('/test/<role>')
def route_test(role):
    return render_template("test.html", role=role)


if __name__ == '__main__':
    app.run()
