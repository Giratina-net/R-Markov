FROM debian:bullseye-slim
RUN apt update -y && apt install -y mecab swig libmecab-dev mecab-ipadic-utf8 libmecab-dev mecab-ipadic python3 python3-pip
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3","run.py"]