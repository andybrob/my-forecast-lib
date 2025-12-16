FROM python:3.9-slim

WORKDIR /app

# Install third-party deps first for caching
COPY requirements.lock.txt /app/
RUN pip install --no-cache-dir -r requirements.lock.txt

# Copy package metadata + source, then install your package
COPY pyproject.toml README.md /app/
COPY src /app/src
RUN pip install --no-cache-dir .

ENTRYPOINT ["forecast-lib"]
