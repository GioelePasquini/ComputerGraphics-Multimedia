# caricare questo file su colab nella cartella input come dataset ed eseguire il blocco note

import flask, logging, ngrok

if __name__ == '__main__':
    ngrok.set_auth_token("2h5uqCeg949GltwEdN8VJXI2JZu_6EoRANAJJnHon5k6HTC53")  # Replace with your ngrok token
    logging.basicConfig(level=logging.INFO)
    listener = ngrok.werkzeug_develop()
    print(listener.url())
    app = flask.Flask(__name__)


    @app.route("/")
    def hello():
        return "Hello, World!"


    app.run(debug=True)
