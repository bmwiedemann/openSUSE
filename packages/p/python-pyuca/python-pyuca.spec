#
# spec file for package python-pyuca
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pyuca
Version:        1.2
Release:        0
Summary:        Python implementation of the Unicode Collation Algorithm
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jtauber/pyuca
Source0:        https://files.pythonhosted.org/packages/source/p/pyuca/pyuca-%{version}.tar.gz
# https://github.com/jtauber/pyuca/issues/21
Source1:        https://raw.githubusercontent.com/jtauber/pyuca/master/test.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a Python implementation of the Unicode Collation Algorithm (UCA). It
passes 100% of the UCA conformances tests for Unicode 6.3.0 with a
variable-weighting setting of Non-ignorable.

%prep
%setup -q -n pyuca-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest test

%files %{python_files}
%license LICENSE*
%doc README.md
%{python_sitelib}/pyuca
%{python_sitelib}/pyuca-%{version}.dist-info

%changelog
