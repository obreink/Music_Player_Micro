FROM python:3.12-slim
WORKDIR /root
RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app/catalog-app.py"]