#
# spec file for package vigra
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} < 1600
%bcond_with numpy
%else
%bcond_without numpy
%endif

#LEMON build doesn't work right now (shared library problem)
%bcond_with    lemon
%define _shlibname libvigraimpex11
Name:           vigra
Version:        1.11.2
Release:        0
Summary:        Computer vision Library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://ukoethe.github.io/vigra/
Source:         https://github.com/ukoethe/vigra/archive/refs/tags/Version-1-11-2.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  openexr-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with numpy}
BuildRequires:  libboost_python3-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-numpy-devel
%endif

%if %{with lemon}
BuildRequires:  lemon-devel
%endif

%description
VIGRA stands for "Vision with Generic Algorithms". It is a novel
computer vision library that puts its main emphasis on customizable
algorithms and data structures. By using template techniques similar to
those in the C++ Standard Template Library, you can easily adapt any
VIGRA component to the needs of your application, without giving up
execution speed.

%package -n %{_shlibname}
Summary:        Computer vision Library
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{_shlibname}
VIGRA stands for "Vision with Generic Algorithms". It is a novel
computer vision library that puts its main emphasis on customizable
algorithms and data structures. By using template techniques similar to
those in the C++ Standard Template Library, you can easily adapt any
VIGRA component to the needs of your application, without giving up
execution speed.

%package devel
Summary:        Development files for VIGRA Library
Group:          Development/Libraries/C and C++
Requires:       %{_shlibname} = %{version}
Requires:       fftw3-devel
Requires:       hdf5-devel
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       libstdc++-devel
Requires:       libtiff-devel
Requires:       openexr-devel
Requires:       python3-base
Requires:       zlib-devel
%if %{with numpy}
Requires:       python3-numpy
%endif

%description devel
VIGRA stands for "Vision with Generic Algorithms". It is a novel
computer vision library that puts its main emphasis on customizable
algorithms and data structures. By using template techniques similar to
those in the C++ Standard Template Library, you can easily adapt any
VIGRA component to the needs of your application, without giving up
execution speed.


%if %{with numpy}
%package -n python3-vigranumpy
Summary:        Numpy support for VIGRA library
Group:          Development/Libraries/C and C++
Requires:       %{name} == %{version}
Requires:       python3-numpy

%description -n python3-vigranumpy
VIGRA stands for "Vision with Generic Algorithms". It is a novel
computer vision library that puts its main emphasis on customizable
algorithms and data structures. By using template techniques similar to
those in the C++ Standard Template Library, you can easily adapt any
VIGRA component to the needs of your application, without giving up
execution speed. This package contains python / numpy bindings for VIGRA


%endif

%prep
%autosetup -p1 -n%{name}-Version-1-11-2
sed -i -e "1s|#!.*|#!/usr/bin/python3|" config/vigra-config.in

%build
%cmake \
    -DDOCINSTALL=%{_docdir} \
    -DWITH_HDF5=1 \
    -DWITH_OPENEXR=1 \
%if %{with lemon}
    -DWITH_LEMON=1
%else
    -DWITH_LEMON=0
%endif

make %{?_smp_mflags}

%install
%cmake_install

rm -rf %{buildroot}%{_docdir}/vigranumpy
%fdupes %{buildroot}/%{_prefix}

%post -n %{_shlibname} -p /sbin/ldconfig
%postun -n %{_shlibname} -p /sbin/ldconfig

%files -n %{_shlibname}
%doc README.md
%license LICENSE.txt
%{_libdir}/*.so.*

%files devel
%{_bindir}/vigra-config
%{_libdir}/*.so
%{_includedir}/*
%dir %{_libdir}/vigra/
%{_libdir}/vigra/*.cmake
%doc %{_docdir}/%{name}

%if %{with numpy}
%files -n python3-vigranumpy
%dir %{python_sitearch}/vigra
%dir %{python_sitearch}/vigra/pyqt
%dir %{_libdir}/vigranumpy
%{python_sitearch}/vigra/*.py
%{python_sitearch}/vigra/pyqt/*.py
%{python_sitearch}/vigra/*.so
%{_libdir}/vigranumpy/*.cmake
%endif

%changelog
