from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body style="background-color:skyblue;">
            <a href="/notice">
                <h1>안녕하세요!</h1>
            </a>
            <a href="/birth">
                <h2>생축!</h2>
            </a>
        </body>
    </html>
    '''

@app.route('/notice')
def notice():

    result = "오늘 엘리스 레이서분들과 스탠딩 파티를 진행합니다"
    piece = 8 / 4

    return f"{result}<br>피자는{piece} 조각"

@app.route('/birth')
def birth():

    return "생일축하합니다."

if __name__ == '__main__':
    app.run(debug=True, port=5000)

