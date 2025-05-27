#
# spec file for package python-fusepy
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


Name:           python-fusepy
Version:        3.0.1
Release:        0
Summary:        A python module that provides a simple interface to FUSE
License:        ISC
URL:            https://github.com/fusepy/fusepy
Source:         https://files.pythonhosted.org/packages/source/f/fusepy/fusepy-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/fusepy/fusepy/refs/heads/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  libfuse2
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
# this is not really fuse3 compatible
Requires:       libfuse2
# both projects use the same python package name
Conflicts:      python-fuse
# fusepy interfaces via ctypes to libfuse, so no arch dependent elements
# should be in the package
BuildArch:      noarch
%python_subpackages

%description
fusepy is a Python module that provides a simple interface to FUSE. It makes
the implementation of userspace file systems based on FUSE and python
possible.

%prep
%setup -q -n fusepy-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

%check
# no upstream tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/fuse.py
%{python_sitelib}/fusepy-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/fuse*

%changelog
