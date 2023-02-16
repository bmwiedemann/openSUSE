#
# spec file for package neochat
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


%define _kf5_version 5.88.0
%bcond_without  released
Name:           neochat
Version:        23.01.0
Release:        0
Summary:        A chat client for Matrix, the decentralized communication protocol
License:        GPL-3.0-or-later AND GPL-3.0-only AND BSD-2-Clause
Group:          Productivity/Networking/Instant Messenger
URL:            https://apps.kde.org/neochat/
Source0:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  cmark
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(QCoro5Coro)
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{_kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_version}
BuildRequires:  cmake(KF5ItemModels) >= %{_kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{_kf5_version}
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_version}
BuildRequires:  cmake(KF5QQC2DesktopStyle) >= %{_kf5_version}
BuildRequires:  cmake(KF5Sonnet) >= %{_kf5_version}
BuildRequires:  cmake(KQuickImageEditor) >= 0.1
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5Gui) >= 5.15.2
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia) >= 5.15.2
BuildRequires:  cmake(Qt5Quick) >= 5.15.2
BuildRequires:  cmake(Qt5QuickControls2) >= 5.15.2
BuildRequires:  cmake(Qt5Svg) >= 5.15.2
BuildRequires:  cmake(Qt5Widgets) >= 5.15.2
BuildRequires:  cmake(Quotient) >= 0.6.3
BuildRequires:  pkgconfig(libcmark)
Requires:       kirigami2
Requires:       kirigami-addons
Requires:       kitemmodels-imports
Requires:       kquickimageeditor-imports
Requires:       syntax-highlighting-imports

%description
Neochat is a client for Matrix, the decentralized communication protocol for instant
messaging.

%lang_package

%prep
%autosetup -p1

%build
# c++-20 is required
%if 0%{?suse_version} == 1500
    export CC=gcc-10 CXX=g++-10
%endif

%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README*
%doc %lang(en) %{_kf5_mandir}/man1/neochat.1%{?ext_man}
%doc %lang(ca) %{_kf5_mandir}/ca/man1/neochat.1%{?ext_man}
%doc %lang(es) %{_kf5_mandir}/es/man1/neochat.1%{?ext_man}
%doc %lang(it) %{_kf5_mandir}/it/man1/neochat.1%{?ext_man}
%doc %lang(nl) %{_kf5_mandir}/nl/man1/neochat.1%{?ext_man}
%doc %lang(uk) %{_kf5_mandir}/uk/man1/neochat.1%{?ext_man}
%dir %{_kf5_sharedir}/krunner/
%dir %{_kf5_sharedir}/krunner/dbusplugins/
%{_kf5_applicationsdir}/org.kde.neochat.desktop
%{_kf5_appstreamdir}/org.kde.neochat.appdata.xml
%{_kf5_bindir}/neochat
%{_kf5_iconsdir}/hicolor/*/apps/org.kde.neochat.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.neochat.tray.svg
%{_kf5_notifydir}/neochat.notifyrc
%{_kf5_sharedir}/krunner/dbusplugins/plasma-runner-neochat.desktop

%files lang -f %{name}.lang

%changelog
