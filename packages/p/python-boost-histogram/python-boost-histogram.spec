#
# spec file for package python-boost-histogram
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


%{?sle15_python_module_pythons}
Name:           python-boost-histogram
Version:        1.5.1
Release:        0
Summary:        The Boost::Histogram Python wrapper
License:        BSD-3-Clause
URL:            https://github.com/scikit-hep/boost-histogram
Source:         https://files.pythonhosted.org/packages/source/b/boost-histogram/boost_histogram-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel >= 2.13.3}
BuildRequires:  %{python_module scikit-build-core >= 0.10}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module hypothesis >= 6.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-numpy
%python_subpackages

%description
Python bindings for Boost::Histogram (source), a C++14 library. This is one of
the fastest libraries for histogramming, while still providing the power of a
full histogram object.

%prep
%setup -q -n boost_histogram-%{version}

%build
export CFLAGS="%{optflags}"
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch --benchmark-disable

%files %{python_files}
%{python_sitearch}/boost_histogram/
%{python_sitearch}/boost_histogram-%{version}.dist-info/

%changelog
