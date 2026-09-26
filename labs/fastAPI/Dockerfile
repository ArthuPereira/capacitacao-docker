FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv sync

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app","--host", "0.0.0.0","--port", "8000", "--reload"]