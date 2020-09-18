#
# spec file for package kdoctools
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


%define lname   libKF5DocTools5
%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdoctools
Version:        5.74.0
Release:        0
Summary:        Tools to create documentation from DocBook
License:        LGPL-2.1-or-later AND MIT
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FEATURE-OPENSUSE
Patch1:         0001-Also-return-KDE4-docs-in-documentationDirs.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl-URI
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
# The XSL templates reference files in here
Requires:       docbook-xsl-stylesheets
Recommends:     %{name}-lang

%description
Provides tools to generate documentation in various format from DocBook files.

%package -n %{lname}
Summary:        Library to create documentation from DocBook
Group:          System/Libraries
%requires_ge    libQt5Core5
Recommends:     %{name} = %{version}

%description -n %{lname}
Provides tools to generate documentation in various format from DocBook files.

%package devel
Summary:        Build environment for kdoctools
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       docbook-xsl-stylesheets
Requires:       extra-cmake-modules >= 1.8.0
Requires:       libxslt-devel
Requires:       cmake(Qt5Core) >= 5.12.0
Provides:       %{name}-devel-static = %{version}

%description devel
Provides tools to generate documentation in various format from DocBook files.
Development files.

%lang_package

%prep
%setup -q
%patch1 -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man --all-name
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files
%license LICENSES/*
%doc README*
%{_kf5_htmldir}/*/
%{_kf5_datadir}/kdoctools/
%{_kf5_bindir}/meinproc5
%{_kf5_bindir}/checkXML5
%doc %lang(en) %{_kf5_mandir}/*/meinproc5.*
%doc %lang(en) %{_kf5_mandir}/*/checkXML5.*
%doc %lang(en) %{_kf5_mandir}/*/kf5options.*
%doc %lang(en) %{_kf5_mandir}/*/qt5options.*

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5DocTools.so.*

%files devel
%{_kf5_libdir}/cmake/KF5DocTools/
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_libdir}/libKF5DocTools.so

%changelog
