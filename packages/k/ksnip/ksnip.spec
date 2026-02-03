#
# spec file for package ksnip
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


%define rev ac15aa97ead20ff25ccadfce8981cf8601c2dc4e

Name:           ksnip
Version:        1.10.1
Release:        0
Summary:        Screenshot tool
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/ksnip/ksnip
Source:         https://github.com/ksnip/ksnip/archive/%{rev}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  xvfb-run
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(kColorPicker-Qt6) >= 0.3.1
BuildRequires:  cmake(kImageAnnotator-Qt6) >= 0.7.1
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-xfixes)

%description
Ksnip is a Qt based cross-platform screenshot tool that provides many
annotation features for your screenshots.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{rev}

# Qt 6.10.1 fix
sed -E -e '/QT_COMPONENTS/s&(Widgets)&\1 GuiPrivate&' -i CMakeLists.txt

%build

%cmake -DBUILD_WITH_QT6=ON
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
