FROM fedora:23
MAINTAINER scrapy <scrapy@i2pmail.org>
WORKDIR /tmp
RUN usermod -d /tmp nobody && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-* && \
    dnf update -y && \
    dnf install -y \
         make \
         cmake \
         gcc \
         gcc-c++ \
         rpmdevtools \
         boost-devel \
         openssl-devel \
         miniupnpc-devel \
         git \
         rpm-build \
         && dnf clean all
USER nobody
