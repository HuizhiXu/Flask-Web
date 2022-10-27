import click

from watchlist import app, db
from watchlist.models import User, Movie


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
def forge():
    db.create_all()

    name = 'Charlie'
    movies = [
        {'title': '肖申克的救赎', 'year': '1994'},
        {'title': '霸王别姬', 'year': '1993'},
        {'title': '阿甘正传', 'year': '1994'},
        {'title': '泰坦尼克号', 'year': '1997'},
        {'title': '这个杀手不太冷', 'year': '1994'},
        {'title': '美丽人生', 'year': '1997'},
        {'title': '千与千寻', 'year': '2001'},
        {'title': '辛德勒的名单', 'year': '1993'},
        {'title': '盗梦空间', 'year': '2010'},
        {'title': '星际穿越', 'year': '2014'},
    ]

    user=User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help = 'The username used to login.')
@click.option('--password', prompt=True, hide_input=True,confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    db.create_all()

    user=User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)

    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('Done.')