#
# spec file for package python-pytest-testconfig
#
# Copyright (c) 2019 SUSE LLC.
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
Name:           python-pytest-testconfig
Version:        0.1.3
Release:        0
Summary:        Test configuration plugin for pytest
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/wojole/pytest-testconfig
Source:         https://github.com/wojole/pytest-testconfig/archive/v%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tox}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.5
Recommends:     python-PyYAML
BuildArch:      noarch
%python_subpackages

%description
pytest-testconfig is a plugin to the pytest test framework used for passing test-specific (or test-run specific) configuration data
to the tests being executed.

%prep
%setup -q -n pytest-testconfig-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
