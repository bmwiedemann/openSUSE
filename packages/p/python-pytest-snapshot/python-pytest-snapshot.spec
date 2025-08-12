#
# spec file for package python-pytest-snapshot
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


Name:           python-pytest-snapshot
Version:        0.9.0
Release:        0
Summary:        A plugin for snapshot testing with pytest
License:        MIT
URL:            https://github.com/joseph-roitman/pytest-snapshot
Source:         https://files.pythonhosted.org/packages/source/p/pytest-snapshot/pytest-snapshot-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.0.0
BuildArch:      noarch
%python_subpackages

%description
A plugin for snapshot testing with pytest.

%prep
%autosetup -p1 -n pytest-snapshot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_assert_match_failure_bytes'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_snapshot
%{python_sitelib}/pytest_snapshot-%{version}.dist-info

%changelog
