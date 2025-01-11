FROM python:3.13-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir poetry

ENV INVENTORY_STATIC_FILES=/static INVENTORY_MEDIA_FILES=/media
RUN mkdir -p "$INVENTORY_MEDIA_FILES" && mkdir -p "$INVENTORY_STATIC_FILES"

COPY pyproject.toml /usr/src/app
COPY poetry.lock /usr/src/app

RUN poetry install --no-root --no-interaction --no-cache
COPY manage.py ./manage.py
COPY inventory ./inventory
COPY inventory_project ./inventory_project
COPY entrypoint.sh /entrypoint.sh

RUN poetry run python manage.py collectstatic

CMD [ "/bin/sh", "/entrypoint.sh" ]