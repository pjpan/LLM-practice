#!/usr/bin/env bash

python3.9 -m vllm.entrypoints.openai.api_server \
    --model  Qwen/Qwen-7B-Chat\
    --tokenizer Qwen/Qwen-7B-Chat\
    --trust-remote-code  \
    --tensor-parallel-size 1