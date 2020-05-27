from flask import Blueprint, render_template, request, redirect, url_for, current_app
from .extensions import db
from .models import Link
from .auth import requires_auth

#https://web.archive.org/web/20190128005233/http://flask.pocoo.org/snippets/ hazır kodlar
short = Blueprint('short', __name__) #linkleri grupladık

"""
Htpp rec header 
{
"user-agent":,
"accept":,
"host":,
"cookie": "session=12345"
}

node üzerinde client-sessions
"""

@short.route("/<short_url>")
def redirect_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    original_url = link.original_url
    if original_url.find("http://") != 0 and original_url.find("https://") != 0:
        original_url = "https://" + original_url
    link.visit = link.visit + 1
    db.session.commit()

    return redirect(original_url)


@short.route("/")
def index():

    return render_template("index.html")


@short.route("/add_link", methods=['POST'])
def add_link():
    original_url = request.form["original_url"]
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template("link_added.html", new_link=link.short_url, original_url=link.original_url)


@short.route("/stats")
@requires_auth
def stats():
    links = Link.query.all()
    return render_template("stats.html", links=links)


@short.errorhandler(404)
def page_not_found(e):
    return "Link oluşturulmadı", 404
