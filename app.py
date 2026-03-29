from flask import Flask, render_template
import pandas as pd
from utils.map_utils import create_map

app = Flask(__name__)

@app.route('/')
def home():
    data = pd.read_csv('data/dataset.csv')
    map_html = create_map(data)
    return render_template('index.html', map=map_html)

if __name__ == '__main__':
    app.run(debug=True)