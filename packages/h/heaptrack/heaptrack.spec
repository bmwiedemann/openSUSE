#
# spec file for package heaptrack
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


# Needed for Leap, see boo#468748
%global __requires_exclude GLIBC_PRIVATE
%bcond_with released
Name:           heaptrack
Version:        1.6.0~pre20260904
Release:        0
Summary:        Heap Memory Allocation Profiler
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/heaptrack/
Source0:        %{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/heaptrack/%{version}/%{name}-%{version}.tar.xz.sig
%endif
Source2:        heaptrack.keyring
# PATCH-FIX-UPSTREAM
Patch1:         0001-Allow-to-use-system-robin-map-instead-of-bundled.patch
Patch2:         0002-Fix-build-with-boost-1.89.patch
Patch3:         0003-Raise-Boost-minimum-version-to-1.70.patch
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  libboost_container-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel >= 1.70
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libunwind-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  cmake(KChart6) >= 2.6.0
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(Qt6Core) >= 6.5.0
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(tsl-robin-map)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libzstd)
Suggests:       heaptrack-gui

%description
A memory profiler for Linux, tracking heap allocations.

%package devel
Summary:        Development files for the Heaptrack API
Requires:       heaptrack = %{version}

%description devel
This package contains files needed to develop for the Heaptrack
API.

%package gui
Summary:        GUI Frontend for Heaptrack
Requires:       heaptrack = %{version}

%description gui
A Qt/KF based GUI for Heaptrack.

%lang_package

%prep
%autosetup -p1

# Disable building tests, they're not used and post-build-checks trips over it
sed -i"" '/add_subdirectory(tests)/d' CMakeLists.txt

%build
%if "%{_lib}" == "lib64"
extra_opts="-DLIB_SUFFIX=64"
%endif

%cmake_kf6 -DHEAPTRACK_USE_SYSTEM_ROBINMAP=ON $extra_opts

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/heaptrack
%{_kf6_bindir}/heaptrack_print
%{_libdir}/heaptrack/

%files devel
%{_includedir}/heaptrack_api.h

%files gui
%{_kf6_bindir}/heaptrack_gui
%{_kf6_applicationsdir}/org.kde.heaptrack.desktop
%{_kf6_appstreamdir}/org.kde.heaptrack.appdata.xml
%dir %{_kf6_iconsdir}/hicolor/*
%dir %{_kf6_iconsdir}/hicolor/*/*
%{_kf6_iconsdir}/*/*/*/*.*

%files lang -f %{name}.lang

%changelog
