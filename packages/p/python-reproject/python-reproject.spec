#
# spec file for package python-reproject
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


Name:           python-reproject
Version:        0.9.1
Release:        0
Summary:        Reproject astronomical images
License:        BSD-3-Clause
URL:            https://reproject.readthedocs.io
# Repo-URL:     https://github.com/astropy/reproject
Source:         https://github.com/astropy/reproject/archive/refs/tags/v%{version}.tar.gz#/reproject-%{version}-gh.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module numpy-devel >= 1.17}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 4
Requires:       python-astropy-healpix >= 0.6
Requires:       python-numpy >= 1.17
Requires:       python-scipy >= 1.3
# SECTION test requirements
BuildRequires:  %{python_module astropy >= 4}
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module asdf}
BuildRequires:  %{python_module astropy-healpix >= 0.6}
BuildRequires:  %{python_module gwcs}
BuildRequires:  %{python_module pytest-arraydiff >= 0.5}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.3}
# /SECTION
%python_subpackages

%description
Reproject astronomical images

%prep
%setup -q -n reproject-%{version}

%build
export CFLAGS="%{optflags}"
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
rm -r %{buildroot}%{$python_sitearch}/reproject/spherical_intersect/*.h
%fdupes %{buildroot}%{$python_sitearch}
}

%check
mkdir cleantestdir
cp setup.cfg cleantestdir
cd cleantestdir
%pytest_arch --pyargs reproject

%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE
%{python_sitearch}/reproject
%{python_sitearch}/reproject-%{version}*-info

%changelog
