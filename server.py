from flask import Flask, render_template

# Короч, если надо запустить, зажимаешь ctrl+shift+P создаёшь новый терминал python и в этом терминале прописываешь flask --app server --debug run

app = Flask(__name__)

nav = [
    {"title" : "Главная", "URL" : "/"},
    {"title" : "Обо мне", "URL" : "/about_me"},
    {"title" : "Звёздные войны", "URL" : "/star_wars"},
    {"title" : "Словарь", "URL" : "/glossary"}
]
nav_dropdown = [
    {"title" : "Дарт Вейдер", "URL" : "/vader"},
    {"title" : "Люк Скайуокер", "URL" : "/luk"},
    {"title" : "Дарт Сидиус", "URL" : "/sidius"}
]

links = {
    "Дарт Вейдер" : "https://starwars.fandom.com/ru/wiki/%D0%AD%D0%BD%D0%B0%D0%BA%D0%B8%D0%BD_%D0%A1%D0%BA%D0%B0%D0%B9%D1%83%D0%BE%D0%BA%D0%B5%D1%80/%D0%9A%D0%B0%D0%BD%D0%BE%D0%BD#%D0%92%D0%BE%D0%B7%D0%B2%D1%8B%D1%88%D0%B5%D0%BD%D0%B8%D0%B5_%D0%94%D0%B0%D1%80%D1%82%D0%B0_%D0%92%D0%B5%D0%B9%D0%B4%D0%B5%D1%80%D0%B0", 
    "Люк Скайуокер" : "https://starwars.fandom.com/ru/wiki/%D0%9B%D1%8E%D0%BA_%D0%A1%D0%BA%D0%B0%D0%B9%D1%83%D0%BE%D0%BA%D0%B5%D1%80/%D0%9A%D0%B0%D0%BD%D0%BE%D0%BD?so=search#%D0%98%D0%B7%D0%B3%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_%D0%90%D0%BA-%D0%A2%D0%BE", 
    "Дарт Cидиус" : "https://starwars.fandom.com/ru/wiki/%D0%A8%D0%B8%D0%B2_%D0%9F%D0%B0%D0%BB%D0%BF%D0%B0%D1%82%D0%B8%D0%BD"}
@app.context_processor
def global_context():
    return {
        "nav" : nav,
        "nav_dropdown" : nav_dropdown,
        "links" : links
    }

@app.route("/")
def index_view():
    return render_template("index.html", name = "Главная")

@app.route("/about_me")
def about_view():
    return render_template("about_me.html", name = "Обо мне")

@app.route("/star_wars")
def star_wars_view():
    return render_template("star_wars.html", name = "Звёздные войны")

@app.route("/glossary")
def glossary_view():
    return render_template("glossary.html", name = "Словарь")

@app.route("/vader")
def vader_view():
    return render_template("vader.html", name = "Дарт Вейдер")

@app.route("/sidius")
def sidius_view():
    return render_template("sidius.html", name = "Дарт Cидиус")

@app.route("/luk")
def luk_view():
    return render_template("luk.html", name = "Люк Скайуокер")