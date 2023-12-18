FROM python:3.9-slim

WORKDIR /app

RUN pip install \
    Flask==2.2.0 \
    redis==3.5.3 \
    Werkzeug==2.3.0 \
    Flask_Injector==0.15.0

ADD *.py ./app

CMD python3 tracking.py --reload
