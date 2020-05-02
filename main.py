from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/blogs.sqlite')
    global session
    session = db_session.create_session()
    app.run()


@app.route('/')
def start():
    default = session.query(Jobs, User).outerjoin(User, Jobs.team_leader == User.id).all()
    return render_template('login.html', users=default)


if __name__ == '__main__':
    main()