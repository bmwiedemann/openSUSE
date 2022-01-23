#
# spec file
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
%define skip_python2 1
%define skip_python36 1
%bcond_with ringdisabled
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# Magic for OBS Staging. Only build the flavors required by
# other packages in the ring.
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-hypothesis%{psuffix}
Version:        6.35.0
Release:        0
Summary:        A library for property based testing
License:        MPL-2.0
URL:            https://github.com/HypothesisWorks/hypothesis
# Source is the `hypothesis-python` subdir of the Github repository.
# Edit the `_service` file and run `osc service runall` for updates.
# See also https://hypothesis.readthedocs.io/en/latest/packaging.html
Source:         hypothesis-python-%{version}.tar.gz
# PATCH-FIX-OPENSUSE dont import numpy and pandas and skip tests if these optional packages are not available.
Patch0:         importorskip-numpy-pandas.patch
%if 0%{?suse_version} >= 1500
BuildRequires:  %{pythons >= 3.5.2}
%else
BuildRequires:  %{python_module base >= 3.5.2}
%endif
BuildRequires:  %{python_module setuptools >= 36.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python-sortedcontainers >= 2.1.0
Requires(post): update-alternatives
Requires(preun):update-alternatives
# SECTION requires_extra
# consuming packages need to declare these optional dependencies explicitly
Recommends:     python-Django >= 2.2
Recommends:     python-black >= 19.10
Recommends:     python-click >= 7.0
Recommends:     python-dpcontracts >= 0.4
Recommends:     python-lark-parser >= 0.6.5
Recommends:     python-libcst >= 0.3.16
Recommends:     python-numpy >= 1.9.0
Recommends:     python-pandas >= 0.25
Recommends:     python-pytest >= 4.6
Recommends:     python-python-dateutil >= 1.4
Recommends:     python-pytz >= 2014.1
Recommends:     python-redis >= 3.0.0
Recommends:     python-rich >= 9.0
Recommends:     (python-importlib_metadata >= 3.6 if python-base < 3.8)
# /SECTION
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module black >= 19.10}
BuildRequires:  %{python_module dpcontracts >= 0.4}
BuildRequires:  %{python_module fakeredis}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hypothesis = %{version}}
BuildRequires:  %{python_module importlib_resources >= 3.3.0 if %python-base < 3.7}
BuildRequires:  %{python_module lark-parser >= 0.6.5}
BuildRequires:  %{python_module libcst >= 0.3.16}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module python-dateutil >= 1.4}
BuildRequires:  %{python_module sortedcontainers >= 2.1.0}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module numpy >= 1.9.0 if (%python-base without python36-base)}
BuildRequires:  %{python_module pandas >= 0.25 if (%python-base without python36-base)}
# /SECTION
%endif
%python_subpackages

%description
Hypothesis is a library for testing your Python code against a much larger range
of examples than you would ever want to write by hand. It's based on the Haskell
library, Quickcheck, and is designed to integrate seamlessly into your existing
Python unit testing work flow.

Hypothesis works with most widely used versions of Python. It supports implementations
compatible with 2.6, 2.7 and 3.3+, and is known to work on CPython and PyPy (but not
PyPy3 until they support a 3.3 compatible version of the language). It does *not* currently
work on Jython or on Python 3.0 through 3.2.

%prep
%setup -q -n hypothesis-python-%{version}
%autopatch -p1

# gh#HypothesisWorks/hypothesis#2447: make sure arr==0.0 is an array on 32-bit
sed -i 's/assert (arr == 0.0)/assert np.asarray(arr == 0.0)/' tests/numpy/test_gen_data.py

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/hypothesis
%endif

%post
%python_install_alternative hypothesis

%postun
%python_uninstall_alternative hypothesis

%check
%if %{with test}
# python3 means Python 3.6 on SLE-15 not a generic exclusion for all Python 3.*
#
# theses tests try to write into global python_sitelib
# https://github.com/HypothesisWorks/hypothesis/issues/2546
donttest="test_updating_the_file_include_new_shrinkers"
donttest+=" or test_can_learn_to_normalize_the_unnormalized"
# extraneous encoding
python36_donttest+=" or (test_cli_python_equivalence and json)"
# typing_extension problem on python36 and Leap 15's python3
python36_donttest+=" or test_mutually_recursive_types_with_typevar"
python3_donttest+=" or test_mutually_recursive_types_with_typevar"
# gh#HypothesisWorks/hypothesis#3035
python310_donttest+=" or test_recursion_error_is_not_flaky"
# requires backports.zoneinfo for python < 3.9
python36_ignoretests=" --ignore tests/datetime/test_zoneinfo_timezones.py"
python38_ignoretests=" --ignore tests/datetime/test_zoneinfo_timezones.py"
python3_ignoretests=" --ignore tests/datetime/test_zoneinfo_timezones.py"
# added for 6.24.x
# generic exclusion of array_api* in not possible :-(
# python3_ignoretests+=" --ignore tests/array_api/test_partial_adoptors.py"
# python3_ignoretests+=" --ignore tests/array_api/test_pretty.py"
# python3_ignoretests+=" --ignore tests/array_api/test_scalar_dtypes.py"
# python3_ignoretests+=" --ignore tests/array_api/test_arrays.py"
# python3_ignoretests+=" --tests/array_api/test_from_dtype.py"
# python3_ignoretests+=" --tests/array_api/test_argument_validation.py"
# python3_ignoretests+=" --tests/array_api/test_indices.py"
python3_ignoretests+=" --ignore tests/array_api*"
# not available for python36
python36_ignoretests+=" --ignore tests/numpy --ignore tests/pandas"
# adapted from pytest.ini in github repo toplevel dir (above hypothesis-python)
echo '[pytest]
addopts=
    --strict-markers
    --tb=native
    -p pytester --runpytest=subprocess
    -v
    -n auto
    -ra
filterwarnings =
    ignore::hypothesis.errors.NonInteractiveExampleWarning
' > pytest.ini
%pytest -c pytest.ini -k "not ($donttest ${$python_donttest})" ${$python_ignoretests} tests
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/hypothesis
%{python_sitelib}/*hypothesis*
%{python_sitelib}/hypothesis-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/*hypothesis*
%endif

%changelog
