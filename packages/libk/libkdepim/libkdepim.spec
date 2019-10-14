#
# spec file for package libkdepim
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


%bcond_without lang
Name:           libkdepim
Version:        19.08.2
Release:        0
Summary:        Base package of kdepim
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-contact-devel
BuildRequires:  akonadi-search-devel
BuildRequires:  akonadi-server-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kcmutils-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kcontacts-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kldap-devel
BuildRequires:  kmime-devel
BuildRequires:  kwallet-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains the libkdepim library.

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

%package -n libKF5Libkdepim5
Summary:        libkdepim library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5Libkdepim5
The libkdepim library

%package -n libKF5LibkdepimAkonadi5
Summary:        libkdepim Akonadi library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5LibkdepimAkonadi5
The libkdepim library for Akonadi related functions

%post -n libKF5Libkdepim5  -p /sbin/ldconfig
%postun -n libKF5Libkdepim5 -p /sbin/ldconfig
%post -n libKF5LibkdepimAkonadi5  -p /sbin/ldconfig
%postun -n libKF5LibkdepimAkonadi5 -p /sbin/ldconfig

%package devel
Summary:        Development package for libkdepim
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       akonadi-contacts-devel
Requires:       akonadi-server-devel
Requires:       libKF5Libkdepim5 = %{version}
Requires:       libKF5LibkdepimAkonadi5 = %{version}

%description devel
The development package for the libkdepim libraries

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Libkdepim/
%{_kf5_cmakedir}/KF5LibkdepimAkonadi/
%{_kf5_cmakedir}/MailTransportDBusService/
%{_kf5_includedir}/Libkdepim/
%{_kf5_includedir}/LibkdepimAkonadi/
%{_kf5_includedir}/libkdepim/
%{_kf5_includedir}/libkdepim_version.h
%{_kf5_includedir}/libkdepimakonadi/
%{_kf5_includedir}/libkdepimakonadi_version.h
%{_kf5_libdir}/libKF5Libkdepim.so
%{_kf5_libdir}/libKF5LibkdepimAkonadi.so
%{_kf5_mkspecsdir}/qt_Libkdepim.pri
%{_kf5_mkspecsdir}/qt_LibkdepimAkonadi.pri

%files
%license COPYING*
%{_kf5_debugdir}/libkdepim.categories
%{_kf5_debugdir}/libkdepim.renamecategories
%{_kf5_dbusinterfacesdir}/org.kde.addressbook.service.xml
%{_kf5_dbusinterfacesdir}/org.kde.mailtransport.service.xml
%{_kf5_plugindir}/designer/
%{_kf5_plugindir}/kcm_ldap.so
%{_kf5_servicesdir}/kcmldap.desktop
%{_kf5_sharedir}/kdepimwidgets/

%files -n libKF5Libkdepim5
%license COPYING*
%{_kf5_libdir}/libKF5Libkdepim.so.*

%files -n libKF5LibkdepimAkonadi5
%license COPYING*
%{_kf5_libdir}/libKF5LibkdepimAkonadi.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
