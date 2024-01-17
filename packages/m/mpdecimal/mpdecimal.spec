#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           mpdecimal%{psuffix}
Version:        2.5.1
Release:        0
Summary:        C/C++ libraries for arbitrary precision decimal floating point arithmetic
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.bytereef.org/mpdecimal/index.html
Source0:        https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-%{version}.tar.gz
Source1:        http://speleotrove.com/decimal/dectest.zip
Source99:       baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
%if %{with test}
BuildRequires:  unzip
%endif

%description
libmpdec is a C implementation of the General Decimal Arithmetic
Specification. The specification defines a general purpose arbitrary
precision data type together with rigorously specified functions and
rounding behavior. libmpdec conforms - with minor restrictions -
to the IEEE 754-2008 Standard for Floating-Point Arithmetic,
provided that the appropriate context parameters are set. libmpdec++
has a thread local context for inline operators and other functions
that use the implicit context.

%package -n libmpdec3
Summary:        C library for arbitrary precision decimal floating point arithmetic
License:        BSD-2-Clause
Group:          System/Libraries

%description -n libmpdec3
libmpdec is a C implementation of the General Decimal Arithmetic
Specification. The specification defines a general purpose arbitrary
precision data type together with rigorously specified functions and
rounding behavior. libmpdec conforms - with minor restrictions - to
the IEEE 754-2008 Standard for Floating-Point Arithmetic.

%package -n libmpdec++3
Summary:        C++ library for arbitrary precision decimal floating point arithmetic
License:        BSD-2-Clause
Group:          System/Libraries
Requires:       libmpdec3 >= %{version}

%description -n libmpdec++3
libmpdec++ is a C++ implementation of the General Decimal Arithmetic
Specification. The specification defines a general purpose arbitrary
precision data type together with rigorously specified functions and
rounding behavior. libmpdec conforms - with minor restrictions - to
the IEEE 754-2008 Standard for Floating-Point Arithmetic.

%package devel
Summary:        Development headers and documentation for mpdecimal
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Requires:       libmpdec++3 = %{version}-%{release}
Requires:       libmpdec3 = %{version}-%{release}

%description devel
The package contains documentation and development headers for
libmpdec and libmpdec++.

%prep
%autosetup -p1 -n mpdecimal-%{version}

%if %{with test}
unzip -d tests/testdata %{SOURCE1}
%endif

%build
# NOTE: without -ffat-lto-objects the inline assembly tests in ./configure
# have false positives on a variety of architectures.
export CFLAGS="%optflags -ffat-lto-objects"
export CXXFLAGS="$CFLAGS"
%configure --docdir="%{_defaultdocdir}/%{name}"
%make_build

%install
%if !%{with test}
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.a
%fdupes -s %{buildroot}/%{_docdir}/%{name}
%endif

%check
%if %{with test}
%make_build check
%endif

%if !%{with test}
%post -n libmpdec3 -p /sbin/ldconfig
%post -n libmpdec++3 -p /sbin/ldconfig
%postun -n libmpdec3 -p /sbin/ldconfig
%postun -n libmpdec++3 -p /sbin/ldconfig

%files -n libmpdec3
%license LICENSE.txt
%{_libdir}/libmpdec.so.3
%{_libdir}/libmpdec.so.%{version}

%files -n libmpdec++3
%{_libdir}/libmpdec++.so.3
%{_libdir}/libmpdec++.so.%{version}

%files devel
%license doc/LICENSE.txt
%doc %{_docdir}/%{name}
%{_libdir}/libmpdec.so
%{_libdir}/libmpdec++.so
%{_includedir}/mpdecimal.h
%{_includedir}/decimal.hh
%endif

%changelog
