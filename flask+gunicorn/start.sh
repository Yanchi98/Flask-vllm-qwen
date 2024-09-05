# 安装依赖
pip install -r requirements.txt

gunicorn -w 1 -b 127.0.0.1:6006 manage:app
