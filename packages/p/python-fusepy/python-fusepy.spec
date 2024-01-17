#
# spec file for package python-fusepy
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
Name:           python-fusepy
Version:        3.0.1
Release:        0
Summary:        A python module that provides a simple interface to FUSE
License:        ISC
URL:            https://github.com/fusepy/fusepy
Source:         https://files.pythonhosted.org/packages/source/f/fusepy/fusepy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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

%build
%python_build

%install
%python_install

%check
# no upstream tests

%files %{python_files}
%{python_sitelib}/*
%doc README.rst

%changelog
