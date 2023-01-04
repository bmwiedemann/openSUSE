#
# spec file for package python-boost-histogram
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# No numpy for python 3.6 on TW
%define skip_python36 1
# py2 not supported
%define skip_python2 1
%define modname boost_histogram
Name:           python-boost-histogram
Version:        1.3.2
Release:        0
Summary:        The Boost::Histogram Python wrapper
License:        BSD-3-Clause
URL:            https://github.com/scikit-hep/boost-histogram
Source:         https://files.pythonhosted.org/packages/source/b/boost-histogram/boost_histogram-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} < 1550
BuildRequires:  python3-dataclasses
%endif
# SECTION test requirements
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# On i586 this test fails for unknown reason, see https://github.com/scikit-hep/boost-histogram/issues/598
%ifarch %ix86
%pytest_arch -k 'not test_log_transform'
%else
%pytest_arch
%endif

%files %{python_files}
%{python_sitearch}/%{modname}/
%{python_sitearch}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
