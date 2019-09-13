#
# spec file for package kjots
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kjots
Version:        5.0.2
Release:        0
Summary:        A note taking application for KDE using Akonadi
License:        GPL-2.0 and LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source0:        http://download.kde.org/stable/kjots/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  akonadi-server-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  grantlee5-devel
BuildRequires:  libxslt-tools
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5PrintSupport)
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains KJOTS, a note taking application for KDE using Akonadi.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build

%make_jobs

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -C "Note Taker" org.kde.kjots    Utility  DesktopUtility
%find_lang %{name}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ANNOUNCE CHANGES COPYING COPYING.LIB README
%_kf5_appstreamdir/
%_kf5_applicationsdir/org.kde.kjots.desktop
%_kf5_bindir/kjots
%_kf5_configkcfgdir/kjots.kcfg
%_kf5_kxmlguidir/kjots/
%_kf5_servicesdir/kjotspart.desktop
%_kf5_plugindir/kjotspart.so
%_kf5_plugindir/kcm_kjots.so
%_kf5_servicesdir/kjots_config_misc.desktop
%_kf5_sharedir/kjots/
%_kf5_iconsdir/hicolor/*/apps/kjots.*
%_kf5_iconsdir/oxygen/*/actions/edit-delete-page.*
%{_kf5_plugindir}/kontact_kjotsplugin.so
%{_datadir}/kontact/
%{_kf5_servicesdir}/kontact/

%files lang -f kjots.lang
%defattr(-,root,root)

%changelog
