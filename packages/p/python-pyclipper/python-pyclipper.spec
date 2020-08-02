#
# spec file for package python-pyclipper
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Xu Zhao (i@xuzhao.net).
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
%bcond_without python2
Name:           python-pyclipper
Version:        1.1.0.post3
Release:        0
Summary:        Cython wrapper for the Clipper library
License:        MIT
URL:            https://github.com/fonttools/pyclipper
Source:         https://files.pythonhosted.org/packages/source/p/pyclipper/pyclipper-%{version}.zip
# https://github.com/fonttools/pyclipper/pull/32
Patch0:         python-pyclipper-no-unittest2.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
%if %{with python2}
# Required because of otherwise missing assertWarns
BuildRequires:  python2-unittest2
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%python_subpackages

%description
Pyclipper is a Cython wrapper exposing public functions and classes of
the C++ translation of the `Angus Johnson's Clipper library (ver.
6.4.2) <http://www.angusj.com/delphi/clipper.php>`__.

%prep
%setup -q -n pyclipper-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
