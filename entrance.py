from flask import Flask, request, render_template , jsonify

from predict import DressLengthClassifier, PantsLengthClassifier , SleeveLengthClassifier

path = '/Users/ousheobin/developer/Server/dress/'
# path = '/deeplearning/dress_upload/'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def cls():
    if request.files.get('file'):
        file = request.files.get('file')
        file.save(path+file.filename)
        skirtAndPantLegnth = DressLengthClassifier.predict(path + file.filename)
        sleeveLength = SleeveLengthClassifier.predict(path + file.filename)
        return jsonify({
            'skirtAndPantLegnth': skirtAndPantLegnth ,
            'sleeveLength': sleeveLength
        })
        # return render_template('result.html', **locals())
    else:
        return index()


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="10.11.3.250", debug=False)