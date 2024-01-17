#
# spec file for package heatshrink
#
# Copyright (c) 2023 SUSE LLC
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


%define libname libheatshrink
%define soversion 0_4_1
Name:           heatshrink
Version:        0.4.1
Release:        0
Summary:        Data compression library for embedded/real-time systems
License:        ISC AND AGPL-3.0-only
URL:            https://github.com/atomicobject/heatshrink
Source0:        https://github.com/atomicobject/heatshrink/archive/refs/tags/v%{version}.tar.gz#/heatshrink-%{version}.tar.gz
Source1:        https://github.com/prusa3d/libbgcode/raw/7aaf717fef6a83e4568b67729d5b0267453de815/deps/heatshrink/CMakeLists.txt
Source2:        https://github.com/prusa3d/libbgcode/raw/7aaf717fef6a83e4568b67729d5b0267453de815/deps/heatshrink/Config.cmake.in
Source3:        https://github.com/prusa3d/libbgcode/raw/7aaf717fef6a83e4568b67729d5b0267453de815/LICENSE#/LICENSE-libbgcode
BuildRequires:  cmake

%description
A data compression/decompression library for embedded/real-time systems.

Key Features:
* Low memory usage (as low as 50 bytes) It is useful for some cases with less than 50 bytes, and useful for many general cases with < 300 bytes.
* Incremental, bounded CPU use You can chew on input data in arbitrarily tiny bites. This is a useful property in hard real-time environments.
* Can use either static or dynamic memory allocation The library doesn't impose any constraints on memory management.
* ISC license You can use it freely, even for commercial purposes.

%package -n %{libname}%{soversion}
Summary:        Data compression library for embedded/real-time systems

%description -n %{libname}%{soversion}
A data compression/decompression library for embedded/real-time systems.

%package -n %{libname}_dynalloc%{soversion}
Summary:        Data compression library for embedded/real-time systems

%description -n %{libname}_dynalloc%{soversion}
A data compression/decompression library for embedded/real-time systems.

%package devel
Summary:        Development files for the heatshrink data compression library
Requires:       %{libname}%{soversion} = %{version}
Requires:       %{libname}_dynalloc%{soversion} = %{version}

%description devel
Header and CMake configuration files required to develop applications using %{name}

%prep
%autosetup -p1 -n heatshrink-%{version}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} ./

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}%{soversion}
%ldconfig_scriptlets -n %{libname}_dynalloc%{soversion}

%files
%license LICENSE
%{_bindir}/heatshrink

%files -n %{libname}%{soversion}
%license LICENSE
%{_libdir}/%{libname}.so.%{version}

%files -n %{libname}_dynalloc%{soversion}
%license LICENSE
%{_libdir}/%{libname}_dynalloc.so.%{version}

%files devel
%license LICENSE LICENSE-libbgcode
%{_libdir}/%{libname}.so
%{_libdir}/%{libname}_dynalloc.so
%{_includedir}/heatshrink/
%{_libdir}/cmake/heatshrink/

%changelog
