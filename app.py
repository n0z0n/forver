from flask import Flask, request, jsonify
from yapf.yapflib.yapf_api import FormatCode
app = Flask(__name__)


@app.route("/", methods=['POST'])
def webhook():
    print(request.form)
    print(request.files)
#    formatedObj = FormatCode(request.json["src"], style_config='pep8')
#    response = dict(formated=formatedObj[0], status=formatedObj[1])
#    return jsonify(response)
    return ""


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
