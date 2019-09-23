#
# spec file for package libcerf
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Christoph Junghans <junghans@votca.org>
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


Name:           libcerf
Version:        1.5
Release:        0

Url:            http://apps.jcns.fz-juelich.de/doku/sc/libcerf
Source:         http://apps.jcns.fz-juelich.de/src/libcerf/%{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        A library that complex error functions
License:        MIT
Group:          Development/Libraries/C and C++

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  pkgconfig
BuildRequires:  fdupes

%description
libcerf is a self-contained numeric library that provides an efficient and accurate implementation of 
complex error functions, along with Dawson, Faddeeva, and Voigt functions.

%package -n libcerf1
Summary:        A library that provides complex error functions
Group:          Development/Libraries/C and C++

%description -n libcerf1
libcerf is a self-contained numeric library that provides an efficient and accurate implementation of 
complex error functions, along with Dawson, Faddeeva, and Voigt functions.

%package devel
Summary:        Development headers and libraries for libcerf
Group:          Development/Libraries/C and C++
Requires:       libcerf1 = %{version}-%{release}

%description devel
libcerf is a self-contained numeric library that provides an efficient and accurate implementation of 
complex error functions, along with Dawson, Faddeeva, and Voigt functions.

This package contains development headers and libraries for libcerf

%prep
%setup

%build
%configure --enable-tests --enable-doxygen --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}
%fdupes %{buildroot}%{_prefix}

%post -n libcerf1 -p /sbin/ldconfig
%postun -n libcerf1 -p /sbin/ldconfig

%check
make check

%files -n libcerf1
%defattr(-,root,root,0755)
%{_libdir}/libcerf.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/libcerf.so
%{_libdir}/pkgconfig/libcerf.pc
%{_mandir}/man3/*
%{_docdir}/%{name}

%changelog
