#
# spec file for package python-httptools
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-httptools
Version:        0.6.1
Release:        0
Summary:        Python framework independent HTTP protocol utils
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/MagicStack/httptools
Source0:        https://github.com/MagicStack/httptools/archive/v%{version}.tar.gz#/httptools-%{version}.tar.gz
Source1:        https://github.com/nodejs/llhttp/archive/refs/tags/release/v6.0.6.tar.gz#/llhttp-release-v6.0.6.tar.gz
Source2:        https://github.com/nodejs/http-parser/archive/refs/tags/v2.9.4.tar.gz#/http-parser-2.9.4.tar.gz
# BuildRequires:  %{python_module Cython >= 0.29.24 with %python-Cython < 3}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
httptools is a Python binding for the nodejs HTTP parser.

%prep
%setup -q -n httptools-%{version}
rm -df vendor/llhttp/
tar -xzf '%{SOURCE1}' -C vendor
mv vendor/llhttp-release*/ vendor/llhttp/
rm -df vendor/http-parser/
tar -xzf '%{SOURCE2}' -C vendor
mv vendor/http-parser*/ vendor/http-parser/

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%if 0%{suse_version} >= 1550
# pytest on suse <= 15.4 does not support the required pytest importlib import mode
%pytest_arch -k 'not test_parser_response_1'
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/httptools
%{python_sitearch}/httptools-%{version}.dist-info

%changelog
