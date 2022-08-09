#
# spec file for package python-kmatch
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
Name:           python-kmatch
Version:        0.4.0
Release:        0
Summary:        A language for matching/validating/filtering Python dictionaries
License:        MIT
URL:            https://github.com/ambitioninc/kmatch
Source:         https://files.pythonhosted.org/packages/source/k/kmatch/kmatch-%{version}.tar.gz
# https://github.com/ambitioninc/kmatch/issues/42
Patch0:         python-kmatch-no-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The kmatch library provides a language for matching Python
dictionaries. Patterns are specified as lists of filters combined
with logical operators.

%prep
%setup -q -n kmatch-%{version}
%patch0 -p1
sed -i '/nose/d' setup.py
dos2unix README.rst LICENSE
chmod a-x README.rst LICENSE
rm -r *.egg-info

%build
mv kmatch/tests/ .tests
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv .tests tests
%pytest tests/*_tests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
