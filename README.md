# Flask-vllm-qwen-
program自用，Flask+vllm推理

# 环境依赖
pip install -r requirements.txt

注意: vllm >= 0.5.5才支持vLLM.chat

https://docs.vllm.ai/en/v0.5.5/dev/offline_inference/llm.html

# 启动服务
bash.start.sh

根据是否存在模型路径判断是否需要下载模型，模型地址修改成自己的地址

`
service.view.py
if not os.path.exists('/root/autodl-tmp/model/Qwen'):
    snapshot_download('qwen/Qwen2-7B-Instruct', cache_dir='/root/autodl-tmp/model')
G_model.load_model('/root/autodl-tmp/model/Qwen/Qwen2-7B-Instruct')
`

# 调用服务

入参：input里的内容必填，request_metadata选填

`
{
    "model_name": "Qwen2-7B-Instruct",
    "input": {
        "prompt": "你好",
        "max_tokens": 500,
        "temperature": 0.1,
        "top_p": 0.1
    },
    "request_metadata": {
        "user_id": "user123",
        "timestamp": "2024-09-05T10:00:00Z"
    }
}
`
