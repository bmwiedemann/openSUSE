#
# spec file for package pimcommon
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
Name:           pimcommon
Version:        19.08.1
Release:        0
Summary:        Base package of KDE PIM PimCommon library
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  grantlee5-devel
BuildRequires:  karchive-devel
BuildRequires:  kcalcore-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcontacts-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kimap-devel
BuildRequires:  kmime-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kpimtextedit-devel >= %{_kapp_version}
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwallet-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdepim-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  purpose-devel
BuildRequires:  sonnet-devel
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Network) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Script) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
This package contains the pimcommon library, used by several KDE PIM
applications.

%package devel
Summary:        Development package for pimcommon
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       akonadi-contacts-devel
Requires:       akonadi-server-devel
Requires:       kconfig-devel
Requires:       kcontacts-devel
Requires:       kimap-devel
Requires:       libKF5PimCommon5 = %{version}
Requires:       libKF5PimCommonAkonadi5 = %{version}

%description devel
The development package for the pimcommon libraries

%package -n libKF5PimCommon5
Summary:        The PimCommon Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5PimCommon5
The PimCommon library

%package -n libKF5PimCommonAkonadi5
Summary:        The PimCommon Akonadi Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5PimCommonAkonadi5
The PimCommon Akonadi library

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DQTWEBENGINE_SUPPORT_OPTION=TRUE

%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post -n libKF5PimCommon5  -p /sbin/ldconfig
%postun -n libKF5PimCommon5 -p /sbin/ldconfig
%post -n libKF5PimCommonAkonadi5  -p /sbin/ldconfig
%postun -n libKF5PimCommonAkonadi5 -p /sbin/ldconfig

%files
%{_kf5_debugdir}/pimcommon.categories
%{_kf5_debugdir}/pimcommon.renamecategories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5PimCommon/
%{_kf5_cmakedir}/KF5PimCommonAkonadi/
%{_kf5_includedir}/PimCommon/
%{_kf5_includedir}/PimCommonAkonadi
%{_kf5_includedir}/pimcommon/
%{_kf5_includedir}/pimcommon_version.h
%{_kf5_includedir}/pimcommonakonadi/
%{_kf5_includedir}/pimcommonakonadi_version.h
%{_kf5_libdir}/libKF5PimCommon.so
%{_kf5_libdir}/libKF5PimCommonAkonadi.so
%{_kf5_mkspecsdir}/qt_PimCommon.pri
%{_kf5_mkspecsdir}/qt_PimCommonAkonadi.pri
%{_kf5_plugindir}/designer/

%files -n libKF5PimCommon5
%license COPYING*
%{_libdir}/libKF5PimCommon.so.*

%files -n libKF5PimCommonAkonadi5
%license COPYING*
%{_libdir}/libKF5PimCommonAkonadi.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
