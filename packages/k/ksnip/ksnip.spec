#
# spec file for package ksnip
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


Name:           ksnip
Version:        1.10.1
Release:        0
Summary:        Screenshot tool
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/ksnip/ksnip
Source:         https://github.com/ksnip/ksnip/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-build-against-kImageAnnotator-and-kColorPicker-t.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xvfb-run
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(kColorPicker-Qt5) >= 0.3.1
BuildRequires:  cmake(kImageAnnotator-Qt5) >= 0.7.1
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-xfixes)

%description
Ksnip is a Qt based cross-platform screenshot tool that provides many
annotation features for your screenshots.

%lang_package

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r org.ksnip.ksnip Utility DesktopUtility

%find_lang %{name} --with-qt

%files
%license LICENSE.txt
%doc CHANGELOG.md CODINGSTYLE.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.ksnip.ksnip.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/org.ksnip.ksnip.appdata.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
