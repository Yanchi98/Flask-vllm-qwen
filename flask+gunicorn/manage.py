from flask import Flask, g
import os
from service import predict_bp
from service.predict import G_model
from modelscope.hub.snapshot_download import snapshot_download
from utils import get_root_path


def create_app():
    app = Flask(__name__)

    app.register_blueprint(predict_bp, url_prefix='/predict')

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='6007')