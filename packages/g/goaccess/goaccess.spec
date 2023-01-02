#
# spec file for package goaccess
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


%global goaccess_services goaccess@.service goaccess@.timer

Name:           goaccess
Version:        1.7
Release:        0
Summary:        Apache Web Log Analyzer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://goaccess.io/
Source0:        http://tar.goaccess.io/goaccess-%{version}.tar.gz
Source10:       goaccess@.service
Source11:       goaccess@.timer
Source20:       README.SUSE.md
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libmaxminddb)
Recommends:     %{name}-lang

%description
GoAccess is an Apache web log analyzer that provides HTTP statistics
for system administrators that require a visual report on the fly.

%lang_package

%prep
%autosetup -p1
cp %{SOURCE20} .

%build
%configure \
    --enable-utf8 \
    --enable-geoip=mmdb

%make_build

%install
%make_install

install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/goaccess@.service
install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/goaccess@.timer

%find_lang %{name}

%pre
%service_add_pre %{goaccess_services}

%post
%service_add_post %{goaccess_services}

%preun
%service_del_preun %{goaccess_services}

%postun
%service_del_postun %{goaccess_services}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.SUSE.md TODO
%{_bindir}/goaccess
%{_mandir}/man1/goaccess.1%{?ext_man}
%dir %{_sysconfdir}/goaccess/
%config %{_sysconfdir}/goaccess/browsers.list
%config %{_sysconfdir}/goaccess/goaccess.conf
%{_sysconfdir}/goaccess/podcast.list
%{_unitdir}/goaccess@.service
%{_unitdir}/goaccess@.timer

%changelog
