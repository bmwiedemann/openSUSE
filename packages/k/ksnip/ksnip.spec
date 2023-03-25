#
# spec file for package ksnip
#
# Copyright (c) 2023 SUSE LLC
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
URL:            https://github.com/DamirPorobic/ksnip
Source:         https://github.com/DamirPorobic/ksnip/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  kColorPicker-devel
BuildRequires:  kImageAnnotator-devel >= 0.6.1
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xvfb-run
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
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
