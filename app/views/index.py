from flask import Blueprint

index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET'])
def home():
    return 'API it is Working...! - v1.1'
