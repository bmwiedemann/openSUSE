#
# spec file for package tsung
#
# Copyright (c) 2025 SUSE LLC
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


Name:           tsung
Version:        1.8.0
Release:        0
Summary:        A distributed multi-protocol load testing tool
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            http://tsung.erlang-projects.org/
Source0:        http://tsung.erlang-projects.org/dist/%{name}-%{version}.tar.gz
BuildRequires:  erlang
BuildRequires:  fdupes
Requires:       bash
Requires:       erlang
Requires:       perl(Template)

%description
tsung is a distributed load testing tool.
It is protocol-independent and can currently be used to stress and
benchmark HTTP, Jabber/XMPP, PostgreSQL, MySQL and LDAP servers.
It simulates user behaviour using an XML description file, reports
many measurements in real time (statistics can be customized with
transactions, and graphics generated using gnuplot).
For HTTP, it supports 1.0 and 1.1, has a proxy mode to record
sessions, supports GET and POST methods, Cookies, and Basic
WWW-authentication. It also has support for SSL.

More information is available at http://tsung.erlang-projects.org/ .

%prep
%setup -q
sed -i "s,^#! /usr/bin/env python3$,#!/usr/bin/python3," src/tsung-plotter/tsplot.py.in

%build
%configure \
  --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}

%files
%license COPYING
%doc CHANGELOG.md CONTRIBUTORS README.md TODO examples
%{_bindir}/tsung
%{_bindir}/tsung-recorder
%{_bindir}/tsplot
%{_libdir}/tsung
%{_datadir}/tsung
%{_mandir}/man1/tsung.1%{?ext_man}
%{_mandir}/man1/tsplot.1%{?ext_man}
%{_mandir}/man1/tsung-recorder.1%{?ext_man}

%changelog
