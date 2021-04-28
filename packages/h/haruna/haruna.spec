#
# spec file for package haruna
#
# Copyright (c) 2021 SUSE LLC
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


Name:           haruna
Version:        0.6.3
Release:        0
Summary:        Video player built with Qt/QML on top of libmpv
License:        CC-BY-4.0 AND GPL-3.0-or-later AND WTFPL
URL:            https://github.com/g-fb/haruna
Source0:        https://github.com/g-fb/haruna/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  breeze5-icons
BuildRequires:  cmake >= 3.15
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  pkgconfig(mpv)
# recheck this one
Requires:       breeze5-icons

%description
%{name} is a video player built with Qt/QML on top of libmpv.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSES/CC-BY-4.0.txt LICENSES/GPL-3.0-or-later.txt LICENSES/WTFPL.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.georgefb.haruna.desktop
%{_datadir}/icons/hicolor/*/apps/com.georgefb.haruna.svg
%{_datadir}/metainfo/com.georgefb.haruna.appdata.xml

%changelog
