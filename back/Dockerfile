FROM python:3.8-alpine

WORKDIR /back

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install flask
RUN pip install flask_cors

EXPOSE 5000

CMD ["python","server.py"]


