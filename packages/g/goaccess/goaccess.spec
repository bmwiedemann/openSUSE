# vim: set sw=4 ts=4 et nu:
#
# spec file for package goaccess
#
# Copyright (c) 2020 SUSE LLC
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


Name:           goaccess
Version:        1.4
Release:        0
Summary:        Apache Web Log Analyzer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://goaccess.io/
Source:         http://tar.goaccess.io/goaccess-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libmaxminddb-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
Recommends:     %{name}-lang

%description
GoAccess is an Apache web log analyzer that provides HTTP statistics
for system administrators that require a visual report on the fly.

%lang_package

%prep
%setup -q

%build
%configure \
    --enable-utf8

%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/goaccess
%{_mandir}/man1/goaccess.1%{?ext_man}
%dir %{_sysconfdir}/goaccess/
%config %{_sysconfdir}/goaccess/browsers.list
%config %{_sysconfdir}/goaccess/goaccess.conf
%{_sysconfdir}/goaccess/podcast.list

%changelog
