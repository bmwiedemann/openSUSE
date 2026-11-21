#
# spec file for package bpfilter
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


%define cc_package clang%{product_libs_llvm_ver}
%define cc_binary clang-%{product_libs_llvm_ver}
%global soname_version 0
Name:           bpfilter
Version:        0.8.0
Release:        0
Summary:        BPF-based packet filtering framework
License:        GPL-2.0-only AND MIT
URL:            https://bpfilter.io
Source:         https://github.com/meta/bpfilter/archive/refs/tags/v%{version}.tar.gz#/bpfilter-%{version}.tar.gz
BuildRequires:  %{cc_package}
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  linux-glibc-devel
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  xxd
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libbpf)
ExclusiveArch:  x86_64 aarch64

%description
BPF-based packet filtering framework to convert text-format filtering rules
into BPF programs attach to your kernel.

%package devel
Summary:        Development files for %{name}
Requires:       libbpfilter%{soname_version}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
BPF-based packet filtering framework to convert text-format filtering rules
into BPF programs attach to your kernel.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libbpfilter%{soname_version}
Summary:        Shared library for %{name}

%description -n libbpfilter%{soname_version}
BPF-based packet filtering framework to convert text-format filtering rules
into BPF programs attach to your kernel.

The libbpfilter%{soname_version} package contains the shared library.

%ldconfig_scriptlets -n libbpfilter%{soname_version}

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWITH_DOCS=OFF -DWITH_TESTS=OFF -DWITH_TESTS_UNIT=OFF \
       -DCLANG_BIN=%{_bindir}/%{cc_binary}
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%license COPYING
%{_sbindir}/bfcli

%files -n libbpfilter%{soname_version}
%license COPYING
%{_libdir}/libbpfilter.so.%{soname_version}
%{_libdir}/libbpfilter.so.%{version}

%files devel
%{_includedir}/bpfilter/
%{_libdir}/libbpfilter.so
%{_libdir}/pkgconfig/bpfilter.pc

%changelog
