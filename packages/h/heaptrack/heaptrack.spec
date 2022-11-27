#
# spec file for package heaptrack
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


%define kf5_version 5.26.0
%bcond_without released
Name:           heaptrack
Version:        1.4.0
Release:        0
Summary:        Heap Memory Allocation Profiler
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/heaptrack/
Source0:        https://download.kde.org/stable/heaptrack/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/heaptrack/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        heaptrack.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_container-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libunwind-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  cmake(KChart) >= 2.6.0
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(Qt5Core) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libzstd)
Suggests:       heaptrack-gui

%description
A memory profiler for Linux, tracking heap allocations.

%package devel
Summary:        Development files for the Heaptrack API
Requires:       %{name} = %{version}

%description devel
This package contains files needed to develop for the Heaptrack
API.

%package gui
Summary:        GUI Frontend for Heaptrack
Requires:       %{name} = %{version}

%description gui
A Qt5/KF5 based GUI for Heaptrack.

%lang_package

%prep
%autosetup -p1

# Disable building tests, they're not used and post-build-checks trips over it
sed -i"" '/add_subdirectory(tests)/d' CMakeLists.txt

%build
%if "%{_lib}" == "lib64"
extra_opts="-DLIB_SUFFIX=64"
%endif

%cmake_kf5 -d build -- $extra_opts

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

# Fixup desktop file
%suse_update_desktop_file org.kde.heaptrack Development Profiling

%files
%license LICENSES/*
%doc README.md
%{_kf5_bindir}/heaptrack
%{_kf5_bindir}/heaptrack_print
%{_libdir}/heaptrack/

%files devel
%license LICENSES/*
%{_includedir}/heaptrack_api.h

%files gui
%{_kf5_bindir}/heaptrack_gui
%{_kf5_applicationsdir}/org.kde.heaptrack.desktop
%{_kf5_appstreamdir}/org.kde.heaptrack.appdata.xml
%dir %{_kf5_iconsdir}/hicolor/*
%dir %{_kf5_iconsdir}/hicolor/*/*
%{_kf5_iconsdir}/*/*/*/*.*

%files lang -f %{name}.lang

%changelog
