#
# spec file for package pgloader
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


Name:           pgloader
Version:        3.6.1
Release:        0
Summary:        Fast data loader for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            https://pgloader.io
Source0:        https://github.com/dimitri/%{name}/releases/download/v%{version}/%{name}-bundle-%{version}.tgz
# Fix compilation errors with sbcl 2.0.1
Source1:        https://github.com/cffi/cffi/archive/v0.21.0.tar.gz
BuildRequires:  fdupes
BuildRequires:  freetds-devel
BuildRequires:  pkgconfig
BuildRequires:  sbcl
BuildRequires:  pkgconfig(sqlite3)
%if 0%{?leap_version} >= 430000 || 0%{?suse_version} > 4300
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%else
BuildRequires:  libopenssl-devel
%endif

%description
pgloader imports data from different kind of sources and COPY it into
PostgreSQL.

The command language is described in the manual page and allows to describe
where to find the data source, its format, and to describe data processing
and transformation.

Supported source formats include SQL Server, CSV, fixed width flat files,
dBase3 files (DBF), and SQLite and MySQL databases. In most of those formats,
pgloader is able to auto-discover the schema and create the tables and the
indexes in PostgreSQL. In the MySQL case it's possible to edit CASTing rules
from the pgloader command directly.

%prep
%setup -q -n %{name}-bundle-%{version}
# clean up old cffi
rm -rf software/cffi_0.20.0
# expand new cffi in place
tar -C software -xf %{SOURCE1}

%build
export CCFLAGS="%{_optflags}"
export CCXFLAGS="%{_optflags}"
export DYNSIZE=""
echo "Arch is : %{_arch}"
%if "%{_arch}" == "i386" || "%{_arch}" == "arm"
export DYNSIZE="DYNSIZE=1024"
%endif
make V=1 %{?_smp_mflags} ${DYNSIZE}

%install
install -d %{buildroot}%{_bindir}
install -m 755 bin/pgloader %{buildroot}%{_bindir}/pgloader

%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%license local-projects/%{name}-%{version}/LICENSE
%doc local-projects/%{name}-%{version}/README.md local-projects/%{name}-%{version}/TODO.md
%{_bindir}/pgloader

%changelog
