#
# spec file for package python-Mathics
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%define skip_python313 1
%define pyname Mathics3
Name:           python-Mathics%{psuffix}
Version:        7.0.0
Release:        0
Summary:        A general-purpose computer algebra system
# Mathics itself is licensed as GPL-3.0 but it includes third-party software with MIT, BSD-3-Clause, and Apache-2.0 Licensing; also includes data from wikipedia licensed under CC-BY-SA-3.0 and GFDL-1.3
License:        Apache-2.0 AND BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            https://mathics.github.io/
Source0:        https://github.com/Mathics3/mathics-core/releases/download/%{version}/%{pyname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-Mathics-sympy1_13.patch badshah400@gmail.com -- Add compatibility for tests against sympy >= 1.13
Patch0:         python-Mathics-sympy1_13.patch
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mpmath >= 0.19}
BuildRequires:  %{python_module numpy < 2}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy >= 1.10.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Mathics-Scanner >= 1.3.0
Requires:       python-Pint
Requires:       python-llvmlite
Requires:       python-mpmath >= 0.19
Requires:       python-numpy < 2
Requires:       python-palettable
Requires:       python-python-dateutil
Requires:       python-requests
Requires:       python-sympy >= 1.10.1
Requires:       (python-Pillow >= 9.2 if python-base >= 3.7)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-scikit-image >= 0.17
%if %{with test}
# SECTION For tests
BuildRequires:  %{python_module Mathics = %{version}}
BuildRequires:  %{python_module Mathics-Scanner >= 1.3.0}
BuildRequires:  %{python_module Pillow >= 9.2 if %python-base >= 3.7}
BuildRequires:  %{python_module Pint}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module llvmlite}
BuildRequires:  %{python_module palettable}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-image >= 0.17}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
%endif
Provides:       python-Mathics3 = %{version}
BuildArch:      noarch
%python_subpackages

%description
Mathics is a general-purpose computer algebra system (CAS). It is meant to be a
free, lightweight alternative to Mathematica.

%prep
%autosetup -p1 -n %{pyname}-%{version}

# REMOVE SHEBANGS FROM FILES INSTALLED TO NON-EXEC LOCATIONS
pushd mathics
for d in `find ./ -prune -type d`
do
  find ${d} -name "*.py" -exec sed -i "1,4{/\/usr\/bin\/env/d}" '{}' \;
done
popd

%build
%if %{without test}
export USE_CYTHON=0
%pyproject_wheel
%endif

%install
%if %{without test}
export USE_CYTHON=0
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mathics
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
PYTHONPATH+=:${PWD}
# test_gudermannian needs network access
# test_image: https://github.com/Mathics3/mathics-core/issues/837
DONTTEST='test_gudermannian or test_image'
# A whole swathe of tests no longer work: https://github.com/Mathics3/mathics-core/issues/1346
DONTTEST+=' or test_element or test_limit or test_private_doctests_'
DONTTEST+=' or test_associations_private_doctests or test_ArcCos or test_add'
DONTTEST+=' or test_set_and_clear or test_compare_many_members or test_cmp1_no_pass'
DONTTEST+=' or test_makeboxes_ or test_returncode or test_predicates_private_doctests'
if [ "%_lib" = "lib" ]; then
  DONTTEST+=' or test_nintegrate or test_cli'
fi
export DONTTEST
export USE_CYTHON=0
%pytest -k "not (${DONTTEST})"
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
%{python_sitelib}/mathics/
%{python_sitelib}/%{pyname}-%{version}*.*-info/
%endif

%changelog
