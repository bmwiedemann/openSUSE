#
# spec file for package ksysguard5
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


%bcond_without lang
Name:           ksysguard5
Version:        5.22.0
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE System Guard daemon
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         ksysguard-%{version}.tar.xz
%if %{with lang}
Source1:        ksysguard-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        ksysguardd.service
# PATCH-FIX-OPENSUSE 0001-Use-run-for-ksysguardd-s-pid-file.patch
Patch0:         0001-Use-run-for-ksysguardd-s-pid-file.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-lmsensors-Fix-buffer-size-passed-to-snprintf.patch
BuildRequires:  extra-cmake-modules >= 5.81.0
BuildRequires:  kf5-filesystem
%ifnarch s390 s390x
BuildRequires:  libsensors4-devel
%endif
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5SysGuard) >= %{_plasma5_version}
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5Widgets)
# kde#421514
BuildRequires:  cmake(Qt5Test)
Recommends:     %{name}-lang
Requires:       libksysguard5-plugins
BuildRequires:  update-desktop-files
Provides:       kdebase4-workspace-ksysguardd = %{version}
Obsoletes:      kdebase4-workspace-ksysguardd < %{version}
%{systemd_ordering}

%description
This package contains the ksysguard daemon and application.

This package can be installed on servers without any other KDE packages
to enable monitoring them remotely with ksysguard.

%lang_package

%prep
%autosetup -p1 -n ksysguard-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif
  %suse_update_desktop_file    org.kde.ksysguard      System Monitor

  install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/ksysguardd.service

%pre
%service_add_pre ksysguardd.service

%preun
%service_del_preun ksysguardd.service

%post
%service_add_post ksysguardd.service

%postun
%service_del_postun ksysguardd.service

%files
%license COPYING*
%{_kf5_bindir}/ksysguard
%{_kf5_bindir}/ksysguardd
%config %{_kf5_sysconfdir}/ksysguarddrc
%{_kf5_knsrcfilesdir}/ksysguard.knsrc
%{_kf5_applicationsdir}/org.kde.ksysguard.desktop
%{_kf5_notifydir}/
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%{_kf5_htmldir}/en/ksysguard/
%{_kf5_iconsdir}/hicolor/*/*/
%{_kf5_sharedir}/ksysguard/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_appstreamdir}/org.kde.ksysguard.appdata.xml
%{_unitdir}/ksysguardd.service

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
