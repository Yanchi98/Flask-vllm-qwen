from . import predict_bp
from .predict import G_model
from flask import Flask, request, Response, abort
import time
import os
import json

@predict_bp.route('/', methods=['POST'])
def predict():
    # 获取并解析请求的 JSON 数据
    request_data = request.get_json()
    if not request_data:
        return Response("{'code': '400', 'msg': '请求数据格式错误'}", mimetype='application/json')

    # 从请求中提取输入参数
    input_data = request_data.get('input', {})
    prompt = input_data.get('prompt')
    max_tokens = input_data.get('max_tokens', 512)
    temperature = input_data.get('temperature', 0.8)
    top_p = input_data.get('top_p', 0.95)

    # 日志输出用户输入
    print("用户输入:", prompt)

    # 调用模型进行推理
    start = time.time()
    res = G_model.get_completion(
        prompts=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p
    )
    end = time.time()

    # 推理耗时输出
    print('推理耗时:', end - start)

    # 返回响应数据
    result = {
        "code": "200",
        "msg": "响应成功",
        "data": res
    }

    return Response(json.dumps(result), mimetype='application/json')

if not os.path.exists('/root/autodl-tmp/model/Qwen'):
    snapshot_download('qwen/Qwen2-7B-Instruct', cache_dir='/root/autodl-tmp/model')
G_model.load_model('/root/autodl-tmp/model/Qwen/Qwen2-7B-Instruct')
