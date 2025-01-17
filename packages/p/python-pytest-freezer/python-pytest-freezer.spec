#
# spec file for package python-pytest-freezer
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


Name:           python-pytest-freezer
Version:        0.4.9
Release:        0
Summary:        Pytest plugin providing a fixture interface for spulec/freezegun
License:        MIT
URL:            https://github.com/pytest-dev/pytest-freezer
Source:         https://files.pythonhosted.org/packages/source/p/pytest-freezer/pytest_freezer-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module freezegun >= 1.1}
BuildRequires:  %{python_module pytest >= 3.6}
# /SECTION
BuildRequires:  fdupes
Requires:       python-freezegun >= 1.1
Requires:       python-pytest >= 3.6
BuildArch:      noarch
%python_subpackages

%description
Pytest plugin providing a fixture interface for freezegun.
The fixture name is freezer. It is a freezegun.api.FrozenDateTimeFactory
instance.

%prep
%autosetup -p1 -n pytest_freezer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_freezer.py
%pycache_only %{python_sitelib}/__pycache__/pytest_freezer*.pyc
%{python_sitelib}/pytest_freezer-%{version}.dist-info

%changelog
