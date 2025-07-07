# 필요한 라이브러리
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
   # return jsonify({'result':'success', 'data': {"feed1":"data", "feed2":"data2"}})
   return {'result':'success', 'data': {"feed1":"data", "feed2":"data2"}}

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
   print(feed_id)
   return jsonify({'result':'success', 'data': {"feed1":"data"}})