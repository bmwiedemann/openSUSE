#
# spec file for package python-pyuca
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
BuildArch:      noarch
Name:           python-pyuca
Version:        1.2
Release:        0
Summary:        Python implementation of the Unicode Collation Algorithm
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/jtauber/pyuca
Source0:        https://pypi.python.org/packages/source/p/pyuca/pyuca-%{version}.tar.gz
# https://github.com/jtauber/pyuca/issues/21
Source1:        https://raw.githubusercontent.com/jtauber/pyuca/master/test.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This is a Python implementation of the Unicode Collation Algorithm (UCA). It
passes 100% of the UCA conformances tests for Unicode 6.3.0 with a
variable-weighting setting of Non-ignorable.

%prep
%setup -q -n pyuca-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -munittest discover -v

%files %{python_files}
%license LICENSE*
%doc README.md
%{python_sitelib}/*

%changelog
