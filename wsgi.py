from flask import Flask
from flask import request
application = Flask(__name__)

@application.route('/', defaults={'path': ''})
def root(path):
    items = []
    mimetype = 'application/json'
    return Response(json.dumps(items, indent=2), mimetype=mimetype)

@application.route('/<path:path>')
def catch_all(path):
    count = 1
    mimetype = 'application/json'
    response = {'path': path, 'hits': '%s' % count}
    return Response(json.dumps(response, indent=2), mimetype=mimetype)


if __name__ == "__main__":
    application.run()
