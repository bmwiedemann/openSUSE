#
# spec file for package kde-fcstd-thumbnailer
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


Name:           kde-fcstd-thumbnailer
Version:        0+git.adc0f19
Release:        0
Summary:        FreeCAD thumbnailer plugin for KDE Plasma / Dolphin
License:        LGPL-3.0-only
URL:            https://github.com/mtorromeo/kde-fcstd-thumbnailer
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)

%description
KDE thumbnail-plugin that generates small images (thumbnails) for FcStd (FreeCAD) files, to be displayed, for example, on Konqueror and Dolphin file managers.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%files
%{_kf5_plugindir}/
%{_kf5_servicesdir}/

%changelog
