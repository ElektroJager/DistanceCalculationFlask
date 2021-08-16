## Flask Modules
from flask import Flask, render_template, request

## Import Blueprint
from distance_blueprint import distance_blueprint

app = Flask(__name__)
app.register_blueprint(distance_blueprint)

if __name__ == '__main__':
   app.run(debug = True)