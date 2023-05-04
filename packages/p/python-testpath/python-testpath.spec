#
# spec file for package python-testpath
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-testpath
Version:        0.6.0
Release:        0
Summary:        Test utilities for code working with files and commands
License:        BSD-3-Clause OR LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/testpath
Source0:        https://files.pythonhosted.org/packages/source/t/testpath/testpath-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Testpath is a collection of utilities for Python code working with
files and commands.

It contains functions to check things on the filesystem, and tools
for mocking system commands and recording calls to those.

%prep
%setup -q -n testpath-%{version}

rm testpath/*.exe

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/testpath/
%{python_sitelib}/testpath-%{version}*-info

%changelog
