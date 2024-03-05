#
# spec file for package python-pytaglib
#
# Copyright (c) 2024 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-pytaglib
Version:        2.1.0
Release:        0
Summary:        Metadata "tagging" library based on TagLib
License:        GPL-3.0-only OR MIT
URL:            https://github.com/supermihi/pytaglib
Source:         https://github.com/supermihi/pytaglib/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/supermihi/pytaglib/pull/123
Patch1:         upgrade_taglib_version.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtag-devel
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
pytaglib is an audio metadata (“tag”) library for Python.
It relies on the TagLib C++ library.

%prep
%autosetup -N -n "pytaglib-%{version}"
%if %{pkg_vcmp libtag-devel >= 2}
%autopatch -p1 1
%endif
# Remove pre-generated source
rm -vf src/taglib.cpp
sed -i -e "1d" src/pyprinttags.py

%build
export PYTAGLIB_CYTHONIZE=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/pyprinttags

%check
export LANG=en_US.UTF-8
%pytest_arch

%post
%python_install_alternative pyprinttags

%postun
%python_uninstall_alternative pyprinttags

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/taglib*.so
%{python_sitearch}/pyprinttags.*
%{python_sitearch}/pytaglib-%{version}.dist-info/
%pycache_only %{python_sitearch}/__pycache__/pyprinttags.*
%python_alternative %{_bindir}/pyprinttags

%changelog
