#
# spec file for package neochat
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


%define _kf5_version 5.76.0
%bcond_without  lang
Name:           neochat
Version:        1.0.1
Release:        0
Summary:        A chat client for Matrix, the decentralized communication protocol
License:        GPL-3.0-or-later AND GPL-3.0-only AND BSD-2-Clause
Group:          Productivity/Networking/Instant Messenger
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/neochat/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.1
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{_kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_version}
BuildRequires:  cmake(KQuickImageEditor) >= 0.1
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(Qt5QuickControls2) >= 5.15.0
BuildRequires:  cmake(Qt5Svg) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Quotient) >= 0.6.3
BuildRequires:  pkgconfig(libcmark)
Requires:       kirigami2
Requires:       kitemmodels-imports
Requires:       kquickimageeditor-imports
Requires:       libQt5Multimedia5
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2
%if %{with lang}
Source1:        https://download.kde.org/stable/neochat/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif

%description
Neochat is a client for Matrix, the decentralized communication protocol for instant
messaging.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%if %{with lang}
    %find_lang %{name} --all-name
%endif

%files
%license LICENSES/*
%doc README*
%{_kf5_bindir}/neochat
%{_kf5_applicationsdir}/org.kde.neochat.desktop
%dir %{_kf5_iconsdir}/hicolor/scalable/apps
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.neochat.svg
%{_kf5_appstreamdir}/org.kde.neochat.appdata.xml
%{_kf5_notifydir}/neochat.notifyrc

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
