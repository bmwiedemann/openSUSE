#
# spec file for package gecode
#
# Copyright (c) 2022 SUSE LLC
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


%define sonum 51

Name:           gecode
Version:        6.3.0~git20211208.6b09bea4
Release:        0
Group:          Productivity/Scientific/Math
Summary:        C++ toolkit for developing constraint-based systems
License:        MIT
URL:            https://www.gecode.org/
# Source:         https://github.com/Gecode/gecode/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - https://github.com/Gecode/gecode/pull/147
Patch0:         0001-Extract-soversion-from-configure.ac-and-set-as-cmake.patch
# PATCH-FIX-UPSTREAM - https://github.com/Gecode/gecode/pull/150
Patch1:         0001-Send-DONE-message-before-disconnecting.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Gecode is an open source C++ toolkit for developing constraint-based
systems and applications. Gecode provides a constraint solver with
state-of-the-art performance while being modular and extensible.

%package -n libgecode%{sonum}
Summary:        C++ toolkit for developing constraint-based systems
Group:          System/Libraries

%description -n libgecode%{sonum}
Gecode is an open source C++ toolkit for developing constraint-based
systems and applications. Gecode provides a constraint solver with
state-of-the-art performance while being modular and extensible.

%package minizinc
Summary:        Gecode minizinc solver
Group:          Productivity/Scientific/Math
Requires:       minizinc
Provides:       minizinc-solver

%description minizinc
Minizinc solver using the Gecode toolkit.

%package devel
Summary:        C++ toolkit for developing constraint-based systems
Group:          Development/Libraries/C and C++
Requires:       libgecode%{sonum} = %{version}

%description devel
Gecode is an open source C++ toolkit for developing constraint-based
systems.

%prep
%autosetup -p1
chmod -x LICENSE

%build
%cmake
%cmake_build
%cmake_build gecode-test && ln -s ./bin/gecode-test ./

%install
%cmake_install
chmod +x %{buildroot}%{_bindir}/*

%check
%ctest

%post -n libgecode%{sonum} -p /sbin/ldconfig
%postun -n libgecode%{sonum} -p /sbin/ldconfig

%post minizinc -p /sbin/ldconfig
%postun minizinc -p /sbin/ldconfig

%files -n libgecode%{sonum}
%license LICENSE
%{_libdir}/libgecode*.so.%{sonum}
%exclude %{_libdir}/libgecodeflatzinc.so.%{sonum}

%files minizinc
%{_bindir}/fzn-gecode
%{_bindir}/mzn-gecode
%{_libdir}/libgecodeflatzinc.so.%{sonum}
%{_datadir}/minizinc

%files devel
%{_includedir}/gecode
%{_libdir}/libgecode*.so

%changelog
