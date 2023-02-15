#
# spec file for package pgloader
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


Name:           pgloader
Version:        3.6.9
Release:        0
Summary:        Fast data loader for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            https://pgloader.io
Source:         https://github.com/dimitri/%{name}/releases/download/v%{version}/%{name}-bundle-%{version}.tgz
BuildRequires:  fdupes
BuildRequires:  freetds-devel
BuildRequires:  pkgconfig
BuildRequires:  sbcl
BuildRequires:  strace
BuildRequires:  pkgconfig(sqlite3)
%if 0%{?suse_version} >= 1500
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

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export DYNSIZE=""
echo "Arch is : %{_arch}"
%if "%{_arch}" == "i386" || "%{_arch}" == "arm"
export DYNSIZE="DYNSIZE=1024"
%endif
%make_build V=1 ${DYNSIZE} %{name}

%install
install -d %{buildroot}%{_bindir}
#
# SBCL produces ELF files that
# (1.) have excessive gaps and which could be fixed by objcopy/strip/etc.
# (2.) do not have any .debug_* sections, therefore rpm's debuginfo
#      mechanism (would do strip) does not trigger at all.
#
# Hence this copyin-copyout call with objcopy, which reduces filesize from 20MB
# to 300KB.
#
objcopy bin/pgloader %{buildroot}%{_bindir}/pgloader

%fdupes %{buildroot}

%files
%license local-projects/%{name}-%{version}/LICENSE
%doc local-projects/%{name}-%{version}/README.md local-projects/%{name}-%{version}/TODO.md
%{_bindir}/pgloader

%changelog
