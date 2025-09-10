#
# spec file for package ffmpegthumbs
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.14.0
%define qt6_version 6.8.0

%bcond_without released
Name:           ffmpegthumbs
Version:        25.08.0
Release:        0
Summary:        FFmpeg-based thumbnail creator for video files
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-UPSTREAM -- ffmpeg 8 compat
Patch0:         ffmpegthumbs-ffmpeg8.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(taglib)

%description
FFmpeg-based thumbnail creator for video files.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_appstreamdir}/org.kde.ffmpegthumbs.metainfo.xml
%{_kf6_configkcfgdir}/ffmpegthumbnailersettings5.kcfg
%{_kf6_debugdir}/ffmpegthumbs.categories
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/ffmpegthumbs.so

%changelog
