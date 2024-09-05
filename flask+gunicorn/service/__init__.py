from flask import Blueprint

predict_bp = Blueprint('predict', __name__)

from . import views