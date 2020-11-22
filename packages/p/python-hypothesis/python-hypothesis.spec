#
# spec file for package python-hypothesis
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
Version:        5.41.2
Release:        0
Summary:        A library for property based testing
License:        MPL-2.0
URL:            https://github.com/HypothesisWorks/hypothesis
# Source is the `hypothesis-python` subdir of the Github repository.
# Edit the `_service` file and run `osc service runall` for updates.
Source:         hypothesis-python-%{version}
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
Requires(preun): update-alternatives
Recommends:     python-Django >= 2.2
Recommends:     python-dpcontracts >= 0.4
Recommends:     python-lark-parser >= 0.6.5
Recommends:     python-numpy >= 1.9.0
Recommends:     python-pandas >= 0.19
Recommends:     python-pytest >= 4.3
Recommends:     python-python-dateutil >= 1.4
Recommends:     python-pytz >= 2014.1
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module dpcontracts >= 0.6.0}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hypothesis = %{version}}
BuildRequires:  %{python_module lark-parser >= 0.6.5}
BuildRequires:  %{python_module numpy >= 1.9.0}
BuildRequires:  %{python_module pandas >= 0.19}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest >= 4.3}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module python-dateutil >= 1.4}
BuildRequires:  %{python_module sortedcontainers >= 2.1.0}
BuildRequires:  %{python_module typing_extensions}
%endif
# /SECTION
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
%setup -q -n %{_sourcedir}/hypothesis-python-%{version} -T -D
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
%endif

%python_clone -a %{buildroot}%{_bindir}/hypothesis

%post
%python_install_alternative hypothesis

%postun
%python_uninstall_alternative hypothesis

%check
%if %{with test}
# theses tests try to write into global python_sitelib
# https://github.com/HypothesisWorks/hypothesis/issues/2546
skiptests="test_updating_the_file_include_new_shrinkers"
skiptests+=" or test_can_learn_to_normalize_the_unnormalized"
%pytest tests -n auto -p pytester --runpytest=subprocess -k "not ($skiptests)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/hypothesis
%{python_sitelib}/hypothesis
%{python_sitelib}/hypothesis-%{version}-py*.egg-info
%endif

%changelog
