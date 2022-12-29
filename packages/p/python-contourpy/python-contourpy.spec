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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-contourpy%{psuffix}
Version:        1.0.6
Release:        0
Summary:        Python library for calculating contours of 2D quadrilateral grids
License:        BSD-3-Clause
URL:            https://github.com/contourpy/contourpy
Source:         https://files.pythonhosted.org/packages/source/c/contourpy/contourpy-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel >= 2.7}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.16
Suggests:       python-bokeh
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module contourpy = %{version}}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy >= 1.16}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
A Python library for calculating contours of 2D quadrilateral grids

It contains the 2005 and 2014 algorithms used in Matplotlib as well
as a newer algorithm that includes more features and is available
in both serial and multithreaded versions. It provides an easy way
for Python libraries to use contouring algorithms without having
to include Matplotlib as a dependency.

%prep
%setup -q -n contourpy-%{version}

%build
%if !%{with test}
export CFLAGS="%{optflags}"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%pytest_arch
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/contourpy
%{python_sitearch}/contourpy-%{version}*-info
%endif

%changelog
