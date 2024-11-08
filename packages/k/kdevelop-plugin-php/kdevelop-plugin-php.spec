#
# spec file for package kdevelop-plugin-php
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


%define rname   kdev-php
%define kf6_version 6.3.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdevelop-plugin-php
Version:        24.08.3
Release:        0
Summary:        PHP plugin for Kdevelop5 Integrated Development Environment
License:        GPL-2.0-or-later
URL:            https://www.kdevelop.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDevPlatform) >= 6.0
BuildRequires:  cmake(KDevelop-PG-Qt) >= 2.3
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# Package was renamed before 24.08 release
Requires:       kdevelop >= 24.08.3
Conflicts:      kdevelop4-plugin-php
Obsoletes:      kdevelop5-plugin-php < %{version}
# Only build on archs where Qt6WebEngine is available
ExclusiveArch:  aarch64 x86_64 %{x86_64} riscv64

%description
PHP plugin for Kdevelop Integrated Development Environment

This plugin enables support for the following features for developing
web applications in PHP using Kdevelop5.

  * PHP built-in functions, classes, constants, superglobals
  * user-defined functions, classes, constants, superglobals, variables, etc.
  * proper code completion for objects which respects access modifiers (private,
    public, protected) and differentiates between static/non-static members and
    methods
  * code completion for overridable and implementable functions inside classes
  * hints in the argument list of function- and method class
  * sane code completion after keywords such as extends, implements, catch(),
    new, throw and some more

%package devel
Summary:        Development package for kdevelop-plugin-php
Requires:       kdevelop-plugin-php = %{version}

%description devel
This package contains the development files needed in order to use the
kdevelop-plugin-php API.

%package lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Supplements:    (bundle-lang-other and %{name})
# Language file conflicts & obsoletes
Conflicts:      kdevelop4-plugins-php
Conflicts:      kdevelop4-plugins-php-doc
Obsoletes:      kdevelop5-plugin-php-lang
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

%find_lang kdevphp %{name}.lang

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc AUTHORS HACKING TODO
%{_kf6_appstreamdir}/org.kde.kdev-php.metainfo.xml
%{_kf6_debugdir}/kdevphpsupport.categories
# NOTE: These are plugins
%{_kf6_libdir}/libkdevphpcompletion.so
%{_kf6_libdir}/libkdevphpduchain.so
%{_kf6_libdir}/libkdevphpparser.so
%{_kf6_plugindir}/kdevplatform/
%dir %{_kf6_sharedir}/kdevappwizard
%dir %{_kf6_sharedir}/kdevappwizard/templates
%{_kf6_sharedir}/kdevappwizard/templates/simple_phpapp.tar.bz2
%{_kf6_sharedir}/kdevphpsupport/

%files devel
%{_includedir}/kdev-php/
%{_kf6_cmakedir}/KDevPHP/

%files lang -f %{name}.lang

%changelog
