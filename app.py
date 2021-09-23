from flask import Flask, request, render_template

from utils import read_users, write_users

app = Flask(__name__)
users = read_users()

@app.route('/')
def index():
    return render_template('index.html', users=users)


@app.route('/search', methods = ['GET', 'POST'])
def search_page():
    if request.method == 'POST':
        found_users = []
        text = request.form.get("seek_req")
        if text:
            for user in users:
                if text in user['name']:
                    found_users.append(user)
        return render_template('search.html', users=users, found_users=found_users)
    return render_template('search.html')


@app.route('/add_user', methods = ['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get('age')
        is_blocked = request.form.get('is_blocked')
        date = request.form.get('unblock_date')
        users = write_users(name, age, is_blocked, date)
        return '''<p> пользователь добавлен</p>
                 <a href="/">Вернутся на главную</a>
                '''
    return render_template('add_user.html')


if __name__ == '__main__':
    app.run()

