#
# spec file for package python-glob2
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
Name:           python-glob2
Version:        0.7
Release:        0
Summary:        Glob module recursive wildcards support
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/glob2
Source:         https://files.pythonhosted.org/packages/source/g/glob2/glob2-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
This module provides an extended version of Python's builtin glob
module with the following additions:

- The ability to capture the text matched by glob patterns, and
  return those matches alongside the filenames.
- A recursive '**' globbing syntax, akin for example to the globstar
  option of the bash shell.
- The ability to replace the filesystem functions used, in order to
  glob on virtual filesystems.

%prep
%setup -q -n glob2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py nosetests

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES
%{python_sitelib}/*

%changelog
