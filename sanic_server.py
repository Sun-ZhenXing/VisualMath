from sanic import Request, Sanic, json
from sanic.response import redirect

from visualmath import compute

app = Sanic('app')
app.static('', './static')


@app.route('/', methods=['GET'])
async def index_(request: Request):
    return redirect('/index.html')


@app.route('/compute', methods=['POST'])
async def compute_(request: Request):
    return json(compute(request.json['text']))


if __name__ == '__main__':
    app.run('127.0.0.1', 3389, fast=True)
