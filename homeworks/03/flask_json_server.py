from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    #TODO прочитать из полученного запроса json-контент
    #В случае, если version==1, то должен вернуться json с версией и полем predict из входящего jsonа {"version":1, "predict":<predict_value>}
    #В случае, если version==0, то должен вернуться json с версией и полем old_predict из входящего jsonа {"version":0, "predict":<old_predict_value>}
    if request.method == 'POST':
        if int(version) == 1:
            return jsonify(version = 1, predict = request.get_json()['predict'])
        else:
            return jsonify(version = 0, predict = request.get_json()['old_predict'])

@app.route("/")
def hello():
    return '''Привет, я простой и бесполезный сайт, принимаю POST-запросы с JSON, содержащим поля predict и/или old_predict. Если тебе зачем-то понадобилось поле predict, которое ты сам мне отправляешь, отправляй запрос на /get_classifier_result/1. Если же тебе нужно поле old_predict, то запрос нужно отправить на /get_classifier_result/0. Ответочка прилетит в формате JSON в виде {"version" : <value>, "predict" : <value>}
    P.S. reddit.com/r/aww/comments/9sh2jc/catching_the_fishy'''

if __name__ == "__main__":
    app.run()
