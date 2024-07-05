#
# spec file for package kio-extras
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
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           kio-extras
Version:        24.05.2
Release:        0
Summary:        Additional KIO slaves for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  gperf
BuildRequires:  libmtp-devel
BuildRequires:  libssh-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(KDSoapWSDiscoveryClient)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{plasma6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# Leap only has openEXR 2
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(OpenEXR) >= 3.0
%endif
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(taglib)
Requires:       trash_kcm
Requires:       qt6-sql-sqlite >= %{qt6_version}
Recommends:     kf6-kimageformats >= %{kf6_version}
Recommends:     qt6-imageformats >= %{qt6_version}
# Packages are only coinstallable since 24.02.0
Conflicts:      kio-extras5 < 24.02.0
Provides:       kfileaudiopreview = 4.100.0
Obsoletes:      kfileaudiopreview < 4.100.0
Provides:       kde-odf-thumbnail = %{version}
Obsoletes:      kde-odf-thumbnail < %{version}

%description
Additional KIO-slaves for KDE applications.

# kcm_trash.desktop conflicts with KF5's kio one. Only one is needed
%package -n trash_kcm
Summary:        Trash KDE module
Conflicts:      kio-core < 5.116

%description -n trash_kcm
This package provides a configuration module to modify trash settings.

%package -n libkioarchive6-6
Summary:        The archiver base class library

%description -n libkioarchive6-6
The archiver base class, used by specific archive formats, is made
available as a library in its own right so that support for other
archive formats can be built outside the kio-extras source tree.

%package -n libkioarchive6-devel
Summary:        Development package for libkioarchive6
Requires:       libkioarchive6-6 = %{version}

%description -n libkioarchive6-devel
This is the development package for libkioarchive6

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets
%ldconfig_scriptlets -n libkioarchive6-6

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol6/
%doc %lang(en) %{_kf6_htmldir}/en/kioworker6/
%{_kf6_applicationsdir}/*.desktop
%{_kf6_configkcfgdir}/jpegcreatorsettings5.kcfg
%{_kf6_debugdir}/kio-extras.categories
%{_kf6_debugdir}/kio-extras.renamecategories
%dir %{_kf6_plugindir}/kf6/kded/
%{_kf6_plugindir}/kf6/kded/filenamesearchmodule.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/forgetfileitemaction.so
%{_kf6_plugindir}/kf6/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
%dir %{_kf6_plugindir}/kf6/kio
%{_kf6_plugindir}/kf6/kio/activities.so
%{_kf6_plugindir}/kf6/kio/afc.so
%{_kf6_plugindir}/kf6/kio/archive.so
%{_kf6_plugindir}/kf6/kio/filter.so
%{_kf6_plugindir}/kf6/kio/fish.so
%{_kf6_plugindir}/kf6/kio/info.so
%{_kf6_plugindir}/kf6/kio/kio_filenamesearch.so
%{_kf6_plugindir}/kf6/kio/man.so
%{_kf6_plugindir}/kf6/kio/mtp.so
%{_kf6_plugindir}/kf6/kio/recentlyused.so
%{_kf6_plugindir}/kf6/kio/sftp.so
%{_kf6_plugindir}/kf6/kio/thumbnail.so
%dir %{_kf6_plugindir}/kf6/kiod
%{_kf6_plugindir}/kf6/kiod/kmtpd.so
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/audiothumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/comicbookthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/directorythumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/djvuthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/ebookthumbnail.so
%if 0%{?suse_version} > 1500
%{_kf6_plugindir}/kf6/thumbcreator/exrthumbnail.so
%endif
%{_kf6_plugindir}/kf6/thumbcreator/imagethumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/jpegthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/kraorathumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/opendocumentthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/svgthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/textthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/windowsexethumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/windowsimagethumbnail.so
%{_kf6_plugindir}/kfileaudiopreview.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_netpref.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_proxy.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_webshortcuts.so
%{_kf6_sharedir}/kio_info/
%{_kf6_sharedir}/konqueror/
%{_kf6_sharedir}/remoteview/
%{_kf6_sharedir}/solid/
%{_kf6_sharedir}/dbus-1/services/org.kde.kmtpd5.service
%{_kf6_plugindir}/kf6/kded/smbwatcher.so
%{_kf6_plugindir}/kf6/kio/smb.so
%{_kf6_libexecdir}/smbnotifier
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%exclude %{_kf6_applicationsdir}/kcm_trash.desktop

%files -n trash_kcm
%{_kf6_applicationsdir}/kcm_trash.desktop
%{_kf6_plugindir}/kcm_trash.so

%files -n libkioarchive6-6
%license LICENSES/*
%{_libdir}/libkioarchive6.so.6*

%files -n libkioarchive6-devel
%{_includedir}/KioArchive6/
%{_libdir}/cmake/KioArchive6/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol6/
%exclude %{_kf6_htmldir}/en/kioworker6/

%changelog
