#
# spec file for package python-pytest-subtests
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


Name:           python-pytest-subtests
Version:        0.9.0
Release:        0
Summary:        Python unittest subTest() support and subtests fixture
License:        MIT
URL:            https://github.com/pytest-dev/pytest-subtests
Source:         https://files.pythonhosted.org/packages/source/p/pytest-subtests/pytest-subtests-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 40.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7.0}
# /SECTION
%python_subpackages

%description
Python unittest subTest() support and subtests fixture.

%prep
%setup -q -n pytest-subtests-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pytest_subtests.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_subtests*.pyc
%{python_sitelib}/pytest_subtests-%{version}*-info

%changelog
