FROM ubuntu:latest

COPY shared/ssh-keys/id_rsa.pub /keys/

RUN apt update && \
    apt install  openssh-server sudo -y && \
    useradd -rm -d /home/test -s /bin/bash -g root -G sudo -u 1000 test && \
    echo 'test:test' | chpasswd && \
    mkdir -p /home/test/.ssh/ && \
    chmod 0700 /home/test/.ssh  && \
    touch /home/test/.ssh/authorized_keys && \
    chmod 600 /home/test/.ssh/authorized_keys && \
    cat /keys/id_rsa.pub >> /home/test/.ssh/authorized_keys && \
    service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]

