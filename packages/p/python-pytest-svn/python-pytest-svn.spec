#
# spec file for package python-pytest-svn
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


Name:           python-pytest-svn
Version:        1.8.0
Release:        0
Summary:        SVN repository fixture for pytest
License:        MIT
URL:            https://github.com/man-group/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-svn/pytest-svn-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-pytest-shutil
Requires:       subversion
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-shutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  subversion
# /SECTION
%python_subpackages

%description
SVN repository fixture for py.test.

%prep
%setup -q -n pytest-svn-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/pytest_svn.py
%pycache_only %{python_sitelib}/__pycache__/pytest_svn*.pyc
%{python_sitelib}/pytest_svn-%{version}.dist-info

%changelog
