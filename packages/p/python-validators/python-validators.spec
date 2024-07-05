#
# spec file for package python-validators
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
Name:           python-validators
Version:        0.30.0
Release:        0
Summary:        Python Data Validation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kvesteri/validators
Source:         https://files.pythonhosted.org/packages/source/v/validators/validators-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python Data Validation for Humans.

%prep
%setup -q -n validators-%{version}
dos2unix README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# missing eth-hash dependency so those tests must be skipped
%pytest -k 'not test_returns_true_on_valid_eth_address and not test_returns_failed_validation_on_invalid_eth_address'

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/validators*

%changelog
