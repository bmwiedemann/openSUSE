#
# spec file for package python-Mathics
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Upstream no longer supports python2
%define skip_python2 1
%define pyname Mathics3
Name:           python-Mathics%{psuffix}
Version:        5.0.2
Release:        0
Summary:        A general-purpose computer algebra system
# Mathics itself is licensed as GPL-3.0 but it includes third-party software with MIT, BSD-3-Clause, and Apache-2.0 Licensing; also includes data from wikipedia licensed under CC-BY-SA-3.0 and GFDL-1.3
License:        Apache-2.0 AND BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            https://mathics.github.io/
Source0:        https://github.com/Mathics3/mathics-core/releases/download/%{version}/%{pyname}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE python-Mathics-relax-sympy-version.patch badshah400@gmail.com -- Allow working with sympy version >= 1.11
Patch0:         python-Mathics-relax-sympy-version.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mpmath >= 0.19}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy >= 1.10.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
Requires:       python-Mathics-Scanner
Requires:       python-Pint
Requires:       python-llvmlite
Requires:       python-mpmath >= 0.19
Requires:       python-palettable
Requires:       python-python-dateutil
Requires:       python-recordclass
Requires:       python-sympy >= 1.10.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
%if %{with test}
# SECTION For tests
BuildRequires:  %{python_module Mathics}
BuildRequires:  %{python_module Mathics-Scanner}
BuildRequires:  %{python_module Pint}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module llvmlite}
BuildRequires:  %{python_module palettable}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module recordclass}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scipy}
# /SECTION
%endif
Provides:       python-Mathics3 = %{version}
%python_subpackages

%description
Mathics is a general-purpose computer algebra system (CAS). It is meant to be a free, lightweight alternative to Mathematica.

%prep
%autosetup -p1 -n %{pyname}-%{version}

# FIX SPURIOUS EXEC PERMISSIONS
chmod -x ./mathics/data/ExampleData/{numberdata.csv,InventionNo1.xml}
chmod -x ./mathics/packages/SciDraw/*.m

# WRONG END-OF-FILE ENCODING
sed -i "s/\r$//" ./mathics/data/ExampleData/numberdata.csv
sed -i "s/\r$//" ./mathics/packages/SciDraw/*.m

# REMOVE SHEBANGS FROM FILES INSTALLED TO NON-EXEC LOCATIONS
pushd mathics
for d in `find ./ -prune -type d`
do
  find ${d} -name "*.py" -exec sed -i "1,4{/\/usr\/bin\/env/d}" '{}' \;
done
popd

%build
%if %{without test}
export USE_CYTHON=1
%python_build
%endif

%install
%if %{without test}
export USE_CYTHON=1
%python_install
%python_clone -a %{buildroot}%{_bindir}/mathics
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# Home page tests require django server up and running, test_gudermannian needs network access
%pytest_arch -k 'not (test_home_page or test_gudermannian)'
%endif

%if %{without test}
%post
%python_install_alternative mathics

%postun
%python_uninstall_alternative mathics

%files %{python_files}
%license COPYING.txt
%doc README.rst AUTHORS.txt
%python_alternative %{_bindir}/mathics
%{python_sitearch}/mathics/
%{python_sitearch}/%{pyname}-%{version}-py%{python_version}.egg-info/
%endif

%changelog
