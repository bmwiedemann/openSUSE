#
# spec file for package isl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define islsover 19
Name:           isl
Version:        0.20
Release:        0
Summary:        Integer Set Library
License:        MIT
Group:          Development/Languages/C and C++
Url:            http://isl.gforge.inria.fr/
Source:         http://isl.gforge.inria.fr/isl-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ISL is a library for manipulating sets and relations of integer points
bounded by linear constraints.
It is used by Cloog and the GCC Graphite optimization framework.

%package devel
Summary:        Development tools for ISL
Group:          Development/Languages/C and C++
Requires:       libisl%{islsover} = %{version}-%{release}

%description devel
Development tools and headers for the ISL.

%package -n libisl%{islsover}
Summary:        The ISL shared library
Group:          System/Libraries

%description -n libisl%{islsover}
The shared library for the ISL.

ISL is a library for manipulating sets and relations of integer points
bounded by linear constraints.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%check
make %{?_smp_mflags} check

%install
%make_install
rm -f  %{buildroot}%{_libdir}/*.la
rm -f  %{buildroot}%{_libdir}/libisl.so.*-gdb.py

%post -n libisl%{islsover} -p /sbin/ldconfig
%postun -n libisl%{islsover} -p /sbin/ldconfig

%files -n libisl%{islsover}
%defattr(-,root,root,-)
%{_libdir}/libisl.so.%{islsover}*

%files devel
%defattr(-,root,root,-)
%{_includedir}/isl
%{_libdir}/libisl.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
