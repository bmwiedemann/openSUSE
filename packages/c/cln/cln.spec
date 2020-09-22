#
# spec file for package cln
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


Name:           cln
Version:        1.3.6
Release:        0
Summary:        Class Library for Numbers (C++)
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.ginac.de/CLN/
Source0:        https://www.ginac.de/CLN/cln-%{version}.tar.bz2
Source1:        pi.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig
BuildRequires:  texinfo
Requires(pre):  %{install_info_prereq}
Provides:       libcln
Provides:       pi

%description
CLN features a rich set of number classes: integer (unlimited
precision), rational, short float, single float, double float, long
float (unlimited precision), complex, modular integer, and univariate
polynomial.  It implements elementary, logical, and transcendental
functions.  C++ as the implementation language brings efficiency, type
safety, and algebraic syntax.  Memory efficiency: small integers and
short floats are immediate, not heap allocated. Automatic,
noninterruptive garbage collection.  Speed efficiency: assembly
language kernel for some CPUs, Karatsuba and Schoenhage-Strassen
multiplication.  Interoperability: garbage collection with no burden on
the main application, hooks for memory allocation and exceptions.

The following C++ features are used: classes, member functions,
overloading of functions and operators, constructors and destructors,
inline, const, multiple inheritance, templates, and namespaces.  The
following C++ features are not used: new, delete, virtual inheritance,
and exceptions.

%package devel
Summary:        Class Library for Numbers (C++)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires(pre):  %{install_info_prereq}

%description devel
CLN features a rich set of number classes: integer (unlimited
precision), rational, short float, single float, double float, long
float (unlimited precision), complex, modular integer, and univariate
polynomial.  It implements elementary, logical, and transcendental
functions.  C++ as the implementation language brings efficiency, type
safety, and algebraic syntax.  Memory efficiency: small integers and
short floats are immediate, not heap allocated. Automatic,
noninterruptive garbage collection.  Speed efficiency: assembly
language kernel for some CPUs, Karatsuba and Schoenhage-Strassen
multiplication.  Interoperability: garbage collection with no burden on
the main application, hooks for memory allocation and exceptions.

The following C++ features are used: classes, member functions,
overloading of functions and operators, constructors and destructors,
inline, const, multiple inheritance, templates, and namespaces.  The
following C++ features are not used: new, delete, virtual inheritance,
and exceptions.

%prep
%setup -q -a 1

%build
%ifarch %{arm}
%global XFLAGS %{optflags} -DNO_ASM
%else
%global XFLAGS %{optflags}
%endif
CFLAGS="%{XFLAGS} -fno-unit-at-a-time" \
CXXFLAGS="%{XFLAGS} -fno-strict-aliasing -fno-unit-at-a-time -fno-reorder-blocks" \
%configure --disable-static
make %{?_smp_mflags}
make %{?_smp_mflags} check
#cd benchmarks
#for i in a ap b ; do
#	./timebench2$i -r 10
#done
#cd ..
g++ %{optflags} -I./include pi.cc -o pi -L./src/.libs/ -lcln -lgmp
make %{?_smp_mflags} html

%install
mkdir -p %{buildroot}%{_docdir}/cln
make DESTDIR=%{buildroot} MANDIR=%{_mandir} htmldir=%{_docdir}/cln install
install -m 755 pi %{buildroot}%{_bindir}
rm -f %{buildroot}%{_libdir}/libcln.la

%check
make %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%doc ChangeLog README NEWS
%license COPYING
%{_bindir}/pi
%{_libdir}/libcln.so.*

%files devel
%doc ChangeLog README NEWS
%license COPYING
%{_includedir}/cln
%{_infodir}/cln.info%{?ext_info}
%{_mandir}/man1/pi.1%{?ext_man}
%{_libdir}/libcln.so
%{_libdir}/pkgconfig/cln.pc

%changelog
