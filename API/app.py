from flask_restful import Api,Resource
from flask import Flask,make_response,render_template
from flask_cors import CORS
import googletrans


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
rest_api = Api(app)

class LanguageList(Resource):
    def post(self):
        return {"langs":list(googletrans.LANGUAGES.values())}
    def get(self):
        return {"langs":list(googletrans.LANGUAGES.values())}

class TranslateText(Resource):
    def get(self,word,lang):
        response = make_response({"result" : googletrans.Translator().translate(text=word,dest=lang).text})
        return response
    
rest_api.add_resource(LanguageList,"/langlist")
rest_api.add_resource(TranslateText,"/translate/<string:word>/<string:lang>")
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def homePage():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
