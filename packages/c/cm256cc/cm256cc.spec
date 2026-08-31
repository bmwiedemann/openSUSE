#
# spec file for package cm256cc
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2017-2025, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
Name:           cm256cc
Version:        1.1.2
Release:        0
Summary:        Fast GF(256) Cauchy MDS Block Erasure Codec in C++
# Legal-Review-Notice: upstream declares no single licence.
# cm256.{cpp,h}/gf256.{cpp,h} carry a 3-clause BSD header (the non-endorsement
# clause is present, so BSD-3-Clause and not BSD-2-Clause as tagged before);
# export.h is GPL-3.0-only and is #included by both installed headers, so the
# built library is GPL-3.0-only; sse2neon.h (NEON path, also installed) is MIT.
# The repository LICENSE file is the GPL-3.0 text.
License:        BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            https://github.com/f4exb/cm256cc
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM cm256cc-fix-pkgconfig-version.patch gh#f4exb/cm256cc#23 --
# PATCH_VERSION was never bumped for 1.1.1 or 1.1.2, so the .pc still claims
# 1.1.0; sdrangel version-checks it and silently disables its cm256cc plugins.
Patch0:         cm256cc-fix-pkgconfig-version.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# Upstream needs SSSE3 (x86) or NEON (ARM) and has no scalar fallback: CMake
# return()s early elsewhere, so nothing is built and %%install dies. i586 would
# compile but SSSE3 is above its baseline; armv7l needs -mfpu=neon, which the
# ENABLE_DISTRIBUTION path does not add.
ExclusiveArch:  x86_64 aarch64

%description
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

%package -n libcm256cc%{sover}
Summary:        Fast GF(256) Cauchy MDS Block Erasure Codec in C++
# the library used to live in the main package, which is gone now; without
# this the two own the same %%{_libdir}/libcm256cc.so.1* paths
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n libcm256cc%{sover}
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

%package devel
Summary:        Development files for the cm256cc library
Requires:       libcm256cc%{sover} = %{version}

%description devel
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

This subpackage contains libraries and header files for developing
applications that want to make use of libcm256cc.

%prep
%autosetup

%build
# ENABLE_DISTRIBUTION pins x86 to the SSSE3 baseline the library needs anyway.
# The default path probes the *build host* CPU with try_run() and records what
# it happens to support, which is not reproducible across OBS workers.
# SKIP_INSTALL_RPATH: upstream hardcodes an install RPATH of %%{_prefix}/lib,
# dead weight on lib64; %%cmake passes the flag itself only on suse_version <= 1500.
%cmake \
  -DENABLE_DISTRIBUTION=ON \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install
# upstream's unit-test and UDP demo programs, not user-facing tools
rm %{buildroot}%{_bindir}/cm256_rx
rm %{buildroot}%{_bindir}/cm256_test
rm %{buildroot}%{_bindir}/cm256_tx

%check
%{__builddir}/cm256_test

%ldconfig_scriptlets -n libcm256cc%{sover}

%files -n libcm256cc%{sover}
%license LICENSE
%{_libdir}/libcm256cc.so.%{sover}*

%files devel
%doc README.md
%{_includedir}/cm256cc
%{_libdir}/libcm256cc.so
%{_libdir}/pkgconfig/libcm256cc.pc

%changelog
