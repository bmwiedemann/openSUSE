#
# spec file for package python-pytaglib
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
Name:           python-pytaglib
Version:        1.4.5
Release:        0
Summary:        Metadata "tagging" library based on TagLib
License:        GPL-3.0-only OR MIT
Group:          Development/Libraries/Python
URL:            https://github.com/supermihi/pytaglib
Source:         https://github.com/supermihi/pytaglib/archive/v%{version}.tar.gz
# https://github.com/supermihi/pytaglib/issues/63
# fix  'LocalPath'object has no attribute 'endswith' for python2
Patch0:         python-pytaglib-python2-localpath.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtag-devel
BuildRequires:  python-rpm-macros

%python_subpackages

%description
pytaglib is an audio metadata (“tag”) library for Python.
It relies on the TagLib C++ library.

%prep
%setup -q -n "pytaglib-%{version}"
%patch0 -p1
# Remove pre-generated source
rm -vf src/taglib.cpp
sed -i -e "1d" src/pyprinttags.py

%build
%python_build "--cython"

%install
%python_install
mv %{buildroot}%{_bindir}/pyprinttags3 %{buildroot}/%{_bindir}/pyprinttags
%python_expand %fdupes -s %{buildroot}%{$python_sitearch}
# https://github.com/supermihi/pytaglib/issues/62
mkdir -p %{buildroot}%{python3_sitelib}
install -m 644 src/pyprinttags.py %{buildroot}%{python3_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%license COPYING
%doc README.md
%python3_only %{_bindir}/pyprinttags
%python3_only %{python3_sitelib}/pyprinttags.py
%{python_sitearch}/taglib*.so
%{python_sitearch}/pytaglib-%{version}-py%{python_version}.egg-info/

%changelog
