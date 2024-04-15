#
# spec file for package kio-extras5
#
# Copyright (c) 2023 SUSE LLC
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


%define rname kio-extras-kf5
%bcond_without released
Name:           kio-extras5
Version:        24.02.2
Release:        0
Summary:        Additional KIO slaves for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# OpenEXR on Leap is incompatible with C++17
%if 0%{?suse_version} > 1500
BuildRequires:  OpenEXR-devel
%endif
BuildRequires:  flac-devel
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-c++
BuildRequires:  gcc13-PIE
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  gperf
BuildRequires:  kdsoap-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libssh-devel
BuildRequires:  libtag-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5ActivitiesStats)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KExiv2)
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
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(smbclient)
# Provides previews for video files
Recommends:     ffmpegthumbs-kf5
Recommends:     kimageformats
# we want some imageformats in
Recommends:     libqt5-qtimageformats
Provides:       kfileaudiopreview = 4.100.0
Obsoletes:      kfileaudiopreview < 4.100.0
Provides:       kde-odf-thumbnail = %{version}
Obsoletes:      kde-odf-thumbnail < %{version}
# Some common files moved to the KF6 version
Requires:       kio-extras >= %{version}

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
%if 0%{?suse_version} == 1500
  export CXX=g++-13
%endif

%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=share/locale/kf5
%cmake_build

%install
%kf5_makeinstall -C build

%{kf5_find_lang}
%{kf5_find_htmldocs}

%ldconfig_scriptlets
%ldconfig_scriptlets -n libkioarchive5

%files
%license LICENSES/*
%doc %lang(en) %{_datadir}/doc/HTML/en/kioslave5
%{_kf5_debugdir}/kio-extras.categories
%{_kf5_debugdir}/kio-extras.renamecategories
%{_kf5_libexecdir}/smbnotifier
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_plugindir}/kf5/kded/filenamesearchmodule.so
%{_kf5_plugindir}/kf5/kded/recentdocumentsnotifier.so
%{_kf5_plugindir}/kf5/kded/smbwatcher.so
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%{_kf5_plugindir}/kf5/kfileitemaction/forgetfileitemaction.so
%{_kf5_plugindir}/kf5/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
 %dir %{_kf5_plugindir}/kf5/kio
%{_kf5_plugindir}/kf5/kio/activities.so
%{_kf5_plugindir}/kf5/kio/afc.so
%{_kf5_plugindir}/kf5/kio/archive.so
%{_kf5_plugindir}/kf5/kio/filter.so
%{_kf5_plugindir}/kf5/kio/fish.so
%{_kf5_plugindir}/kf5/kio/info.so
%{_kf5_plugindir}/kf5/kio/kio_filenamesearch.so
%{_kf5_plugindir}/kf5/kio/man.so
%{_kf5_plugindir}/kf5/kio/mtp.so
%{_kf5_plugindir}/kf5/kio/recentdocuments.so
%{_kf5_plugindir}/kf5/kio/recentlyused.so
%{_kf5_plugindir}/kf5/kio/sftp.so
%{_kf5_plugindir}/kf5/kio/smb.so
%{_kf5_plugindir}/kf5/kio/thumbnail.so
%dir %{_kf5_plugindir}/kf5/kiod
%{_kf5_plugindir}/kf5/kiod/kmtpd.so
%dir %{_kf5_plugindir}/kf5/thumbcreator
%{_kf5_plugindir}/kf5/thumbcreator/audiothumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/comicbookthumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/djvuthumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/ebookthumbnail.so
%if 0%{?suse_version} > 1500
%{_kf5_plugindir}/kf5/thumbcreator/exrthumbnail.so
%endif
%{_kf5_plugindir}/kf5/thumbcreator/imagethumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/jpegthumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/kraorathumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/opendocumentthumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/svgthumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/textthumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/windowsexethumbnail.so
%{_kf5_plugindir}/kf5/thumbcreator/windowsimagethumbnail.so
%{_kf5_plugindir}/kfileaudiopreview.so
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/

%files -n libkioarchive-devel
%{_includedir}/KioArchive/
%{_libdir}/cmake/KioArchive/

%files -n libkioarchive5
%license LICENSES/*
%{_libdir}/libkioarchive.so.5*

%files lang -f %{name}.lang

%changelog
