#
# spec file for package python-xmlschema
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
Name:           python-xmlschema
Version:        1.0.14
Release:        0
Summary:        An XML Schema validator and decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/brunato/xmlschema
Source:         https://files.pythonhosted.org/packages/source/x/xmlschema/xmlschema-%{version}.tar.gz
BuildRequires:  %{python_module elementpath >= 1.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-elementpath >= 1.2.0
BuildArch:      noarch
%python_subpackages

%description
The *xmlschema* library is an implementation of `XML Schema <http://www.w3.org/2001/XMLSchema>`_
for Python (supports Python 2.7 and Python 3.5+).

%prep
%setup -q -n xmlschema-%{version}
# do not hardcode versions
sed -i -e 's:~=:>=:' setup.py
# do not bother with memory validation
rm xmlschema/tests/check_memory.py
rm xmlschema/tests/test_memory.py

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/xmlschema/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
