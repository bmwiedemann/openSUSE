#
# spec file for package falkon
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           falkon
Version:        24.05.2
Release:        0
Summary:        Modern web browser
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/falkon
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-network-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebChannel) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineCore) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xcb-util)
# 2024-02-11 still fails to build with python deps
# BuildRequires:  cmake(PySide6)
# BuildRequires:  cmake(Shiboken6)
# BuildRequires:  python3-devel
Requires:       qt6-sql-sqlite >= %{qt6_version}
Recommends:     falkon-kde
Provides:       qupzilla = %{version}
Obsoletes:      qupzilla < %{version}
Provides:       web_browser
Provides:       falkon-gnome-keyring = %{version}
Obsoletes:      falkon-gnome-keyring < %{version}
# No QtWebEngine for other archs
ExclusiveArch:  aarch64 x86_64 %{x86_64} riscv64

%description
Falkon is a web browser designed to well integrate with all
common Linux desktops like GNOME and KDE Plasma.
It supports current web standards and comes with many features,
such as an integrated ad blocker.

It was previously known as QupZilla.

%package kde
Summary:        Plugin for tighter integration of KDE technologies
Requires:       falkon = %{version}
Supplements:    (%{name} and plasma5-workspace)
Supplements:    (%{name} and plasma6-workspace)
Provides:       falkon-kwallet = %{version}
Obsoletes:      falkon-kwallet < %{version}
Provides:       qupzilla-kwallet = %{version}
Obsoletes:      qupzilla-kwallet < %{version}

%description kde
Plugin for the Falkon browser that allows tighter integration of KDE technologies,
such as storing passwords in KWallet.

%lang_package

%prep
%autosetup -p1

%if %{with released}
# The plugins are not installed if PySide is not present at build time.
find po/ -name "falkon_helloqml.po" -o -name "falkon_hellopython.po" -exec rm {} \;
%endif

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-qt

%fdupes %{buildroot}%{_kf6_sharedir}

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_kf6_appstreamdir}/org.kde.falkon.appdata.xml
%{_kf6_bindir}/falkon
%{_kf6_iconsdir}/hicolor/*/apps/falkon.*
%{_kf6_libdir}/libFalkonPrivate.so.*
%{_kf6_plugindir}/falkon/
%{_kf6_sharedir}/applications/org.kde.falkon.desktop
%{_kf6_sharedir}/bash-completion/
%{_kf6_sharedir}/falkon/
%exclude %{_kf6_plugindir}/falkon/KDEFrameworksIntegration.so

%files kde
%{_kf6_plugindir}/falkon/KDEFrameworksIntegration.so

%files lang -f %{name}.lang

%changelog
