

import flask

app = flask.Flask(__name__)

Anime =["One Piece", "Bleach", "Hunter x Hunter", "Fate stay night ", 
              "Evangelion"]
              

@app.route("/")
def index():
  
    return flask.render_template("index.html", len = len(Anime), Anime = Anime)

app.run(use_reloader = True, debug = True)

