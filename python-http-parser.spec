#
# spec file for package python-http-parser
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


%{?sle15allpythons}
Name:           python-http-parser
Version:        0.9.0
Release:        0
Summary:        HTTP Request/Response Parser for Python in C
License:        MIT
URL:            https://github.com/benoitc/http-parser/
Source:         https://files.pythonhosted.org/packages/source/h/http-parser/http-parser-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#benoitc/http-parser#101
Patch0:         remove-imp-module.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
HTTP request/response parser for Python in C, based on
http-parser from Ryan Dahl.

%prep
%autosetup -p1 -n http-parser-%{version}

%build
# fix wrongly generated cyx files
find . -name '*.pyx' -exec cython {} \;
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
# Remove exec bits from example scripts
chmod a-x examples/*
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc NOTICE README.rst examples
%{python_sitearch}/http_parser
%{python_sitearch}/http_parser-%{version}.dist-info

%changelog
