FROM ubuntu:trusty
MAINTAINER scrapy <scrapy@i2pmail.org>
WORKDIR /tmp
RUN usermod -d /tmp nobody && \
    apt-get update -qq && \
    apt-get install -y --force-yes \
            libboost-chrono-dev \
            libboost-date-time-dev \
            libboost-filesystem-dev \
            libboost-program-options-dev \
            libboost-regex-dev \
            libboost-system-dev \
            libboost-thread-dev \
            libssl-dev \
            libminiupnpc-dev \
            build-essential \
            cmake \
            git \
            fakeroot \
            devscripts \
    && apt-get clean
USER nobody
