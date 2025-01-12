#
# spec file for package python-click
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
Name:           python-click
Version:        8.1.8
Release:        0
Summary:        A wrapper around optparse for command line utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitsuhiko/click
Source:         https://files.pythonhosted.org/packages/source/c/click/click-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Click is a Python package for creating command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit". It is configurable, and comes with
defaults out of the box.

%prep
%autosetup -p1 -n click-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -rs --tb=short

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.md
%{python_sitelib}/click
%{python_sitelib}/click-%{version}.dist-info

%changelog
