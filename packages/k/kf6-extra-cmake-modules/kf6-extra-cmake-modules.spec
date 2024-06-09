#
# spec file for package kf6-extra-cmake-modules
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%global pkg_suffix -doc
%endif

%define rname extra-cmake-modules

# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without doc
%bcond_without released
Name:           kf6-extra-cmake-modules%{?pkg_suffix}
Version:        6.3.0
Release:        0
Summary:        CMake modules
License:        BSD-3-Clause
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  cmake >= 3.16
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
BuildRequires:  gcc13-PIE
%endif
BuildRequires:  kf6-filesystem
%if "%{flavor}" != "doc"
Requires:       cmake >= 3.16
%if 0%{?suse_version} > 1500
Requires:       gcc-c++
%else
Requires:       gcc13-c++
Requires:       gcc13-PIE
%endif
# kf6-extra-cmake-modules is used to build both kf5 and kf6 based packages
# it has to require the resp. -filesystem package
Requires:       kf5-filesystem
Requires:       kf6-filesystem
Recommends:     kf6-extra-cmake-modules-doc
Provides:       extra-cmake-modules = %{version}
Obsoletes:      extra-cmake-modules < %{version}
%else
BuildRequires:  python3-Sphinx
Provides:       extra-cmake-modules-doc = %{version}
Obsoletes:      extra-cmake-modules-doc < %{version}
%endif
BuildArch:      noarch

%description
Extra modules and scripts for CMake.
%if "%{flavor}" == "doc"

This package provides documentation for kf6-extra-cmake-modules
%endif

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%if "%{flavor}" == "doc"
rm -r %{buildroot}%{_datadir}/ECM
%endif

%files
%if "%{flavor}" != "doc"
%license LICENSES/*
%{_datadir}/ECM/
%else
%doc %{_datadir}/doc/ECM/
%doc %lang(en) %{_mandir}/man7/ecm*.7*
%endif

%changelog
