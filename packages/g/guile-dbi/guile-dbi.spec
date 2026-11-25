#
# spec file for package guile-dbi
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 2.1)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           guile-dbi
Version:        3.3.0
Release:        0
Summary:        Guile interface to SQL databases
License:        GPL-2.0-or-later
URL:            https://github.com/opencog/guile-dbi
Source0:        https://github.com/opencog/guile-dbi/archive/guile-dbi-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  texinfo
BuildRequires:  pkgconfig(guile-3.0)
Requires:       guile
Requires:       libguile-dbi4 = %{version}-%{release}

%description
guile-dbi is a simple, generic, easy-to-use Guile scheme interface to
SQL databases such as PostgreSQL, MySQL/MariaDB or SQLite3. The same
programming interface (the database-independent front end) works with
every database; database-dependent plugins connect to the actual SQL
server. This package holds the database-independent core and its
scheme module; the DBD back ends live in the same upstream repository
as separate build trees.

%package -n libguile-dbi4
Summary:        Guile DBI runtime library

%description -n libguile-dbi4
Runtime C library for guile-dbi, the Guile scheme interface to SQL
databases. The scheme module in the main package loads it at run time.

%package devel
Summary:        Development files for guile-dbi
Requires:       libguile-dbi4 = %{version}-%{release}
Requires:       libltdl-devel
Requires:       pkgconfig(guile-3.0)

%description devel
C header, pkgconfig file and link library for building DBD back ends
and other C extensions against guile-dbi.

%prep
%setup -q -n %{name}-%{name}-%{version}
%autopatch -p1

%build
cd %{name}
./autogen.sh --no-configure
%configure --disable-static
%make_build

%install
cd %{name}
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libguile-dbi4 -p /sbin/ldconfig
%postun -n libguile-dbi4 -p /sbin/ldconfig

%check
# check-local assumes an installed (dbi dbi) module; use the just-installed tree
export GUILE_LOAD_PATH="%{buildroot}%{_datadir}/guile/site/3.0"
cd %{name}
%make_build check

%files
%license guile-dbi/COPYING
%doc README.md guile-dbi/ChangeLog
%dir %{_datadir}/guile/site/3.0
%{_datadir}/guile/site/3.0/dbi/
%{_libdir}/libguile-dbd-test.so*
%{_infodir}/guile-dbi.info%{?ext_info}

%files -n libguile-dbi4
%{_libdir}/libguile-dbi.so.4*

%files devel
%{_includedir}/guile-dbi/
%{_libdir}/libguile-dbi.so
%{_libdir}/pkgconfig/guile-dbi.pc

%changelog
