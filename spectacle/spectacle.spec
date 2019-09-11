#
# spec file for package spectacle
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           spectacle
Version:        19.08.0
Release:        0
Summary:        Screen Capture Program
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Use-qdbus-qt5-instead-of-qdbus.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kglobalaccel-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifications-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkipi-devel
BuildRequires:  libkscreen2-devel
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  purpose-devel
BuildRequires:  update-desktop-files
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
Obsoletes:      kscreengenie < %{version}
Provides:       kscreengenie = %{version}
# Upstream changed name twice (kscreengenie - kapture - spectacle)
Obsoletes:      kapture < %{version}
Provides:       kapture = %{version}
Recommends:     %{name}-lang

%description
Spectactle is a screenshot-taking program made by KDE. It allows taking screenshots
of screens, windows, regions of the screen, and to export them to files or other
online services.

%package doc
Summary:        Documentation for Spectacle
Group:          Productivity/Graphics/Other
Requires:       %{name}

%description doc
This package contains the documentation available for Spectacle, which is a
screenshot capture program by KDE.

%if %{with lang}
%lang_package
%endif

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.spectacle     Utility DesktopUtility

%files
%dir %{_kf5_appstreamdir}
%dir %{_kf5_libdir}/kconf_update_bin
%dir %{_kf5_sharedir}/kconf_update
%dir %{_kf5_sharedir}/kglobalaccel
%{_kf5_applicationsdir}/org.kde.spectacle.desktop
%{_kf5_appstreamdir}/org.kde.spectacle.appdata.xml
%{_kf5_bindir}/spectacle
%{_kf5_dbusinterfacesdir}/org.kde.Spectacle.xml
%{_kf5_iconsdir}/hicolor/*/*/spectacle*
%{_kf5_notifydir}/spectacle.notifyrc
%{_kf5_sharedir}/dbus-1/services/org.kde.Spectacle.service
%{_kf5_libdir}/kconf_update_bin/spectacle-migrate-shortcuts
%{_kf5_sharedir}/kconf_update/spectacle_shortcuts.upd
%{_kf5_sharedir}/kglobalaccel/org.kde.spectacle.desktop
%{_kf5_debugdir}/spectacle.categories

%files doc
%license COPYING.DOC
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/spectacle/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
