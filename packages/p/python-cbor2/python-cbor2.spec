#
# spec file for package python-cbor2
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-cbor2
Version:        5.4.6
Release:        0
Summary:        Pure Python CBOR (de)serializer with extensive tag support
License:        MIT
URL:            https://github.com/agronholm/cbor2
Source:         https://files.pythonhosted.org/packages/source/c/cbor2/cbor2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module setuptools_scm >= 6.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Pure Python CBOR (de)serializer with extensive tag support

%prep
%setup -q -n cbor2-%{version}
# Remove test dependency on pytest-cov
sed -i 's/--cov//' pyproject.toml

%build
export LANG=en_US.UTF8
%pyproject_wheel

%install
export LANG=en_US.UTF8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
