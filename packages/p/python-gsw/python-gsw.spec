#
# spec file for package python-gsw
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


Name:           python-gsw
Version:        3.6.18
Release:        0
Summary:        Gibbs Seawater Oceanographic Package of TEOS-10
# Note: Python code is MIT licensed
# C-code IS BSD-3-Clause licensed (see src/c_gsw/LICENSE)
# MATLAB function names and documentation are BSD-3-Clause licensed (see http://teos-10.org/pubs/gsw/html/gsw_licence.html)
License:        BSD-3-Clause AND MIT
URL:            https://github.com/TEOS-10/GSW-python
# gh#TEOS-10/GSW-Python#39 -- Tests are not included in the source tarball
Source0:        https://github.com/TEOS-10/GSW-Python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.5}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-numpy
# SECTION tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pandas}
# /SECTION
%python_subpackages

%description
Python implementation of the Thermodynamic Equation of
Seawater 2010 (TEOS-10).

%prep
%setup -q -n GSW-Python-%{version}

%build
CFLAGS="%{optflags}"
%ifarch i586 armv7l
CFLAGS="$CFLAGS -ffloat-store"
%endif
export CFLAGS
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}}

%check
%pytest_arch ${donttest:+-k "not (${donttest:4})"}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/gsw
%{python_sitearch}/gsw-%{version}.dist-info

%changelog
