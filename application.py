# application.py, application.py
from flask import Flask, request
import json
# connection=MongoClient(host="localhost", port=27017)
# db=connection.test# connection,database name
# collection=db.employee
application = Flask(__name__)

@application.route("/",methods=["GET"])
def test():
    return "hello world Lambda from vcube"
    # html code
    # css code

@application.route("/test",methods=['POST'])
def posttest():
    data=request.data
    print(json.loads(data))
    return "received"


if __name__ == '__main__':
    application.run(host="0.0.0.0",port=5000)
