FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 10001 bot

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Main.py Base_Commands.py Config.py Processing_Search_Price.py ./
COPY Images/ Images/

ENV CHROMIUM_NO_SANDBOX=1
USER bot
CMD ["python", "Main.py"]
