#
# spec file for package kio-extras5
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


%define rname kio-extras
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kio-extras5
Version:        22.12.0
Release:        0
Summary:        Additional KIO slaves for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# openEXR causes build issues for Leap 15.2 & 15.3
%if 0%{?suse_version} > 1500
BuildRequires:  OpenEXR-devel
%endif
BuildRequires:  flac-devel
BuildRequires:  gperf
BuildRequires:  kdsoap-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libssh-devel
BuildRequires:  libtag-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5ActivitiesStats)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(smbclient)
Recommends:     kimageformats
# we want some imageformats in
Recommends:     libqt5-qtimageformats
Provides:       kfileaudiopreview = 4.100.0
Obsoletes:      kfileaudiopreview < 4.100.0
Provides:       kde-odf-thumbnail = %{version}
Obsoletes:      kde-odf-thumbnail < %{version}

%description
Additional KIO-slaves for KDE applications.

%package -n libkioarchive5
Summary:        The archiver base class library

%description -n libkioarchive5
The archiver base class, used by specific archive formats, is made
available as a library in its own right so that support for other
archive formats can be built outside the kio-extras source tree.

%package -n libkioarchive-devel
Summary:        Development package for libkioarchive5
Requires:       libkioarchive5 = %{version}

%description -n libkioarchive-devel
This is the development package for libkioarchive

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=share/locale/kf5
%cmake_build

%install
%kf5_makeinstall -C build

%{kf5_find_lang}
%{kf5_find_htmldocs}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   -n libkioarchive5 -p /sbin/ldconfig
%postun -n libkioarchive5 -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_datadir}/doc/HTML/en/kioslave5
%{_kf5_configkcfgdir}/
%{_kf5_debugdir}/kio-extras.categories
%{_kf5_debugdir}/kio-extras.renamecategories
%{_kf5_libexecdir}/smbnotifier
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/kio_bookmarks/
%{_kf5_sharedir}/kio_docfilter/
%{_kf5_sharedir}/kio_info/
%{_kf5_sharedir}/konqueror/
%{_kf5_sharedir}/remoteview/
%{_kf5_sharedir}/solid/
%{_kf5_sharedir}/dbus-1/services/org.kde.kmtpd5.service
%{_kf5_sharedir}/mime/packages/org.kde.kio.smb.xml

%files -n libkioarchive-devel
%{_kf5_includedir}/kio_archivebase.h
%{_kf5_includedir}/libkioarchive_export.h
%{_libdir}/cmake/KioArchive/

%files -n libkioarchive5
%license LICENSES/*
%{_libdir}/libkioarchive.so.5*

%files lang -f %{name}.lang

%changelog
