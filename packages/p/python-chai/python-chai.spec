#
# spec file for package python-chai
#
# Copyright (c) 2023 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-chai
Version:        1.1.2
Release:        0
Summary:        Mocking/stub framework for Python
License:        BSD-3-Clause
URL:            https://github.com/agoragames/chai
Source:         https://files.pythonhosted.org/packages/source/c/chai/chai-%{version}.tar.gz
# https://github.com/agoragames/chai/pull/37
Patch0:         0001-Fix-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Chai provides an API for mocking/stubbing Python
objects, patterned after the Mocha library for Ruby.

%prep
%setup -q -n chai-%{version}
rm -rf chai.egg-info
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -s tests/ -v

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
