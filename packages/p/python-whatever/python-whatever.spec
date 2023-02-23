#
# spec file for package python-whatever
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


Name:           python-whatever
Version:        0.7
Release:        0
Summary:        Module to make anonymous functions by partial application of operators
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Suor/whatever
Source:         https://github.com/Suor/whatever/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python module to make lambdas by partial application of python operators.
It is inspired by the Perl 6 one, see http://perlcabal.org/syn/S02.html#The_Whatever_Object

%prep
%setup -q -n whatever-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/whatever.py
%{python_sitelib}/whatever-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
