#
# spec file for package sse2neon
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


Name:           sse2neon
Version:        1.9.1
Release:        0
Summary:        A translator from Intel SSE intrinsics to Arm/Aarch64 NEON implementation
License:        MIT
URL:            https://github.com/DLTcollab/sse2neon
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  aarch64
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
sse2neon is a translator of Intel SSE (Streaming SIMD Extensions) intrinsics to
Arm NEON, shortening the time needed to get an Arm working program that then
can be used to extract profiles and to identify hot paths in the code. The
header file sse2neon.h contains several of the functions provided by Intel
intrinsic headers such as <xmmintrin.h>, only implemented with NEON-based
counterparts to produce the exact semantics of the intrinsics.

%package    devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description devel
sse2neon is a translator of Intel SSE (Streaming SIMD Extensions) intrinsics to
Arm NEON, shortening the time needed to get an Arm working program that then
can be used to extract profiles and to identify hot paths in the code. The
header file sse2neon.h contains several of the functions provided by Intel
intrinsic headers such as <xmmintrin.h>, only implemented with NEON-based
counterparts to produce the exact semantics of the intrinsics.

Devel package

%prep
%autosetup -p1

%install
install -dm755 %{buildroot}%{_includedir}
install -pm644 %{name}.h %{buildroot}%{_includedir}

%check
%make_build check

%files devel
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_includedir}/%{name}.h

%changelog
