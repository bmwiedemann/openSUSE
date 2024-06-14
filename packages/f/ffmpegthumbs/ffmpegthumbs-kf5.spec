#
# spec file for package ffmpegthumbs
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


%define kf5_version 5.92.0
%define qt5_version 5.15.0

%define rname ffmpegthumbs
%bcond_without released
Name:           ffmpegthumbs-kf5
Version:        24.05.1
Release:        0
Summary:        FFmpeg-based thumbnail creator for video files
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source0:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(taglib)
# Provides ffmpegthumbnailersettings5.kcfg and org.kde.ffmpegthumbs.metainfo.xml
Requires:       ffmpegthumbs = %{version}

%description
FFmpeg-based thumbnail creator for video files.
This package will only work for packages still using KDE Frameworks 5

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

# These files are already shipped by ffmpegthumbs
rm %{buildroot}%{_kf5_appstreamdir}/org.kde.ffmpegthumbs.metainfo.xml
rm %{buildroot}%{_kf5_configkcfgdir}/ffmpegthumbnailersettings5.kcfg

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_debugdir}/ffmpegthumbs.categories
%dir %{_kf5_plugindir}/kf5/thumbcreator
%{_kf5_plugindir}/kf5/thumbcreator/ffmpegthumbs.so

%changelog
