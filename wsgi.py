from flask import Flask
from flask import request
application = Flask(__name__)

@application.route("/")
def hello():
    return "test openshift flask deployemnt"

@application.route("/hello")
def sayhello():
    curr_route_name = request.url_rule
    return "route {}".format(curr_route_name)



if __name__ == "__main__":
    application.run()
