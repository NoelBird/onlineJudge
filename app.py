from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problems/1_palindrome/')
def problem():
    return render_template('problems/1_palindrome.html')

@app.route('/submit/', methods=["POST"])
def submit():
    from templates.problems import evaluator
    result, err, duration = evaluator.evaluator(request.form["code"])
    context = {
        "result": result,
        "error": err,
        "duration": duration
    }
    return render_template('result.html', **context)
    # return redirect('/result/', **context)

# @app.route('/result/')
# def result():
#     return render_template('result.html')

if __name__ == "__main__":
    app.run(port=50080, debug=True, host="0.0.0.0")