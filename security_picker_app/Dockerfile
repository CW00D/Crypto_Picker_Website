# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /security_picker_app

COPY pyproject.toml requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements.txt

COPY src/ src/
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels .
RUN ls -R /security_picker_app


# Stage 2: Runner
FROM python:3.12-slim AS runner

WORKDIR /security_picker_app

COPY --from=builder /security_picker_app/wheels /wheels
RUN pip install --no-cache /wheels/* && pip list

COPY src/ src/
ENV FLASK_APP=/security_picker_app/src/app/main.py

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]