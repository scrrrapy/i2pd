Summary: load-balanced unspoofable packet switching network - C++ port
Name: i2pd
Version: 2.2.0
Release: 2
License: BSD3
Source0: %{name}-%{version}-%{release}.tgz
Source1: %{name}.service
Source2: %{name}.tmpfiles.d.conf
Source3: %{name}.default
Packager: scrapy <scrapy@i2pmail.org>
BuildRequires: cmake make gcc boost openssl-devel
%define hardened_build 1
%description
 I2P is an anonymizing network, offering a simple layer that identity-sensitive
 applications can use to securely communicate. All data is wrapped with several
 layers of encryption, and the network is both distributed and dynamic, with no
 trusted parties.

 This package contains the port of the I2P router to C++. Unless willing
 to test and report problems, you should install the 'i2p' package instead.
%prep
%autosetup -c %{name}
%build %{?_smp_mflags}
cd build
cmake -DCMAKE_BUILD_TYPE=Release
make %{name}
%post
%tmpfiles_create %{name}.conf
%systemd_post %{name}.service
#chown -R %{name} %{_sysconfdir}/%{name}
#chmod 700 %{_sysconfdir}/%{name}
#chmod 600 %{_sysconfdir}/%{name}/*
%pre
{
    if ! getent passwd %{name}
    then
        getent group %{name} || groupadd -r %{name}
        mkdir -p /var/lib/%{name}
        useradd -r -g %{name} -s /sbin/nologin -d /var/lib/%{name} -c "%{summary}" %{name}
        chown %{name}:%{name} /var/lib/%{name}
    fi
} > /dev/null
%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%clean
rm -rf $RPM_BUILD_ROOT

%install
install -m0755 -D    build/i2pd                $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m0700 -D    config/i2pd.conf          $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/i2pd.conf
install -m0700 -D    config/tunnels.conf       $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tunnels.conf
install -m0700 -D    config/subscriptions.txt  $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/subscriptions.txt
install -m0700 -D -d contrib/certificates      $RPM_BUILD_ROOT/usr/share/%{name}/certificates
install -m0644 -D -p %{SOURCE1}                $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -m0644 -D -p %{SOURCE2}                $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -m0644 -D -p %{SOURCE3}                $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/i2pd.conf
%config(noreplace) %{_sysconfdir}/%{name}/tunnels.conf
%config(noreplace) %{_sysconfdir}/%{name}/subscriptions.txt
/usr/share/%{name}/certificates/
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sysconfdir}/%{name}
