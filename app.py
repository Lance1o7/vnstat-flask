from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route('/')
def index():
    stats = os.popen("vnstat --oneline").read().split(';')
    tx = float(stats[9][0:-4])
    return render_template('index.html', tx=tx, tx_p=tx/1000.0)


if __name__ == '__main__':
    app.run()
