FROM python:3.8

WORKDIR /back

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install flask
RUN pip install flask_cors
RUN pip install waitress
RUN pip install pandas
RUN pip install matplotlib
RUN pip install scikit-learn 

EXPOSE 5000

CMD ["python","server.py"]


