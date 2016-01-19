#!/usr/bin/env bash
set -e

VERSION="${VERSION:-0.0.0-0}"
ret=0

if ! {
    set -x
    rpmdev-setuptree
    ln -s `pwd`/rpm/i2pd.spec ~/rpmbuild/SPECS/
    ln -s `pwd`/systemd/* ~/rpmbuild/SOURCES/
    tar czf ~/rpmbuild/SOURCES/i2pd-${VERSION}.tgz .
    sed -ie "s|^Version:.\+|Version: ${VERSION%%-*}|" rpm/i2pd.spec
    sed -ie "s|^Release:.\+|Release: ${VERSION##*-}|" rpm/i2pd.spec
    cd ~/rpmbuild/SPECS
    rpmbuild -ba i2pd.spec
    set +x
} 1> build-rpm.builder.log
then
    ret=1
    tail -n 50 build-rpm.builder.log
fi

tar c ~/rpmbuild/{RPMS,SRPMS}
exit $ret
