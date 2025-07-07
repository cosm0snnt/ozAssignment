from flask import Flask, render_template

app = Flask(__name__)

# 기본 경로에 대한 라우트
@app.route('/')
def home():
    return 'Hello, this is the home page!'

# 다른 경로에 대한 라우트
# 127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'This is the about page.'

# 127.0.0.1:5000/project
@app.route('/project')
def project():
    return 'The project page'

# 동적인 URL 파라미터 사용
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

# URL에 변수 및 타입 지정
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'