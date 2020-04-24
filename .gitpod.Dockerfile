FROM gitpod/workspace-full-vnc

USER gitpod

RUN sudo apt-get update && sudo apt-get install build-essential checkinstall
RUN sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN cd /usr/src
RUN sudo apt-get install wget
RUN wget https://www.python.org/ftp/python/3.5.6/Python-3.5.6.tgz
RUN sudo tar xzf Python-3.5.6.tgz
RUN cd Python-3.5.6
RUN sudo ./configure --enable-optimizations
RUN sudo make altinstall
