#
# spec file for package labwc-tweaks
#
# Copyright (c) 2025 Shawn W. Dunn <sfalken@opensuse.org>
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


Name:           labwc-tweaks
Version:        0~git.20241209.b4fcde7
Release:        0
Summary:        GUI Configuration app for labwc
License:        GPL-2.0-only and BSD-3-Clause
URL:            https://github.com/labwc/labwc-tweaks
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       labwc

%description
labwc-tweaks is a GUI configuration application for the labwc Wayland compositor

%lang_package

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%check
%ctest

%files
%license LICENSE BSD-3-Clause
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/labwc_tweaks.appdata.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
