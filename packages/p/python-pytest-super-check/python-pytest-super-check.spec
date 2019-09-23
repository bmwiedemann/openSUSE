#
# spec file for package python-pytest-super-check
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
Name:           python-pytest-super-check
Version:        2.0.0
Release:        0
Summary:        Pytest plugin to check your TestCase classes call super in setUp, tearDown, etc
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/adamchainz/pytest-super-check
Source:         https://files.pythonhosted.org/packages/source/p/pytest-super-check/pytest-super-check-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-runner}
# /SECTION
%python_subpackages

%description
Pytest plugin to check your TestCase classes call super in setUp, tearDown, etc.

%prep
%setup -q -n pytest-super-check-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py pytest

%files %{python_files}
%doc README.rst HISTORY.rst
%license LICENSE
%{python_sitelib}/*

%changelog
