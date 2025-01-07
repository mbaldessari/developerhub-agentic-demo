FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /projects

# By default, listen on port 8080
EXPOSE 8080/tcp
ENV FLASK_PORT=8080

# Copy the dependencies file to the working directory
COPY agent .

# Install any dependencies
RUN pip install -r requirements.txt

# Specify the command to run on container start
CMD ["python", "main.py"]
