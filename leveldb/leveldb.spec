#
# spec file for package leveldb
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           leveldb
Version:        1.20
Release:        0
Summary:        A key/value-store
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/google/leveldb
Source0:        https://github.com/google/leveldb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-debian-ports.patch
BuildRequires:  gcc-c++
BuildRequires:  snappy-devel

%description
leveldb implements a system for maintaining a persistent key/value store.

%define lib_name libleveldb1

%package -n %{lib_name}
Summary:        Shared library from leveldb
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{lib_name}
leveldb implements a system for maintaining a persistent key/value store.

This package holds the shared library of leveldb.

%package devel
Summary:        Development files for leveldb
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
leveldb implements a system for maintaining a persistent key/value store.

This package holds the development files for leveldb.

%package devel-static
Summary:        Development files for statically link leveldb
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
leveldb implements a system for maintaining a persistent key/value store.

This package holds the development files for statically linking leveldb.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} OPT="%{optflags}"

%install
install -d -m 0755 \
  %{buildroot}%{_includedir} \
  %{buildroot}%{_libdir} \
  %{buildroot}%{_bindir}

cp -a \
  out-static/libleveldb.a   \
  out-shared/libleveldb.so* \
  %{buildroot}%{_libdir}

cp -a include/leveldb \
  %{buildroot}%{_includedir}

cp -a \
  out-shared/db_bench \
  %{buildroot}%{_bindir}

%check
make %{?_smp_mflags} check

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/db_bench

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/libleveldb.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NEWS README.md TODO doc/*
%{_includedir}/leveldb/
%{_libdir}/libleveldb.so

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/libleveldb.a

%changelog
