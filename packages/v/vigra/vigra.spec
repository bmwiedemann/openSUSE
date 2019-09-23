#
# spec file for package vigra
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


%define _shlibname libvigraimpex11
Name:           vigra
Version:        1.11.1
Release:        0
Summary:        Computer vision Library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://ukoethe.github.io/vigra/
Source:         https://github.com/ukoethe/vigra/releases/download/Version-1-11-1/vigra-%{version}-src.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
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

%description devel
VIGRA stands for "Vision with Generic Algorithms". It is a novel
computer vision library that puts its main emphasis on customizable
algorithms and data structures. By using template techniques similar to
those in the C++ Standard Template Library, you can easily adapt any
VIGRA component to the needs of your application, without giving up
execution speed.

%prep
%setup -q
sed -i -e "1s|#!.*|#!/usr/bin/python3|" config/vigra-config.in

%build
%cmake \
    -DDOCINSTALL=%{_docdir} \
    -DWITH_HDF5=1 \
    -DWITH_OPENEXR=1
make %{?_smp_mflags}

%install
%cmake_install

rm -rf %{buildroot}%{_docdir}/vigranumpy
%fdupes %{buildroot}/%{_prefix}

%post -n %{_shlibname} -p /sbin/ldconfig
%postun -n %{_shlibname} -p /sbin/ldconfig

%files -n %{_shlibname}
%doc README.md LICENSE.txt
%{_libdir}/*.so.*

%files devel
%{_bindir}/vigra-config
%{_libdir}/*.so
%{_includedir}/*
%dir %{_libdir}/vigra/
%{_libdir}/vigra/*.cmake
%doc %{_docdir}/%{name}

%changelog
