#
# spec file for package kdevelop5-plugin-php
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


%define rname   kdev-php
Name:           kdevelop5-plugin-php
Version:        5.6.2
Release:        0
Summary:        PHP plugin for Kdevelop5 Integrated Development Environment
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            https://www.kdevelop.org
Source0:        https://download.kde.org/stable/kdevelop/%{version}/src/%{rname}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kcmutils-devel
BuildRequires:  kdevelop5-pg-qt
BuildRequires:  kdevplatform-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  pkgconfig
BuildRequires:  threadweaver-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       kdevelop5
Recommends:     %{name}-lang
Conflicts:      kdevelop4-plugin-php

%description
PHP plugin for Kdevelop Integrated Development Environment

This plugin enables support for the following features for developing
web applications in PHP using Kdevelop5.

  * PHP built-in functions, classes, constants, superglobals
  * user-defined functions, classes, constants, superglobals, variables, etc.
  * proper code completion for objects which respects access modifiers (private, public, protected) and differentiates between static/non-static members and methods
  * code completion for overridable and implementable functions inside classes
  * hints in the argument list of function- and method class
  * sane code completion after keywords such as extends, implements, catch(), new, throw and some more

%package devel
Summary:        Development package for kdevelop5-plugin-php
Group:          Development/Tools/IDE
Requires:       kdevelop5-plugin-php = %{version}

%description devel
This package contains the development files needed in order to use the
kdevelop5-plugin-php API.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Supplements:    packageand(bundle-lang-other:%{name})
# Language file conflicts
Conflicts:      kdevelop4-plugins-php
Conflicts:      kdevelop4-plugins-php-doc
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %find_lang kdevphp %{name}.lang

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS HACKING TODO
%{_kf5_appstreamdir}/org.kde.kdev-php.metainfo.xml
%{_kf5_debugdir}/kdevphpsupport.categories
%{_kf5_libdir}/*.so*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/kdev*/

%files devel
%license COPYING
%{_includedir}/kdev-php/
%{_kf5_cmakedir}/KDevPHP/

%files lang -f %{name}.lang

%changelog
