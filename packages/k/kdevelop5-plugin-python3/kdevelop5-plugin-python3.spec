#
# spec file for package kdevelop5-plugin-python3
#
# Copyright (c) 2020 SUSE LLC
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
Name:           kdevelop5-plugin-python3
Version:        5.6.0
Release:        0
Summary:        Python support for KDevelop
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            https://www.kdevelop.org
Source0:        https://download.kde.org/stable/kdevelop/%{version}/src/%{rname}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kdevelop5
BuildRequires:  kf5-filesystem
BuildRequires:  python3 >= 3.4.3
BuildRequires:  python3-devel >= 3.4.3
BuildRequires:  cmake(KDevPlatform)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kdevelop5
Recommends:     %{name}-lang
Recommends:     python3-pep8
Provides:       kdevelop4-plugin-python = %{version}
Obsoletes:      kdevelop4-plugin-python < %{version}
# The following are needed due to old unstable packages in KDE repositories
Provides:       kdevelop4-plugin-python3 = %{version}
Obsoletes:      kdevelop4-plugin-python3 < %{version}

%description
A KDevelop plugin which provides Python language support, including code completion and debugging using PDB.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Supplements:    (bundle-lang-other and %{name})
Conflicts:      kdevelop4-plugin-python-lang
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%setup -q -n %{rname}-%{version}

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
%license COPYING
%doc README
%{_kf5_appstreamdir}/org.kde.kdev-python.metainfo.xml
%{_kf5_debugdir}/kdevpythonsupport.categories
%{_kf5_libdir}/libkdev*python*.so*
%{_kf5_plugindir}/
%{_kf5_sharedir}/kdevappwizard/
%{_kf5_sharedir}/kdevpythonsupport/

%files lang -f %{name}.lang

%changelog
