#
# spec file for package python-pyerfa
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


%if 0%{suse_version} <= 1500
# use the bundled ERFA in Leap <=15.X, because the system provided one is too old
%bcond_with systemlibs
%else
%bcond_without systemlibs
%endif

%define erfaversion 2.0.1
Name:           python-pyerfa
Version:        2.0.1.5
Release:        0
Summary:        Python bindings for ERFA
License:        BSD-3-Clause
URL:            https://github.com/liberfa/pyerfa
Source:         https://files.pythonhosted.org/packages/source/p/pyerfa/pyerfa-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module numpy-devel >= 1.25}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-doctestplus >= 0.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if %{with systemlibs}
BuildRequires:  pkgconfig(erfa) >= %{erfaversion}
%endif
Requires:       python-numpy >= 1.19.3
%python_subpackages

%description
A Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU).  All C routines are wrapped as Numpy universal functions,
so that they can be called with scalar or array inputs.

The project is a split of astropy._erfa module, developed in the
context of Astropy project, into a standalone package.

%prep
%setup -q -n pyerfa-%{version}
%if %{with systemlibs}
rm -rf liberfa/
%endif

%build
%if %{with systemlibs}
export PYERFA_USE_SYSTEM_LIBERFA=1
%endif
%pyproject_wheel

%install
%if %{with systemlibs}
export PYERFA_USE_SYSTEM_LIBERFA=1
%endif
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%if %{with systemlibs}
# detection of non-embedded lib fails on ppc
%define skip_embedded_test -k "not test_version_with_embedded_liberfa"
%endif
%pytest_arch --pyargs erfa %{?skip_embedded_test}

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%if !%{with systemlibs}
%license licenses/ERFA.rst
%endif
%{python_sitearch}/erfa
%{python_sitearch}/pyerfa-%{version}.dist-info

%changelog
