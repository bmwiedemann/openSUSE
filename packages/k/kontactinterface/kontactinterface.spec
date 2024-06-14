#
# spec file for package kontactinterface
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kontactinterface
Version:        24.05.1
Release:        0
Summary:        KDE PIM Libraries: Interface to Contacts
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKPim6KontactInterface6
Summary:        KDE PIM Libraries: Interface to Contacts
Requires:       kontactinterface >= %{version}
# Renamed
Obsoletes:      kontactinterface-lang <= 23.04.0

%description  -n libKPim6KontactInterface6
This package provides the interface to contacts for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       libKPim6KontactInterface6 = %{version}
Requires:       cmake(KF6Parts) >= %{kf6_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package -n libKPim6KontactInterface6

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6KontactInterface6

%files
%{_kf6_debugdir}/kontactinterface.categories
%{_kf6_debugdir}/kontactinterface.renamecategories

%files -n libKPim6KontactInterface6
%license LICENSES/*
%{_kf6_libdir}/libKPim6KontactInterface.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6KontactInterface.*
%{_includedir}/KPim6/KontactInterface/
%{_kf6_cmakedir}/KPim6KontactInterface/
%{_kf6_libdir}/libKPim6KontactInterface.so

%files -n libKPim6KontactInterface6-lang -f %{name}.lang

%changelog
