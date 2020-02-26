#
# spec file for package python-Theano
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-Theano%{psuffix}
Version:        1.0.4
Release:        0
Summary:        A scientific python library
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/Theano/Theano
Source:         https://files.pythonhosted.org/packages/source/T/Theano/Theano-%{version}.tar.gz
Source1:        python-Theano.rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       c++_compiler
Requires:       python-devel
Requires:       python-numpy >= 1.9.1
Requires:       python-numpy-devel >= 1.9.1
Requires:       python-scipy >= 0.14
Requires:       python-six >= 1.9.0
# The tests are compiling and are arch specific
%if !%{with test}
BuildArch:      noarch
%endif
%if %{with test}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module scipy >= 0.14}
BuildRequires:  %{python_module six >= 1.9.0}
%endif
%python_subpackages

%description
Theano is a Python library that allows you to define, optimize, and
evaluate mathematical expressions involving multi-dimensional arrays.

Theano features:
* tight integration with numpy - Use numpy.ndarray in Theano-compiled
  functions.
* transparent use of a GPU
* symbolic differentiation - Let Theano do your derivatives.
* speed and stability optimizations – Get the right answer for log(1+x)
  even when x is really tiny.
* dynamic C code generation - Evaluate expressions faster.
* extensive unit-testing and self-verification – Detect and diagnose
  many types of mistake.

%prep
%setup -q -n Theano-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install

# remove binaries and stuff thats not supposed to end up on system
%python_expand rm -r %{buildroot}%{$python_sitelib}/bin
# Other pkgs use theano tests as a basis (see Keras)
#%%python_expand rm -r %{buildroot}%{$python_sitelib}/theano/tests
#%%python_expand rm -r %{buildroot}%{$python_sitelib}/theano/*/tests

# replace duplicate .pyo/.pyc with hardlinks
%python_expand %fdupes %{buildroot}%{_defaultdocdir}/%{name}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# https://github.com/Theano/Theano/issues/6719
rm theano/tensor/tests/test_var.py
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} theano/tests -v -e '(test_scan_err1|test_remove0|test_csm_unsorted|test_good|test_vector_arguments|test_vector_arguments)'
%endif

%if !%{with test}
%files %{python_files}
%doc DESCRIPTION.txt EMAIL.txt HISTORY.txt NEWS.txt README.rst
%license doc/LICENSE.txt
%python3_only %{_bindir}/theano-cache
%python3_only %{_bindir}/theano-nose
%{python_sitelib}/theano
%{python_sitelib}/Theano-%{version}-*.egg-info
%endif

%changelog
