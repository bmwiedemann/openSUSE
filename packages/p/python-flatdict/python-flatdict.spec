#
# spec file for package python-flatdict
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


%{?sle15allpythons}
Name:           python-flatdict
Version:        4.0.1
Release:        0
Summary:        Python module for interacting with nested dicts
License:        BSD-3-Clause
URL:            https://github.com/gmr/flatdict
Source:         https://github.com/gmr/flatdict/archive/%{version}.tar.gz#/flatdict-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python module for interacting with nested dicts as a single level dict with delimited keys.

%prep
%setup -q -n flatdict-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/flatdict.py
%{python_sitelib}/flatdict-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/flatdict*

%changelog
