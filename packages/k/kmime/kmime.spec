#
# spec file for package kmime
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
Name:           kmime
Version:        24.05.1
Release:        0
Summary:        KDE PIM libraries MIME support
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Conflicts:      libKF5Mime5 < %{version}

%description
This package contains the basic packages for KDE PIM applications.

%package -n libKPim6Mime6
Summary:        KDE PIM libraries MIME Support
Requires:       kmime >= %{version}

%description  -n libKPim6Mime6
This package provides MIME support for KDE PIM applications

%package devel
Summary:        Build environment for the KDE PIM MIME libraries
Requires:       libKPim6Mime6 = %{version}
Requires:       cmake(KF6Codecs) >= %{kf6_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package -n libKPim6Mime6

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=TRUE -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6Mime6

%files
%{_kf6_debugdir}/kmime.categories

%files -n libKPim6Mime6
%license LICENSES/*
%{_kf6_libdir}/libKPim6Mime.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Mime.*
%{_includedir}/KPim6/KMime/
%{_kf6_cmakedir}/KPim6Mime/
%{_kf6_libdir}/libKPim6Mime.so

%files -n libKPim6Mime6-lang -f %{name}.lang

%changelog
