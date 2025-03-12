FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS base

WORKDIR /app

# ---- MINIMAL DEPENDENCIES ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ---- ENVIRONMENT VARIABLES ----
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    VIRTUAL_ENV="/app/.venv" \
    PYTHONPATH="/app" \
    UV_CACHE_DIR=/opt/uv-cache \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

# ---------------------
# ---- BUILD STAGE ----
# ---------------------

#FROM base AS node
#
## ---- BUILD-ESSENTIALS ----
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    curl \
#    nodejs \
#    npm \
#    && rm -rf /var/lib/apt/lists/*
#
## ---- BUILD FRONTEND ----
#COPY package.json package-lock.json ./
#COPY postcss.config.js tailwind.config.js ./
#RUN npm install
#
#COPY . .
#RUN npm run build

# ---------------------
# ----- DEV STAGE -----
# ---------------------
FROM base AS development

# ---- DEVELOPMENT-ESSENTIALS ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    npm \
    vim \
    sudo \
    && rm -rf /var/lib/apt/lists/*


RUN useradd -m devuser && \
    echo "devuser ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/devuser && \
    chmod 0440 /etc/sudoers.d/devuser

#COPY --from=node /app .
COPY . .

# ---- CACHE-CONFIGURATION ----
RUN --mount=type=cache,target=/opt/uv-cache \
    uv sync

# ---- DEVELOPMENT-MODE SETUP ----
RUN chown -R devuser:devuser /app
USER devuser
# RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

## ---------------------
## ----- PROD STAGE ----
## ---------------------
#FROM base AS production
#
## ---- RUNTIME-ESSENTIALS ----
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    nodejs \
#    xvfb \
#    melt \
#    python3-mlt \
#    frei0r-plugins \
#    bs2b-ladspa \
#    && apt-get upgrade -y \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*
#
#COPY --from=node /app .
#
## ---- NON-ROOT USER ----
#RUN useradd -m produser && \
#    chown -R produser:produser /app && \
#    chmod -R ugo-w /app
#
#USER produser
#
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]