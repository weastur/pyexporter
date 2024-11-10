ARG PYTHON_VERSION="3.9"
ARG UV_VERSION="latest"

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv
FROM python:${PYTHON_VERSION}-slim-bookworm

LABEL org.opencontainers.image.authors="Pavel Sapezhka <me@weastur.com>"
LABEL org.opencontainers.image.created=2024-10-23T09:13:54Z
LABEL org.opencontainers.image.url=https://pyexporter.weastur.com
LABEL org.opencontainers.image.documentation=https://pyexporter.weastur.com
LABEL org.opencontainers.image.source=https://github.com/weastur/pyexporter
LABEL org.opencontainers.image.version=0.0.0-dev0
LABEL org.opencontainers.image.licenses=MIT

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV TERM=xterm-color

ARG APP_USER=app
ARG APP_USER_UID=1010
ARG APP_USER_GID=${APP_USER_UID}
ARG APP_HOME=/${APP_USER}
RUN mkdir -p ${APP_HOME} \
    && groupadd --gid ${APP_USER_GID} ${APP_USER} \
    && useradd --uid ${APP_USER_UID} --gid ${APP_USER_GID} -m ${APP_USER} -s /bin/bash \
    && chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

USER ${APP_USER}

WORKDIR ${APP_HOME}

COPY --from=uv /uv /uvx /bin/

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD --chown=${APP_USER_UID}:${APP_USER_GID} . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 9123

ENTRYPOINT ["py-exporter"]
