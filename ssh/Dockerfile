FROM ubuntu:latest

COPY shared/ssh-keys/id_rsa.pub /keys/

# Update package list and install [openssh-server, sudo]
RUN apt update && \
    apt install  openssh-server sudo -y && \
# Configure user test with password test
    useradd -rm -d /home/test -s /bin/bash -g root -G sudo -u 1000 test && \
    echo 'test:test' | chpasswd && \
# Add ssh key
    mkdir -p /home/test/.ssh/ && \
    chmod 0700 /home/test/.ssh  && \
    touch /home/test/.ssh/authorized_keys && \
    chmod 600 /home/test/.ssh/authorized_keys && \
    cat /keys/id_rsa.pub >> /home/test/.ssh/authorized_keys && \
# Start ssh
    service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]

