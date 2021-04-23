#
# spec file for package python-sphinxcontrib-trio
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sphinxcontrib-trio
Version:        1.1.2
Release:        0
Summary:        Sphinx extension for documenting Python functions and methods
License:        MIT OR Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/sphinxcontrib-trio
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-trio/sphinxcontrib-trio-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 1.7}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module cssselect}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 >= 1.21.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.6
BuildArch:      noarch
%python_subpackages

%description
This sphinx extension helps documenting Python code that uses
async/await, or abstract methods, or context managers, or generators.
It works by making sphinx's regular directives
for documenting Python functions and methods smarter.

%prep
%setup -q -n sphinxcontrib-trio-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%{python_sitelib}/sphinxcontrib_trio
%{python_sitelib}/sphinxcontrib_trio-%{version}-*.egg-info

%changelog
