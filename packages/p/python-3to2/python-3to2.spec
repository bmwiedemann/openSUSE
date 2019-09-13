#
# spec file for package python-3to2
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
Name:           python-3to2
Version:        1.1.1
Release:        0
Summary:        Tool to refactor Python 3.x syntax into 2.7 syntax
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://bitbucket.org/amentajo/lib3to2
Source:         https://files.pythonhosted.org/packages/source/3/3to2/3to2-%{version}.zip
Source1:        https://bitbucket.org/amentajo/lib3to2/raw/0f0c4b993212207473596fb064e7c33f5cc7bca0/LICENSE
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch

%python_subpackages

%description
3to2 is a set of fixers that are intended to backport code written for
Python version 3.x into Python version 2.x.  The final target 2.x version is
the latest version of the 2.7 branch, as that is the last release in the Python
2.x branch.

%prep
%setup -q -n 3to2-%{version}
cp %SOURCE1 .
sed -i 's/\r$//' README

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Issue with test reported https://bitbucket.org/amentajo/lib3to2/issues/53
%python_exec -m nose lib3to2/tests -e test_argument_unpacking

%files %{python_files}
%doc README
%license LICENSE
%python3_only %{_bindir}/3to2
%{python_sitelib}/*

%changelog
