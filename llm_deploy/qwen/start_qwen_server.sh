#!/usr/bin/env bash

python3.9 -m vllm.entrypoints.openai.api_server \
    --model  Qwen/Qwen-14B-Chat\
    --tokenizer Qwen/Qwen-14B-Chat\
    --trust-remote-code       \
    --tensor-parallel-size 1   \
    --tokenizer-mode  auto    \
    --gpu-memory-utilization  0.8 \
    --port 8000     \
    --host 0.0.0.0