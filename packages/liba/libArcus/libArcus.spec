#
# spec file for package libArcus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        4.1.0
Release:        0
Summary:        3D printer control software
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            http://github.com/Ultimaker/%name
Source:         %name-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel >= 3.0.0
BuildRequires:  python3-sip-devel

%description
Communication library between internal components for Ultimaker software

%package -n %name%{sover}
Summary:        3D printer control software
Group:          System/Libraries

%description -n %name%{sover}
Communication library between internal components for Ultimaker software

%package devel
Summary:        Header files for libArcus
Group:          Development/Libraries/C and C++
Requires:       libArcus%{sover} = %{version}
Requires:       protobuf-devel >= 3.0.0
Requires:       python3-sip-devel

%description devel
The %{name}-devel package includes the header files, libraries and development
tools necessary for compiling and linking programs which use %{name}.

%prep
%setup

%build
%cmake
make %{?_smp_mflags}

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
%{python3_sitelib}/Arcus.so
%{_libdir}/libArcus.so.*

%changelog
