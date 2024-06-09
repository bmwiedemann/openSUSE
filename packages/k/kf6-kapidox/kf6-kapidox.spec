#
# spec file for package kf6-kapidox
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


%define rname kapidox
%bcond_without released
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
Name:           kf6-kapidox
Version:        6.3.0
Release:        0
Summary:        Scripts and data for building API documentation
License:        BSD-2-Clause
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-broken-installation.patch
BuildRequires:  fdupes
BuildRequires:  kf6-filesystem
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-setuptools
Requires:       doxygen
Requires:       graphviz
Requires:       graphviz-gd
Requires:       python3-Jinja2
Requires:       python3-xml
Requires:       qt6-tools
Recommends:     python3-PyYAML
Conflicts:      kapidox
BuildArch:      noarch

%description
The kapidox framework enables the generation of API documentation from
Doxygen-formatted codde comments in a standard format and style.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_kf6_prefix} --root=%{buildroot}
%fdupes -s %{buildroot}

%files
%license LICENSES/*
%doc README*
%{_kf6_bindir}/depdiagram_generate_all
%{_kf6_bindir}/kapidox-depdiagram-generate
%{_kf6_bindir}/kapidox-depdiagram-prepare
%{_kf6_bindir}/kapidox-generate
%{python3_sitelib}/kapidox/
%{python3_sitelib}/kapidox-*.egg-info

%changelog
