#
# spec file for package libqaccessibilityclient
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


%define rname  libqaccessibilityclient
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
ExclusiveArch: do_not_build
%endif
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
# TODO add kf6-extra-cmake-modules when available
%define qt6_version 6.5.0
%endif
%if "%{flavor}" == "qt5"
%define qt5 1
%define pkg_suffix -qt5
%define qt5_version 5.15.2
%endif
%bcond_without released
Name:           libqaccessibilityclient%{?pkg_suffix}
Version:        0.6.0
Release:        0
Summary:        Accessibilty tools helper library, used e.g. by screen readers
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz.sig
Source2:        libqaccessibilityclient.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules
%if 0%{?qt6}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
%else
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
%endif

%description
This library is used when writing accessibility clients such as screen readers.

%package -n libqaccessibilityclient%{pkg_suffix}-0
Summary:        Accessibilty tools helper library, used e.g. by screen readers
Requires:       libqaccessibilityclient%{?pkg_suffix} >= %{version}
Requires:       at-spi2-core

%description -n libqaccessibilityclient%{pkg_suffix}-0
This library is used when writing accessibility clients such as screen readers.

%package devel
Summary:        Accessibilty tools helper library, used e.g. by screen readers
Requires:       libqaccessibilityclient%{pkg_suffix}-0 = %{version}
%if 0%{?qt6}
Conflicts:      libqaccessibilityclient-qt5-devel
%endif

%description devel
This library is used when writing accessibility clients such as screen readers.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%define extra_options -DBUILD_TESTING:BOOL=TRUE -DCMAKE_SKIP_RPATH:BOOL=TRUE
%if 0%{?qt6}
%cmake_qt6 -DBUILD_WITH_QT6:BOOL=TRUE %{extra_options}
%qt6_build
%else
%cmake_kf5 -d build -- %{extra_options}
%cmake_build
%endif

%install
%if 0%{?qt6}
%qt6_install
%else
%kf5_makeinstall -C build
%endif

# Not that useful for debugging
rm %{buildroot}%{_bindir}/dumper

%fdupes %{buildroot}

%ldconfig_scriptlets -n libqaccessibilityclient%{pkg_suffix}-0

%files
%if 0%{?qt6}
%{_kf6_debugdir}/libqaccessibilityclient.categories
%else
%{_kf5_debugdir}/libqaccessibilityclient.categories
%endif

%files -n libqaccessibilityclient%{pkg_suffix}-0
%license LICENSES/*
%{_libdir}/libqaccessibilityclient%{pkg_suffix}.so.*

%files devel
%doc README.md
%{_libdir}/libqaccessibilityclient%{pkg_suffix}.so
%if 0%{?qt6}
%{_includedir}/QAccessibilityClient6/
%{_libdir}/cmake/QAccessibilityClient6/
%else
%{_kf5_cmakedir}/QAccessibilityClient/
%{_includedir}/QAccessibilityClient/
%endif

%changelog
