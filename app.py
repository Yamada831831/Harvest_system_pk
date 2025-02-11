from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQLの接続設定
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://harvest_user:nsG5JUKazujysFe7OSSjxdn04CmJ5qL5@dpg-cujdt18gph6c73bemdc0-a/harvest_db_ezlw"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 在庫データのモデル
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# アプリ起動時にデータベースを初期化＆サンプルデータを登録
with app.app_context():
    db.create_all()
    
    # もしデータが空ならサンプルデータを追加
    if Inventory.query.count() == 0:
        sample_items = [
            Inventory(name="段ボール", quantity=100),
            Inventory(name="袋", quantity=200),
            Inventory(name="トレー", quantity=150),
            Inventory(name="ネット", quantity=50),
            Inventory(name="シール", quantity=300),
        ]
        db.session.add_all(sample_items)
        db.session.commit()

@app.route('/')
def home():
    items = Inventory.query.all()
    return "<h1>包材在庫管理システム</h1>" + "".join([f"<p>{item.name}: {item.quantity}個</p>" for item in items])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
