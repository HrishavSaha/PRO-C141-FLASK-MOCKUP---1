from flask import Flask, jsonify, request
import pandas as pd

df1 = pd.read_csv('updatedSharedArticles.csv')
title = df1['title'].tolist()

likedTitle = []
notLikedTitle = []

app = Flask(__name__)

@app.route('/getTitles')
def getTitles():
  return jsonify({
    'data':title,
    'status':'Success'
  }, 200)

@app.route('/liked')
def liked():
  likedTitleName = title.pop(0)
  likedTitle.append(likedTitleName)
  return jsonify({
    'data':likedTitle,
    'status':'Success'
  }, 200)

@app.route('/notLiked')
def notLiked():
  notLikedTitleName = title.pop(0)
  notLikedTitle.append(notLikedTitleName)
  return jsonify({
    'data':notLikedTitle,
    'status':'Success'
  }, 200)

if __name__ == '__main__':
  app.run()