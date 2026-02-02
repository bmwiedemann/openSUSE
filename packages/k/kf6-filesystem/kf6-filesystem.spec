#
# spec file for package kf6-filesystem
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           kf6-filesystem
Version:        20251007
Release:        0
Summary:        RPM macros for KDE packages using Qt6
License:        MIT
URL:            https://www.opensuse.org
Source0:        macros.kf6
Source1:        LICENSE.MIT
Requires:       cmake
Requires:       hicolor-icon-theme
Requires:       ninja

%description
This package contains macros which are used when building KDE packages.

%define _kf6_prefix            %{_prefix}

%define _kf6_sysconfdir        %{_sysconfdir}
%define _kf6_libexecdir        %{_libexecdir}/kf6

%define _kf6_bindir            %{_kf6_prefix}/bin
%define _kf6_includedir        %{_kf6_prefix}/include/KF6
%define _kf6_libdir            %{_kf6_prefix}/%{_lib}
%define _kf6_sbindir           %{_kf6_prefix}/sbin
%define _kf6_sharedir          %{_kf6_prefix}/share

%define _kf6_datadir           %{_kf6_sharedir}/kf6

%define _kf6_configdir         %{_kf6_sysconfdir}/xdg

%define _kf6_cmakedir          %{_kf6_libdir}/cmake
%define _kf6_pkgconfigdir      %{_kf6_libdir}/pkgconfig

%define _kf6_qchdir            %{_kf6_sharedir}/doc/qt6

%define _kf6_importdir         %{_kf6_libdir}/qt6/imports
%define _kf6_mkspecsdir        %{_kf6_libdir}/qt6/mkspecs/modules
%define _kf6_plugindir         %{_kf6_libdir}/qt6/plugins
%define _kf6_qmldir            %{_kf6_libdir}/qt6/qml

%define _kf6_appsdir           %{_kf6_sharedir}
%define _kf6_applicationsdir   %{_kf6_sharedir}/applications
%define _kf6_configkcfgdir     %{_kf6_sharedir}/config.kcfg
%define _kf6_dbusinterfacesdir %{_kf6_sharedir}/dbus-1/interfaces
%define _kf6_dbuspolicydir     %{_kf6_sharedir}/dbus-1/system.d
%define _kf6_htmldir           %{_kf6_sharedir}/doc/HTML
%define _kf6_iconsdir          %{_kf6_sharedir}/icons
%define _kf6_notificationsdir  %{_kf6_sharedir}/knotifications6
%define _kf6_knsrcfilesdir     %{_kf6_sharedir}/knsrcfiles
%define _kf6_kxmlguidir        %{_kf6_sharedir}/kxmlgui5
%define _kf6_localedir         %{_kf6_sharedir}/locale/kf6
%define _kf6_mandir            %{_kf6_sharedir}/man
%define _kf6_appstreamdir      %{_kf6_sharedir}/metainfo
%define _kf6_plasmadir         %{_kf6_sharedir}/plasma
%define _kf6_debugdir          %{_kf6_sharedir}/qlogging-categories6
%define _kf6_wallpapersdir     %{_kf6_sharedir}/wallpapers

%prep

%build

%install
install -D -m644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.kf6
install -D -m644 %{SOURCE1} %{buildroot}%{_defaultlicensedir}/kf6-filesystem/LICENSE.MIT

# Let kf6-filesystem 'own' directories not already owned by the filesystem package
mkdir -p %{buildroot}%{_kf6_includedir}
mkdir -p %{buildroot}%{_kf6_libexecdir}
mkdir -p %{buildroot}%{_kf6_datadir}
mkdir -p %{buildroot}%{_kf6_configkcfgdir}
mkdir -p %{buildroot}%{_kf6_htmldir}
mkdir -p %{buildroot}%{_kf6_notificationsdir}
mkdir -p %{buildroot}%{_kf6_knsrcfilesdir}
mkdir -p %{buildroot}%{_kf6_kxmlguidir}
mkdir -p %{buildroot}%{_kf6_localedir}
mkdir -p %{buildroot}%{_kf6_plasmadir}
mkdir -p %{buildroot}%{_kf6_debugdir}
mkdir -p %{buildroot}%{_kf6_wallpapersdir}

# Own the HTML docs directories for all supported languages
pushd /usr/share/locale
for i in *; do
    mkdir %{buildroot}%{_kf6_htmldir}/$i
    # Work around that filesystem does not own all supported subdirs...
    mkdir -p %{buildroot}%{_kf6_mandir}/$i/man1
done
popd

# Additional install directories used by KDE packages
mkdir -p %{buildroot}%{_includedir}/KPim6
mkdir -p %{buildroot}%{_kf6_libdir}/kconf_update_bin
mkdir -p %{buildroot}%{_kf6_libexecdir}/kauth
mkdir -p %{buildroot}%{_kf6_plugindir}/designer
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6/kded
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6/kio
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6/parts
mkdir -p %{buildroot}%{_kf6_plugindir}/pim6
mkdir -p %{buildroot}%{_kf6_plugindir}/pim6/akonadi
mkdir -p %{buildroot}%{_kf6_plugindir}/plasma/applets
mkdir -p %{buildroot}%{_kf6_plugindir}/plasma/kcms/systemsettings
mkdir -p %{buildroot}%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets
mkdir -p %{buildroot}%{_kf6_qmldir}/org/kde
mkdir -p %{buildroot}%{_kf6_sharedir}/kconf_update
mkdir -p %{buildroot}%{_kf6_sharedir}/kdevappwizard/templates
mkdir -p %{buildroot}%{_kf6_sharedir}/kglobalaccel
mkdir -p %{buildroot}%{_kf6_sharedir}/krunner/dbusplugins
mkdir -p %{buildroot}%{_kf6_sharedir}/plasma/plasmoids

%files
%dir %{_defaultlicensedir}/kf6-filesystem
%license %{_defaultlicensedir}/kf6-filesystem/LICENSE.MIT
%{_rpmmacrodir}/macros.kf6
%dir %{_kf6_configkcfgdir}
%dir %{_kf6_datadir}
%dir %{_kf6_debugdir}
%dir %{_kf6_htmldir}
%dir %{_kf6_htmldir}/*
%dir %{_kf6_includedir}
%dir %{_kf6_knsrcfilesdir}
%dir %{_kf6_kxmlguidir}
%dir %{_kf6_libexecdir}
%dir %{_kf6_localedir}
%dir %{_kf6_mandir}/*
%dir %{_kf6_mandir}/*/man1
%dir %{_kf6_notificationsdir}
%dir %{_kf6_plasmadir}
%dir %{_kf6_wallpapersdir}
#
%dir %{_includedir}/KPim6
%dir %{_kf6_libdir}/kconf_update_bin
%dir %{_kf6_libdir}/qt6
%dir %{_kf6_libexecdir}/kauth
%dir %{_kf6_plugindir}
%dir %{_kf6_plugindir}/designer
%dir %{_kf6_plugindir}/kf6
%dir %{_kf6_plugindir}/kf6/kded
%dir %{_kf6_plugindir}/kf6/kio
%dir %{_kf6_plugindir}/kf6/parts
%dir %{_kf6_plugindir}/pim6
%dir %{_kf6_plugindir}/pim6/akonadi
%dir %{_kf6_plugindir}/plasma
%dir %{_kf6_plugindir}/plasma/applets
%dir %{_kf6_plugindir}/plasma/kcms
%dir %{_kf6_plugindir}/plasma/kcms/systemsettings
%dir %{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets
%dir %{_kf6_qmldir}
%dir %{_kf6_qmldir}/org
%dir %{_kf6_qmldir}/org/kde
%dir %{_kf6_sharedir}/kconf_update
%dir %{_kf6_sharedir}/kdevappwizard
%dir %{_kf6_sharedir}/kdevappwizard/templates
%dir %{_kf6_sharedir}/kglobalaccel
%dir %{_kf6_sharedir}/krunner
%dir %{_kf6_sharedir}/krunner/dbusplugins
%dir %{_kf6_sharedir}/plasma/plasmoids

%changelog
