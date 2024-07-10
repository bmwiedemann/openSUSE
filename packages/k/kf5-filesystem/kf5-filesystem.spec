#
# spec file for package kf5-filesystem
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


Name:           kf5-filesystem
URL:            https://www.kde.org
Version:        20220307
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        KF5 Directory Layout
License:        LGPL-2.1-or-later
Group:          System/Fhs
Source0:        macros.kf5
Source1:        COPYING
# https://github.com/openSUSE/rpm-config-SUSE/blob/54f9f71bacdfb944d88f722d71a4d35651f7cc8a/fileattrs/locale.attr
# edited for /usr/share/locale/kf5/
Source2:        localekf5.attr
Source3:        https://raw.githubusercontent.com/openSUSE/rpm-config-SUSE/54f9f71bacdfb944d88f722d71a4d35651f7cc8a/scripts/locale.prov#/localekf5.prov
Requires:       hicolor-icon-theme

%description
This package provides macros which are utilized with extra-cmake-modules' KDEInstallDirs.

%define _kf5_prefix     %{_prefix}
%define _kf5_bindir     %{_kf5_prefix}/bin
%define _kf5_sharedir   %{_datadir}
%define _kf5_datadir    %{_kf5_sharedir}/kf5
%define _kf5_includedir %{_includedir}/KF5
%define _kf5_libdir     %{_kf5_prefix}/%{_lib}
%define _kf5_libexecdir %{_libexecdir}/kf5
%define _kf5_mandir     %{_mandir}
%define _kf5_sbindir    %{_sbindir}
%define _kf5_notifydir  %{_kf5_sharedir}/knotifications5
%define _kf5_sysconfdir %{_sysconfdir}
%define _kf5_plugindir  %{_kf5_libdir}/qt5/plugins
%define _kf5_plasmadir  %{_kf5_sharedir}/plasma
%define _kf5_importdir  %{_kf5_libdir}/qt5/imports
%define _kf5_qmldir     %{_kf5_libdir}/qt5/qml
%define _kf5_cmakedir   %{_kf5_libdir}/cmake
%define _kf5_mkspecsdir %{_kf5_libdir}/qt5/mkspecs/modules
%define _kf5_appstreamdir    %{_kf5_sharedir}/metainfo
%define _kf5_dbusinterfacesdir %{_kf5_sharedir}/dbus-1/interfaces
%define _kf5_dbuspolicydir   %{_kf5_sharedir}/dbus-1/system.d
%define _kf5_configdir       %{_kf5_sysconfdir}/xdg
%define _kf5_iconsdir        %{_kf5_sharedir}/icons
%define _kf5_wallpapersdir   %{_kf5_sharedir}/wallpapers
%define _kf5_appsdir         %{_kf5_sharedir}
%define _kf5_configkcfgdir   %{_kf5_sharedir}/config.kcfg
%define _kf5_servicesdir     %{_kf5_sharedir}/kservices5
%define _kf5_servicetypesdir %{_kf5_sharedir}/kservicetypes5
%define _kf5_htmldir         %{_kf5_sharedir}/doc/HTML
%define _kf5_kxmlguidir      %{_kf5_sharedir}/kxmlgui5
%define _kf5_knsrcfilesdir   %{_kf5_sharedir}/knsrcfiles
%define _kf5_debugdir        %{_kf5_sharedir}/qlogging-categories5

%prep
%autosetup -T -c
cp %{SOURCE1} .

%build

%install
install -D -m644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
%if 0%{?suse_version} >= 1550
# On TW, foo-lang packages use automatic locale(foo:en) provides, but that
# does not match locale/kf5
install -D -m644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/fileattrs/localekf5.attr
install -D -m755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/fileattrs/localekf5.prov
%endif

mkdir -p %{buildroot}%{_kf5_datadir}
mkdir -p %{buildroot}%{_kf5_importdir}
mkdir -p %{buildroot}%{_kf5_includedir}
mkdir -p %{buildroot}%{_kf5_libexecdir}
mkdir -p %{buildroot}%{_kf5_notifydir}
mkdir -p %{buildroot}%{_kf5_plasmadir}
mkdir -p %{buildroot}%{_kf5_plugindir}
mkdir -p %{buildroot}%{_kf5_plugindir}/kf5
mkdir -p %{buildroot}%{_kf5_qmldir}
mkdir -p %{buildroot}%{_kf5_cmakedir}
mkdir -p %{buildroot}%{_kf5_mkspecsdir}
mkdir -p %{buildroot}%{_kf5_dbusinterfacesdir}
mkdir -p %{buildroot}%{_kf5_dbuspolicydir}
mkdir -p %{buildroot}%{_kf5_configdir}
mkdir -p %{buildroot}%{_kf5_wallpapersdir}
mkdir -p %{buildroot}%{_kf5_configkcfgdir}
mkdir -p %{buildroot}%{_kf5_servicesdir}
mkdir -p %{buildroot}%{_kf5_servicetypesdir}
mkdir -p %{buildroot}%{_kf5_htmldir}
mkdir -p %{buildroot}%{_kf5_kxmlguidir}
mkdir -p %{buildroot}%{_kf5_appstreamdir}
mkdir -p %{buildroot}%{_kf5_knsrcfilesdir}
mkdir -p %{buildroot}%{_kf5_debugdir}

for size in scalable 128x128 64x64 48x48 32x32 22x22 16x16; do
  for type in actions apps devices filesystems mimetypes places status; do
    mkdir -p %{buildroot}%{_kf5_sharedir}/icons/oxygen/$size/$type
  done
done
mkdir -p %{buildroot}%{_kf5_sharedir}/icons/oxygen/scalable/apps/small/{16x16,32x32}
mkdir -p %{buildroot}%{_kf5_sharedir}/icons/oxygen/scalable/status/small/{16x16,22x22,48x48}

# Own the htmldocs directories for all supported languages
pushd /usr/share/locale
for i in *; do
    mkdir %{buildroot}%{_kf5_htmldir}/$i
    # Work around that filesystem does not own all supported subdirs...
    mkdir -p %{buildroot}%{_mandir}/$i/man1
done
popd

%files
%license COPYING
%{_rpmconfigdir}/macros.d/macros.kf5
%if 0%{?suse_version} >= 1550
%{_rpmconfigdir}/fileattrs/localekf5.attr
%{_rpmconfigdir}/fileattrs/localekf5.prov
%endif
%dir %{_kf5_datadir}
%dir %{_kf5_includedir}
%dir %{_kf5_libexecdir}
%dir %{_mandir}/*
%dir %{_mandir}/*/man1
%dir %{_kf5_notifydir}
%dir %{_kf5_libdir}/qt5
%dir %{_kf5_plugindir}
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plasmadir}
%dir %{_kf5_importdir}
%dir %{_kf5_qmldir}
%dir %{_kf5_cmakedir}
%dir %{_kf5_libdir}/qt5/mkspecs
%dir %{_kf5_mkspecsdir}
%dir %{_kf5_sharedir}/dbus-1
%dir %{_kf5_dbuspolicydir}
%dir %{_kf5_dbusinterfacesdir}
%dir %{_kf5_configdir}
%dir %{_kf5_iconsdir}/oxygen
%dir %{_kf5_iconsdir}/oxygen/*
%dir %{_kf5_iconsdir}/oxygen/*/*
%dir %{_kf5_wallpapersdir}
%dir %{_kf5_configkcfgdir}
%dir %{_kf5_servicesdir}
%dir %{_kf5_servicetypesdir}
%dir %{_kf5_sharedir}/doc/HTML
%dir %{_kf5_sharedir}/doc/HTML/en
%dir %{_kf5_kxmlguidir}
%dir %{_kf5_appstreamdir}
%dir %{_kf5_knsrcfilesdir}
%dir %{_kf5_debugdir}
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/*

%changelog
