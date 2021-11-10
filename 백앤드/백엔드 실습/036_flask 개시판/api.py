from flask import Blueprint, render_template, jsonify, request
from db_connect import db
from models import Post

board = Blueprint('board',__name__)

# 작성한 게시글을 볼 수 있도록 함수를 완성하세요.
@board.route("/")
def home():
    total_records = db.session.query(Post).order_by(Post.created_at.desc()).all()
    return render_template('index.html', data=total_records)
    
@board.route("/post",methods=["POST"])
def create_post():
    #process
    content = request.form['content']
    author = request.form['author']
    #DB write
    post = Post(author, content)
    db.session.add(post)
    db.session.commit()
    #return jsonify({'result':'success'})
    #total_records = db.session.query(Post).all()

    return render_template('index.html')
    
@board.route("/like",methods=["PATCH"])
def update_like():
    db.session.query(Post)
    return jsonify("good")