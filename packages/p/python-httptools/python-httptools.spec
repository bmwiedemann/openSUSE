#
# spec file for package python-httptools
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-httptools
Version:        0.1.1
Release:        0
Summary:        Python framework independent HTTP protocol utils
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/MagicStack/httptools
Source:         https://github.com/MagicStack/httptools/archive/v%{version}.tar.gz#/httptools-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  http-parser-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
httptools is a Python binding for the nodejs HTTP parser.

%prep
%setup -q -n httptools-%{version}
# unpin Cython
sed -i 's/Cython==/Cython>=/' setup.py
cp %{_includedir}/http_parser.h vendor/http-parser/

%build
%python_build build_ext --use-system-http-parser

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitearch}/httptools/parser/parser.c
%fdupes %{buildroot}%{$python_sitearch}
}

%check
mv httptools .httptools
%pytest_arch -k 'not (test_parser_response_1 or test_parser_url_2)'
mv .httptools httptools

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/*

%changelog
