FROM nvidia/cuda:11.7.1-runtime-ubuntu20.04

RUN apt-get update -y && apt-get install -y python3.9 python3.9-distutils curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.9 get-pip.py
RUN pip3 install fschat[model_worker,webui] pydantic==1.10.13  vllm -i  http://mirrors.aliyun.com/pypi/simple/ --no-cache-dir --trusted-host mirrors.aliyun.com

RUN export http_proxy=http://10.110.63.27:8080
RUN export https_proxy=http://10.110.63.27:8080

WORKDIR /app
# copy local requirments
COPY requirements.txt requirements.txt
# install requirement python packages
RUN pip install --upgrade pip -i  http://mirrors.aliyun.com/pypi/simple/ --no-cache-dir --trusted-host mirrors.aliyun.com \
    && pip install -r requirements.txt -i  http://mirrors.aliyun.com/pypi/simple/ --no-cache-dir --trusted-host mirrors.aliyun.com
#ENV MODEL_NAME=Qwen/Qwen-7B-Chat  TOKENIZER=Qwen/Qwen-7B-Chat
COPY . .

# 暴露8000端口
EXPOSE 8000

# 执行CMD
CMD ["sh", "start_qwen_server.sh"]