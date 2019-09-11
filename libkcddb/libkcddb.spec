#
# spec file for package libkcddb
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkcddb
Version:        19.08.0
Release:        0
Summary:        CDDB library for KDE Applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kcodecs-devel
BuildRequires:  kconfig-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libmusicbrainz5-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Network) > 5.2.0
BuildRequires:  pkgconfig(Qt5Test) > 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) > 5.2.0
Obsoletes:      libkcddb5 < %{version}
Provides:       libkcddb5 = %{version}
Obsoletes:      libkcddb16 < %{version}
Provides:       libkcddb16 < %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
The KDE Compact Disc DataBase library provides an API for
applications to fetch and submit audio CD
information over the Internet.

%package devel
Summary:        Development files for KDE CDDB library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libKF5Cddb5 = %{version}
Requires:       libKF5CddbWidgets5 = %{version}
Obsoletes:      libkcddb5-devel < %{version}
Provides:       libkcddb5-devel = %{version}

%description devel
This package includes the development headers for %{name}.

%package -n libKF5CddbWidgets5
Summary:        CDDB widgets library for KDE Applications
Group:          System/Libraries

%description -n libKF5CddbWidgets5
This package includes the libkcddb widgets library.

%package -n libKF5Cddb5
Summary:        CDDB library for KDE Applications
Group:          System/Libraries

%description -n libKF5Cddb5
The KDE Compact Disc DataBase library provides an API for
applications to fetch and submit audio CD
information over the Internet.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%post -n libKF5Cddb5   -p /sbin/ldconfig
%postun -n libKF5Cddb5 -p /sbin/ldconfig
%post -n libKF5CddbWidgets5   -p /sbin/ldconfig
%postun -n libKF5CddbWidgets5 -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_configkcfgdir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/

%files -n libKF5Cddb5
%license COPYING*
%{_kf5_libdir}/libKF5Cddb.so.*

%files -n libKF5CddbWidgets5
%license COPYING*
%{_kf5_libdir}/libKF5CddbWidgets.so.*

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Cddb/
%{_kf5_includedir}/KCddb
%{_kf5_includedir}/kcddb_version.h
%{_kf5_libdir}/libKF5Cddb.so
%{_kf5_libdir}/libKF5CddbWidgets.so
%{_kf5_mkspecsdir}/qt_KCddb.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
