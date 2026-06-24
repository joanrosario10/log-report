# Pinned by digest for a reproducible agent + verifier environment.
# python:3.13-slim-bookworm (multi-arch index digest, resolved from Docker Hub).
FROM python:3.13-slim-bookworm@sha256:05b95397cac02b060ff1251afaa78087d92d7034369afbc8eb765631cada8257

# Verifier dependencies are baked in so the verify phase performs no installs.
# pytest-json-ctrf provides the --ctrf flag used to emit /logs/verifier/ctrf.json.
RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

# Only the task input ships in the agent image. No solution is copied in.
COPY access.log /app/access.log
