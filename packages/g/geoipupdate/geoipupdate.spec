#
# spec file for package geoipupdate
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           geoipupdate
Version:        3.1.1
Release:        0
Summary:        GeoIP update client code
License:        GPL-2.0-only
Group:          Productivity/Networking/System
URL:            https://www.maxmind.com
Source0:        https://github.com/maxmind/geoipupdate-legacy/archive/v%{version}/%{name}-legacy-%{version}.tar.gz
Source1:        geoipupdate.timer
Source2:        geoipupdate.service
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Conflicts:      GeoIP < 1.6.0
%{?systemd_requires}

%description
The GeoIP Update program performs automatic updates of GeoIP2 and GeoIP
Legacy binary databases. Currently the program only supports Linux and
other Unix- like systems.

%prep
%setup -q -n %{name}-legacy-%{version}

%build
autoreconf --install
%configure \
  --datadir=%{_localstatedir}/lib
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_localstatedir}/lib/GeoIP
install -D -p -m 0644 conf/GeoIP.conf.default \
  %{buildroot}%{_sysconfdir}/GeoIP.conf.default
rm -rf %{buildroot}%{_datadir}/doc/geoipupdate
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.timer
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

%check
make %{?_smp_mflags} check

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md ChangeLog.md
%config(noreplace) %{_sysconfdir}/GeoIP.conf
%config %{_sysconfdir}/GeoIP.conf.default
%dir %{_localstatedir}/lib/GeoIP
%{_bindir}/geoipupdate
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_mandir}/man1/geoipupdate.1%{?ext_man}
%{_mandir}/man5/GeoIP.conf.5%{?ext_man}

%changelog
