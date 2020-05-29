#
# spec file for package python-mutatorMath
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
Name:           python-mutatorMath
Version:        3.0.1
Release:        0
Summary:        Calculation of piecewise linear interpolations in multiple dimensions
License:        BSD-3-Clause
URL:            https://github.com/LettError/MutatorMath
Source:         https://files.pythonhosted.org/packages/source/M/MutatorMath/MutatorMath-%{version}.zip
Source99:       https://raw.githubusercontent.com/LettError/MutatorMath/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module defcon}
BuildRequires:  %{python_module fontMath}
BuildRequires:  %{pythons}
# /SECTION
%python_subpackages

%description
MutatorMath is a Python library for the calculation of piecewise linear
interpolations in n-dimensions with any number of masters. It was
developed for interpolating data related to fonts, but if can handle any
arithmetic object.

%prep
%setup -q -n MutatorMath-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=./Lib $python Lib/mutatorMath/test/run.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
