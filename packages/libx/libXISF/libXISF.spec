#
# spec file for package libXISF
#
# Copyright (c) 2023 SUSE LLC
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
Name:           libXISF
Version:        0.2.1
Release:        0
Summary:        Library to read/write PixInsight XISF files
License:        GPL-3.0-or-later
URL:            https://gitea.nouspiro.space/nou/libXISF
Source:         https://gitea.nouspiro.space/nou/libXISF/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core) >= 5.14.0
%if 0%{?suse_version} < 1590
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif

%description
C++ library that can read and write XISF files produced by PixInsight.

%package -n %{name}%{sover}
Summary:        Library to read/write PixInsight XISF files

%description -n %{name}%{sover}
C++ library that can read and write XISF files produced by PixInsight.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
This package contains all the needed development files to use %{name}.

%prep
%autosetup -p1 -n libxisf

%build
%cmake \
%if 0%{?suse_version} < 1590
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++-10 \
%else
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++ \
%endif
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_BUILD_TYPE=release \
    -DLIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%{_libdir}/libXISF.so.%{sover}
%{_libdir}/libXISF.so.%{version}
%license LICENSE

%files devel
%doc README.md
%{_includedir}/libXISF_global.h
%{_includedir}/libxisf.h
%{_libdir}/libXISF.so

%changelog
