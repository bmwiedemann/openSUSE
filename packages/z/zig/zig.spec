#
# spec file for package zig
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


%global _lto_cflags %{nil}
%global __builder   ninja
%bcond_without  macro
%bcond_without  test

Name:           zig
Version:        0.13.0
Release:        0
Summary:        Compiler for the Zig language
License:        MIT
Group:          Development/Languages/Other
URL:            https://ziglang.org/
Source0:        https://ziglang.org/download/%{version}/%{name}-%{version}.tar.xz
Source1:        macros.%{name}
Source2:        zig-rpmlintrc
Patch0:         0000-remove-lld-in-cmakelist.patch
Patch1:         0001-invoke-lld.patch
Patch2:         0002-no-lld-libs-and-includes.patch
BuildRequires:  clang18
BuildRequires:  clang18-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc
BuildRequires:  glibc-devel
BuildRequires:  help2man
BuildRequires:  lld18
BuildRequires:  llvm18-devel
BuildRequires:  ninja
BuildRequires:  zlib-devel
Requires:       lld18

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
%autosetup -n %{name}-%{version} -p1

%build
# NOTE: ix86 architectures will still fail to build due to OOM. Once 0.11.x lands,
# this won't be an issue anymore since that version does not use much memory
%cmake \
%ifarch aarch64 s390x
  -DCMAKE_BUILD_TYPE=Release \
%endif
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_C_COMPILER="clang-18" \
  -DCMAKE_CXX_COMPILER="clang++-18" \
  -DZIG_SHARED_LLVM=On \
  -DZIG_TARGET_MCPU="baseline" \
  -DZIG_VERSION:STRING="%{version}"

%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr "%{buildroot}%{_bindir}/%{name}" --version-option=version --output=%{buildroot}%{_mandir}/man1/%{name}.1

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -p -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}

sed -i -e "s|@@ZIG_VERSION@@|%{version}|"  %{buildroot}%{_rpmmacrodir}/macros.%{name}

mv -v doc/langref.html.in doc/langref.html

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
