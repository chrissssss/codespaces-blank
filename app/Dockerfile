# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:latest

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt update && \
    apt install -y openssh-client python3-pip python3 

# Install pip requirements
COPY app/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser --home /home/appuser -u 5678 --disabled-password --gecos "" appuser && \
    chown -R appuser /app && \
    mkdir -p /home/appuser/.ssh

# Setup ssh public key
COPY shared/ssh-keys/id_rsa /home/appuser/.ssh

RUN chown appuser:appuser /home/appuser/.ssh/id_rsa 

USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "app.py"]
