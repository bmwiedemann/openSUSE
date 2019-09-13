#
# spec file for package python-fb-re2
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
Name:           python-fb-re2
Version:        1.0.7
Release:        0
Summary:        Python wrapper for Google's RE2
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/facebook/pyre2
Source:         https://github.com/facebook/pyre2/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  re2-devel

%python_subpackages

%description
Python wrapper for Google's RE2

%prep
%setup -q -n pyre2-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
