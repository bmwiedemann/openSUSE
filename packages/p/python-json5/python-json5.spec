#
# spec file for package python-json5
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
Name:           python-json5
Version:        0.8.5
Release:        0
License:        Apache-2.0
Summary:        A Python implementation of the JSON5 data format
Url:            https://github.com/dpranke/pyjson5
Group:          Development/Languages/Python
Source:         https://github.com/dpranke/pyjson5/archive/v%{version}.tar.gz#/pyjson5-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A Python implementation of the JSON5 data format.

JSON5 extends the JSON data interchange format to make it
slightly more usable as a configuration language:

  * JavaScript-style comments (both single and multi-line) are legal.
  * Object keys may be unquoted if they are legal ECMAScript identifiers
  * Objects and arrays may end with trailing commas.
  * Strings can be single-quoted, and multi-line string literals are allowed.


%prep
%setup -q -n pyjson5-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/pyjson5
%{python_sitelib}/*

%changelog
