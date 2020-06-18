#
# spec file for package sysbench
#
# Copyright (c) 2020 SUSE LLC
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


Name:           sysbench
Version:        1.0.20
Release:        0
Summary:        A MySQL benchmarking tool
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            https://github.com/akopytov/sysbench
Source0:        https://github.com/akopytov/sysbench/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libaio-devel
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  mysql-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  postgresql-server-devel
%endif
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(ck)
BuildRequires:  pkgconfig(luajit)
%endif

%description
This benchmark was designed for identifying basic system parameters, as
they are important for systems using MySQL (w Innodb) under intensive
load.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --without-gcc-arch \
  %if 0%{?is_opensuse}
  --with-system-ck \
  --with-system-luajit \
  %endif
  --with-pgsql
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/sysbench

%files
%license COPYING
%doc ChangeLog README.md doc/manual.html
%{_bindir}/sysbench
%{_datadir}/sysbench

%changelog
