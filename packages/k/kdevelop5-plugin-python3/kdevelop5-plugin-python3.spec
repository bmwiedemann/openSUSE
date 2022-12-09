#
# spec file for package kdevelop5-plugin-python3
#
# Copyright (c) 2022 SUSE LLC
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
%if 0%{suse_version} >= 1550
%define mypython python310
%else 
%define mypython python3
%endif
%bcond_without released
Name:           kdevelop5-plugin-python3
Version:        22.12.0
Release:        0
Summary:        Python support for KDevelop
License:        GPL-2.0-or-later
URL:            https://www.kdevelop.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kdevelop5
BuildRequires:  kf5-filesystem
BuildRequires:  %mypython >= 3.4.3
BuildRequires:  %mypython-devel >= 3.4.3
BuildRequires:  cmake(KDevPlatform)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kdevelop5
Recommends:     %{name}-lang
Recommends:     %mypython-pep8
Provides:       kdevelop4-plugin-python = %{version}
Obsoletes:      kdevelop4-plugin-python < %{version}
# The following are needed due to old unstable packages in KDE repositories
Provides:       kdevelop4-plugin-python3 = %{version}
Obsoletes:      kdevelop4-plugin-python3 < %{version}
# Only build on archs where Qt5WebEngine is available
ExcludeArch:    ppc ppc64 ppc64le s390 s390x

%description
A KDevelop plugin which provides Python language support, including code completion and debugging using PDB.

%package lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Supplements:    (bundle-lang-other and %{name})
Conflicts:      kdevelop4-plugin-python-lang
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%make_build parser
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang kdevpython %{name}.lang

%fdupes -s %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README
%{_kf5_appstreamdir}/org.kde.kdev-python.metainfo.xml
%{_kf5_debugdir}/kdevpythonsupport.categories
%{_kf5_libdir}/libkdev*python*.so*
%{_kf5_plugindir}/
%{_kf5_sharedir}/kdevappwizard/
%{_kf5_sharedir}/kdevpythonsupport/

%files lang -f %{name}.lang

%changelog
