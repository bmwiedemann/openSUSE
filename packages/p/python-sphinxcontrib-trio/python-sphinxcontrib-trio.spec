#
# spec file for package python-sphinxcontrib-trio
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


Name:           python-sphinxcontrib-trio
Version:        1.2.0
Release:        0
Summary:        Sphinx extension for documenting Python functions and methods
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/sphinxcontrib-trio
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-trio/sphinxcontrib_trio-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 2.2}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module cssselect}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 >= 1.21.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 2.2
BuildArch:      noarch
%python_subpackages

%description
This sphinx extension helps documenting Python code that uses
async/await, or abstract methods, or context managers, or generators.
It works by making sphinx's regular directives
for documenting Python functions and methods smarter.

%prep
%autosetup -p1 -n sphinxcontrib_trio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#python-trio/sphinxcontrib-trio#260
%pytest -k 'not test_end_to_end' tests

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%{python_sitelib}/sphinxcontrib_trio
%{python_sitelib}/sphinxcontrib_trio-%{version}*-info

%changelog
