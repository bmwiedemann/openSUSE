#
# spec file for package privoxy
#
# Copyright (c) 2023 SUSE LLC
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


%define chroot %{_localstatedir}/lib/privoxy
Name:           privoxy
Version:        3.0.34
Release:        0
Summary:        The Internet Junkbuster - HTTP Proxy Server
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            https://www.privoxy.org/
Source:         https://www.privoxy.org/sf-download-mirror/Sources/%{version}%%20%%28stable%%29/%{name}-%{version}-stable-src.tar.gz
Source2:        https://www.privoxy.org/sf-download-mirror/Sources/%{version}%%20%%28stable%%29/%{name}-%{version}-stable-src.tar.gz.asc
Source3:        %{name}.service
Source4:        %{name}.logrotate.systemd
Source5:        https://www.fabiankeil.de/gpg-keys/fk-8BA2371C.asc#/%{name}.keyring
Patch1:         %{name}-3.0.21-config.patch
Patch2:         %{name}-3.0.17-utf8.patch
Patch3:         %{name}-3.0.16-networkmanager.systemd.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  w3m
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Requires:       logrotate
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
%{?systemd_ordering}

%description
The Internet Junkbuster - HTTP Proxy Server: A non-caching HTTP proxy
server that runs between a web browser and a web server and filters
contents as described in the configuration files.

%package doc
Summary:        The documentation of Privoxy
Group:          Productivity/Networking/Web/Proxy
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Documentation files for the Privoxy: The Internet Junkbuster - HTTP
Proxy Server. A non-caching HTTP proxy server that runs between a web
browser and a web server and filters contents as described in the
configuration files.

%prep
%autosetup -p1 -n privoxy-%{version}-stable

%build
autoreconf -fiv
%configure \
	--enable-compression \
	--with-openssl\
	--with-brotli \
	--enable-extended-statistics \
	--enable-pcre-host-patterns \
	--enable-dynamic-pcre

%make_build

%install
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}/%{chroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}/%{chroot}/log
mkdir -p %{buildroot}/%{chroot}%{_localstatedir}/log
mkdir -p %{buildroot}/%{chroot}%{_localstatedir}/run
mkdir -p %{buildroot}/%{chroot}/%{_lib}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d
cp -a templates %{buildroot}/%{chroot}%{_sysconfdir}
install -m 644 config *.action *.filter trust %{buildroot}/%{chroot}%{_sysconfdir}
sed -e 's/@lib@/%{_lib}/g' %{SOURCE3} > %{buildroot}/%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -m 755 privoxy %{buildroot}%{_sbindir}
install -m 755 privoxy_nm %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/privoxyd
install -m 644 privoxy.8 %{buildroot}%{_mandir}/man8
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/privoxy
ln -s ../../log %{buildroot}/%{chroot}%{_localstatedir}/log/privoxy
ln -sf %{chroot}%{_sysconfdir}/ %{buildroot}%{_sysconfdir}/privoxy

%pre
%service_add_pre %{name}.service
%{_sbindir}/groupadd -r privoxy 2> /dev/null ||:
%{_sbindir}/useradd -r -g privoxy -s /bin/false -c "Daemon user for privoxy" \
 -d %{_localstatedir}/lib/privoxy privoxy 2> /dev/null ||:
exit 0

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc AUTHORS README ChangeLog
%{_sbindir}/privoxy
%{_sysconfdir}/NetworkManager/dispatcher.d/privoxyd
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%{_mandir}/man8/privoxy.8%{?ext_man}
%config(noreplace) %{_sysconfdir}/logrotate.d/privoxy
%dir /%{chroot}%{_sysconfdir}
%config(noreplace) /%{chroot}%{_sysconfdir}/config
%config(noreplace) /%{chroot}%{_sysconfdir}/trust
%config /%{chroot}%{_sysconfdir}/match-all.action
%config %attr(640,privoxy,root) /%{chroot}%{_sysconfdir}/default.action
%config(noreplace) %attr(640,privoxy,root) /%{chroot}%{_sysconfdir}/user.action
%config(noreplace) /%{chroot}%{_sysconfdir}/*.filter
%dir %{chroot}
%{chroot}%{_sysconfdir}/templates
%dir %attr(770,root,privoxy) %{chroot}/log
%{chroot}%{_localstatedir}
%{chroot}/%{_lib}
%{chroot}%{_sysconfdir}/regression-tests.action
%{_unitdir}/%{name}.service
%{_sbindir}/rcprivoxy
%{_sysconfdir}/privoxy

%files doc
%license LICENSE
%doc doc/source

%changelog
