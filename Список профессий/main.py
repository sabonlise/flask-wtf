from flask import Flask, render_template


app = Flask(__name__)


@app.route('/list_prof/<list_type>')
def mission(list_type):
    return render_template('professions.html', list_type=list_type)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
