#
# spec file for package falco-libs
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 0
%define driver_version 10.2.0
Name:           falco-libs
Version:        0.25.4
Release:        0
Summary:        Libraries for system inspection (libscap and libsinsp)
License:        Apache-2.0
URL:            https://github.com/falcosecurity/libs
Source0:        https://github.com/falcosecurity/libs/archive/%{version}.tar.gz#/falco-libs-%{version}.tar.gz
# PATCH-FIX-UPSTREAM support-bshoshany-thread-pool-v5.patch -- build against
# bshoshany-thread-pool v5 (BS::thread_pool is now a class template) while
# staying compatible with v4
Patch0:         support-bshoshany-thread-pool-v5.patch
# abseil-cpp-devel is pulled in transitively by re2's headers
BuildRequires:  abseil-cpp-devel
BuildRequires:  bpftool
BuildRequires:  bshoshany-thread-pool-devel
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libbpf-devel
BuildRequires:  ninja
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
# uthash-devel does NOT provide pkgconfig(uthash) in openSUSE; keep the -devel
BuildRequires:  uthash-devel
BuildRequires:  valijson-devel
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)
# modern BPF ships a vendored vmlinux.h only for these arches
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

%description
The falcosecurity libs are the core libraries behind Falco and sysdig:

* libscap (system capture) reads kernel events from the various drivers
  (kernel module, eBPF, modern eBPF) and from capture files.
* libsinsp (system inspection) provides state engine, filtering, event
  formatting, and the plugin framework on top of libscap.

%package -n libscap%{sover}
Summary:        System capture library of the falcosecurity libs

%description -n libscap%{sover}
libscap reads system events from the falcosecurity drivers and from
scap capture files.

%package -n libsinsp%{sover}
Summary:        System inspection library of the falcosecurity libs
Requires:       libscap%{sover} = %{version}

%description -n libsinsp%{sover}
libsinsp adds the state engine, filtering, formatting and plugin
framework on top of libscap.

%package devel
Summary:        Development files for the falcosecurity libs
Requires:       libscap%{sover} = %{version}
Requires:       libsinsp%{sover} = %{version}

%description devel
Headers, shared-library symlinks, pkg-config and CMake files for
building against the falcosecurity libs (libscap and libsinsp).

%prep
%autosetup -p1 -n libs-%{version}

%build
%define __builder ninja
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DUSE_BUNDLED_DEPS=OFF \
  -DUSE_BUNDLED_JSONCPP=OFF \
  -DUSE_BUNDLED_TBB=OFF \
  -DUSE_BUNDLED_RE2=OFF \
  -DUSE_BUNDLED_VALIJSON=OFF \
  -DUSE_BUNDLED_LIBBPF=OFF \
  -DUSE_BUNDLED_LIBELF=OFF \
  -DUSE_BUNDLED_UTHASH=OFF \
  -DUSE_BUNDLED_ZLIB=OFF \
  -DUSE_BUNDLED_BS_THREADPOOL=OFF \
  -DUSE_BUNDLED_GTEST=OFF \
  -DENABLE_THREAD_POOL=ON \
  -DBUILD_LIBSCAP_MODERN_BPF=ON \
  -DBUILD_LIBSCAP_GVISOR=ON \
  -DBUILD_DRIVER=OFF \
  -DBUILD_BPF=OFF \
  -DCREATE_TEST_TARGETS=ON \
  -DBUILD_LIBSINSP_EXAMPLES=OFF \
  -DFALCOSECURITY_LIBS_VERSION=%{version} \
  -DFALCOSECURITY_LIBS_DRIVER_VERSION=%{driver_version} \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -Wno-dev
%cmake_build

%install
%cmake_install
# Drop the kernel driver / DKMS source tree: we build the userspace libs only,
# not the scap kernel module (the driver is shipped/built elsewhere).
rm -rf %{buildroot}%{_prefix}/src/scap-*
# test_input is a unit-test fixture engine, but with CREATE_TEST_TARGETS libsinsp
# links it (DT_NEEDED), so ship its runtime lib; drop only the unused devel symlink
rm -f %{buildroot}%{_libdir}/libscap_engine_test_input.so
%fdupes -s %{buildroot}%{_includedir}/falcosecurity

%check
# run the libsinsp gtest unit suite via upstream's make target (tests are not
# registered with ctest); libscap/driver tests need a real kernel, so skip them
cd %__builddir
%cmake_build run-unit-test-libsinsp

%ldconfig_scriptlets -n libscap%{sover}
%ldconfig_scriptlets -n libsinsp%{sover}

# libscap is split by upstream into the core plus per-engine and helper
# components (platform, event_schema, the modern-bpf/kmod/nodriver/source_plugin
# engines, and libpman); they are all libscap runtime components, kept together.
%files -n libscap%{sover}
%license COPYING
%{_libdir}/libscap.so.*
%{_libdir}/libscap_engine_modern_bpf.so.*
%{_libdir}/libscap_engine_kmod.so.*
%{_libdir}/libscap_engine_nodriver.so.*
%{_libdir}/libscap_engine_source_plugin.so.*
%{_libdir}/libscap_engine_test_input.so.*
%{_libdir}/libscap_event_schema.so
%{_libdir}/libscap_platform.so
%{_libdir}/libpman.so

%files -n libsinsp%{sover}
%license COPYING
%{_libdir}/libsinsp.so.*

%files devel
%license COPYING
%doc README.md
%{_includedir}/falcosecurity/
%{_includedir}/libpman.h
%{_libdir}/libscap.so
%{_libdir}/libsinsp.so
%{_libdir}/libscap_engine_modern_bpf.so
%{_libdir}/libscap_engine_kmod.so
%{_libdir}/libscap_engine_nodriver.so
%{_libdir}/libscap_engine_source_plugin.so
%{_libdir}/pkgconfig/libscap.pc
%{_libdir}/pkgconfig/libsinsp.pc
%{_libdir}/pkgconfig/libpman.pc

%changelog
