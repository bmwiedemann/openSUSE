#
# spec file for package knewstuff
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


%define lname   libKF5NewStuff5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           knewstuff
Version:        5.101.0
Release:        0
Summary:        Framework for downloading and sharing additional application data
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
BuildRequires:  cmake(KF5Syndication) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(Qt5UiPlugin) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package -n %{lname}
Summary:        Framework for downloading and sharing additional application data
Requires:       %{name}
Obsoletes:      libKF5NewStuff4

%description -n %{lname}
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package -n libKF5NewStuffCore5
Summary:        Framework for downloading and sharing additional application data

%description -n libKF5NewStuffCore5
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package -n libKF5NewStuffWidgets5
Summary:        Framework for downloading and sharing additional application data

%description -n libKF5NewStuffWidgets5
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package imports
Summary:        Framework for downloading and sharing additional application data

%description imports
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package core-devel
Summary:        Framework for downloading and sharing additional application data
Requires:       extra-cmake-modules
Requires:       libKF5NewStuffCore5 = %{version}
Requires:       cmake(KF5Attica) >= %{_kf5_bugfix_version}

%description core-devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%package quick-devel
Summary:        Framework for downloading and sharing additional application data
Requires:       %{name}-core-devel = %{version}
Requires:       %{name}-imports = %{version}
Requires:       extra-cmake-modules

%description quick-devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%package devel
Summary:        Framework for downloading and sharing additional application data
Requires:       %{lname} = %{version}
Requires:       %{name}-core-devel = %{version}
Requires:       extra-cmake-modules
Requires:       libKF5NewStuffCore5 = %{version}
Requires:       libKF5NewStuffWidgets5 = %{version}
Requires:       cmake(KF5Service) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Widgets) >= 5.15.0
# Required by KF5NewStuffConfig.cmake
Requires:       cmake(KF5NewStuffQuick) >= %{_kf5_bugfix_version}

%description devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang knewstuff5

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libKF5NewStuffCore5 -p /sbin/ldconfig
%postun -n libKF5NewStuffCore5 -p /sbin/ldconfig
%post -n libKF5NewStuffWidgets5 -p /sbin/ldconfig
%postun -n libKF5NewStuffWidgets5 -p /sbin/ldconfig

%files -n %{lname}-lang -f knewstuff5.lang

%files
%{_kf5_bindir}/knewstuff-dialog
%{_kf5_datadir}/kmoretools/
%{_kf5_debugdir}/knewstuff.categories
%{_kf5_debugdir}/*.renamecategories

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5NewStuff.so.*

%files -n libKF5NewStuffCore5
%{_kf5_libdir}/libKF5NewStuffCore.so.*

%files -n libKF5NewStuffWidgets5
%{_kf5_libdir}/libKF5NewStuffWidgets.so.*

%files imports
%{_kf5_qmldir}/

%files core-devel
%{_kf5_libdir}/libKF5NewStuffCore.so
%{_kf5_libdir}/cmake/KF5NewStuffCore/
%dir %{_kf5_includedir}/KNewStuff3
%{_kf5_includedir}/KNewStuff3/knewstuffcore_version.h
%{_kf5_includedir}/KNewStuff3/KNSCore/
%{_kf5_includedir}/KNewStuff3/knscore/
%{_kf5_mkspecsdir}/qt_KNewStuffCore.pri

%files quick-devel
%{_kf5_libdir}/cmake/KF5NewStuffQuick/
%dir %{_kf5_includedir}/KNewStuff3
%{_kf5_includedir}/KNewStuff3/knewstuffquick_version.h

%files devel
%{_kf5_libdir}/libKF5NewStuff.so
%{_kf5_libdir}/libKF5NewStuffWidgets.so
%{_kf5_libdir}/cmake/KF5NewStuff/
%dir %{_kf5_plugindir}/designer
%{_kf5_plugindir}/designer/knewstuffwidgets.so
%dir %{_kf5_includedir}/KNewStuff3/
 %{_kf5_includedir}/KNewStuff3/knewstuff_version.h
%{_kf5_includedir}/KMoreTools/
%{_kf5_includedir}/KNewStuff3/KNS3/
%{_kf5_includedir}/KNewStuff3/kns3/
%{_kf5_includedir}/KNewStuff3/knswidgets/
%{_kf5_includedir}/KNewStuff3/KNSWidgets/
%{_kf5_mkspecsdir}/qt_KNewStuff.pri

%changelog
