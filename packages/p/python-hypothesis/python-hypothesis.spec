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
Version:        6.61.0
Release:        0
Summary:        A library for property based testing
License:        MPL-2.0
URL:            https://github.com/HypothesisWorks/hypothesis
# Source is the `hypothesis-python` subdir of the Github repository.
# Edit the `_service` file and run `osc service runall` for updates.
# See also https://hypothesis.readthedocs.io/en/latest/packaging.html
Source:         hypothesis-python-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python-exceptiongroup >= 1.0.0
Requires:       python-sortedcontainers >= 2.1.0
Requires(post): update-alternatives
Requires(preun):update-alternatives
# SECTION requires_extra
# consuming packages need to declare these optional dependencies explicitly
Recommends:     python-Django >= 2.2
Recommends:     python-black >= 19.10
Recommends:     python-click >= 7.0
Recommends:     python-dpcontracts >= 0.4
Recommends:     python-lark >= 0.10.1
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
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module sortedcontainers >= 2.1.0}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module backports.zoneinfo >= 0.2.1 if %python-base < 3.9}
BuildRequires:  %{python_module black >= 19.10}
BuildRequires:  %{python_module dpcontracts >= 0.4}
BuildRequires:  %{python_module fakeredis}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hypothesis = %{version}}
BuildRequires:  %{python_module lark >= 0.10.1}
BuildRequires:  %{python_module libcst >= 0.3.16}
BuildRequires:  %{python_module numpy >= 1.9.0}
BuildRequires:  %{python_module pandas >= 1.0}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module python-dateutil >= 1.4}
# /SECTION
%endif
%python_subpackages

%description
Hypothesis is a family of testing libraries which let you write tests parametrized
by a source of examples. A Hypothesis implementation then generates simple and
comprehensible examples that make your tests fail. This simplifies writing your
tests and makes them more powerful at the same time, by letting software automate
the boring bits and do them to a higher standard than a human would, freeing you
to focus on the higher level test logic.

This sort of testing is often called "property-based testing", and the most widely
known implementation of the concept is the Haskell library QuickCheck, but
Hypothesis differs significantly from QuickCheck and is designed to fit idiomatically
and easily into existing styles of testing that you are used to, with absolutely no
familiarity with Haskell or functional programming needed.

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
# theses tests try to write into global python_sitelib
# https://github.com/HypothesisWorks/hypothesis/issues/2546
donttest="test_updating_the_file_include_new_shrinkers"
donttest+=" or test_can_learn_to_normalize_the_unnormalized"
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
    error
    ignore::hypothesis.errors.NonInteractiveExampleWarning
    # https://github.com/pandas-dev/pandas/issues/41199
    default:Creating a LegacyVersion has been deprecated and will be removed in the next major release:DeprecationWarning
    default:distutils Version classes are deprecated\. Use packaging\.version instead:DeprecationWarning
    # https://github.com/pandas-dev/pandas/issues/32056 (?)
    default:numpy\.ufunc size changed, may indicate binary incompatibility\. Expected 216 from C header, got 232 from PyObject:RuntimeWarning
    # https://github.com/lark-parser/lark/pull/1140
    default:module 'sre_constants' is deprecated:DeprecationWarning
    default:module 'sre_parse' is deprecated:DeprecationWarning
    # https://github.com/pandas-dev/pandas/issues/34848
    default:`np\.bool` is a deprecated alias for the builtin `bool`:DeprecationWarning
    default:`np\.complex` is a deprecated alias for the builtin `complex`:DeprecationWarning
    default:`np\.object` is a deprecated alias for the builtin `object`:DeprecationWarning
' > pytest.ini
%pytest -c pytest.ini -k "not ($donttest)" tests
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
