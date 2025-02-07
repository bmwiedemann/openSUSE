#
# spec file for package kdevelop-plugin-python3
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


%define rname kdev-python
%define mypython python3
%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdevelop-plugin-python3
Version:        24.12.2
Release:        0
Summary:        Python support for KDevelop
License:        GPL-2.0-or-later
URL:            https://www.kdevelop.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         fix-for-python3.6.patch
BuildRequires:  %{mypython} >= 3.4.3
BuildRequires:  %{mypython}-devel >= 3.4.3
BuildRequires:  fdupes
BuildRequires:  kdevelop >= 6.0
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDevPlatform)
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# Package was renamed before 24.08 release
Requires:       kdevelop >= 24.08.0
Recommends:     %{mypython}-pep8
Provides:       kdevelop4-plugin-python = %{version}
Obsoletes:      kdevelop4-plugin-python < %{version}
Obsoletes:      kdevelop5-plugin-python3 < %{version}
# Only build on archs where Qt6WebEngine is available
ExclusiveArch:  aarch64 x86_64 %{x86_64} riscv64

%description
A KDevelop plugin which provides Python language support, including code
completion and debugging using PDB.

%package lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Supplements:    (bundle-lang-other and %{name})
Conflicts:      kdevelop4-plugin-python-lang
Obsoletes:      kdevelop5-plugin-python3-lang < %{version}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# Remove obsolete docs
rm -r %{buildroot}%{_kf6_sharedir}/kdevpythonsupport/documentation_files/{PyKDE4,PyQt4}

%find_lang kdevpython %{name}.lang

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README
%{_kf6_appstreamdir}/org.kde.kdev-python.metainfo.xml
%{_kf6_debugdir}/kdevpythonsupport.categories
%{_kf6_libdir}/libkdevpythoncompletion.so
%{_kf6_libdir}/libkdevpythonduchain.so
%{_kf6_libdir}/libkdevpythonparser.so
%{_kf6_plugindir}/kdevplatform/
%dir %{_kf6_sharedir}/kdevappwizard
%dir %{_kf6_sharedir}/kdevappwizard/templates
%{_kf6_sharedir}/kdevappwizard/templates/django_project.tar.bz2
%{_kf6_sharedir}/kdevappwizard/templates/qtdesigner_app.tar.bz2
%{_kf6_sharedir}/kdevappwizard/templates/simple_pythonapp.tar.bz2
%{_kf6_sharedir}/kdevpythonsupport/

%files lang -f %{name}.lang

%changelog
