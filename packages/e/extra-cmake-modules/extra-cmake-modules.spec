#
# spec file for package extra-cmake-modules
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


%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%if 0%{?suse_version} >= 1330
%bcond_without doc
%else
%bcond_with doc
%endif
# Only needed for the package signature condition
%bcond_without lang
Name:           extra-cmake-modules
Version:        5.75.0
Release:        0
Summary:        CMake modules
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         bundle-lang.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
Requires:       cmake >= 3.5
Requires:       gcc-c++
Requires:       kf5-filesystem
Recommends:     %{name}-doc
Provides:       kf5umbrella = 4.99.0
Obsoletes:      kf5umbrella < 4.99.0
%if %{with doc}
BuildRequires:  python3-Sphinx
%endif

%description
Extra modules and scripts for CMake.

For more information see https://community.kde.org/KDE_Core/Platform_11/Buildsystem/FindFilesSurvey

%package doc
Summary:        Documentation for extra-cmake-modules
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Extra modules and scripts for CMake.

For more information see https://community.kde.org/KDE_Core/Platform_11/Buildsystem/FindFilesSurvey
This package provides documentation for extra-cmake-modules

%prep
%setup -q
%patch0 -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license LICENSES/*
%{_datadir}/ECM/

%if %{with doc}
%files doc
%doc %{_datadir}/doc/ECM/
%doc %lang(en) %{_mandir}/man7/ecm*.7*
%endif

%changelog
