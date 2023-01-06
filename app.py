from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def index():
    stats = os.popen("vnstat --oneline").read().split(',')
    tx = stats[9]
    return tx


if __name__ == '__main__':
    app.run()
