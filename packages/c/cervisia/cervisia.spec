#
# spec file for package cervisia
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           cervisia
Version:        22.12.1
Release:        0
Summary:        CVS Frontend
License:        GPL-2.0-only AND GFDL-1.2-only AND LGPL-2.0-only
URL:            https://apps.kde.org/cervisia
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  subversion-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Su)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)

%description -n cervisia
Cervisia is a tool to browse and work with CVS repositories.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
  %cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
  %cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.cervisia Development RevisionControl

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.DOC COPYING.LIB
%doc ChangeLog README
%doc %lang(en) %{_kf5_htmldir}/en/cervisia/
%{_kf5_applicationsdir}/org.kde.cervisia.desktop
%{_kf5_appstreamdir}/org.kde.cervisia.appdata.xml
%{_kf5_bindir}/cervisia
%{_kf5_bindir}/cvsaskpass
%{_kf5_bindir}/cvsservice5
%{_kf5_configkcfgdir}/cervisiapart.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.cervisia5.*.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/cervisia/
%{_kf5_kxmlguidir}/cervisiapart/
%{_kf5_libdir}/libkdeinit5_cervisia.so
%{_kf5_libdir}/libkdeinit5_cvsaskpass.so
%{_kf5_libdir}/libkdeinit5_cvsservice.so
%{_kf5_mandir}/man1/cervisia.1%{ext_man}
%{_kf5_notifydir}/cervisia.notifyrc
%{_kf5_plugindir}/cervisiapart5.so
%{_kf5_servicesdir}/org.kde.cervisiapart5.desktop
%{_kf5_servicesdir}/org.kde.cvsservice5.desktop

%files lang -f %{name}.lang

%changelog
