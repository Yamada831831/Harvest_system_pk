from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>包材在庫管理システム</h1><p>ここに在庫データを表示</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
