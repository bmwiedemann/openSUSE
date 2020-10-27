#
# spec file for package hiawatha
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013-2020 Mariusz Fik <fisiu@opensuse.org>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define webroot /srv/www
%define mbedtls_version %(rpm -q mbedtls-devel --qf "%%{VERSION}")

Name:           hiawatha
Version:        10.11
Release:        0
Summary:        A secure and advanced webserver
License:        GPL-2.0-only
Group:          Productivity/Networking/Web/Servers
URL:            http://www.hiawatha-webserver.org
Source0:        http://www.hiawatha-webserver.org/files/%{name}-%{version}.tar.gz
Source1:        %{name}.logrotate
Source2:        %{name}.service
Source102:      %{name}.firewalld
Source103:      %{name}-ssl.firewalld
BuildRequires:  cmake >= 3.0
BuildRequires:  firewall-macros
BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel >= 2.3
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Requires:       logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
Hiawatha is a webserver for Unix and has been build with security in mind.

This resulted in a highly secure webserver, in both code and features.

This webserver runs on Linux, BSD, MacOS X and Windows. Although it can run any
kind of CGI / FastCGI application, it has been optimized for usage with PHP.
Most well known PHP frameworks and CMS applications have been tested with
Hiawatha and ran without a problem. Hiawatha supports many web and HTTP features
such as CGI/FastCGI, HTTP authentication, virtual host support, request
pipelining, keep alive connections, URL rewriting and many more.

%package letsencrypt
Summary:        Let's Encrypt script for the Hiawatha webserver
Group:          Productivity/Networking/Web/Servers
Requires:       %{name}
Requires:       php-cli

%description letsencrypt
This is the Let's Encrypt script for the Hiawatha webserver. It can be used to
request, renew and revoke certificated as provided by Let's Encrypt in a very
easy way. It requires the PHP command line interface and uses version 2 of the
ACME protocol to communicate with the Let's Encrypt server.

%prep
%setup -q
# Remove bundled source for mbedtls, we use system version
rm -rv mbedtls

# mbedtls 2.7.0 and its backward comaptybility...
%if "%{mbedtls_version}" >= "2.7.0"
sed -i 's/MBEDTLS_DHM_RFC5114_MODP_2048_P/MBEDTLS_DHM_RFC5114_MODP_P/' src/tls.c
%endif

# disable CHACHA2 cipher, it's not available in Leap 15.0 mbedtls
%if 0%{?suse_version} == 1500
sed '/MBEDTLS_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256/d' -i src/tls.c
sed '/MBEDTLS_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256/d' -i src/tls.c
sed '/MBEDTLS_TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256/d' -i src/tls.c
%endif

%build
%cmake \
    -DCONFIG_DIR="%{_sysconfdir}/hiawatha" \
    -DLOG_DIR="%{_localstatedir}/log/hiawatha" \
    -DPID_DIR="%{_localstatedir}/run" \
    -DWORK_DIR="%{_localstatedir}/lib/hiawatha" \
    -DWEBROOT_DIR="%{webroot}/%{name}/htdocs" \
    -DENABLE_CACHE=On \
    -DENABLE_HTTP2=On \
    -DENABLE_IPV6=On \
    -DENABLE_MONITOR=On \
    -DENABLE_RPROXY=On \
    -DENABLE_TLS=On \
    -DENABLE_TOMAHAWK=On \
    -DENABLE_TOOLKIT=On \
    -DENABLE_XSLT=On \
    -DUSE_SYSTEM_MBEDTLS=On \
    -DUSE_SYSTEM_NGHTTP2=On
%make_jobs

%install
%cmake_install
install -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# run as wwwrun user
sed "s/#ServerId = www-data/ServerId = wwwrun/" -i %{buildroot}%{_sysconfdir}/hiawatha/hiawatha.conf

install -D -m 0644 %{SOURCE102} \
    %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
install -D -m 0644 %{SOURCE103} \
    %{buildroot}%{_prefix}/lib/firewalld/services/%{name}-ssl.xml

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/ssi-cgi
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_sbindir}/wigwam
%attr(0755,root,root) %verify(not mode) %{_sbindir}/cgi-wrapper
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/cgi-wrapper.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/mimetype.conf
%config(noreplace) %{_sysconfdir}/%{name}/index.xslt
%config(noreplace) %{_sysconfdir}/%{name}/error.xslt
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{name}.xml
%{_prefix}/lib/firewalld/services/%{name}-ssl.xml
%{_mandir}/man1/{cgi-wrapper,hiawatha,ssi-cgi,wigwam}.1%{ext_man}
%dir %{webroot}/%{name}
%dir %{webroot}/%{name}/htdocs
%{webroot}/%{name}/htdocs/index.html
%dir %attr(-,wwwrun,www) %{_localstatedir}/lib/%{name}/
%dir %attr(750,wwwrun,www) %{_localstatedir}/log/%{name}/

%files letsencrypt
%defattr(-,root,root)
%{_sbindir}/lefh
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/letsencrypt
%{_mandir}/man1/lefh.1%{ext_man}

%changelog
