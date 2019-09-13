#
# spec file for package python-subst
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
Name:           python-subst
Version:        0.4.0
Release:        0
License:        MIT
Summary:        Utility to replace one string into another in given list of files
Url:            http://mysz.github.io/subst/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/subst/subst-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/msztolcman/subst/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
`subst` is simple utility to replace one string into another in given list of files.

%prep
%setup -q -n subst-%{version}
cp %{SOURCE1} .

sed -i '/argparse/d' setup.py

sed -i '1{/^#!/d}' subst.py

touch test/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}/test
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/subst
%{python_sitelib}/*

%changelog
