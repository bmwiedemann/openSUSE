#
# spec file for package grantleetheme
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
Name:           grantleetheme
Version:        19.08.2
Release:        0
Summary:        Grantlee theme support
License:        GPL-2.0-only
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  grantlee5-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  knewstuff-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Network) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
the grantleetheme library adds Grantlee theme support for PIM applications.

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
%endif

%package -n libKF5GrantleeTheme5
Summary:        GrantleeTheme library for kdepim
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       grantleetheme = %{version}

%description -n libKF5GrantleeTheme5
The GrantleeTheme library

%post -n libKF5GrantleeTheme5  -p /sbin/ldconfig
%postun -n libKF5GrantleeTheme5 -p /sbin/ldconfig

%package devel
Summary:        Development package for grantleetheme
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libKF5GrantleeTheme5 = %{version}

%description devel
The development package for the grantleetheme library

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5GrantleeTheme/
%{_kf5_includedir}/GrantleeTheme/
%{_kf5_includedir}/grantleetheme/
%{_kf5_includedir}/grantleetheme_version.h
%{_kf5_libdir}/libKF5GrantleeTheme.so
%{_kf5_mkspecsdir}/qt_GrantleeTheme.pri

%files
%license COPYING*
%{_kf5_debugdir}/grantleetheme.categories
%{_kf5_debugdir}/grantleetheme.renamecategories
%{_kf5_libdir}/grantlee/

%files -n libKF5GrantleeTheme5
%{_kf5_libdir}/libKF5GrantleeTheme.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING
%endif

%changelog
