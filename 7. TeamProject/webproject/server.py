from flask import Flask, render_template, url_for, request, redirect
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import sys
if sys.platform in ["win32", "win64"]:
    font_name = "malgun gothic"
elif sys.platform == "darwin":
    font_name = "AppleGothic"
    
rc('font',family=font_name)    


app= Flask(__name__)

@app.route('/')
def hello_world():	
  return render_template("main.html")	

@app.route('/map/<alarm>')
def map(alarm):
  alarm=alarm+'.html'
  return render_template("map.html",alarm=alarm)	

@app.route('/drive')
def drive():
      df = pd.read_excel("static/data/final_drive.xlsx") 
      address = df['주소']
      nation = df['지역/국가명'] 
      a = ''
  
      for i in range(len(address)):
            a = a + '0'
      return render_template("drive.html", drive_link = address, drive_nation = nation, length=a) 

@app.route('/marker')
def marker():	
  return render_template("marker.html")	

correct = ["중국","일본","미국","태국","베트남"]
i = 0
@app.route('/keyword', methods=["POST","GET"])
def instar():
      search = ""
      global correct, i
      correct.append(search)
      
      get_search = request.form.get('get_search')
      if request.method == "POST":
            if get_search == correct[0]:
                  return redirect(url_for('china'))
            elif get_search == correct[1]:
                  return redirect(url_for('japan'))
            elif get_search == correct[2]:
                  return redirect(url_for('usa'))
            elif get_search == correct[3]:
                  return redirect(url_for('tai'))
            elif get_search == correct[4]:
                  return redirect(url_for('veit'))
            elif get_search >= correct[5]:
                msg = "아래 나라 중 검색하세요"
                  
      return render_template('keyword.html')

@app.route('/china')
def china():
      tag_counts_df = pd.read_excel('static/data/china.xlsx')
      
      plt.figure(figsize=(10,8))
      sns.barplot(x='counts', y='tags', data = tag_counts_df)
      plt.title('중국_China')
      return render_template('china.html', data=plt.show())
  
@app.route('/japan')
def japan():
      tag_counts_df = pd.read_excel('static/data/japan.xlsx')
      
      plt.figure(figsize=(10,8))
      
      sns.barplot(x='counts', y='tags', data = tag_counts_df)
      plt.title('일본_Japan')
      return render_template('japan.html', data=plt.show())
  
@app.route('/usa')
def usa():
      tag_counts_df = pd.read_excel('static/data/usa.xlsx')
      
      plt.figure(figsize=(10,8))
      sns.barplot(x='counts', y='tags', data = tag_counts_df)
      plt.title('미국_USA')
      return render_template('usa.html', data=plt.show())
  
@app.route('/veit')
def veit():
      tag_counts_df = pd.read_excel('static/data/viet.xlsx')
      
      plt.figure(figsize=(10,8))
      sns.barplot(x='counts', y='tags', data = tag_counts_df)
      plt.title('베트남_Vietnam')
      return render_template('veit.html', data=plt.show())

@app.route('/tai')
def tai():
      tag_counts_df = pd.read_excel('static/data/thai.xlsx')
      
      plt.figure(figsize=(10,8))
      sns.barplot(x='counts', y='tags', data = tag_counts_df)
      plt.title('태국_Thailand')
      return render_template('tai.html', data=plt.show())

if __name__ == '__main__':
  app.run(debug=True)