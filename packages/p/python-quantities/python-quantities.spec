#
# spec file for package python-quantities
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


Name:           python-quantities
Version:        0.16.1
Release:        0
Summary:        Package for physical quantities with units
License:        BSD-3-Clause
URL:            https://github.com/python-quantities/python-quantities/
Source:         https://files.pythonhosted.org/packages/source/q/quantities/quantities-%{version}.tar.gz
Patch0:         reproducible.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module numpy >= 1.22}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.22
BuildArch:      noarch
%python_subpackages

%description
Support for physical quantities with units, based on numpy.

%prep
%autosetup -p1 -n quantities-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv quantities .quantities
%pytest -v --pyargs quantities.tests
mv .quantities quantities

%files %{python_files}
%doc CHANGES.txt README.rst
%license doc/user/license.rst
%{python_sitelib}/quantities
%{python_sitelib}/quantities-%{version}.dist-info

%changelog
