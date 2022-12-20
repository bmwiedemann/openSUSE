#
# spec file for package krusader
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


Name:           krusader
Version:        2.8.0
Release:        0
Summary:        Twin panel file manager for KDE Plasma and other desktops
License:        GPL-2.0-or-later
URL:            https://krusader.org/
Source:         https://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz
Source1:        krusader_browse_iso.desktop
Source2:        org.kde.krusader.root-mode.desktop
BuildRequires:  extra-cmake-modules >= 5.68.0
BuildRequires:  fdupes
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent) >= 5.12.0
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Gui) >= 5.12.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0
Requires:       kio_iso = %{version}
Suggests:       %{name}-doc

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
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

mkdir -p %{buildroot}%{_kf5_servicesdir}/ServiceMenus/
cp %{SOURCE1} %{buildroot}%{_kf5_servicesdir}/ServiceMenus/
cp %{SOURCE2} %{buildroot}%{_kf5_applicationsdir}/

%suse_update_desktop_file org.kde.krusader.root-mode FileManager Utility

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README AUTHORS ChangeLog
%exclude %{_kf5_htmldir}/*/krusader
%{_kf5_applicationsdir}/org.kde.krusader*.desktop
%{_kf5_appsdir}/krusader
%{_kf5_appstreamdir}/org.kde.krusader.appdata.xml
%{_kf5_bindir}/krusader
%{_kf5_iconsdir}/??color/*/apps/krusader*.png
%{_kf5_kxmlguidir}/
%doc %lang(en) %{_kf5_mandir}/man1/krusader.1%{?ext_man}
%{_kf5_plugindir}/kf5/kio/kio_krarc.so

%files -n kio_iso
%license LICENSES/*
%config %{_kf5_configdir}/kio_isorc
%dir %{_kf5_servicesdir}/ServiceMenus
%{_kf5_plugindir}/kf5/kio/kio_iso.so*
%{_kf5_servicesdir}/ServiceMenus/krusader_browse_iso.desktop

%files doc
%doc %lang(en) %{_kf5_htmldir}/en/krusader

%files lang -f %{name}.lang
%{_kf5_mandir}/*/man1/krusader.1%{?ext_man}

%changelog
