from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Cao Rale!</h1>"
