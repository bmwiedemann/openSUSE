#
# spec file for package siege
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           siege
Version:        4.0.7
Release:        0
Summary:        HTTP Regression Testing/Benchmarking Utility
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://www.joedog.org/siege-home/
Source:         http://download.joedog.org/siege/siege-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%{perl_requires}

%description
Siege is a regression test and benchmark utility. It can stress test a
single URL with a user defined number of simulated users, or it can read
many URLs into memory and stress them simultaneously. The program reports
the total number of hits recorded, bytes transferred, response time,
concurrency, and return status. Siege supports HTTP/1.0 and 1.1 protocols,
GET and POST directives, cookies, transaction logging, and basic
authentication. Its features are configurable on a per user basis. Since
3.0.0 it also supports FTP.

%prep
%setup -q

%build
%configure \
  --sysconfdir="%{_sysconfdir}/%{name}"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/siegerc
%config(noreplace) %{_sysconfdir}/%{name}/urls.txt
%{_bindir}/bombardment
%{_bindir}/siege
%{_bindir}/siege2csv.pl
%{_bindir}/siege.config
%{_mandir}/man1/bombardment.1%{ext_man}
%{_mandir}/man1/siege.1%{ext_man}
%{_mandir}/man1/siege.config.1%{ext_man}
%{_mandir}/man1/siege2csv.1%{ext_man}

%changelog
