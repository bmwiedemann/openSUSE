#
# spec file for package python-mccabe
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-mccabe
Version:        0.6.1
Release:        0
Summary:        McCabe checker, plugin for flake8
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/flintwork/mccabe
Source:         https://files.pythonhosted.org/packages/source/m/mccabe/mccabe-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Ned's script to check McCabe complexity.
This module provides a plugin for flake8, the Python code checker.

%prep
%setup -q -n mccabe-%{version}
# do not require pytest-runner for setup
sed -i 's:pytest-runner::' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
