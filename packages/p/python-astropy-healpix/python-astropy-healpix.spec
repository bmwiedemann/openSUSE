#
# spec file for package python-astropy-healpix
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


Name:           python-astropy-healpix
Version:        0.7
Release:        0
Summary:        HEALPix for Astropy
License:        BSD-3-Clause
URL:            https://github.com/astropy/astropy-healpix
Source:         https://files.pythonhosted.org/packages/source/a/astropy_healpix/astropy_healpix-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 3
Requires:       python-numpy
Provides:       python-astropy_healpix = %{version}-%{release}
# SECTION test requirements
BuildRequires:  %{python_module astropy >= 3}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-astropy}
# /SECTION
%python_subpackages

%description
This is a BSD-licensed HEALPix package developed by the Astropy project
and based on C code written by Dustin Lang in astrometry.net.

%prep
%setup -q -n astropy_healpix-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir cleantestdir
cd cleantestdir
%pytest_arch --pyargs astropy_healpix

%files %{python_files}
%{python_sitearch}/astropy_healpix
%{python_sitearch}/astropy_healpix-%{version}*-info

%changelog
