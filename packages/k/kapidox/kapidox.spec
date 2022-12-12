#
# spec file for package kapidox
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


# Only needed for the package signature condition
%bcond_without released
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
Name:           kapidox
Version:        5.101.0
Release:        0
Summary:        Scripts and data for building API documentation
License:        BSD-2-Clause
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-broken-installation.patch
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-setuptools
Requires:       doxygen
Requires:       graphviz
Requires:       graphviz-gd
Requires:       libqt5-qttools
Requires:       python3-Jinja2
Requires:       python3-xml
Recommends:     python3-PyYAML
BuildArch:      noarch

%description
The kapidox framework enables the generation of API documentation from
Doxygen-formatted codde comments in a standard format and style.

%prep
%autosetup -p1

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_kf5_prefix} --root=%{buildroot}
%fdupes -s %{buildroot}

%files
%license LICENSES/*
%doc README*
%{_kf5_bindir}/depdiagram_generate_all
%{_kf5_bindir}/kapidox-depdiagram-generate
%{_kf5_bindir}/kapidox-depdiagram-prepare
%{_kf5_bindir}/kapidox-generate
%{python3_sitelib}/kapidox/
%{python3_sitelib}/kapidox-*.egg-info

%changelog
