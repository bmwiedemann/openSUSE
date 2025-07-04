#
# spec file for package python-outcome
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-outcome
Version:        1.3.0.post0
Release:        0
Summary:        Function for capturing the outcome of Python function calls
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/outcome
Source:         https://github.com/python-trio/outcome/archive/v%{version}.tar.gz#/outcome-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module pytest}
%if 0%{?suse_version} >= 1550 || (0%{?suse_version} == 1500 && 0%{?sle_version} >= 150400)
# for more than one python 3 flavor, but no python2 flavor
BuildRequires:  %{python_module pytest-asyncio}
%else
BuildRequires:  python3-pytest-asyncio
%endif
# /SECTION
%python_subpackages

%description
Outcome provides a function for capturing the outcome of a Python
function call, so that it can be passed around.

%prep
%setup -q -n outcome-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/outcome
%{python_sitelib}/outcome-%{version}*-info

%changelog
