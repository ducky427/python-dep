#!/bin/sh

mkdir -p /root/.pip/wheels

apt-get install build-essential \
                tmux \
                htop \
                python-dev \
                libxml2-dev \
                libxslt-dev \
                libsqlite3-dev \
                libpq-dev \
                libmysqlclient18 \
                mysql-common \
                libevent-dev \
                libzmq-dev \
                libmemcached-dev \
                libssl1.0.0 \
                libc6 \
                swig \
                libfreetype6 \
                libfreetype6-dev \
                libpng12-0 \
                libpng12-dev \
                tk8.5 \
                tcl8.5 \
                libqt4-gui

