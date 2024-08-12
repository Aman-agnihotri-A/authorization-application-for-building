from flask import Flask , render_template, request

app = Flask(__name__)



def printword(word):
    print(word)


@app.route('/',methods=["GET","POST"])
def hello():
    if request.method=="POST":
        firstname=request.form["firstname"]
        lastname=request.form.get("lastname")
        address=request.form.get("address")
        Phone=request.form.get("phone")
        visitflat=request.form.get("visitflat")
        printword(firstname)
    return render_template('/index.html')


if __name__ == "__main__":
    app.run(port=5000)