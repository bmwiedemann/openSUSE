#
# spec file for package optiimage
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

Name:           optiimage
Version:        1.0.0
Release:        0
Summary:        Image optimizer tool
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/optiimage/
Source0:        https://download.kde.org/stable/optiimage/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/optiimage/%{name}-%{version}.tar.xz.sig
Source2:        optiimage.keyring
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami2) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 1.5.0
BuildRequires:  cmake(QCoro6Core) >= 0.4
BuildRequires:  cmake(QCoro6Qml) >= 0.4
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       %{_bindir}/cwebp
Requires:       %{_bindir}/jpegoptim
Requires:       %{_bindir}/oxipng
Requires:       %{_bindir}/scour
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 1.5.0
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
Optimize your images with OptiImage, a useful image compressor that supports
PNG, JPEG, WebP and SVG file types.

It supports both lossless and lossy compression modes with an option whether to
keep or not metadata of images. It additionally has a safe mode, where a new
image is created instead of overwriting the old one.

It uses the following tools:

    oxipng for PNG images
    jpegoptim for JPEG images
    scour for SVG images
    cwebp for WebP images

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.optiimage.desktop
%{_kf6_appstreamdir}/org.kde.optiimage.metainfo.xml
%{_kf6_bindir}/optiimage
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.optiimage.svg

%files lang -f %{name}.lang

%changelog
