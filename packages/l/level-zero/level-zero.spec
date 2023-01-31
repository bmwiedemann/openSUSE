#
# spec file for package level-zero
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Alessandro de Oliveira Faria (A.K.A CABELO) <cabelo@opensuse.org>
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


Name:           level-zero
Version:        1.9.4
Release:        0
Summary:        oneAPI Level Zero Specification Headers and Loader
License:        MIT
URL:            https://github.com/oneapi-src/level-zero
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  opencl-headers
ExclusiveArch:  x86_64

%description
The objective of the oneAPI Level-Zero Application Programming Interface (API)
is to provide direct-to-metal interfaces to offload accelerator devices. Its
programming interface can be tailored to any device needs and can be adapted to
support broader set of languages features such as function pointers, virtual
functions, unified memory, and I/O capabilities.

%package devel
Summary:        The oneAPI Level Zero Specification Headers and Loader development package.
Requires:       %{name} = %{version}-%{release}

%description   devel
The %{name}-devel package contains library and header files for developing
applications that use %{name}.

%prep
%setup -q -n level-zero-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libze_loader.so.*
%{_libdir}/libze_validation_layer.so.*
%{_libdir}/libze_tracing_layer.so.*

%files devel
%dir %{_includedir}/level_zero
%{_includedir}/level_zero/*
%{_libdir}/libze_loader.so
%{_libdir}/libze_validation_layer.so
%{_libdir}/libze_tracing_layer.so
%{_libdir}/pkgconfig/libze_loader.pc
%{_libdir}/pkgconfig/level-zero.pc

%changelog
