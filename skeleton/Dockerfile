FROM registry.access.redhat.com/ubi9/python-311

# Install system dependencies
USER root
RUN dnf install -y gcc libffi-devel openssl-devel && \
    dnf clean all

# Set working directory
WORKDIR /app


# Copy application files
COPY ./agent .

# Copy and install Python dependencies
#COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# By default, listen on port 8080
EXPOSE 8080

# Set default command
CMD ["python", "main.py"]