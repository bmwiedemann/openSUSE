#
# spec file for package python-geolinks
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


%bcond_without libalternatives
Name:           python-geolinks
Version:        0.2.3
Release:        0
Summary:        Utilities to deal with geospatial links
License:        MIT
URL:            https://github.com/geopython/geolinks
# The PyPI sdist ships no tests, hence the tag archive.
Source:         https://github.com/geopython/geolinks/archive/%{version}.tar.gz#/geolinks-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-click
BuildArch:      noarch
%python_subpackages

%description
Python implementation of Cat-Interop utilities for geospatial links.

%prep
%autosetup -n geolinks-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/geolinks
%python_group_libalternatives geolinks
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/run_tests.py

%pre
%python_libalternatives_reset_alternative geolinks

%files %{python_files}
%license LICENSE.md
%doc README.md
%python_alternative %{_bindir}/geolinks
%{python_sitelib}/geolinks
%{python_sitelib}/geolinks-%{version}.dist-info

%changelog
