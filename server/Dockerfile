FROM python:3.7 as server

WORKDIR /server

RUN apt-get update

COPY . .

RUN pip install -r requirements.txt
ENV PYTHONPATH=/server/src

CMD ["python", "-u", "/server/src/app.py"]