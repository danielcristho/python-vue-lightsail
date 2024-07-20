# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app
COPY requirements-dev.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements-dev.txt

COPY . .

ENV FLASK_APP wsgi.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 5000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]

FROM builder AS dev-envs

RUN <<EOF
apk update
apk add git
EOF

CMD ["flask", "run"]