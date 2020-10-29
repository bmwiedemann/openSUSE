#
# spec file for package python-elementpath
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
Name:           python-elementpath
Version:        2.0.3
Release:        0
Summary:        XPath 1.0/20 parsers and selectors for ElementTree and lxml
License:        MIT
URL:            https://github.com/sissaschool/elementpath
Source:         https://github.com/sissaschool/elementpath/archive/v%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The proposal of this package is to provide XPath 1.0 and 2.0 selectors for Python's ElementTree XML
data structures, both for the standard ElementTree library and for the
`lxml.etree <http://lxml.de>`_ library.

%prep
%setup -q -n elementpath-%{version}
# avoid cycle between us and xmlschema
rm tests/test_schema_proxy.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_compare_strings_function depends on LOCALE to produce proper results
# test_hashing is arch specific and overflows on 32bit platforms
%pytest -k 'not test_compare_strings_function and not test_hashing'

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
