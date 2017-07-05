from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="POST">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign in</button></p>
              </form>'''

@app.route('/signin', methods=["POST"])
def signin():
    # 需要从request中读取信息
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Welcome, admin!</h3>'
    return '<h3>bad username or password</h3>'

if __name__ == '__main__':
    app.run()