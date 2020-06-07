#
# spec file for package falkon
#
# Copyright (c) 2020 SUSE LLC
# Copyright © 2015 Mariusz Fik <fisiu@opensuse.org>
# Copyright © 2019 Markus S. <kamikazow@opensuse.org>
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


Name:           falkon
Version:        3.1.0
Release:        0
Summary:        Modern web browser
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://www.falkon.org/
Source:         %{name}-%{version}.tar.xz
# Used to get a timestamp to override __DATE__ and __TIME__ with
Source1:        %{name}.changes
# Search engine favicons.
Source2:        obs.png
Source3:        opensusesoftware.png
# PATCH-FIX-UPSTREAM
Patch0:         Add-missing-include-in-last-qt5.14.patch
# PATCH-FIX-UPSTREAM
Patch1:         Fix-crash-when-KWallet-is-not-available.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-Qt-5.15.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  ki18n-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libressl-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CoreAddons) >= 5.54.0
BuildRequires:  cmake(KF5Crash) >= 5.54.0
BuildRequires:  cmake(KF5KIO) >= 5.54.0
BuildRequires:  cmake(KF5Purpose) >= 5.54.0
BuildRequires:  cmake(KF5Wallet) >= 5.54.0
BuildRequires:  cmake(Qt5Concurrent) >= 5.9.0
BuildRequires:  cmake(Qt5Core) >= 5.9.0
BuildRequires:  cmake(Qt5DBus) >= 5.9.0
BuildRequires:  cmake(Qt5Gui) >= 5.9.0
BuildRequires:  cmake(Qt5Network) >= 5.9.0
BuildRequires:  cmake(Qt5Positioning) >= 5.9.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.9.0
BuildRequires:  cmake(Qt5Qml) >= 5.9.0
BuildRequires:  cmake(Qt5Quick) >= 5.9.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.9.0
BuildRequires:  cmake(Qt5Script) >= 5.9.0
BuildRequires:  cmake(Qt5Sql) >= 5.9.0
BuildRequires:  cmake(Qt5Test) >= 5.9.0
BuildRequires:  cmake(Qt5WebChannel) >= 5.9.0
BuildRequires:  cmake(Qt5WebEngineCore) >= 5.9.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.9.0
BuildRequires:  cmake(Qt5Widgets) >= 5.9.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.9.0
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(xcb-atom)
Recommends:     %{name}-kde
Recommends:     %{name}-lang
# it doesn't start without it (boo#1067547)
Requires:       libQt5Sql5-sqlite
Provides:       qupzilla = %{version}
Provides:       web_browser
Obsoletes:      qupzilla < %{version}

%lang_package

%description
Falkon is a web browser designed to well integrate with all
common Linux desktops like GNOME and KDE Plasma.
It supports current web standards and comes with many features,
such as an integrated ad blocker.

It was previously known as QupZilla.

%package gnome-keyring
Summary:        GNOME Keyring plugin for Falkon
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:gnome-keyring)
Provides:       qupzilla-gnome-keyring = %{version}
Obsoletes:      qupzilla-gnome-keyring < %{version}

%description gnome-keyring
Plugin for the Falkon browser that allows storing passwords in
GNOME Keyring.

%package kde
Summary:        Plugin for tighter integration of KDE technologies
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Requires:       kwalletd5
Supplements:    packageand(%{name}:kwalletd5)
Provides:       falkon-kwallet = %{version}
Obsoletes:      falkon-kwallet < %{version}
Provides:       qupzilla-kwallet = %{version}
Obsoletes:      qupzilla-kwallet < %{version}

%description kde
Plugin for the Falkon browser that allows tighter integration of KDE technologies,
such as storing passwords in KWallet.

%prep
%autosetup -p1 -n %{name}-%{version}

# Remove __DATE__ and __TIME__
FAKE_DATE="\"$(LC_ALL=C date -u -r %{SOURCE1} '+%%b %%e %%Y')\""
FAKE_TIME="\"$(LC_ALL=C date -u -r %{SOURCE1} '+%%H:%%M')\""
find .  -type f -regex '.*\.\(h\|c\|cpp\)' | xargs sed -i "s/__DATE__/${FAKE_DATE}/g;s/__TIME__/${FAKE_TIME}/g"

# openSUSE icons.
cp -f %{SOURCE2} %{SOURCE3} src/lib/data/icons/sites/

%build
  export USE_WEBGL=true
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall DESTDIR=%{buildroot} -C build
# FIXME: Split library into a separate package and also create falkon-devel with libfalkon.so ???
rm -vf %{buildroot}%{_libdir}/libFalkonPrivate.so
# We don't need two test plugins that do nothing.
rm -vf %{buildroot}%{_libdir}/%{name}/libTestPlugin.so
rm -vrf %{buildroot}%{_kf5_plugindir}/falkon/qml/helloqml/

%suse_update_desktop_file org.kde.falkon
%fdupes %{buildroot}%{_kf5_sharedir}/

%find_lang %{name} --all-name --with-qt

%post
%desktop_database_post
%icon_theme_cache_post
/sbin/ldconfig

%postun
%desktop_database_postun
%icon_theme_cache_postun
/sbin/ldconfig

%files
%doc CHANGELOG COPYING README.md
%exclude %{_kf5_plugindir}/falkon/GnomeKeyringPasswords.so
%exclude %{_kf5_plugindir}/falkon/KDEFrameworksIntegration.so
%{_kf5_appstreamdir}/org.kde.falkon.appdata.xml
%{_kf5_bindir}/falkon
%{_kf5_libdir}/libFalkonPrivate.so.*
%{_kf5_plugindir}/falkon/
%{_kf5_sharedir}/applications/org.kde.falkon.desktop
%{_kf5_sharedir}/bash-completion/
%{_kf5_sharedir}/falkon/
%{_kf5_sharedir}/icons/hicolor/*/apps/falkon.*
%{_kf5_sharedir}/pixmaps/falkon.png

%files gnome-keyring
%{_kf5_plugindir}/falkon/GnomeKeyringPasswords.so

%files kde
%{_kf5_plugindir}/falkon/KDEFrameworksIntegration.so

%files lang -f %{name}.lang

%changelog
