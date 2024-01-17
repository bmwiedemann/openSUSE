#
# spec file for package python-pytest-percent
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
Name:           python-pytest-percent
Version:        0.1.2
Release:        0
Summary:        Pytest plugin to exit successfully when a required percent of tests pass
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dillonm197/pytest.percent
Source:         https://files.pythonhosted.org/packages/source/p/pytest-percent/pytest-percent-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/dillonm197/pytest.percent/master/tests/test_percent.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 5.2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 5.2.0}
# /SECTION
%python_subpackages

%description
Change the exit code of pytest test sessions when a required percent of tests pass.

%prep
%setup -q -n pytest-percent-%{version}
cp %{SOURCE1} .
printf "[pytest]\naddopts = --required-percent=80" > pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
