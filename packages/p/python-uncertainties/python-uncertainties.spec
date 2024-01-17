#
# spec file for package python-uncertainties
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


%{?sle15_python_module_pythons}
Name:           python-uncertainties
Version:        3.1.7
Release:        0
Summary:        Uncertainties on the Quantities Involved (aka "Error Propagation")
License:        BSD-3-Clause
URL:            https://github.com/lebigot/uncertainties/
Source:         https://files.pythonhosted.org/packages/source/u/uncertainties/uncertainties-%{version}.tar.gz
Patch0:         remove-future-requirement.patch
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module tools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if 0%{?suse_version}
Recommends:     python-numpy
%endif
%python_subpackages

%description
"uncertainties" allows calculations such as (2±0.1)*2 = 4±0.2 to be
performed transparently. Much more complex mathematical expressions
involving numbers with uncertainties can also be evaluated directly.

%prep
%autosetup -p1 -n uncertainties-%{version}
sed -i -e '/^#!\//, 1d' uncertainties/1to2.py
sed -i -e '/^#!\//, 1d' uncertainties/lib1to2/test_1to2.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/uncertainties/
%{python_sitelib}/uncertainties-%{version}.dist-info

%changelog
