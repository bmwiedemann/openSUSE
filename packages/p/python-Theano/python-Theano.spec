#
# spec file for package python-Theano
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Theano
Version:        1.0.4
Release:        0
Summary:        A scientific python library
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://deeplearning.net/software/theano/
Source:         https://files.pythonhosted.org/packages/source/T/Theano/Theano-%{version}.tar.gz
Source1:        python-Theano.rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       c++_compiler
Requires:       python-numpy >= 1.9.1
Requires:       python-scipy >= 0.14
Requires:       python-six >= 1.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose >= 1.3.0}
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module scipy >= 0.14}
BuildRequires:  %{python_module six >= 1.9.0}
# /SECTION
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
%python_install

# replace duplicate .pyo/.pyc with hardlinks
%python_expand %fdupes %{buildroot}%{_defaultdocdir}/%{name}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Fix python-bytecode-inconsistent-mtime
%python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/theano
%python_expand $python -O -m compileall -d %{$python_sitelib}  %{buildroot}%{$python_sitelib}/theano

%files %{python_files}
%doc DESCRIPTION.txt EMAIL.txt HISTORY.txt NEWS.txt README.rst
%license doc/LICENSE.txt
%python3_only %{_bindir}/theano-cache
%python3_only %{_bindir}/theano-nose
%{python_sitelib}/bin
%{python_sitelib}/theano
%{python_sitelib}/Theano-%{version}-*.egg-info

%changelog
