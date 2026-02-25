#
# spec file for package qpl
#
# Copyright (c) 2026 SUSE LLC
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

%define libname libqpl
%define sover   1
Name:           qpl
Version:        1.9.0
Release:        0
Summary:        Intel Query Processing Library
License:        MIT
URL:            https://github.com/intel/qpl
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove-submodule-dependencies.patch antonio.teixeira@suse.com -- Use system googletest and don't build benchmarks as they don't get installed anyway
Patch0:         remove-submodule-dependencies.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  pkgconfig(gtest)
# For the hardware-accelerated path, libaccel-config is dynamically loaded by libqpl if present
Suggests:       libaccel-config1
ExclusiveArch:  x86_64

%description
The Intel Query Processing Library (Intel QPL) is an open-source
library to provide high-performance query processing operations on
Intel CPUs.

%package        devel
Summary:        Development files for Intel Query Processing Library
Requires:       %{libname}%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{libname}%{sover}
Summary:        Intel Query Processing Library
License:        MIT

%description -n %{libname}%{sover}
The Intel Query Processing Library (Intel QPL) is an open-source
library to provide high-performance query processing operations on
Intel CPUs.

%package        data
Summary:        Auxiliary files for Intel QPL
License:        MIT
BuildArch:      noarch
# accel-config utility is needed by the accel_conf.py script
Requires:       /usr/bin/accel-config

%description    data
Auxiliary config files and scripts for configuring Intel IAA devices.

%prep
%autosetup -p1

%build
%cmake \
    -DQPL_LIBRARY_TYPE=SHARED \
    -DQPL_TREAT_WARNINGS_AS_ERRORS=OFF
    
%cmake_build

%install
%cmake_install

# Add shebang in accel_conf.sh
sed -i '1i#!%{_bindir}/bash' %{buildroot}%{_datadir}/QPL/scripts/accel_conf.sh

%check
%ctest

%ldconfig_scriptlets -n %{libname}%{sover}

%files -n %{libname}%{sover}
%license LICENSE
%{_libdir}/%{libname}.so.%{sover}*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/QPL

%files data
%{_datadir}/QPL

%changelog
