#
# spec file for package python-pytest-openfiles
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pytest-openfiles
Version:        0.5.0
Release:        0
Summary:        Pytest plugin for detecting inadvertent open file handles
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/astropy/pytest-openfiles
Source:         https://files.pythonhosted.org/packages/source/p/pytest-openfiles/pytest-openfiles-%{version}.tar.gz
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-psutil
Requires:       python-pytest >= 4.6
BuildArch:      noarch
%python_subpackages

%description
This package provides a plugin for the pytest framework that allows
developers to detect whether any file handles or other file-like objects were
inadvertently left open at the end of a unit test.

%prep
%setup -q -n pytest-openfiles-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# do not override pytest config
rm setup.cfg
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pytest_openfiles
%{python_sitelib}/pytest_openfiles-%{version}-py*.egg-info

%changelog
