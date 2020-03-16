# from flask import Flask, render_template, request, jsonify
#
# # import request
# from Scraper import getReviewsFromURL
#
# app = Flask(__name__)  # initialising the flask app with the name 'app'
#
#
# # response = 'Welcome!'
#
#
# # @app.route('/')  # route for redirecting to the home page
# # @cross_origin()
# # def home():
# #     return render_template('index.html')
#
#
# @app.route('/getreviews', methods=['POST'])  # route to return the list of file locations for API calls
# def getReviewsData():
#     # if request.method == 'POST':
#     print("entered post")
#     url = request.json['url']  # assigning the value of the input keyword to the variable keyword
#     websiteURL = request.json['websiteURL']
#     reviewObj = getReviewsFromURL(websiteURL, url)
#
#     return jsonify(reviewObj)  # send the url list in JSON format
#
#
# if __name__ == "__main__":
#     # app.run(host='127.0.0.1', port=8000) # port to run on local machine
#     app.run(debug=True)  # to run on cloud

from wsgiref import simple_server

from flask import Flask, render_template, request, jsonify
import os
# import request
from Scraper import getReviewsFromURL

app = Flask(__name__)  # initialising the flask app with the name 'app'

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# response = 'Welcome!'


# @app.route('/')  # route for redirecting to the home page
# @cross_origin()
# def home():
#     return render_template('index.html')


@app.route('/getreviews', methods=['POST'])  # route to return the list of file locations for API calls
def getReviewsData():
    # if request.method == 'POST':
    print("entered post")
    url = request.json['url']  # assigning the value of the input keyword to the variable keyword
    websiteURL = request.json['websiteURL']
    reviewObj = getReviewsFromURL(websiteURL, url)

    return jsonify(reviewObj)  # send the url list in JSON format


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
