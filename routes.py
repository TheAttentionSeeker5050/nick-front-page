# have the routes here
from flask import Blueprint

# import render_template
from flask import render_template
# impor request object
from flask import request

main_bp = Blueprint('/', __name__)

@main_bp.route('/')
def index():
    # if get 
    if request.method == 'GET':
        # render the index.html
        return render_template('index.html')
    else:
        return render_template('invalid_method.html')


# @main_bp.route('/invalid_method')
# def invalid_method():
#     return render_template('invalid_method.html')