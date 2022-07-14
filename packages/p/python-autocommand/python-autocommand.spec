#
# spec file for package python-autocommand
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
Name:           python-autocommand
Version:        2.2.1
Release:        0
Summary:        A library to create a command-line program from a function
License:        LGPL-3.0
URL:            https://github.com/Lucretiel/autocommand
Source:         https://files.pythonhosted.org/packages/source/a/autocommand/autocommand-%{version}.tar.gz
# PATCH-FIX-UPSTREAM autocommand-fixtests.patch gh#Lucretiel/autocommand#20
Patch1:         https://github.com/Lucretiel/autocommand/commit/031c9750c74e3313b954b09e3027aaa6595649bb.patch#/autocommand-fixtests.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Autocommand turns a function into a command-line program. It converts the function's parameter
signature into command-line arguments, and automatically runs the function if the module was
called as __main__. In effect, it lets your create a smart main function.

%prep
%autosetup -p1 -n autocommand-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/autocommand
%{python_sitelib}/autocommand-%{version}*-info

%changelog
