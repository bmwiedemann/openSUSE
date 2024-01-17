#
# spec file for package python-pytaglib
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytaglib
Version:        1.5.0
Release:        0
Summary:        Metadata "tagging" library based on TagLib
License:        GPL-3.0-only OR MIT
URL:            https://github.com/supermihi/pytaglib
Source:         https://github.com/supermihi/pytaglib/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtag-devel
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
pytaglib is an audio metadata (“tag”) library for Python.
It relies on the TagLib C++ library.

%prep
%setup -q -n "pytaglib-%{version}"
# Remove pre-generated source
rm -vf src/taglib.cpp
sed -i -e "1d" src/pyprinttags.py

%build
sed -i "s:\(script_name =\).*:\1 'pyprinttags':" setup.py
export PYTAGLIB_CYTHONIZE=1
%python_build

%install
%python_install
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
%license COPYING
%doc README.md
%{python_sitearch}/taglib*.so
%{python_sitearch}/pyprinttags.*
%{python_sitearch}/pytaglib-%{version}-py%{python_version}.egg-info/
%pycache_only %{python_sitearch}/__pycache__/pyprinttags.*
%python_alternative %{_bindir}/pyprinttags

%changelog
