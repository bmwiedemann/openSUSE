#
# spec file for package python-xmlschema
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
Name:           python-xmlschema
Version:        1.1.2
Release:        0
Summary:        An XML Schema validator and decoder
License:        MIT
URL:            https://github.com/brunato/xmlschema
Source:         https://files.pythonhosted.org/packages/source/x/xmlschema/xmlschema-%{version}.tar.gz
BuildRequires:  %{python_module elementpath >= 1.4.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-elementpath >= 1.4.0
Requires:       python-lxml
BuildArch:      noarch
%python_subpackages

%description
The *xmlschema* library is an implementation of `XML Schema <http://www.w3.org/2001/XMLSchema>`_
for Python.

%prep
%setup -q -n xmlschema-%{version}
# do not hardcode versions
sed -i -e 's:~=:>=:' setup.py
# do not bother with memory validation
rm tests/check_memory.py
rm tests/test_memory.py

%build
export LANG="en_US.UTF8"
%python_build

%install
export LANG="en_US.UTF8"
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_element_tree_import_script is (easily workaroundable) https://github.com/sissaschool/xmlschema/issues/167
# tests_factory setup is broken
export LANG="en_US.UTF8"
%pytest -k "not (test_element_tree_import_script or tests_factory)" tests

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
