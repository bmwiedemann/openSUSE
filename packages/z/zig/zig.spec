#
# spec file for package zig
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global _lto_cflags %{nil}
%global __builder   ninja
%bcond_without  macro
%bcond_without  test

Name:           zig
Version:        0.15.1
Release:        0
Summary:        Compiler for the Zig language
License:        MIT
Group:          Development/Languages/Other
URL:            https://ziglang.org/
Source0:        https://ziglang.org/download/%{version}/%{name}-%{version}.tar.xz
Source1:        macros.%{name}
# The vendored tarball is for tests. This contains the
# cached deps. See https://en.opensuse.org/Zig#Packaging
Source2:        vendor.tar.zst
Source3:        zig-rpmlintrc
Patch0:         0000-remove-lld-in-cmakelist.patch
Patch1:         0001-invoke-lld.patch
Patch2:         0002-no-lld-libs-and-includes.patch
# Just copying from Archlinux. Thanks
Patch3:         https://gitlab.archlinux.org/archlinux/packaging/packages/zig/-/raw/main/skip-localhost-test.patch
# to improve reproducible-builds -- https://github.com/ziglang/zig/pull/22673
Patch4:         reproducible.patch
BuildRequires:  clang20
BuildRequires:  clang20-devel
BuildRequires:  cmake
BuildRequires:  elfutils
BuildRequires:  gcc-c++
BuildRequires:  glibc
BuildRequires:  glibc-devel
BuildRequires:  glibc-devel-32bit
BuildRequires:  help2man
BuildRequires:  libelf-devel
BuildRequires:  liburing-devel
BuildRequires:  lld20
BuildRequires:  llvm20-devel
BuildRequires:  mold
BuildRequires:  ninja
BuildRequires:  zlib-devel
BuildRequires:  zstd
BuildRequires:  (gcc13-c++ if gcc13)
BuildRequires:  (gcc14-c++ if gcc14)
BuildRequires:  (gcc15-c++ if gcc15)
Requires:       lld20

# llvm-config is missing targets for ppc and arm architectures.
# ExcludeArch:    ppc64 ppc64le %%arm %%ix86
ExclusiveArch:  x86_64 aarch64 riscv64 %{mips64}

# Zig needs this to work
Requires:       %{name}-libs = %{version}

# Zig Macros
Recommends:     %{name}-rpm-macros

%description
General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

* Robust - behavior is correct even for edge cases such as out of memory.
* Optimal - write programs the best way they can behave and perform.
* Reusable - the same code works in many environments which have different constraints.
* Maintainable - precisely communicate intent to the compiler and other programmers.
The language imposes a low overhead to reading code and is resilient to changing requirements and environments.

%package libs
Summary:        Zig Standard Library
BuildArch:      noarch

%description libs
%{name} Standard Library

%if %{with macro}
%package        rpm-macros
Summary:        Common RPM macros for %{name}
Requires:       rpm
BuildArch:      noarch

%description    rpm-macros
This package contains common RPM macros for %{name}.
%endif

%prep
%autosetup -n %{name}-%{version} -p1 -a2

%build
# CMAKE on Tumbleweed has the CMAKE_LINKER_TYPE option
%if 0%{?suse_version} > 1600

%cmake \
%ifarch aarch64 s390x
  -DCMAKE_BUILD_TYPE=Release \
%endif
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_C_COMPILER="clang-20" \
  -DCMAKE_CXX_COMPILER="clang++-20" \
  -DCMAKE_LINKER_TYPE=MOLD \
  -DZIG_SHARED_LLVM=On \
  -DZIG_USE_LLVM_CONFIG=ON \
  -DZIG_TARGET_MCPU="baseline" \
  -DZIG_VERSION:STRING="%{version}"

%else

%cmake \
%ifarch aarch64 s390x
  -DCMAKE_BUILD_TYPE=Release \
%endif
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_C_COMPILER="clang-20" \
  -DCMAKE_CXX_COMPILER="clang++-20" \
  -DZIG_SHARED_LLVM=On \
  -DZIG_USE_LLVM_CONFIG=ON \
  -DZIG_TARGET_MCPU="baseline" \
  -DZIG_VERSION:STRING="%{version}"

%endif

# Workaround since CMAKE on Leap does not have
# the CMAKE_LINKER_TYPE option
%if 0%{?suse_version} > 1600
%cmake_build
%else
mold -run %cmake_build
%endif

%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr "%{buildroot}%{_bindir}/%{name}" --version-option=version --output=%{buildroot}%{_mandir}/man1/%{name}.1

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -p -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}

sed -i -e "s|@@ZIG_VERSION@@|%{version}|"  %{buildroot}%{_rpmmacrodir}/macros.%{name}

mv -v doc/langref.html.in doc/langref.html

%if 0%{?with test}
%check
./build/stage3/bin/zig build test -Dconfig_h=build/config.h \
	-Dcpu=baseline \
	-Dskip-debug \
	-Dskip-release-safe \
	-Dskip-release-small \
        -Dstatic-llvm=false \
	-Denable-llvm=true \
	-Dskip-non-native=true
%endif

%files
%license LICENSE
%{_bindir}/zig
%{_mandir}/man1/%{name}.1%{?ext_man}
%doc README.md
%doc lib/docs
%doc doc/langref.html

%files libs
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/*

%if %{with macro}
%files rpm-macros
%{_rpmmacrodir}/macros.%{name}
%endif

%changelog
