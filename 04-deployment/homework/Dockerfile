FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

# do stuff here
RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

COPY ["starter_app.py","./"]

RUN pipenv install --system --deploy

EXPOSE 9696
ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "starter_app:app"]