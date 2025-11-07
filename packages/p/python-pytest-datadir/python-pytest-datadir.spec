#
# spec file for package python-pytest-datadir
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
Name:           python-pytest-datadir
Version:        1.8.0
Release:        0
Summary:        Plugin for test data directories and files
License:        MIT
URL:            https://github.com/gabrielcnr/pytest-datadir
Source:         https://files.pythonhosted.org/packages/source/p/pytest-datadir/pytest_datadir-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest >= 7.0}
# /SECTION
%python_subpackages

%description
pytest plugin for test data directories and files.

%prep
%setup -q -n pytest_datadir-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.md
%license LICENSE
%{python_sitelib}/pytest_datadir
%{python_sitelib}/pytest_datadir-%{version}.dist-info

%changelog
