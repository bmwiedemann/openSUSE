#
# spec file for package python-syrupy
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


%{?sle15_python_module_pythons}
Name:           python-syrupy
Version:        4.7.2
Release:        0
Summary:        Pytest Snapshot Test Utility
License:        Apache-2.0
URL:            https://github.com/tophat/syrupy
Source:         https://github.com/tophat/syrupy/archive/refs/tags/v%{version}.tar.gz#/syrupy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.4.0}
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  %{python_module pytest-benchmark >= 4.0.0}
BuildRequires:  %{python_module pytest-xdist >= 3.1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 7.0.0
BuildArch:      noarch
%python_subpackages

%description
Syrupy is a [pytest](https://docs.pytest.org/en/latest/) snapshot plugin. It enables developers to write tests which assert immutability of computed results.

The most popular snapshot test plugin compatible with pytest has some core limitations which this package attempts to address by upholding some key values:

- Extensible: If a particular data type is not supported, users should be able to easily and quickly add support.
- Idiomatic: Snapshot testing should fit naturally among other test cases in pytest, e.g. `assert x == snapshot` vs. `snapshot.assert_match(x)`.
- Soundness: Snapshot tests should uncover even the most minute issues. Unlike other snapshot libraries, Syrupy will fail a test suite if a snapshot does not exist, not just on snapshot differences.

%prep
%autosetup -p1 -n syrupy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_colors_off_does_not_call_colored - actually needs to access colored
%pytest -k "not test_colors_off_does_not_call_colored"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/syrupy
%{python_sitelib}/syrupy-%{version}.dist-info

%changelog
