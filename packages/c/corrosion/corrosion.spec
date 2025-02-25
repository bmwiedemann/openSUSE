#
# spec file for package corrosion
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


Name:           corrosion
Version:        0.5.1
Release:        0
Summary:        Rust integration into existing CMake project
License:        MIT
URL:            https://corrosion-rs.github.io/corrosion/
Source0:        https://github.com/corrosion-rs/corrosion/archive/refs/tags/v%{version}.tar.gz#/corrosion-%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:  cmake >= 3.22
BuildRequires:  gcc-c++
BuildRequires:  rust
Requires:       cargo
Requires:       cmake >= 3.12
Requires:       rust

%description
Corrosion, formerly known as cmake-cargo, is a tool for integrating Rust into
an existing CMake project. Corrosion can automatically import executables,
static libraries, and dynamic libraries from a workspace or package manifest
(Cargo.toml file).

%prep
%autosetup -p1

%build
%cmake -DCORROSION_BUILD_TESTS:BOOL=TRUE

%install
%cmake_install

%check
# Some tests need rustup which conflicts with cargo
excluded_tests="cbindgen_rust2cpp_build|cbindgen_rust2cpp_run_cpp-exe|rustup_proxy_build|hostbuild_build|hostbuild_run_rust-host-program|parse_target_triple_build"
%ctest --exclude-regex "${excluded_tests}"

%files
%license LICENSE
%doc README.md RELEASES.md
%{_datadir}/cmake/Corrosion.cmake
%{_datadir}/cmake/CorrosionGenerator.cmake
%{_datadir}/cmake/FindRust.cmake
%{_libdir}/cmake/Corrosion/

%changelog
