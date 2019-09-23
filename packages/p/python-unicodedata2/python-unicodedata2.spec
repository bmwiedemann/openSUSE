#
# spec file for package python-unicodedata2
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-unicodedata2
Version:        12.0.0
Release:        0
License:        Apache-2.0 and Python-2.0
Summary:        Python unicodedata backport
Url:            http://github.com/mikekap/unicodedata2
Group:          Development/Languages/Python
Source:         https://github.com/mikekap/unicodedata2/archive/12.0.0.tar.gz#/unicodedata2-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes

%python_subpackages

%description
Unicodedata backport for python 2/3 updated to the latest unicode version.

%prep
%setup -q -n unicodedata2-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/*

%changelog
