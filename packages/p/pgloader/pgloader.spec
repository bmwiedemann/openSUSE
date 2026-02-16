#
# spec file for package pgloader
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Patch0:         fix-unbreak-after-SBCL-internals-change.patch
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
Requires:       /usr/bin/sbcl
# keep in sync with the sbcl package
ExcludeArch:    s390x
# fails to build for i586
ExcludeArch:    %{ix86}

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
%autosetup -n %{name}-bundle-%{version} -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export DYNSIZE=""
echo "Arch is : %{_arch}"
%if "%{_arch}" == "i386" || "%{_arch}" == "arm"
export DYNSIZE="DYNSIZE=1024"
%endif
#
# SBCL "programs" are similar to self-extracting archives, i.e. they are
# comprised of a well-known stub plus some data appended. Such appendages
# (called "core" in SBCL) are generally prone to getting removed by e.g.
# strip, upx, etc.
#
# Build just the core. This has two benefits:
# * reuse /usr/bin/sbcl interpreter and save bytes
# * the core itself is not ELF, so not subject to strip
#
%make_build V=1 ${DYNSIZE} COMPRESS_CORE_OPT="--compress-core --core-only" %{name}

%install
# That core is likely arch-dependent, so place into libexecdir not datadir.
#
mkdir -p "%{buildroot}/%{_bindir}" "%{buildroot}/%{_libexecdir}/%{name}"
cp bin/pgloader "%{buildroot}/%{_libexecdir}/%{name}/"
cat >"%{buildroot}/%{_bindir}/pgloader" <<-EOF
	#!/bin/sh
	exec /usr/bin/sbcl --core %{_libexecdir}/%{name}/pgloader "\$@"
EOF
chmod a+x "%{buildroot}/%{_bindir}/pgloader"

%fdupes %{buildroot}/%{_prefix}

%files
%license local-projects/%{name}-%{version}/LICENSE
%doc local-projects/%{name}-%{version}/README.md local-projects/%{name}-%{version}/TODO.md
%{_bindir}/pgloader
%{_libexecdir}/%{name}/

%changelog
