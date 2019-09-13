#
# spec file for package python-zstandard
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
Name:           python-zstandard
Version:        0.11.1
Release:        0
Summary:        Zstandard bindings for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/indygreg/python-zstandard
Source:         https://files.pythonhosted.org/packages/source/z/zstandard/zstandard-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libzstd-devel
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
Requires:       python-cffi >= 1.11
Requires:       zstd
Conflicts:      python-zstd
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 1.11}
BuildRequires:  %{python_module nose}
# /SECTION
%python_subpackages

%description
Zstandard bindings for Python

%prep
%setup -q -n zstandard-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir tester
cp -r tests tester/
pushd tester
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
export PYTHONDONTWRITEBYTECODE=1
rm -rf build _build*
nosetests-%{$python_bin_suffix} -v
}
popd

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
