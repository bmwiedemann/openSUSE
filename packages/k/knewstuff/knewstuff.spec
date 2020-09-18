#
# spec file for package knewstuff
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


%define lname   libKF5NewStuff5
%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           knewstuff
Version:        5.74.0
Release:        0
Summary:        Framework for downloading and sharing additional application data
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
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Attica) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Completion) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Package) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Qml) >= 5.12.0
BuildRequires:  cmake(Qt5Quick) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package -n %{lname}
Summary:        Framework for downloading and sharing additional application data
Group:          System/GUI/KDE
Requires:       %{name}
Obsoletes:      libKF5NewStuff4
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package -n libKF5NewStuffCore5
Summary:        Framework for downloading and sharing additional application data
Group:          System/GUI/KDE

%description -n libKF5NewStuffCore5
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package imports
Summary:        Framework for downloading and sharing additional application data
Group:          System/GUI/KDE

%description imports
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package core-devel
Summary:        Framework for downloading and sharing additional application data
Group:          Development/Libraries/KDE
Requires:       extra-cmake-modules
Requires:       libKF5NewStuffCore5 = %{version}
Requires:       cmake(KF5Attica) >= %{_kf5_bugfix_version}

%description core-devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%package quick-devel
Summary:        Framework for downloading and sharing additional application data
Group:          Development/Libraries/KDE
Requires:       %{name}-core-devel = %{version}
Requires:       %{name}-imports = %{version}
Requires:       extra-cmake-modules

%description quick-devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%package devel
Summary:        Framework for downloading and sharing additional application data
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       %{name}-core-devel = %{version}
Requires:       extra-cmake-modules
Requires:       libKF5NewStuffCore5 = %{version}
Requires:       cmake(KF5Service) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Widgets) >= 5.12.0

%description devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libKF5NewStuffCore5 -p /sbin/ldconfig
%postun -n libKF5NewStuffCore5 -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files
%license LICENSES/*
%doc README*
%{_kf5_bindir}/knewstuff-dialog
%{_kf5_datadir}/kmoretools/
%{_kf5_debugdir}/knewstuff.categories
%{_kf5_debugdir}/*.renamecategories

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5NewStuff.so.*

%files -n libKF5NewStuffCore5
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5NewStuffCore.so.*

%files imports
%license LICENSES/*
%doc README*
%{_kf5_qmldir}/

%files core-devel
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5NewStuffCore.so
%{_kf5_libdir}/cmake/KF5NewStuffCore/
%{_kf5_includedir}/knewstuffcore_version.h
%dir %{_kf5_includedir}/KNewStuff3
%{_kf5_includedir}/KNewStuff3/KNSCore/
%{_kf5_includedir}/KNewStuff3/knscore/
%{_kf5_mkspecsdir}/qt_KNewStuffCore.pri

%files quick-devel
%license LICENSES/*
%doc README*
%{_kf5_libdir}/cmake/KF5NewStuffQuick/
%{_kf5_includedir}/knewstuffquick_version.h

%files devel
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5NewStuff.so
%{_kf5_libdir}/cmake/KF5NewStuff/
%dir %{_kf5_includedir}/KNewStuff3
%{_kf5_includedir}/KNewStuff3/KNS3/
%{_kf5_includedir}/KNewStuff3/kns3/
%{_kf5_includedir}/knewstuff_version.h
%{_kf5_mkspecsdir}/qt_KNewStuff.pri

%changelog
