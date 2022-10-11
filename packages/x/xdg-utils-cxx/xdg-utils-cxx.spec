#
# spec file for package xdg-utils-cxx
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


%define soname1 libXdgUtilsBaseDir1_0_1
%define soname2 libXdgUtilsDesktopEntry1_0_1

Name:           xdg-utils-cxx
Version:        1.0.1
Release:        0
Summary:        Freedesktop Standards C++ Implementation
License:        MIT
Group:          System/Libraries
URL:            https://github.com/azubieta/xdg-utils-cxx
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/xdg-utils-cxx-%{version}.tar.gz
Patch0:         https://salsa.debian.org/qt-kde-team/3rdparty/xdg-utils-cxx/-/raw/master/debian/patches/fix_so_version.patch
Patch1:         https://salsa.debian.org/qt-kde-team/3rdparty/xdg-utils-cxx/-/raw/master/debian/patches/fix_install_path.patch
BuildRequires:  binutils
BuildRequires:  cmake >= 3.0
BuildRequires:  c++_compiler
BuildRequires:  libstdc++-devel

%description
Implementation of the FreeDesktop specifications to be used in c++ projects.

%package -n %{soname1}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{soname1}
Implementation of the FreeDesktop specifications to be used in c++ projects.
Shared library for %{name}.

%package -n %{soname2}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{soname2}
Implementation of the FreeDesktop specifications to be used in c++ projects.
Shared library for %{name}.

%package devel
Summary:        Development files for xdg-utils-cxx
Group:          Development/Languages/C and C++
Requires:       %{soname1} = %{version}
Requires:       %{soname2} = %{version}

%description devel
Development files for %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DXDG_UTILS_SHARED=ON \
	-DXDG_UTILS_TESTS=OFF \
	%{nil}
%cmake_build

%install
%cmake_install

%if %{suse_version} >= 1599
%ldconfig_scriptlets -n %{soname1}
%ldconfig_scriptlets -n %{soname2}

%else

%post -n %{soname1} -p /sbin/ldconfig
%postun -n %{soname1} -p /sbin/ldconfig

%post -n %{soname2} -p /sbin/ldconfig
%postun -n %{soname2} -p /sbin/ldconfig

%endif

%files -n %{soname1}
%license LICENSE
%{_libdir}/libXdgUtilsBaseDir.so.*

%files -n %{soname2}
%license LICENSE
%{_libdir}/libXdgUtilsDesktopEntry.so.*

%files devel
%license LICENSE
%dir %{_libdir}/cmake/XdgUtils
%{_libdir}/cmake/XdgUtils/*.cmake
%dir %{_includedir}/XdgUtils
%{_includedir}/XdgUtils/
%{_libdir}/libXdgUtilsBaseDir.so
%{_libdir}/libXdgUtilsDesktopEntry.so

%changelog
