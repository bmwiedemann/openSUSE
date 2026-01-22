#
# spec file for package python-agate-lookup
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_with     test
Name:           python-agate-lookup
Version:        0.3.4
Release:        0
License:        MIT
Summary:        Remote lookup tables for agate
URL:            http://agate-lookup.readthedocs.org/
Source:         https://github.com/wireservice/agate-lookup/archive/refs/tags/%{version}.tar.gz#/agate-lookup-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.9.1}
# /SECTION
Requires:       python-agate >= 1.5.0
Requires:       python-PyYAML >= 3.11
Requires:       python-requests >= 2.9.1
BuildArch:      noarch

%python_subpackages

%description
Agate-lookup adds one-line access to lookup tables to agate.

%prep
%setup -q -n agate-lookup-%{version}
sed -i -e '/^#!\//, 1d' agatelookup/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# online tests
#%%pytest

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/agatelookup
%{python_sitelib}/agate_lookup-%{version}.dist-info

%changelog
