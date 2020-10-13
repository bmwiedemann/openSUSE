#
# spec file for package kdf
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdf
Version:        20.08.2
Release:        0
Summary:        Disk Usage Viewer
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch1:         desktop-files.diff
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
KDE free disk space utility

%lang_package

%prep
%setup -q -n kdf-%{version}
%patch1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file org.kde.kdf System Filesystem

%package -n kwikdisk
Summary:        Removable Media Utility
Group:          System/GUI/KDE

%description -n kwikdisk
This utility allows you to manage removable media.

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_htmldir}/en/kcontrol/
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/blockdevices/
%doc %lang(en) %{_kf5_htmldir}/en/kdf/
%{_kf5_applicationsdir}/org.kde.kdf.desktop
%{_kf5_bindir}/kdf
%{_kf5_iconsdir}/hicolor/*/*/kcmdf.png
%{_kf5_iconsdir}/hicolor/*/*/kdf.png
%{_kf5_libdir}/libkdfprivate.so.*
%{_kf5_plugindir}/libkcm_kdf.so
%{_kf5_servicesdir}/kcmdf.desktop
%{_kf5_kxmlguidir}/kdf/
%{_kf5_appstreamdir}/org.kde.kdf.appdata.xml
%{_kf5_debugdir}/kdf.categories

%files -n kwikdisk
%license COPYING*
%{_kf5_applicationsdir}/org.kde.kwikdisk.desktop
%{_kf5_bindir}/kwikdisk
%{_kf5_iconsdir}/hicolor/*/*/kwikdisk.png

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
