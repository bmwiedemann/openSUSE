#
# spec file for package libXISF
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


%if 0%{?suse_version} && 0%{?suse_version} < 1590
%global force_gcc_version 12
%endif

%define sover 0
%define full_sover 0.2.12

Name:           libXISF
Version:        0.2.12+git5.d00de20
Release:        0
Summary:        Library to read/write PixInsight XISF files
License:        GPL-3.0-or-later
URL:            https://gitea.nouspiro.space/nou/libXISF
#Source:         https://gitea.nouspiro.space/nou/libXISF/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12
BuildRequires:  liblz4-devel
BuildRequires:  libzstd-devel
BuildRequires:  pkg-config
BuildRequires:  pugixml-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Core) >= 5.14.0

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
%autosetup -p1

%build
%cmake \
%if 0%{?force_gcc_version}
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++-%{?force_gcc_version} \
%endif
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_BUILD_TYPE=release \
    -DLIBDIR=%{_libdir} \
    -DUSE_BUNDLED_LIBS=OFF
%cmake_build

%install
%cmake_install

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%{_libdir}/libXISF.so.%{sover}
%{_libdir}/libXISF.so.%{full_sover}
%license LICENSE

%files devel
%doc README.md
%{_includedir}/libXISF_global.h
%{_includedir}/libxisf.h
%{_libdir}/libXISF.so
%{_libdir}/pkgconfig/libxisf.pc

%changelog
