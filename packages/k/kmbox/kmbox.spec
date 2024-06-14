#
# spec file for package kmbox
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           kmbox
Version:        24.05.1
Release:        0
Summary:        KDE PIM Libraries: Mailbox functionality
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Conflicts:      libKF6MBox5 < %{version}

%description
This package contains the basic packages for KDE PIM applications.

%package -n libKPim6Mbox6
Summary:        KDE PIM Libraries: Mailbox functionality
Requires:       kmbox >= %{version}
Obsoletes:      libKF5Mbox5 < %{version}
Obsoletes:      libKPim5Mbox5 < %{version}

%description  -n libKPim6Mbox6
This package provides the mailbox functionality for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       libKPim6Mbox6 = %{version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKPim6Mbox6

%files
%license LICENSES/*
%{_kf6_debugdir}/kmbox.categories
%{_kf6_debugdir}/kmbox.renamecategories

%files -n libKPim6Mbox6
%{_kf6_libdir}/libKPim6Mbox.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Mbox.*
%{_includedir}/KPim6/KMbox/
%{_kf6_cmakedir}/KPim6Mbox/
%{_kf6_libdir}/libKPim6Mbox.so

%changelog
