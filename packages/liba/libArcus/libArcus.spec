#
# spec file for package libArcus
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 3
Name:           libArcus
%define sversion        4.9
Version:        4.9.0
Release:        0
Summary:        3D printer control software
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/Ultimaker/%name
Source:         https://github.com/Ultimaker/libArcus/archive/%{sversion}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE - use Qt5 sip import name, taken from Fedora
Patch0:         libArcus-3.5.1-PyQt5.sip.patch
# PATCH-FIX-UPSTREAM - https://github.com/Ultimaker/libArcus/pull/113
Patch1:         0001-Fix-build-with-Python-3.8-and-no-undefined-linker-flags.patch
BuildRequires:  cmake >= 3.6
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel >= 3.0.0
BuildRequires:  python3-sip-devel < 5
%if 0%{?suse_version} >= 1550
BuildRequires:  python3-qt5-sip
%else
BuildRequires:  python3-sip
%endif

%description
Communication library between internal components for Ultimaker software

%package -n %name%{sover}
Summary:        3D printer control software
# The forked libArcus-lulzbot uses the same SONAME ...
Group:          System/Libraries
Provides:       libArcus-Ultimaker

%description -n %name%{sover}
Communication library between internal components for Ultimaker software

%package devel
Summary:        Header files for libArcus
Group:          Development/Libraries/C and C++
Requires:       libArcus%{sover} = %{version}
Requires:       protobuf-devel >= 3.0.0
Requires:       python3-sip-devel < 5

%description devel
The %{name}-devel package includes the header files, libraries and development
tools necessary for compiling and linking programs which use %{name}.

%package -n python3-Arcus
Summary:        Python bindings for libArcus
Group:          Development/Languages/Python
Requires:       libArcus-Ultimaker
%if 0%{?suse_version} >= 1550
Requires:       python3-qt5-sip
%else
Requires:       python3-sip
%endif

%description -n python3-Arcus
Python bindings for the Arcus communication library.

%prep
%autosetup -n %{name}-%{sversion} -p1

%build
%cmake

%cmake_build

%install
%cmake_install

%post   -n %name%{sover} -p /sbin/ldconfig

%postun -n %name%{sover} -p /sbin/ldconfig

%files devel
%doc TODO.md
%{_includedir}/Arcus
%{_libdir}/cmake/Arcus
%{_libdir}/libArcus.so

%files -n %name%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libArcus.so.*

%files -n python3-Arcus
%license LICENSE
%{python3_sitearch}/Arcus.so

%changelog
