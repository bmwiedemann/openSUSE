#
# spec file for package python-cliff
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


Name:           python-cliff
Version:        4.7.0
Release:        0
Summary:        Command Line Interface Formulation Framework
License:        Apache-2.0
URL:            https://docs.openstack.org/cliff/latest/
Source:         https://files.pythonhosted.org/packages/source/c/cliff/cliff-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module autopage >= 0.4.0}
BuildRequires:  %{python_module PrettyTable >= 0.7.2}
BuildRequires:  %{python_module PyYAML >= 3.12}
BuildRequires:  %{python_module Sphinx >= 2.0.0}
BuildRequires:  %{python_module cmd2 >= 1.0.0}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module importlib_metadata >= 4.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module stevedore >= 2.0.1}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools >= 2.2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-PyYAML >= 3.12
Requires:       python-autopage >= 0.4.0
Requires:       python-cmd2 >= 1.0.0
Requires:       python-importlib_metadata >= 4.4
Requires:       python-stevedore >= 2.0.1
BuildArch:      noarch
%python_subpackages

%description
Command Line Interface Formulation Framework

%prep
%autosetup -p1 -n cliff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# doesn't work with pytest atm
rm -v cliff/tests/test_commandmanager.py
%pytest cliff/tests

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/cliff
%{python_sitelib}/cliff-%{version}.dist-info

%changelog
