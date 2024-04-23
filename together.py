from flask import Flask, render_template, request
import smtplib
import requests
import warnings
from linebot import LineBotSdkDeprecatedIn30
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
from flask import Flask, render_template


app = Flask(__name__, template_folder='C:/Users/gjess/OneDrive/桌面/learn pyhon/linebot/iPortfolio')

@app.route('/')
def index():
    return render_template('index.html')




@app.route("/send")
def home():
  line_bot_api = LineBotApi('J+p8JesDYQwMZMNO8Sx4oyAhH7TwVk4EoTRb8AJM0+ZJ4uROv/5dDvXQHhOQBkmqav7UHB0WCRvE+eWfj+FDFsyWtp6FkIh6GUvbTYE7Rvs67Ah1+ylvChWRcAiiHzsjjVj5EOClpGYQMT0RzZhzIgdB04t89/1O/w1cDnyilFU=')
  try:
    # 網址被執行時，等同使用 GET 方法發送 request，觸發 LINE Message API 的 push_message 方法 userID=='Uaf1c91579f554baa611bd9218ef373fa'
    line_bot_api.push_message('Uaf1c91579f554baa611bd9218ef373fa', TextSendMessage(text='阿涵,我成功了'))
    return '發送QQ'
  except:
    print('error')




if __name__ == "__main__":
    app.run(debug=True)
