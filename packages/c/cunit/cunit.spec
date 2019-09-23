#
# spec file for package cunit
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   CUnit
%define _version 2.1-3
%define _libname libcunit1
Name:           cunit
Version:        2.1.3
Release:        0
Summary:        It provides C programmers a basic testing functionality
License:        LGPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://cunit.sourceforge.net/
Source0:        http://download.sourceforge.net/cunit/%{_name}-%{_version}.tar.bz2
Patch0:         cunit-link-ncurses.diff
Patch1:         cunit-ncurses6.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CUnit is a unit testing framework for C.
This package installs the CUnit static library,
headers, and documentation files.

%package devel
Summary:        CUnit development files
Group:          Development/Libraries/C and C++
Requires:       %{_libname} = %{version}
Requires:       ncurses-devel
Requires:       pkg-config
%if 0%{?suse_version} || 0%{?fedora_version}
Recommends:     %{name}-doc = %{version}
%endif

%description devel
CUnit is a unit testing framework for C.
This package installs the CUnit development files.

%package doc
Summary:        CUnit documentation
Group:          Documentation/Man
Requires:       %{_libname} = %{version}

%description doc
CUnit is a unit testing framework for C.
This package installs the CUnit
documentation files.

%package -n %{_libname}
Summary:        CUnit shared library
Group:          System/Libraries

%description  -n %{_libname}
CUnit is a unit testing framework for C.
This package installs the CUnit shared library.

%prep
%setup -q -n %{_name}-%{_version}
%patch0 -p1
%patch1 -p1

chmod -x AUTHORS ChangeLog COPYING NEWS README TODO doc/*.html doc/*.css

%build
autoreconf -fi
%configure \
    --disable-static \
    --enable-automated \
    --enable-basic \
    --enable-console \
    --enable-curses \
    --enable-examples \
    --enable-test
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_prefix}/doc
# arch dependent files
mkdir -p %{buildroot}%{_libdir}/CUnit/
mv %{buildroot}%{_datadir}/CUnit/Examples/ %{buildroot}%{_libdir}/CUnit/
mv %{buildroot}%{_datadir}/CUnit/Test/     %{buildroot}%{_libdir}/CUnit/
chmod -x doc/headers/*
rm doc/headers/Makefile*
rm doc/headers/Jamfile*
rm doc/Makefile*
rm doc/Jamfile*

%post -n %{_libname} -p /sbin/ldconfig

%postun -n %{_libname} -p /sbin/ldconfig

%files -n %{_libname}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/libcunit.so.*

%files doc
%defattr(-,root,root,-)
%doc doc/*
%dir %{_datadir}/CUnit
%{_datadir}/CUnit/*
%{_mandir}/man3/CUnit.3.gz

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/CUnit
%{_includedir}/CUnit/*
%dir %{_libdir}/CUnit
%{_libdir}/CUnit/*
%{_libdir}/libcunit.so
%{_libdir}/pkgconfig/cunit.pc

%changelog
