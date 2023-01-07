#
# spec file for package falkon
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


%bcond_without released
Name:           falkon
Version:        22.12.1
Release:        0
Summary:        Modern web browser
License:        GPL-3.0-or-later
URL:            https://www.falkon.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# Search engine favicons.
Source3:        obs.png
Source4:        opensusesoftware.png
# No QtWebEngine for other archs
ExclusiveArch:  %{arm} aarch64 %{ix86} x86_64 %{mips} %{riscv}
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngineCore)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xcb-util)
# It fails to build for the moment
#BuildRequires:  cmake(PySide2)
#BuildRequires:  cmake(Shiboken2)
#BuildRequires:  python3-devel
# it doesn't start without it (boo#1067547)
Requires:       libQt5Sql5-sqlite
Recommends:     %{name}-kde
Provides:       web_browser
Provides:       qupzilla = %{version}
Obsoletes:      qupzilla < %{version}
Provides:       falkon-gnome-keyring = %{version}
Obsoletes:      falkon-gnome-keyring < %{version}

%description
Falkon is a web browser designed to well integrate with all
common Linux desktops like GNOME and KDE Plasma.
It supports current web standards and comes with many features,
such as an integrated ad blocker.

It was previously known as QupZilla.

%package kde
Summary:        Plugin for tighter integration of KDE technologies
Requires:       %{name} = %{version}
Requires:       kwalletd5
Supplements:    (%{name} and kwalletd5)
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

# openSUSE icons.
cp -f %{SOURCE3} %{SOURCE4} src/lib/data/icons/sites/

%if %{with released}
# The plugins are not installed if PySide is not present at build time.
find po/ -name "falkon_helloqml.po" -o -name "falkon_hellopython.po" -exec rm {} \;
%endif

# Decrease the minimum CMake version for 15.3.
# There's no technical reason for requiring CMake 3.18.
sed -i 's/VERSION 3.18/VERSION 3.17/' CMakeLists.txt

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name --with-qt

%suse_update_desktop_file org.kde.falkon
%fdupes %{buildroot}%{_kf5_sharedir}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc CHANGELOG README.md
%{_kf5_appstreamdir}/org.kde.falkon.appdata.xml
%{_kf5_bindir}/falkon
%{_kf5_libdir}/libFalkonPrivate.so.*
%{_kf5_plugindir}/falkon/
%{_kf5_sharedir}/applications/org.kde.falkon.desktop
%{_kf5_sharedir}/bash-completion/
%{_kf5_sharedir}/falkon/
%{_kf5_sharedir}/icons/hicolor/*/apps/falkon.*
%exclude %{_kf5_plugindir}/falkon/KDEFrameworksIntegration.so

%files kde
%{_kf5_plugindir}/falkon/KDEFrameworksIntegration.so

%files lang -f %{name}.lang

%changelog
