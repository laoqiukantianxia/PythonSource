FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /code
CMD ["python", "run.py", "--fbidhttp=False", "--logging=debug"]
