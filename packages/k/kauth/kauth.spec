#
# spec file for package kauth
#
# Copyright (c) 2021 SUSE LLC
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
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kauth
Version:        5.101.0
Release:        0
Summary:        Framework which lets applications perform actions as a privileged user
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libpolkit-qt5-1-devel
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package -n libKF5AuthCore5
Summary:        Framework which lets applications perform actions as a privileged user
Recommends:     %{lname}-lang = %{version}

%description -n libKF5AuthCore5
KAuth is a framework to let applications perform actions as a privileged user.

%package -n %{lname}
Summary:        Framework which lets applications perform actions as a privileged user
Requires:       libKF5AuthCore5 = %{version}
Obsoletes:      libKF5Auth4

%description -n %{lname}
KAuth is a framework to let applications perform actions as a privileged user.

%package devel
Summary:        Framework which lets applications perform actions as a privileged user
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}

%description devel
KAuth is a framework to let applications perform actions as a privileged user.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DSYSCONF_INSTALL_DIR=%{_kf5_sysconfdir}
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kauth5 --with-qt --without-mo

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libKF5AuthCore5 -p /sbin/ldconfig
%postun -n libKF5AuthCore5 -p /sbin/ldconfig

%files -n %{lname}-lang -f kauth5.lang

%files -n %{lname}
%dir %{_libexecdir}/kauth
%{_kf5_dbuspolicydir}/org.kde.kf5auth.conf
%{_kf5_debugdir}/kauth.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Auth.so.*
%{_kf5_plugindir}/kauth/
%{_libexecdir}/kauth/kauth-policy-gen

%files -n libKF5AuthCore5
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5AuthCore.so.*

%files devel
%{_kf5_datadir}/kauth/
%{_kf5_includedir}/KAuth/
%{_kf5_includedir}/KAuthCore/
%{_kf5_includedir}/KAuthWidgets/
%{_kf5_libdir}/cmake/KF5Auth/
%{_kf5_libdir}/libKF5Auth.so
%{_kf5_libdir}/libKF5AuthCore.so
%{_kf5_mkspecsdir}/qt_KAuth.pri
%{_kf5_mkspecsdir}/qt_KAuthCore.pri

%changelog
