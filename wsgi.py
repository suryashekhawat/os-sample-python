from flask import Flask, Response
import json
from flask import request
application = Flask(__name__)

@application.route('/<path:path>')
def catch_all(path):
    count = 1
    mimetype = 'application/json'
    response = {'path': path, 'hits': '%s' % count}
    return Response(json.dumps(response, indent=2), mimetype=mimetype)


if __name__ == "__main__":
    application.run()
