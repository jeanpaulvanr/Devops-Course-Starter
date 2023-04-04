FROM python:3.8 as base
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
WORKDIR /opt/todoapp
COPY .env.test poetry.lock pyproject.toml /opt/todoapp/
RUN poetry install
EXPOSE 5000

FROM base as production

COPY ./todo_app /opt/todoapp/todo_app
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:5000 "todo_app.app:create_app()"

FROM base as development
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as test
COPY ./todo_app /opt/todoapp/todo_app
ENTRYPOINT ["poetry", "run", "pytest"]