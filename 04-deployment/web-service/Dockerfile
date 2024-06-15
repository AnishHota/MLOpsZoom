FROM python:3.10.14-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["predict.py","lr_model.bin","./"]

EXPOSE 9696

ENTRYPOINT [ "waitress-serve","--listen=0.0.0.0:9696", "predict:app" ]
