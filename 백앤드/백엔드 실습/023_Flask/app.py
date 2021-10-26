import random
from flask import Flask
from flask import request
from flask import redirect
from flask import send_from_directory
from flask import render_template
from flask import make_response
from flask import make_response
from flask import Response
import json
from flask_cors import CORS


import sqlite3
app = Flask(__name__)
CORS(app)

resp = Response()
resp.headers['Access-Control-Allow-Origin'] = '*'


@app.route('/topics', defaults={'topic_id':None}, methods=['GET', 'POST'])
@app.route('/topics/<topic_id>', methods=['PUT', 'GET', 'DELETE'])
def topics(topic_id):
    try:
        db = sqlite3.connect('topics.db')
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='topic'")
        if cursor.fetchone()[0] == 1:
            print('Table exist')
        else:
            sql = """
                CREATE TABLE "topic" (
                    "id"	INTEGER,
                    "title"	TEXT,
                    "body"	TEXT,
                    PRIMARY KEY("id" AUTOINCREMENT)
                )
            """
            cursor.execute(sql)
            db.commit()
        
        if request.method == 'GET':
            if topic_id == None:
                sql = "SELECT * FROM topic"
                cursor.execute(sql)
                topics = cursor.fetchall()
                output = []
                for topic in topics:
                    output.append({'id':topic['id'], 'title':topic['title'], 'body':topic['body']})
                resp.set_data(json.dumps(output))
                return resp
            else:
                sql = "SELECT * FROM topic WHERE id = "+str(topic_id)
                cursor.execute(sql)
                topic = cursor.fetchone()                
                output = json.dumps({'id':topic['id'], 'title':topic['title'], 'body':topic['body']})
                resp.set_data(output)
                return resp
        elif request.method == 'POST':
            form = request.get_json()
            sql = """
                INSERT INTO topic (title, body) 
                VALUES(
                    '%(title)s',
                    '%(body)s'
                )
                """ % {'title':form['title'], 'body':form['body']}
            cursor.execute(sql)
            db.commit()
            output = json.dumps({'id':cursor.lastrowid, 'title':form['title'], 'body':form['body'] })
            resp.set_data(output)
            return resp
        elif request.method == 'PUT':
            form = request.get_json()
            sql = """
                UPDATE topic SET 
                    title = '%(title)s', 
                    body = '%(body)s'
                WHERE id = '%(topic_id)s'
                """ % {'topic_id': topic_id, 'title':form['title'], 'body':form['body']}
            cursor.execute(sql)
            db.commit()
            output = json.dumps({'id':topic_id, 'title':form['title'], 'body':form['body'] })
            resp.set_data(output)
            return resp
        elif request.method == 'DELETE':
            sql = """
                DELETE FROM topic WHERE id = %(id)s            
                """ % {'id':topic_id}
            cursor.execute(sql)
            db.commit()
            output = json.dumps({'id':topic_id})
            resp.set_data(output)
            return resp
    except Exception as e:
        print('error', e)
    finally:
        cursor.close()
        db.close()

##
@app.route("/hihi")
def hehe():
    return "<h1>" + random.choice(['hi', 'hello', '안녕'])+"</h1>"
##

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

@app.route('/', defaults={'path':None})
@app.route('/<path>')
def index(path):
    resp.set_data(render_template('index.html'))   ## templates 폴더 읽기
    return resp

if __name__ == '__main__':
	app.run(debug=True)

