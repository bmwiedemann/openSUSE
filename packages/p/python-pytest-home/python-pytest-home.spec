#
# spec file for package python-pytest-home
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


Name:           python-pytest-home
Version:        0.5.1
Release:        0
Summary:        Home directory fixtures
License:        MIT
URL:            https://github.com/jaraco/pytest-home
Source:         https://files.pythonhosted.org/packages/source/p/pytest-home/pytest-home-0.5.1.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  git
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest
Suggests:       python-sphinx >= 3.5
Suggests:       python-sphinx < 7.2.5
Suggests:       python-jaraco.packaging >= 9.3
Suggests:       python-rst.linker >= 1.9
Suggests:       python-furo
Suggests:       python-sphinx-lint
Suggests:       python-pytest >= 6
Suggests:       python-pytest-checkdocs >= 2.4
Suggests:       python-pytest-cov
Suggests:       python-pytest-enabler >= 2.2
Suggests:       python-pytest-ruff
Suggests:       python-pytest-black >= 0.3.7
Suggests:       python-pytest-mypy >= 0.9.1
BuildArch:      noarch
%python_subpackages

%description
Home directory fixtures

%prep
%autosetup -p1 -n pytest-home-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=$(pwd)
%pytest

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/pytest_home
%{python_sitelib}/pytest_home-%{version}.dist-info

%changelog
