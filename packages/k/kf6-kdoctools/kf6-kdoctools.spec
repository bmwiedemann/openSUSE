#
# spec file for package kf6-kdoctools
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


%define qt6_version 6.6.0

%define rname kdoctools
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kdoctools
Version:        6.3.0
Release:        0
Summary:        Tools to create documentation from DocBook
License:        LGPL-2.1-or-later AND MIT
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  perl-URI
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
Provides:       kf6-kdoctools-doc = %{version}
Obsoletes:      kf6-kdoctools-doc < %{version}
# The XSL templates reference files in here
Requires:       docbook-xsl-stylesheets

%description
Provides tools to generate documentation in various format from DocBook files.

%package -n libKF6DocTools6
Summary:        Library to create documentation from DocBook
Requires:       kf6-kdoctools >= %{version}

%description -n libKF6DocTools6
Provides tools to generate documentation in various format from DocBook files.

%package devel
Summary:        Build environment for kdoctools
Requires:       docbook-xsl-stylesheets
Requires:       kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
Requires:       libKF6DocTools6 = %{version}
Requires:       libxslt-devel
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Provides tools to generate documentation in various format from DocBook files.
Development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kdoctools6 --with-man --all-name

%ldconfig_scriptlets -n libKF6DocTools6

%files
%{_kf6_datadir}/kdoctools/
%{_kf6_bindir}/meinproc6
%{_kf6_bindir}/checkXML6
# The HTML files need to be in the main package or khelpcenter will have
# display issues
%{_kf6_htmldir}/*/
%doc %lang(en) %{_kf6_mandir}/*/meinproc6.*
%doc %lang(en) %{_kf6_mandir}/*/checkXML6.*
%doc %lang(en) %{_kf6_mandir}/*/kf6options.*
%doc %lang(en) %{_kf6_mandir}/*/qt6options.*

%files -n libKF6DocTools6
%license LICENSES/*
%doc README*
%{_kf6_libdir}/libKF6DocTools.so.*

%files devel
%doc %{_kf6_qchdir}/KF6DocTools.*
%{_kf6_cmakedir}/KF6DocTools/
%{_kf6_includedir}/KDocTools/
%{_libdir}/libKF6DocTools.so

%files lang -f kdoctools6.lang
%if 0%{?suse_version} == 1500
%{_kf6_mandir}/tr/
%endif

%changelog
