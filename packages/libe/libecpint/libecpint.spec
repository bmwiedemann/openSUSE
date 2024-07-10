#
# spec file for package libecpint
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2021 Christoph Junghans
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


Name:           libecpint
Version:        v1.0.7+git20230218.8e788d4
Release:        0
%global         sover 1
Summary:        Efficient evaluation of integrals over ab initio effective core potentials
License:        MIT
Group:          Productivity/Scientific/Chemistry
URL:            https://github.com/robashaw/libecpint
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.12
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  libcerf-devel >= 1.17
BuildRequires:  pugixml-devel
BuildRequires:  python3
BuildRequires:  sphinx

%description
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.

%package -n libecpint%sover
Summary:        Efficient evaluation of integrals over ab initio effective core potentials
Group:          System/Libraries

%description -n libecpint%sover
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.

%package -n ecpint-common
Summary:        Architecture independent data files for libecpint
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch
Requires:       %{name}%{sover} = %{version}-%{release}

%description -n ecpint-common
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.

This package contains architecture independent data files for libecpint

%package devel
Summary:        Devel package for libecpint
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}-%{release}
Requires:       libcerf-devel >= 1.17

%description devel
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.
This package contains development headers and libraries for libecpint

%prep
%setup -q

%build
%{cmake} -DCMAKE_SKIP_RPATH=OFF -DLIBECPINT_USE_CERF=ON
%cmake_build

%install
%cmake_install

%check
# https://github.com/robashaw/libecpint/issues/27
%ifarch %ix86
%global testargs --exclude-regex Type1Test2
%endif
%ctest %{?testargs}

%post -n libecpint%sover -p /sbin/ldconfig
%postun -n libecpint%sover -p /sbin/ldconfig

%files -n libecpint%sover
%license LICENSE
%{_libdir}/lib*.so.%{sover}

%files -n ecpint-common
%doc README.md CITATION
%license LICENSE
%{_datadir}/%{name}

%files devel
%{_includedir}/libecpint/
%{_includedir}/libecpint.hpp
%{_libdir}/cmake/ecpint
%{_libdir}/lib*.so

%changelog
