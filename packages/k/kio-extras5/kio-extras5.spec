#
# spec file for package kio-extras5
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kio-extras5
Version:        19.08.2
Release:        0
Summary:        Additional KIO slaves for KDE applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source99:       %{name}-rpmlintrc
BuildRequires:  OpenEXR-devel
BuildRequires:  flac-devel
BuildRequires:  gperf
BuildRequires:  kactivities5-devel
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdnssd-framework-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  khtml-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kpty-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libssh-devel
BuildRequires:  libtag-devel
BuildRequires:  openslp-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  solid-devel
BuildRequires:  syntax-highlighting-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5DBus) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(smbclient)
Recommends:     %{name}-lang
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
Group:          System/Libraries

%description -n libkioarchive5
The archiver base class, used by specific archive formats, is made
available as a library in its own right so that support for other
archive formats can be built outside the kio-extras source tree.

%package -n libkioarchive-devel
Summary:        Development package for libkioarchive5
Group:          Development/Libraries/C and C++
Requires:       libkioarchive5 = %{version}

%description -n libkioarchive-devel
This is the development package for libkioarchive

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n %{rname}-%{version}
sed -i '/^add_subdirectory( doc )/d' CMakeLists.txt

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=share/locale/kf5
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %{kf5_find_lang}
    %{kf5_find_htmldocs}
  %endif
  # we don't need nor want devel symlink, and dbus interface -- kio-extras don't install any headers,
  # nor are meant for development
  rm -rf %{buildroot}%{_kf5_sharedir}/dbus-1/

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   -n libkioarchive5 -p /sbin/ldconfig
%postun -n libkioarchive5 -p /sbin/ldconfig

%files
%license COPYING.*
%{_kf5_configkcfgdir}/
%{_kf5_libdir}/libmolletnetwork5.so.*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/kio_bookmarks/
%{_kf5_sharedir}/kio_docfilter/
%{_kf5_sharedir}/kio_info/
%{_kf5_sharedir}/konqsidebartng/
%{_kf5_sharedir}/konqueror/
%{_kf5_sharedir}/mime/packages/kf5_network.xml
%{_kf5_sharedir}/remoteview/
%{_kf5_sharedir}/solid/
%{_kf5_debugdir}/kio-extras.categories

%files -n libkioarchive-devel
%{_kf5_includedir}/kio_archivebase.h
%{_kf5_includedir}/libkioarchive_export.h
%{_libdir}/cmake/KioArchive/

%files -n libkioarchive5
%license COPYING.*
%{_libdir}/libkioarchive.so.5*

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
