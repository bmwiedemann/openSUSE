#
# spec file for package trytond_country
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2014-2025 Dr. Axel Braun
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


%if 0%{?suse_version} >= 1550
%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define mysitelib %{expand:%%%{mypython}_sitelib}
%endif

%define majorver 7.0
Name:           trytond_country
Version:        %{majorver}.0
Release:        0
Summary:        The "country" module for the Tryton ERP system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
# List of additional build dependencies
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros
Requires:       %{mypython}-pycountry
Requires:       proteus
Requires:       trytond
BuildArch:      noarch

%description
The country module defines the concepts of country and subdivision in
the Tryton application platform. The module comes preloaded with the
ISO 3166 list of countries and subdivisions thanks to the pycountry
module.

%prep
%setup -q
# TW uses newer pycountry
## %if 0%{?suse_version} > 1500
## %patch -P 0 -P 1 -P 2 -p1
## %endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{mysitelib}

%files
%defattr(-,root,root)
%attr(755,root,tryton) %{_bindir}/trytond_import*
%{mysitelib}/tryton*

%changelog
