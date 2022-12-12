#
# spec file for package extra-cmake-modules
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%global pkg_suffix -doc
%endif

%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without doc
# Only needed for the package signature condition
%bcond_without released
Name:           extra-cmake-modules%{?pkg_suffix}
Version:        5.101.0
Release:        0
Summary:        CMake modules
License:        BSD-3-Clause
URL:            https://www.kde.org
Source:         extra-cmake-modules-%{version}.tar.xz
%if %{with released}
Source1:        extra-cmake-modules-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         bundle-lang.patch
BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
%if "%{flavor}" != "doc"
Requires:       cmake >= 3.16
Requires:       gcc-c++
Requires:       kf5-filesystem
Recommends:     extra-cmake-modules-doc
Provides:       kf5umbrella = 4.99.0
Obsoletes:      kf5umbrella < 4.99.0
%else
BuildRequires:  python3-Sphinx
%endif
BuildArch:      noarch

%description
Extra modules and scripts for CMake.
%if "%{flavor}" == "doc"

This package provides documentation for extra-cmake-modules
%endif

%prep
%autosetup -p1 -n extra-cmake-modules-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

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
