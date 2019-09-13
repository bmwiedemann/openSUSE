#
# spec file for package python-lz4
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
Name:           python-lz4
Version:        2.1.10
Release:        0
Summary:        LZ4 Bindings for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-lz4/python-lz4
Source:         https://files.pythonhosted.org/packages/source/l/lz4/lz4-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-future
Requires:       python-psutil
%ifpython2
Requires:       python2-future
%endif
%python_subpackages

%description
This package provides python bindings for the lz4 compression library.

%prep
%setup -q -n lz4-%{version}
# do not set -O3
sed -i -e '/-O3/d' setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# tests get stuck
#%%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/lz4/
%{python_sitearch}/lz4-%{version}-py*.egg-info/

%changelog
