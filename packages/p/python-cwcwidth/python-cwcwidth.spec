#
# spec file for package python-cwcwidth
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-cwcwidth
Version:        0.1.8
Release:        0
Summary:        Python bindings for wc(s)width
License:        MIT
URL:            https://github.com/sebastinas/cwcwidth
Source:         https://files.pythonhosted.org/packages/source/c/cwcwidth/cwcwidth-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for wc(s)width

%prep
%setup -q -n cwcwidth-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitearch}/*

%changelog
