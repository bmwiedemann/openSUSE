#
# spec file for package python-PyHamcrest
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


%{?sle15_python_module_pythons}
Name:           python-PyHamcrest
Version:        2.1.0
Release:        0
Summary:        Hamcrest framework for matcher objects
License:        BSD-3-Clause
URL:            https://github.com/hamcrest/PyHamcrest
Source:         https://files.pythonhosted.org/packages/source/p/pyhamcrest/pyhamcrest-%{version}.tar.gz
Patch0:         0001-Add-boolean-matchers.patch
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hypothesis >= 1.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-hamcrest = %{version}
Obsoletes:      python-hamcrest < %{version}
BuildArch:      noarch
%python_subpackages

%description
Hamcrest framework for matcher objects.
PyHamcrest is a framework for writing matcher objects,
allowing you to declaratively define “match” rules.

%prep
%setup -q -n pyhamcrest-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/hamcrest

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/hamcrest
%{python_sitelib}/pyhamcrest-%{version}.dist-info

%changelog
