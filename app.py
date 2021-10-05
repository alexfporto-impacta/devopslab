from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World!! Comando para correção do erro de SSL https://docs.travis-ci.com/user/reference/focal/"

if __name__ == '__main__':
    app.run(debug=True)