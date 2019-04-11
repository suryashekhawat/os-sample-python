from flask import Flask, Response
import json
from flask import request
from sqlalchemy import create_engine

DB_NAME = "sampledb"
DB_USER = "postgresql"
DB_PASS = "postgresql"
APP_HOSTNAME = "172.30.2.228" 

engine = create_engine("postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASS, APP_HOSTNAME, DB_NAME))

class Url(db.Model):
    url_id = db.Column(db.Integer, primary_key=True)
    visited_route = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Url %r>' % self.visited_route

application = Flask(__name__)

@application.route('/<path:path>')
def catch_all(path):
    count = 1
    mimetype = 'application/json'
    response = {'path': path, 'hits': '%s' % count}
    return Response(json.dumps(response, indent=2), mimetype=mimetype)


if __name__ == "__main__":
    application.run()
