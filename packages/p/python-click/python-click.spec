#
# spec file for package python-click
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


%define oldpython python
%define skip_python2 1
Name:           python-click
Version:        8.1.3
Release:        0
Summary:        A wrapper around optparse for command line utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitsuhiko/click
Source:         https://files.pythonhosted.org/packages/source/c/click/click-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if "%{python_flavor}" == "python36"
Requires:       python-importlib-metadata
%endif
%python_subpackages

%description
Click is a Python package for creating command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit". It is configurable, and comes with
defaults out of the box.

%prep
%setup -q -n click-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -rs --tb=short

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/click
%{python_sitelib}/click-%{version}-py%{python_version}.egg-info

%changelog
