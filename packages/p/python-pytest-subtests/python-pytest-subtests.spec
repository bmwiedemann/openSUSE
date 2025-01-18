#
# spec file for package python-pytest-subtests
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
Name:           python-pytest-subtests
Version:        0.14.1
Release:        0
Summary:        Python unittest subTest() support and subtests fixture
License:        MIT
URL:            https://github.com/pytest-dev/pytest-subtests
Source:         https://files.pythonhosted.org/packages/source/p/pytest-subtests/pytest_subtests-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python-pytest >= 7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7.0}
# /SECTION
%python_subpackages

%description
Python unittest subTest() support and subtests fixture.

%prep
%setup -q -n pytest_subtests-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pytest_subtests
%{python_sitelib}/pytest_subtests-%{version}.dist-info

%changelog
