#
# spec file for package python-cPyparsing
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
Name:           python-cPyparsing
Version:        2.4.0.1.0.0
Release:        0
Summary:        Cython implementation of PyParsing
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/evhub/cpyparsing
Source:         https://files.pythonhosted.org/packages/source/c/cPyparsing/cPyparsing-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Cython implementation of PyParsing created for use in Coconut and Undebt.

%prep
%setup -q -n cPyparsing-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/*

%changelog
