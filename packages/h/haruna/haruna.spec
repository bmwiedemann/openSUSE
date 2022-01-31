#
# spec file for package haruna
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


Name:           haruna
Version:        0.7.3
Release:        0
Summary:        Video player built with Qt/QML on top of libmpv
License:        CC-BY-4.0 AND GPL-3.0-or-later AND WTFPL
URL:            https://invent.kde.org/multimedia/haruna
Source0:        https://invent.kde.org/multimedia/haruna/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# PATCH-FIX-UPSTREAM haruna-mpv_v2_fix.patch
Patch0:         haruna-mpv_v2_fix.patch
BuildRequires:  cmake >= 3.15
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  youtube-dl
BuildRequires:  cmake(Breeze)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
# not actually optional
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(mpv)
Requires:       breeze5-icons
Recommends:     youtube-dl

%description
%{name} is a video player built with Qt/QML on top of libmpv.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# let's remove the documentation for now
rm -rf %{buildroot}%{_datadir}/doc

%files
%license LICENSES/CC-BY-4.0.txt LICENSES/GPL-3.0-or-later.txt LICENSES/WTFPL.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.haruna.desktop
%{_datadir}/icons/hicolor/*/apps/haruna.svg
%{_datadir}/metainfo/org.kde.haruna.metainfo.xml

%changelog
