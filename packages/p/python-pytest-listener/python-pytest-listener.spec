#
# spec file for package python-pytest-listener
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pytest-listener
Version:        1.7.0
Release:        0
Summary:        A simple network listener for py.test
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-listener/pytest-listener-%{version}.tar.gz
# https://github.com/man-group/pytest-plugins/issues/209
Patch0:         python-pytest-listener-no-six.patch
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest-server-fixtures
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-server-fixtures}
# /SECTION
%python_subpackages

%description
Simple JSON listener using TCP that listens for data and stores it in a queue for later retrieval.

%prep
%autosetup -p1 -n pytest-listener-%{version}
# required to find the one file in the topdir
sed -i "/packages=find_packages/ a \        py_modules=['pytest_listener']," setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/pytest_listener.py*
%{python_sitelib}/pytest_listener-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/pytest_listener*.pyc

%changelog
