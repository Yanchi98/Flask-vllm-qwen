# vllm_model.py
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
import os
import json
from utils import get_root_path
from modelscope.hub.snapshot_download import snapshot_download


class Qwen7BInfer:
    def __init__(self):
        self.model = 'autodl-tmp/model/qwen/Qwen2-7B-Instruct'
        self.llm = None

    def load_model(self, path, tokenizer=None, max_tokens=512, temperature=0.8, top_p=0.95, max_model_len=2048):
        self.llm = LLM(model=path, tokenizer=tokenizer, max_model_len=max_model_len, trust_remote_code=True,
                       gpu_memory_utilization=0.9, enforce_eager=True)
        print("加载模型成功！")

    def get_completion(self, prompts, max_tokens=512, temperature=0.1, top_p=0.95, max_model_len=2048):
        # 创建采样参数，确保接收到的参数被应用
        sampling_params = SamplingParams(
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens
        )

        # 将输入的 prompt 封装成对话消息格式
        messages = [
            {"role": "system", "content": "你是一个热情、积极向上而客观严谨的接待员，为客人提供问答服务。"},
            {"role": "user", "content": prompts}
        ]

        # 使用模型生成输出，根据传递的采样参数
        try:
            response = self.llm.chat(messages, sampling_params)
        except Exception as e:
            # 可以在这里处理异常，比如记录错误日志
            print(f"模型生成错误: {str(e)}")
            return None

        # 筛选出需要的字段
        output_data = []
        for output in response:
            print(output)
            output_data.append({
                'text': output.outputs[0].text if output.outputs else '',  # 假设 outputs 是非空列表
                'finish_reason': output.outputs[0].finish_reason if output.outputs else 'unknown'
            })

        return output_data


G_model = Qwen7BInfer()