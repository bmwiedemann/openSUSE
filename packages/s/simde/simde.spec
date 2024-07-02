#
# spec file for package simde
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


Name:           simde
Version:        0.8.2+git20240621.c903416
Release:        0
Summary:        Fallback implementation for SIMD intrinsics
License:        MIT
URL:            https://github.com/simd-everywhere/%{name}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  c++_compiler
# simde >= 0.8.0, build errors out if this is set related to simde.pc
#BuildArch:      noarch

%description
Portable implementations of SIMD intrinsics.

%package devel
Summary:        Fallback implementation for SIMD intrinsics

%description devel
The SIMDe header-only library provides fast, portable implementations of SIMD
intrinsics on hardware which do not natively support them, such as calling
SSE functions on ARM. There is no performance penalty if the hardware supports
the native implementation (e.g. SSE/AVX runs at full speed on x86, NEON on
ARM, etc.).

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/simde.pc
%license COPYING
%doc README.md

%changelog

