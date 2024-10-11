# Flask-vllm-qwen deployment
program self-use，vllm infer, Flask api

# Hardware
RTX 4090D * 1卡 26G

# Env requirements
pip install -r requirements.txt

注意: vllm >= 0.5.5才支持vLLM.chat

https://docs.vllm.ai/en/v0.5.5/dev/offline_inference/llm.html

# Run service
bash.start.sh

if need model download:

`
service.view.py
if not os.path.exists('/root/autodl-tmp/model/Qwen'):
    snapshot_download('qwen/Qwen2-7B-Instruct', cache_dir='/root/autodl-tmp/model')
G_model.load_model('/root/autodl-tmp/model/Qwen/Qwen2-7B-Instruct')
`

# Request

body：input(needed)，request_metadata(optional)

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

# Update
9.6: update output json format, vllm>=0.5.5
`
return Response(str(result), mimetype='application/json')
return Response(json.dumps(result), mimetype='application/json')`
