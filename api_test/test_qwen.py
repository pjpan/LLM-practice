#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 12:00 下午
# @Author  : ppj
# @File    : test_qwen.py
# @Software: PyCharm

import requests
import json


headers = {"User-Agent": "qwen-clinet"}

# prompt_template

payload = {
    "prompt": "<|im_start|>system\n你现在是一个新能源汽车客服，主要提供车相关的咨询解答服务，我会提供一段客服和用户的聊天记录。请针对这通聊天记录进行摘要，摘要内容要具体和详细，请以json格式返回，json的key为\"follow_up_summary\".<|im_end|>\n<|im_start|>user\n 客服和用户的聊天记录：[{'客服': '嗯。'}, {'用户': '喂。'}, {'客服': '喂，喂，先生，你好，我是那个未来饭店专员，呃，咱们咱们是在那个信溪谷饭店是吧？现在嗯我看是呃，我看好像是博快进单的时候停了是吧嗯？'}, {'用户': '我觉得我嗯。'}, {'用户': '对对对，我刚才。'}, {'用户': '对啊，因为我这个终止了，你要再帮我再再下个单吧，我这已经终止了。'}, {'客服': '终止了是吧？行行，那要不这样，我把订单慢慢取消，然后咱再看咱再试一下，咱这个车上有故障没有，就是雷达故障呀，这些故障嗯。'}, {'用户': '嗯。'}, {'用户': '嗯嗯，好的好的好的。'}, {'用户': '雷达可能右侧那个雷达右前侧的雷达稍微有点问题，但是基本都能换的。'}, {'客服': '哦，他有时候可能雷达报故障，有时候可能也不行。那这样吧，我先我先那个把订单给咱取消，然后咱们重新下个单试一下，是后面好像又又来了个用户换电吧，应该行。嗯，行，那我这样我先给咱把订单取消吧。'}, {'用户': '是便。'}, {'用户': '好的好的好的好的。'}, {'用户': '好像是。'}, {'用户': '嗯嗯嗯。'}, {'客服': '好嗯。'}]<|im_end|>\n<|im_start|>assistant\n",
    "n": 1,
    "use_beam_search": False,
    "temperature": 0,
    "max_tokens": 100,
    "stream": False,
    "stop": ["<|im_end|>", "<|im_start|>",],
    "model": "Qwen/Qwen-14B-Chat"
}

response = requests.post("http://up-llm-qwen-server.p-up-inference.nurss.nioint.com/v1/completions", headers=headers, json=payload, stream=True)

print(json.loads(response.content.decode()))










