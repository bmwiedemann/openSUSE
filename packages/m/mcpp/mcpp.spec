#
# spec file for package mcpp
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


Name:           mcpp
Version:        2.7.2
Release:        0
Summary:        Matsui's C Preprocessor
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Url:            http://mcpp.sourceforge.net/
Source0:        http://sourceforge.net/projects/mcpp/files/mcpp/V.%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
mcpp is a small and portable C/C++ preprocessor implementing all of
C90, C99 and C++98.

%define _libname libmcpp0

%package -n %{_libname}
Summary:        The shared library of Matsui's C Preprocessor
Group:          Development/Libraries/C and C++

%description -n %{_libname}
mcpp is a small and portable C/C++ preprocessor implementing all of
C90, C99 and C++98.

This package holds the shared libraries of libev.

%package devel
Summary:        Development files for mcpp
Group:          Development/Libraries/C and C++
Requires:       %{_libname} = %{version}
Requires:       %{name} = %{version}

%description devel
mcpp is a small and portable C/C++ preprocessor implementing all of
C90, C99 and C++98.

This package holds the development files for libev.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags} -D_BSD_SOURCE"
%configure --enable-mcpplib
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -rf %{buildroot}%{_datadir}/doc/mcpp
rm -rf %{buildroot}%{_libdir}/libmcpp.*a

%post   -n %{_libname} -p /sbin/ldconfig

%postun -n %{_libname} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc doc/mcpp-manual.html LICENSE NEWS README
%{_bindir}/*
%{_mandir}/man1/mcpp.1.gz

%files -n %{_libname}
%defattr(-,root,root,-)
%{_libdir}/libmcpp.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/mcpp_*.h
%{_libdir}/libmcpp.so

%changelog
