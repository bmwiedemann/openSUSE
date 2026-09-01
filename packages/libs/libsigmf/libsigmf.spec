#
# spec file for package libsigmf
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


Name:           libsigmf
Version:        1.0.2
Release:        0
Summary:        C++ library for the SigMF signal metadata format
License:        Apache-2.0
URL:            https://github.com/deepsig/libsigmf
Source0:        https://github.com/deepsig/libsigmf/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libsigmf-install-interface-include-path.patch -- README says
# `#include <sigmf.h>`, but the installed interface exposed only <prefix>/include,
# so that (and the angle-bracket include inside flatbuffers_type_to_json.h) failed.
# gh#deepsig/libsigmf@3bc4be190368, unreleased since 1.0.2; drop when it ships.
Patch0:         libsigmf-install-interface-include-path.patch
BuildRequires:  cmake
# plain name, not pkgconfig(flatbuffers): what is needed is the flatc binary, not the .pc
BuildRequires:  flatbuffers-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(nlohmann_json)

%description
libsigmf is a C++ library for reading and writing SigMF metadata.

The Signal Metadata Format (SigMF) describes sets of recorded digital
signal samples with metadata written in JSON: general information about
a sample collection, the characteristics of the system that generated
it, features of the signals themselves, and the relationships between
recordings.

# both requires are load-bearing: the installed libsigmfConfig.cmake
# find_dependency()s nlohmann_json and Flatbuffers
%package        devel
Summary:        Development files for libsigmf
Requires:       flatbuffers-devel
Requires:       pkgconfig(nlohmann_json)

%description    devel
libsigmf is header-only, so this package carries the entire library:
the SigMF headers, the FlatBuffers schemas and the CMake package config.

%prep
%autosetup -p1

%build
# USE_SYSTEM_*: upstream carries nlohmann/json and flatbuffers as git submodules
# (empty in the release tarball); these build against the Factory packages instead,
# so nothing is bundled. Examples are the only compile-time test of a header-only
# library; they are not installed.
# -UNDEBUG: the examples' asserts ARE their verification, and each prints
# "passed" unconditionally, so without this the tests only prove they ran.
# NDEBUG comes from CMake's default RelWithDebInfo flags, not from the
# openSUSE optflags, so overriding just this variable leaves those intact.
%cmake \
        -DUSE_SYSTEM_FLATBUFFERS=ON \
        -DUSE_SYSTEM_JSON=ON \
        -DENABLE_EXAMPLES=ON \
        -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-UNDEBUG"
%cmake_build

%install
%cmake_install

%check
# Upstream registers these as ctest cases but never calls enable_testing(), so
# ctest finds nothing; run them directly rather than carry a patch for it.
# Their asserts are live (see the build section), so a wrong result fails here.
%{__builddir}/examples/example_record_with_variadic_dataclass
%{__builddir}/examples/example_record_with_multiple_namespaces
%{__builddir}/examples/example_sigmf_json_roundtrip
# The point of this package is downstream find_package(libsigmf), and its
# libsigmfConfig.cmake find_dependency()s nlohmann_json and Flatbuffers. Configure
# and build a throwaway consumer against the staged tree so a break in that
# contract fails here rather than in every consumer. Only <sigmf.h> is exercised:
# <sigmf/sigmf.h> also works once installed, but relies on /usr/include being an
# implicit system dir, which the staged buildroot is not.
mkdir -p %{_builddir}/consumer-test
cat > %{_builddir}/consumer-test/CMakeLists.txt <<'EOF'
cmake_minimum_required(VERSION 3.20)
project(consumer LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
find_package(libsigmf REQUIRED)
add_executable(consumer main.cpp)
target_link_libraries(consumer libsigmf::libsigmf)
EOF
cat > %{_builddir}/consumer-test/main.cpp <<'EOF'
#include <sigmf.h>
#include <iostream>
int main() {
  sigmf::SigMF<sigmf::VariadicDataClass<sigmf::core::GlobalT>,
               sigmf::VariadicDataClass<sigmf::core::CaptureT>,
               sigmf::VariadicDataClass<sigmf::core::AnnotationT> > rec;
  rec.global.access<sigmf::core::GlobalT>().sample_rate = 1500000.0;
  std::cout << rec.global.access<sigmf::core::GlobalT>().sample_rate.value()
            << std::endl;
  return 0;
}
EOF
cmake -S %{_builddir}/consumer-test -B %{_builddir}/consumer-test/build \
        -DCMAKE_PREFIX_PATH=%{buildroot}%{_prefix}
cmake --build %{_builddir}/consumer-test/build
%{_builddir}/consumer-test/build/consumer

%files devel
%license LICENSE NOTICE
%doc README.md
%{_includedir}/sigmf
%dir %{_libdir}/cmake/libsigmf
%{_libdir}/cmake/libsigmf/libsigmfConfig.cmake
%{_libdir}/cmake/libsigmf/libsigmfConfigVersion.cmake
%{_libdir}/cmake/libsigmf/libsigmfTargets.cmake

%changelog
