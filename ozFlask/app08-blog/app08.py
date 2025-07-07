import yaml
from flask import Flask, render_template
from flask_smorest import Api
from flask_mysqldb import MySQL
from postsRoutes import createPostsBlp


app = Flask(__name__)

db = yaml.load(open("db.yaml"), Loader = yaml.FullLoader)
app.config['MYSQL_HOST'] = db["mysqlHost"]
app.config['MYSQL_USER'] = db["mysqlUser"]
app.config['MYSQL_PASSWORD'] = db["mysqlPassword"]
app.config['MYSQL_DB'] = db["mysqlDB"]

mysql = MySQL(app)

# Blueprint 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
postsBlp = createPostsBlp(mysql)
api.register_blueprint(postsBlp)

if __name__ == "__main__":
    app.run(debug = True)