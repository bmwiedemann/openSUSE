#
# spec file for package python-quantities
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-quantities
Version:        0.12.4
Release:        0
Summary:        Package for physical quantities with units
License:        BSD-3-Clause
URL:            https://github.com/python-quantities/python-quantities/
Source:         https://github.com/python-quantities/python-quantities/archive/v%{version}.tar.gz#/python-quantities-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.8.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.8.2
BuildArch:      noarch
%python_subpackages

%description
Support for physical quantities with units, based on numpy.

%prep
%autosetup -p1 -n python-quantities-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No longer fails https://github.com/python-quantities/python-quantities/issues/8
%pytest -k 'not test_fix'

%files %{python_files}
%doc CHANGES.txt README.rst
%license doc/user/license.rst
%{python_sitelib}/*

%changelog
