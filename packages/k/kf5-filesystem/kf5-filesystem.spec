#
# spec file for package kf5-filesystem
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


%if 0%{?suse_version} >= 1330
# Not set to 0 in the else branch, so it can be overwritten in the prjconf
%global with_python 0
%endif

Name:           kf5-filesystem
Url:            http://www.kde.org
Version:        20170414
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        KF5 Directory Layout
License:        LGPL-2.1-or-later
Group:          System/Fhs
%if 0%{?with_python}
# Yes, we need this just to get the site-packages path...
BuildRequires:  python-base
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
%endif
Source0:        macros.kf5
Source1:        COPYING

%description
This package provides macros which are utilized with extra-cmake-modules' KDEInstallDirs.

%define _kf5_prefix     %{_prefix}
%define _kf5_bindir     %{_kf5_prefix}/bin
%define _kf5_sharedir   %{_datadir}
%define _kf5_datadir    %{_kf5_sharedir}/kf5
%define _kf5_includedir %{_includedir}/KF5
%define _kf5_libdir     %{_kf5_prefix}/%{_lib}
%define _kf5_libexecdir %{_kf5_libdir}/libexec/kf5
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
%define _kf5_py2kf5dir       %{python2_sitelib}/PyKF5
%define _kf5_py3kf5dir       %{python3_sitelib}/PyKF5
%define _kf5_pysipdir        %{_kf5_sharedir}/sip/PyKF5
%define _kf5_knsrcfilesdir   %{_kf5_sharedir}/knsrcfiles
%define _kf5_debugdir        %{_kf5_sharedir}/qlogging-categories5

%prep

%build
%if 0%{?suse_version} <= 1320 && 0%{?sle_version} <= 120100
    sed -i 's|%%{_kf5_sharedir}/metainfo|%%{_kf5_sharedir}/appdata|g' $RPM_SOURCE_DIR/macros.kf5
%define _kf5_appstreamdir    %{_kf5_sharedir}/appdata
%else
%define _kf5_appstreamdir    %{_kf5_sharedir}/metainfo
%endif

%install
install -D -m644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
install -D -m644 %{SOURCE1} %{buildroot}%{_docdir}/kf5-filesystem/COPYING

mkdir -p %{buildroot}%{_kf5_includedir}
mkdir -p %{buildroot}%{_kf5_libexecdir}
mkdir -p %{buildroot}%{_kf5_libdir}/qt5
mkdir -p %{buildroot}%{_kf5_libdir}/qt5/plugins
mkdir -p %{buildroot}%{_kf5_plugindir}
mkdir -p %{buildroot}%{_kf5_qmldir}
mkdir -p %{buildroot}%{_kf5_datadir}
mkdir -p %{buildroot}%{_kf5_plasmadir}
mkdir -p %{buildroot}%{_kf5_importdir}
mkdir -p %{buildroot}%{_kf5_mandir}
mkdir -p %{buildroot}%{_kf5_mandir}/man{1,2,3,4,5,6,7,8,9}
mkdir -p %{buildroot}%{_kf5_sbindir}
mkdir -p %{buildroot}%{_kf5_notifydir}
mkdir -p %{buildroot}%{_kf5_sysconfdir}
mkdir -p %{buildroot}%{_kf5_sysconfdir}/xdg
mkdir -p %{buildroot}%{_kf5_cmakedir}
mkdir -p %{buildroot}%{_kf5_dbusinterfacesdir}
mkdir -p %{buildroot}%{_kf5_dbuspolicydir}
mkdir -p %{buildroot}%{_kf5_servicesdir}
mkdir -p %{buildroot}%{_kf5_servicetypesdir}
mkdir -p %{buildroot}%{_kf5_configdir}
mkdir -p %{buildroot}%{_kf5_sharedir}
mkdir -p %{buildroot}%{_kf5_htmldir}
mkdir -p %{buildroot}%{_kf5_kxmlguidir}
mkdir -p %{buildroot}%{_kf5_appstreamdir}
mkdir -p %{buildroot}%{_kf5_knsrcfilesdir}
mkdir -p %{buildroot}%{_kf5_debugdir}

for size in scalable 128x128 64x64 48x48 32x32 22x22 16x16; do
  for type in actions apps devices filesystems mimetypes places status; do
    for theme in crystalsvg oxygen hicolor locolor; do
      mkdir -p %{buildroot}%{_kf5_sharedir}/icons/$theme/$size/$type
    done
  done
done
mkdir -p %{buildroot}%{_kf5_sharedir}/icons/oxygen/scalable/apps/small/{16x16,32x32}
mkdir -p %{buildroot}%{_kf5_sharedir}/icons/oxygen/scalable/status/small/{16x16,22x22,48x48}

%if 0%{?with_python}
mkdir -p %{buildroot}%{_kf5_py2kf5dir}
mkdir -p %{buildroot}%{_kf5_py3kf5dir}

touch %{buildroot}%{_kf5_py2kf5dir}/__init__.py
touch %{buildroot}%{_kf5_py3kf5dir}/__init__.py
%endif

# Own the htmldocs directories for all supported languages
pushd /usr/share/locale
for i in *; do
    mkdir %{buildroot}%{_kf5_htmldir}/$i
    # Work around that filesystem does not own all supported subdirs...
    mkdir -p %{buildroot}%{_mandir}/$i/man1
done
popd

%files
%defattr(-,root,root)
%{_rpmconfigdir}/macros.d/macros.kf5
%dir %{_docdir}/kf5-filesystem
%{_docdir}/kf5-filesystem/COPYING
%dir %{_kf5_includedir}
%dir %{_kf5_plugindir}
%dir %{_kf5_libdir}/libexec
%dir %{_kf5_libexecdir}
%dir %{_kf5_libdir}/qt5
%dir %{_kf5_libdir}/qt5/plugins
%dir %{_kf5_plugindir}
%dir %{_kf5_datadir}
%dir %{_kf5_qmldir}
%dir %{_kf5_plasmadir}
%dir %{_kf5_importdir}
%dir %{_kf5_notifydir}
%dir %{_kf5_sysconfdir}/xdg
%dir %{_kf5_cmakedir}
%dir %{_kf5_sharedir}/dbus-1
%dir %{_kf5_sharedir}/dbus-1/interfaces
%dir %{_kf5_sharedir}/dbus-1/system.d
%dir %{_kf5_dbusinterfacesdir}
%dir %{_kf5_servicesdir}
%dir %{_kf5_servicetypesdir}
%dir %{_kf5_configdir}
%dir %{_kf5_sharedir}/icons/*
%dir %{_kf5_sharedir}/icons/*/*
%dir %{_kf5_sharedir}/icons/*/*/*
%dir %{_kf5_sharedir}/doc/HTML
%dir %{_kf5_sharedir}/doc/HTML/en
%dir %{_kf5_kxmlguidir}
%dir %{_kf5_appstreamdir}
%dir %{_kf5_knsrcfilesdir}
%dir %{_kf5_debugdir}
%if 0%{?with_python}
%{_kf5_py2kf5dir}/
%{_kf5_py3kf5dir}/
%endif
%{_kf5_htmldir}/
%exclude %{_mandir}/man*
%{_mandir}/*

%changelog
