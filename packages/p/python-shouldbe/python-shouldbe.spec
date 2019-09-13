#
# spec file for package python-shouldbe
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
Name:           python-shouldbe
Version:        0.1.2
Release:        0
Summary:        Python Assertion Helpers inspired by Shouldly
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/directxman12/should_be
Source:         https://files.pythonhosted.org/packages/source/s/shouldbe/shouldbe-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/DirectXMan12/should_be/master/LICENSE.txt
BuildRequires:  %{python_module forbiddenfruit}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-forbiddenfruit
BuildArch:      noarch
%python_subpackages

%description
Python Assertion Helpers inspired by Shouldly

%prep
%setup -q -n shouldbe-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest should_be/tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
