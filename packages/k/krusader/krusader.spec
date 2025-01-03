#
# spec file for package krusader
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
%define qt6_version 6.4.0

%bcond_without released
Name:           krusader
Version:        2.9.0
Release:        0
Summary:        Twin panel file manager for KDE Plasma and other desktops
License:        GPL-2.0-or-later
URL:            https://krusader.org/
Source0:        https://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/raw/master/keys/abikadorov@key1.asc
Source2:        krusader.keyring
%endif
Source3:        org.kde.krusader.root-mode.desktop
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       kio_iso = %{version}

%description
Krusader is an advanced twin panel (commander style) file manager for KDE Plasma
and other desktops in the *nix world.

%package -n kio_iso
Summary:        KIO slave to access ISO images
Provides:       kde4-kio_iso = 1.80.99
Obsoletes:      kde4-kio_iso < 1.80.99

%description -n kio_iso
KIO slave to access ISO images like zip- or tar.gz-archives in your
file-browser.

%package doc
Summary:        Krusader documentation

%description doc
Krusader is an advanced twin panel (commander style) file manager for KDE Plasma
and other desktops in the *nix world.

This package contains the krusader documentation.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name}

cp %{SOURCE3} %{buildroot}%{_kf6_applicationsdir}/

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README AUTHORS ChangeLog
%doc %lang(en) %{_kf6_mandir}/man1/krusader.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.krusader.desktop
%{_kf6_applicationsdir}/org.kde.krusader.root-mode.desktop
%{_kf6_appstreamdir}/org.kde.krusader.appdata.xml
%{_kf6_bindir}/krusader
%{_kf6_iconsdir}/hicolor/*/apps/krusader*.png
%{_kf6_kxmlguidir}/krusader/
%{_kf6_plugindir}/kf6/kio/kio_krarc.so
%{_kf6_sharedir}/krusader/
%exclude %{_kf6_htmldir}/*/krusader

%files -n kio_iso
%license LICENSES/*
%config %{_kf6_configdir}/kio_isorc
%{_kf6_plugindir}/kf6/kio/kio_iso.so

%files doc
%doc %lang(en) %{_kf6_htmldir}/en/krusader

%files lang -f %{name}.lang
%{_kf6_mandir}/*/man1/krusader.1%{?ext_man}

%changelog
