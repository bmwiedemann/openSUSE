#
# spec file for package kpmcore
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
%global sover 11
Name:           kpmcore
Version:        21.12.3
Release:        0
Summary:        KDE Partition Manager core library
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# Upstream changes related to boo#1178848
Patch0:         0001-Add-new-job-to-change-permission-of-the-newly-create.patch
Patch1:         0001-Move-the-changePosixPermission-to-the-Filesystem.patch
Patch2:         0001-Add-posix-permissions-on-filesystems-used-in-posix-s.patch
Patch3:         0001-Allow-running-chmod-in-externalcommand-helper.patch
Patch4:         0001-Add-support-for-copying-unknown-partitions.patch
Patch5:         0001-Fix-davfs-entries-being-omitted-from-fstab-file.patch
Patch6:         0001-Changing-swap-labels-while-swap-is-active-does-not-s.patch
Patch7:         0001-Update-description-of-polkit-helper.patch
Patch8:         0001-Fix-a-typo-in-definition-of-MiB-constant.patch
Patch9:         0001-Set-false-as-the-default-return-value-and-change-it-.patch
Patch10:        0001-Add-a-few-more-comments-explaining-copy-direction.patch
Patch11:        0001-Rename-blockSize-to-chunkSize-to-avoid-confusion-wit.patch
Patch12:        0001-Restrict-CreateFile-method-to-WriteFstab-method-in-p.patch
Patch13:        0001-Rename-variables-into-more-appropriate-fstabPath-and.patch
Patch14:        0001-Add-a-comment-about-WriteOnly.patch
BuildRequires:  extra-cmake-modules
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5CoreAddons) >= 5.73
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(blkid) >= 2.33.2

%description
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

%package devel
Summary:        Development package for KDE Partition Manager core library
Group:          Development/Languages/C and C++
Requires:       libkpmcore%{sover} = %{version}

%description devel
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

Development package for kpmcore.

%package -n libkpmcore%{sover}
Summary:        KDE Partition Manager core library
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libkpmcore%{sover}
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

Main kpmcore library.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} <= 1500
  export CXX=g++-10
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with released}
  %find_lang kpmcore --all-name
%endif

%post -n libkpmcore%{sover} -p /sbin/ldconfig
%postun -n libkpmcore%{sover} -p /sbin/ldconfig

%files
%{_kf5_dbuspolicydir}/org.kde.kpmcore.*.conf
%{_kf5_plugindir}/libpmdummybackendplugin.so
%{_kf5_plugindir}/libpmsfdiskbackendplugin.so
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kpmcore.helperinterface.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy
%{_libexecdir}/kpmcore_externalcommand

%files -n libkpmcore%{sover}
%license LICENSES/*
%{_kf5_libdir}/libkpmcore.so.%{sover}
%{_kf5_libdir}/libkpmcore.so.%{version}

%files devel
%{_includedir}/kpmcore/
%{_kf5_cmakedir}/KPMcore/
%{_kf5_libdir}/libkpmcore.so

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
