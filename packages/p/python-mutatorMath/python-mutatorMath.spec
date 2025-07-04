#
# spec file for package python-mutatorMath
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


Name:           python-mutatorMath
Version:        3.0.1
Release:        0
Summary:        Calculation of piecewise linear interpolations in multiple dimensions
License:        BSD-3-Clause
URL:            https://github.com/LettError/MutatorMath
Source:         https://files.pythonhosted.org/packages/source/M/MutatorMath/MutatorMath-%{version}.zip
Source99:       https://raw.githubusercontent.com/LettError/MutatorMath/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools
Requires:       python-defcon
Requires:       python-fontMath
# requires fonttools' extras_require[ufo] for the "ufo subpackage", despite not specified by setup.py
Requires:       python-fs
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools}
BuildRequires:  %{python_module defcon}
BuildRequires:  %{python_module fontMath}
BuildRequires:  %{python_module fs}
# Full stdlib required to avoid resource warnings in test suite.
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=./Lib $python Lib/mutatorMath/test/run.py -v

%files %{python_files}
%license LICENSE
%{python_sitelib}/mutatorMath
%{python_sitelib}/[Mm]utator[Mm]ath-%{version}*-info

%changelog
