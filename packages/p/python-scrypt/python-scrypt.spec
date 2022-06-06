#
# spec file for package python-scrypt
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-scrypt
Version:        0.8.20
Release:        0
Summary:        Bindings for scrypt
License:        BSD-2-Clause
URL:            https://github.com/holgern/py-scrypt
Source0:        https://files.pythonhosted.org/packages/source/s/scrypt/scrypt-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(openssl)
%python_subpackages

%description
Bindings for the scrypt key derivation function library.

%prep
%setup -q -n scrypt-%{version}
dos2unix -R README.rst scrypt/*.py
sed -i '1{/^#!/ d}' scrypt/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -s scrypt/tests -v

%files %{python_files}
%doc README.rst
%license LICENSE
%pycache_only %{python_sitearch}/scrypt/__pycache__
%{python_sitearch}/_scrypt*.so
%{python_sitearch}/scrypt/
%{python_sitearch}/scrypt-%{version}-py%{python_version}.egg-info

%changelog
