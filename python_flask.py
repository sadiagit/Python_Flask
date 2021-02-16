from flask import Flask, request, jsonify
from flask_restful import Api, Resource

# this is important as the name will be different depending on started as a application 
# or importaed as single module
app = Flask(__name__) # creates an instance of the class

api =  Api(app)

def checkPostedData(posted_data, function_name):
        if (function_name ==  'add' or function_name ==  'subtract' or  function_name == 'multiply'):
            if "x" not in posted_data or "y" not in posted_data:
                return 301
            else:
                return 200
        if ( function_name == "divide"):
            if "x" not in posted_data or "y" not in posted_data:
                return 301
            elif (int(posted_data["y"])== 0):
                return 302
            else:
                return 200

class Add(Resource):
    

    def post(self):
        # get posted data
        posted_data = request.get_json()
        status_code = checkPostedData(posted_data, 'add')

        if (status_code != 200):
            retJson = {
                "Message":"An error occurred",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = int(posted_data["x"])
        y = int(posted_data["y"])

      
        retJson = {
            'Message': x+y,
            'Status Code': status_code
        }
        return jsonify(retJson)

class Subtract(Resource):
     def post(self):
        # get posted data
        posted_data = request.get_json()
        status_code = checkPostedData(posted_data, 'subtract')

        if (status_code != 200):
            retJson = {
                "Message":"An error occurred",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = int(posted_data["x"])
        y = int(posted_data["y"])

      
        retJson = {
            'Message': x-y,
            'Status Code': status_code
        }
        return jsonify(retJson)
class Multiply(Resource):
    def post(self):
        # get posted data
        posted_data = request.get_json()
        status_code = checkPostedData(posted_data, 'multiply')

        if (status_code != 200):
            retJson = {
                "Message":"An error occurred",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = int(posted_data["x"])
        y = int(posted_data["y"])

      
        retJson = {
            'Message': x*y,
            'Status Code': status_code
        }
        return jsonify(retJson)
        
class Divide(Resource):
    def post(self):
        # get posted data
        posted_data = request.get_json()
        status_code = checkPostedData(posted_data, 'divide')

        if (status_code != 200):
            retJson = {
                "Message":"An error occurred",
                "Status Code": status_code
            }
            return jsonify(retJson)
        
        x = int(posted_data["x"])
        y = int(posted_data["y"])

      
        retJson = {
            'Message': x/y,
            'Status Code': status_code
        }
        return jsonify(retJson)


#added the resouce, listening at add endpoint
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


if( __name__ == "__main__"):
    app.run(debug=True)

