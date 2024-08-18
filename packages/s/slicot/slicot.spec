#
# spec file for package slicot
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


Name:           slicot
Version:        5.9
Release:        0
Summary:        A Fortran subroutines library for systems and control 
License:        BSD-3-Clause
URL:            https://github.com/SLICOT/SLICOT-Reference
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-fortran

%description
SLICOT - Subroutine Library In COntrol Theory - is a general purpose basic
mathematical library for control theoretical computations. The library provides
tools to perform essential system analysis and synthesis tasks.

%package devel-static
Summary:        Static library for slicot

%description devel-static
This package provides the static library for slicot.

%prep
%autosetup -p1 -n SLICOT-Reference-%{version}
sed -Ei "s/^OPTS = .*/OPTS = %{optflags} -ffat-lto-objects/" make_Unix.inc

%build
%make_build -f makefile_Unix lib

%install
mkdir -p %{buildroot}%{_libdir}
install -m0644 slicot.a %{buildroot}%{_libdir}/libslicot.a

%files devel-static
%license LICENSE
%doc README.md
%{_libdir}/libslicot.a

%changelog

