from flask import Flask, render_template
from replit import db

app = Flask(__name__)


if 'number' not in db:
  db['number'] = 0

@app.route('/')
def home():
    return render_template('index.html', number=db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  return render_template('index.html', number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  return render_template('index.html', number=db['number'])
  
app.run(host='0.0.0.0', port=81)


##html
  # <link rel="stylesheet" href="./static/counter_styles.css">
    
  #   <span>{{ number }}</span>
  #   <div>
  #   <form action="/decrement">
  #     <button id='increment'>-</button>
  #   </form>
  #   <form action="/increment">
  #     <button id='decrement'>+</button>
  #   </form>
  #   </div>
