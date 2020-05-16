#
# spec file for package python-pytest-flake8dir
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
%define skip_python2 1
Name:           python-pytest-flake8dir
Version:        2.2.0
Release:        0
Summary:        A pytest fixture for testing flake8 plugins
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/adamchainz/pytest-flake8dir
Source:         https://github.com/adamchainz/pytest-flake8dir/archive/%{version}.tar.gz
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
A pytest fixture for testing flake8 plugins.

%prep
%setup -q -n pytest-flake8dir-%{version}
# fix gh#adamchainz/pytest-flake8dir#126
sed -i '107 d' tests/test_pytest_flake8dir.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc HISTORY.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
