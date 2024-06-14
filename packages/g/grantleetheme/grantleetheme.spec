#
# spec file for package grantleetheme
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
Name:           grantleetheme
Version:        24.05.1
Release:        0
Summary:        Grantlee theme support
License:        GPL-2.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
the grantleetheme library adds Grantlee theme support for PIM applications.

%package -n libKPim6GrantleeTheme6
Summary:        GrantleeTheme library for KDE PIM applications
License:        LGPL-2.1-or-later
Requires:       grantleetheme >= %{version}

%description -n libKPim6GrantleeTheme6
The GrantleeTheme library

%package devel
Summary:        Development package for grantleetheme
License:        LGPL-2.1-or-later
Requires:       libKPim6GrantleeTheme6 = %{version}
Requires:       cmake(KF6TextTemplate)

%description devel
The development package for the grantleetheme library

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6GrantleeTheme6

%files
%{_kf6_debugdir}/grantleetheme.categories
%{_kf6_debugdir}/grantleetheme.renamecategories
%{_kf6_plugindir}/kf6/ktexttemplate/kde_grantlee_plugin.so

%files -n libKPim6GrantleeTheme6
%license LICENSES/*
%{_kf6_libdir}/libKPim6GrantleeTheme.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6GrantleeTheme.*
%{_includedir}/KPim6/GrantleeTheme/
%{_kf6_cmakedir}/KPim6GrantleeTheme/
%{_kf6_libdir}/libKPim6GrantleeTheme.so

%files lang -f %{name}.lang

%changelog
