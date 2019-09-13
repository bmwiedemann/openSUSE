#
# spec file for package python-bz2file
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python3 1
Name:           python-bz2file
Version:        0.98
Release:        0
Summary:        Python module to read and write bzip2-compressed files
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nvawda/bz2file
Source:         https://files.pythonhosted.org/packages/source/b/bz2file/bz2file-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
# devel contains a test module, nothing to do with architecture
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-devel
BuildArch:      noarch
%python_subpackages

%description
Bz2file is a Python library for reading and writing bzip2-compressed files.

It contains a drop-in replacement for the file interface in the standard
library's bz2 module, including features from the latest development
version of CPython that are not available in older releases.

%prep
%setup -q -n bz2file-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_bz2file.py

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
