#
# spec file for package haruna
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


Name:           haruna
Version:        1.1.2
Release:        0
Summary:        Video player built with Qt/QML on top of libmpv
License:        CC-BY-4.0 AND GPL-3.0-or-later AND WTFPL
URL:            https://apps.kde.org/haruna
Source0:        https://download.kde.org/stable/haruna/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/haruna/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        haruna.keyring
BuildRequires:  cmake >= 3.15
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-extra-cmake-modules >= 6.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(Breeze)
BuildRequires:  cmake(KF6ColorScheme) >= 6.0.0
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(MpvQt)
BuildRequires:  cmake(Qt6Core) >= 6.6.0
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil) >= 58.29.100
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(mpv)
Requires:       kf6-breeze-icons
Requires:       yt-dlp

%description
%{name} is a video player built with Qt/QML on top of libmpv.

%lang_package

%prep
%autosetup -p1

%build
export CXX=g++
test -x "$(type -p g++-13)" && export CXX=g++-13
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

# let's remove the documentation for now
rm -r %{buildroot}%{_datadir}/doc

# remove oddly-sized icons
rm -r %{buildroot}%{_datadir}/icons/hicolor/44x44 \
       %{buildroot}%{_datadir}/icons/hicolor/150x150 \
       %{buildroot}%{_datadir}/icons/hicolor/310x310

%files
%license LICENSES/CC-BY-4.0.txt LICENSES/GPL-3.0-or-later.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.haruna.desktop
%{_datadir}/icons/hicolor/*/apps/haruna.*g
%{_datadir}/metainfo/org.kde.haruna.metainfo.xml

%files lang -f %{name}.lang

%changelog
