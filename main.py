from flask import Flask , render_template, request

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def hello():
    if request.method=="POST":
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        address=request.form.get("address")
        Phone=request.form.get("phone")
        visitflat=request.form.get("visitflat")
    return render_template('/index.html')


if __name__ == "__main__":
    app.run(port=5000)