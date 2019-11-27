#
# spec file for package python-flatdict
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-flatdict
Version:        3.4.0
Release:        0
Summary:        Python module for interacting with nested dicts
License:        BSD-3-Clause
URL:            https://github.com/gmr/flatdict
Source:         https://github.com/gmr/flatdict/archive/%{version}.tar.gz#/flatdict-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python module for interacting with nested dicts as a single level dict with delimited keys.

%prep
%setup -q -n flatdict-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
