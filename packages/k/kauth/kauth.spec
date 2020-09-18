#
# spec file for package kauth
#
# Copyright (c) 2020 SUSE LLC
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


%define lname   libKF5Auth5
%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kauth
Version:        5.74.0
Release:        0
Summary:        Framework which lets applications perform actions as a privileged user
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libpolkit-qt5-1-devel
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.12.0
%endif

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package -n libKF5AuthCore5
Summary:        Framework which lets applications perform actions as a privileged user
Group:          System/GUI/KDE
Recommends:     %{lname}-lang = %{version}

%description -n libKF5AuthCore5
KAuth is a framework to let applications perform actions as a privileged user.

%package -n %{lname}
Summary:        Framework which lets applications perform actions as a privileged user
Group:          System/GUI/KDE
Requires:       libKF5AuthCore5 = %{version}
Recommends:     %{lname}-lang = %{version}
Obsoletes:      libKF5Auth4

%description -n %{lname}
KAuth is a framework to let applications perform actions as a privileged user.

%package devel
Summary:        Framework which lets applications perform actions as a privileged user
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}

%description devel
KAuth is a framework to let applications perform actions as a privileged user.
Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build -- -DSYSCONF_INSTALL_DIR=%{_kf5_sysconfdir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libKF5AuthCore5 -p /sbin/ldconfig
%postun -n libKF5AuthCore5 -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%dir %{_kf5_libdir}/libexec
%{_kf5_dbuspolicydir}/org.kde.kf5auth.conf
%{_kf5_debugdir}/kauth.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Auth.so.*
%{_kf5_libdir}/libexec/kauth
%{_kf5_plugindir}/

%files -n libKF5AuthCore5
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5AuthCore.so.*

%files devel
%license LICENSES/*
%dir %{_kf5_includedir}/*/
%{_kf5_datadir}/kauth/
%{_kf5_includedir}/*.h
%{_kf5_includedir}/*/
%{_kf5_libdir}/cmake/KF5Auth/
%{_kf5_libdir}/libKF5Auth.so
%{_kf5_libdir}/libKF5AuthCore.so
%{_kf5_mkspecsdir}/qt_KAuth.pri
%{_kf5_mkspecsdir}/qt_KAuthCore.pri

%changelog
