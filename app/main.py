from flask import Flask, render_template

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return ''

@app.route('/')
def index():
    res = {
        "title": "メイン"
    }
    return render_template('index.html', res=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)