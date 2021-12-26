#
# spec file for package crow-translate
#
# Copyright (c) 2021 SUSE LLC
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


%define _qonlinetranslator_version 1.5.2
%define _qhotkey_version           1.4.2
%define _qtaskbarcontrol_version   2.0.2
%define _singleapplication_version 3.2.0
%define _circle_flags_version      2.3.0
%define _fluent_icon_theme_version 2021-08-15
%define  _name  io.crow_translate.CrowTranslate
Name:           crow-translate
Version:        2.9.1
Release:        0
Summary:        A Qt GUI for Google, Yandex and Bing translators
License:        GPL-3.0-only
Group:          Productivity/Networking/Web/Frontends
URL:            https://crow-translate.github.io/
Source0:        https://codeload.github.com/%{name}/%{name}/tar.gz/refs/tags/%{version}#/%{name}-%{version}.tar.gz
# SECTION 3rd-party sources
# QOnlineTranslator is licensed under GPL-3.0
Source1:        https://codeload.github.com/%{name}/QOnlineTranslator/tar.gz/refs/tags/%{_qonlinetranslator_version}#/QOnlineTranslator-%{_qonlinetranslator_version}.tar.gz
# QHotkey is licensed under BSD-3-Clause
Source2:        https://codeload.github.com/Skycoder42/QHotkey/tar.gz/refs/tags/%{_qhotkey_version}#/QHotkey-%{_qhotkey_version}.tar.gz
# QTaskbarControl is licensed under BSD-3-Clause
Source3:        https://codeload.github.com/Skycoder42/QTaskbarControl/tar.gz/refs/tags/%{_qtaskbarcontrol_version}#/QTaskbarControl-%{_qtaskbarcontrol_version}.tar.gz
# SingleApplication is licensed under MIT
Source4:        https://codeload.github.com/itay-grudev/SingleApplication/tar.gz/refs/tags/v%{_singleapplication_version}#/SingleApplication-%{_singleapplication_version}.tar.gz
# circle-flags is licensed under MIT
Source5:        https://codeload.github.com/HatScripts/circle-flags/tar.gz/refs/tags/v%{_circle_flags_version}#/circle-flags-%{_circle_flags_version}.tar.gz
# Fluent-icon-theme is licensed under GPL-3.0
Source6:        https://codeload.github.com/vinceliuice/Fluent-icon-theme/tar.gz/refs/tags/%{_fluent_icon_theme_version}#/Fluent-icon-theme-%{_fluent_icon_theme_version}.tar.gz
Patch0:         Fix-install-path.patch
Patch1:         fetchcontent.patch
BuildRequires:  cmake >= 3.16.0
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(tesseract) >= 4.0
BuildRequires:  pkgconfig(xcb)
Requires:       gstreamer-plugins-good
# SECTION 3rd-party BuildRequires
BuildRequires:  pkgconfig(Qt5Core)
#uildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
#uildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
# /SECTION
Provides:       bundled(qonlinetranslator) = %{_qonlinetranslator_version}
Provides:       bundled(qhotkey) = %{_qhotkey_version}
Provides:       bundled(qtaskbarcontrol) = %{_qtaskbarcontrol_version}
Provides:       bundled(singleapplication) = %{_singleapplication_version}

%description
A simple and lightweight translator that allows to translate and speak
text using Google, Yandex and Bing written with Qt5.

%lang_package

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a6
%patch0 -p1
sed -i '/GIT_TAG/d' cmake/ExternalLibraries.cmake
%patch1 -p1
mkdir -p src/qonlinetranslator/ src/third-party/qhotkey/ src/third-party/qtaskbarcontrol/ \
src/third-party/singleapplication/ src/circle-flags src/Fluent-icon-theme
mv QOnlineTranslator-%{_qonlinetranslator_version}/* src/qonlinetranslator/
mv QHotkey-%{_qhotkey_version}/* src/third-party/qhotkey/
mv QTaskbarControl-%{_qtaskbarcontrol_version}/* src/third-party/qtaskbarcontrol/
mv SingleApplication-%{_singleapplication_version}/* src/third-party/singleapplication/
mv circle-flags-%{_circle_flags_version}/* src/circle-flags/
mv Fluent-icon-theme-%{_fluent_icon_theme_version}/* src/Fluent-icon-theme/

%build
%cmake \
    -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r %{_name} Office Dictionary
# remove icons with unusual sizes
rm -rf %{buildroot}%{_datadir}/icons/hicolor/{310x310,150x150,44x44}

%find_lang %{name} --with-qt

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/icons/hicolor/*/status/%{name}-tray-*.??g

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{name}
%dir %{_datadir}/%{name}/%{name}/translations

%changelog
