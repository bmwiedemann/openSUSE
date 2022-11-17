#
# spec file for package crow-translate
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%define  _name  io.crow_translate.CrowTranslate
Name:           crow-translate
Version:        2.10.0
Release:        0
Summary:        A Qt GUI for Google, Yandex and Bing translators
License:        GPL-3.0-only
Group:          Productivity/Networking/Web/Frontends
URL:            https://crow-translate.github.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}-source.tar.gz
Patch0:         third-party-library-static.patch
Patch1:         cmakelists-txt.patch
Patch2:         desktop-file.patch
BuildRequires:  cmake >= 3.16.0
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(tesseract) >= 4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Requires:       gstreamer-plugins-good

%description
A simple and lightweight translator that allows to translate and speak
text using Google, Yandex and Bing written with Qt5.

%lang_package

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r %{_name} Office Dictionary

%find_lang %{name} --with-qt

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/icons/hicolor/*/status/%{name}-tray-*.??g
%{_datadir}/metainfo/%{_name}.metainfo.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{name}
%dir %{_datadir}/%{name}/%{name}/translations

%changelog
