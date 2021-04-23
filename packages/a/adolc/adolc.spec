#
# spec file for package adolc
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


%define lname   libadolc2
Name:           adolc
Version:        2.7.2
Release:        0
Summary:        Algorithmic Differentiation Library for C/C++
License:        GPL-2.0-or-later OR EPL-1.0
URL:            https://github.com/coin-or/ADOL-C
Source0:        https://github.com/coin-or/ADOL-C/archive/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  ColPack-devel
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif

%description
ADOL-C (Automatic Differentiation by OverLoading in C++) facilitates
the evaluation of first and higher derivatives of vector functions
written in C or C++.

%package -n %{lname}
Summary:        Algorithmic Differentiation Library for C/C++

%description -n %{lname}
ADOL-C (Automatic Differentiation by OverLoading in C++) facilitates
the evaluation of first and higher derivatives of vector functions
written in C or C++. The resulting derivative evaluation routines may
be called from C/C++, Fortran, or any other language that can be
linked with C.

The numerical values of derivative vectors are obtained free of
truncation errors at a small multiple of the run time and randomly
accessed memory of the given function evaluation program.

%package devel
Summary:        Development files for the Algorithmic Differentiation Library
Requires:       %{lname} = %{version}

%description devel
This package provides the development environment for ADOL-C
(Automatic Differentiation by OverLoading in C++).

%package doc
Summary:        Algorithmic Differentiation Library for C/C++ -- documentation
%if 0%{?suse_version}
BuildArch:      noarch
%endif

%description doc
This package provides the user's manual for ADOL-C.

%prep
%autosetup -n ADOL-C-releases-%{version}

%build
# autoreconf -v --install --force
%configure
%make_build
# pushd ADOL-C/doc
# for ((i=0; i < 3; i++)); do
#    pdflatex adolc-manual.tex &>/dev/null
# done

%install
%make_install
find %{buildroot} -type f "(" -name "*.a" -o -name "*.la" ")" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%{_libdir}/libadolc.so.*

%files devel
%dir %{_includedir}/adolc
%dir %{_includedir}/adolc/drivers
%dir %{_includedir}/adolc/internal
%dir %{_includedir}/adolc/lie
%dir %{_includedir}/adolc/sparse
%dir %{_includedir}/adolc/tapedoc
%{_includedir}/adolc/*.h
%{_includedir}/adolc/drivers/*.h
%{_includedir}/adolc/internal/*.h
%{_includedir}/adolc/lie/drivers.h
%{_includedir}/adolc/sparse/*.h
%{_includedir}/adolc/tapedoc/*.h
%{_libdir}/libadolc.so
%{_libdir}/pkgconfig/adolc.pc

%files doc
%doc README AUTHORS BUGS TODO
%doc ADOL-C/doc/adolc-manual.pdf
%doc ADOL-C/doc/short_ref.pdf
%license LICENSE

%changelog
