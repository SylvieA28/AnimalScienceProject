from flask import Flask, request, render_template,jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bunny.html')
def bunny():
    return render_template('bunny.html')

@app.route('/cat.html')
def cat():
    return render_template('cat.html')

@app.route('/chicken.html')
def chicken():
    return render_template('chicken.html')

@app.route('/dog.html')
def dog():
    return render_template('dog.html')

@app.route('/fish.html')
def fish():
    return render_template('fish.html')

@app.route('/guinea-pig.html')
def guinea():
    return render_template('guinea-pig.html')

@app.route('/parakeet.html')
def parakeet():
    return render_template('parakeet.html')

@app.route('/zebra-finch.html')
def finch():
    return render_template('zebra-finch.html')

if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='0.0.0.0', port=5000)