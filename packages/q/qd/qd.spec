#
# spec file for package qd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libqd0

Name:           qd
Version:        2.3.22
Release:        0
Summary:        Quad Double computation package
License:        BSD-3-Clause-LBNL
Group:          Development/Libraries/C and C++
Url:            http://crd-legacy.lbl.gov/~dhbailey/mpdist/
Source0:        http://crd.lbl.gov/~dhbailey/mpdist/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
qd provides numeric types of twice the precision of IEEE double
(106 mantissa bits, or approximately 32 decimal digits) and four
times the precision of IEEE double (212 mantissa bits, or approximately
64 decimal digits).  Due to features such as operator and function
overloading, these facilities can be utilized with only minor modifications
to conventional C++ and Fortran-90 programs.

%package -n %libname
Summary:        A library for nonlinear optimization
Group:          System/Libraries

%description -n %libname
qd provides numeric types of twice the precision of IEEE double
(106 mantissa bits, or approximately 32 decimal digits) and four
times the precision of IEEE double (212 mantissa bits, or approximately
64 decimal digits).  Due to features such as operator and function
overloading, these facilities can be utilized with only minor modifications
to conventional C++ and Fortran-90 programs.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %libname = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

rm -rf %{buildroot}%{_datadir}/doc/qd

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING docs/qd.pdf NEWS README
%license BSD-LBNL-License.doc
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.so

%changelog
