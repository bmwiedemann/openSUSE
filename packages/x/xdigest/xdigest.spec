#
# spec file for package xdigest
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Name:           xdigest
Version:        0.4.1
Release:        0
Summary:        Digest algorithm library designed for speed
License:        Apache-2.0
URL:            https://github.com/rinrab/xdigest
Source:         https://github.com/rinrab/xdigest/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
Xdigest is a digest algorithm implementation library designed for speed. It
uses assembly optimization for performance, is designed to be small and
lightweight and provides a simple API.

%package -n lib%{name}%{sover}
Summary:        Digest algorithm library designed for speed

%description -n lib%{name}%{sover}
Xdigest is a digest algorithm implementation library designed for speed. It
uses assembly optimization for performance, is designed to be small and
lightweight and provides a simple API.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description devel
Xdigest is a digest algorithm implementation library designed for speed. It
uses assembly optimization for performance, is designed to be small and
lightweight and provides a simple API.

This package contains the files needed to develop and build using %{name}.

%prep
%autosetup -p1

%build
%cmake \
%ifnarch %{ix86} x86_64
	-DUSE_ASM:BOOL=OFF \
%endif
%ifarch %{arm} ppc64le riscv64 s390x
	-DENABLE_TESTS:BOOF=OFF \
%endif
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%license LICENSE NOTICE
%{_libdir}/libxdigest.so.%{sover}{,.*}

%files devel
%license LICENSE NOTICE
%doc CHANGELOG.md README.md
%{_includedir}/xdigest
%dir %{_prefix}/lib/cmake
%{_prefix}/lib/cmake/xdigest
%{_libdir}/libxdigest.so
%{_libdir}/pkgconfig/xdigest.pc

%changelog
