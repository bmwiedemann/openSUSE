#
# spec file for package pmemkv
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


Name:           pmemkv
Version:        1.3
Release:        0
Summary:        Key/Value Datastore for Persistent Memory
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://pmem.io/pmdk/
Source:         https://github.com/pmem/pmemkv/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libpmemobj-cpp-devel >= 1.11
BuildRequires:  libpmemobj-devel >= 1.8
BuildRequires:  memkind-devel >= 1.8.0
BuildRequires:  pkgconfig
BuildRequires:  pmdk-tools >= 1.8
BuildRequires:  pkgconfig(RapidJSON)
ExclusiveArch:  x86_64 ppc64le

%description
pmemkv is a local/embedded key-value datastore optimized for persistent memory.
Rather than being tied to a single language or backing implementation, `pmemkv`
provides different options for language bindings and storage engines.

%package -n libpmemkv1
Summary:        Key/Value Datastore for Persistent Memory
Group:          System/Libraries
Requires:       libpmemkv_json_config1 >= %{version}

%description -n libpmemkv1
pmemkv is a local/embedded key-value datastore optimized for persistent memory.
Rather than being tied to a single language or backing implementation, `pmemkv`
provides different options for language bindings and storage engines.

%package -n libpmemkv_json_config1
Summary:        Helper library for libpmemkv
Group:          System/Libraries

%description -n libpmemkv_json_config1
pmemkv is a local/embedded key-value datastore optimized for persistent memory.
Rather than being tied to a single language or backing implementation, `pmemkv`
provides different options for language bindings and storage engines.

%package devel
Summary:        Key/Value Datastore for Persistent Memory
Group:          Development/Libraries/C and C++
Requires:       libpmemkv1 >= %{version}
Requires:       libpmemkv_json_config1 >= %{version}
Requires:       libpmemobj++-devel >= 1.10

%description devel
This package contains the header files for libpmemkv and libpmemkv_json_config

%prep
%setup -q

%build
# ENGINE_VCMAP needs package-config(tbb) which is currently not available
%cmake -DTESTS_USE_VALGRIND=0 -DENGINE_VCMAP=0
%make_build

%install
%cmake_install

%post   -n libpmemkv1 -p /sbin/ldconfig
%postun -n libpmemkv1 -p /sbin/ldconfig
%post   -n libpmemkv_json_config1 -p /sbin/ldconfig
%postun -n libpmemkv_json_config1 -p /sbin/ldconfig

%files -n libpmemkv1
%license LICENSE
%{_libdir}/libpmemkv.so.1*

%files -n libpmemkv_json_config1
%license LICENSE
%{_libdir}/libpmemkv_json_config.so.1*

%files devel
%doc ChangeLog
%{_includedir}/libpmemkv*.h
%{_includedir}/libpmemkv*.hpp
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpmemkv.so
%{_libdir}/libpmemkv_json_config.so

%changelog
