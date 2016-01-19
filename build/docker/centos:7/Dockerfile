FROM centos:7
MAINTAINER scrapy <scrapy@i2pmail.org>
WORKDIR /tmp
RUN usermod -d /tmp nobody && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-* && \
    yum update -y && \
    yum install -y \
         make \
         gcc \
         gcc-c++ \
         boost-devel \
         openssl-devel \
         miniupnpc-devel \
         git \
         rpmdevtools \
         && yum clean all

# Centos 7 has old CMake version, we will repack fc21 2.8.12 CMake here
RUN curl -Ls https://kojipkgs.fedoraproject.org/packages/cmake/2.8.12/3.fc21/src/cmake-2.8.12-3.fc21.src.rpm > cmake-2.8.12-3.fc21.src.rpm && \
    yum-builddep -y cmake-2.8.12-3.fc21.src.rpm \
    && yum clean all
USER nobody
RUN rpmbuild --rebuild cmake-2.8.12-3.fc21.src.rpm
USER root
RUN yum install -y rpmbuild/RPMS/x86_64/cmake-2.8.12-3.el7.centos.x86_64.rpm && \
    rm -rf rpmbuild && \
    && yum clean all

USER nobody
