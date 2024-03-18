from flask import Flask, render_template, request
#import webbrowser
#import time
import openai


str1 = 'sk-6DurzFcba69Gqq8KkZeAT3B'
str2 = 'lbkFJYWeBEwHHM'
str3 = 'JVnBzt79unM'

app = Flask (__name__)
@app.route ('/')
def index ():
    return render_template('index2.html')

@app.route('/', methods=['POST'])
def getvalue():
    #name = request.form['name']
    #age = request.form['age']
    chatgpt = request.form ['chatgpt']
    #db = request.form ['dateofbirth']

    openai.api_key = str1 + str2 + str3
    x = chatgpt
    #"Give me 7 ideas for a date in Paris"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": x}])
    y = [completion.choices[0].message.content]
    #print(name)
    #print(y)
    return render_template ('index2.html', chatgpt_question=chatgpt,  chatgpt_output=y)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')