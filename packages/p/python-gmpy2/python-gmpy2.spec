#
# spec file for package python-gmpy2
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-gmpy2
Version:        2.3.0
Release:        0
Summary:        GMP/MPIR, MPFR, and MPC interface to Python 2.6+ and 3x
License:        LGPL-3.0-only
URL:            https://github.com/aleaxit/gmpy
Source:         https://files.pythonhosted.org/packages/source/g/gmpy2/gmpy2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module setuptools_scm >= 6.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  mpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  python-rpm-macros

%python_subpackages

%description
gmpy2 is a C-coded Python extension module that supports
multiple-precision arithmetic. In addition to supporting
GMP or MPIR for multiple-precision integer and rational
arithmetic, gmpy2 adds support for the MPFR (correctly
rounded real floating-point arithmetic) and MPC (correctly
rounded complex floating-point arithmetic) libraries.

%prep
%setup -q -n gmpy2-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license COPYING COPYING.LESSER
%doc README.rst
%{python_sitearch}/gmpy2
%{python_sitearch}/gmpy2-%{version}.dist-info

%changelog
