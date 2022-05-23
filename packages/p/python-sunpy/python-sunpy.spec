#
# spec file for package python-sunpy
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


%{?!python_module:%define python_module() python3-%{**}}
# python-xmlsec doesn’t support 3.10 gh#mehcode/python-xmlsec#204
%define skip_python310 1
Name:           python-sunpy
Version:        3.1.5
Release:        0
Summary:        SunPy: Python for Solar Physics
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/sunpy/sunpy
Source0:        https://files.pythonhosted.org/packages/source/s/sunpy/sunpy-%{version}.tar.gz
Source100:      python-sunpy-rpmlintrc
# PATCH-FIX-OPENSSUSE sunpy-test-ignore-warnings.patch -- g#sunpy/sunpy#6030
Patch1:         sunpy-test-ignore-warnings.patch
BuildRequires:  %{python_module aioftp}
BuildRequires:  %{python_module asdf >= 2.6}
BuildRequires:  %{python_module astropy >= 4.2}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel > 1.17.0}
BuildRequires:  %{python_module packaging >= 19}
BuildRequires:  %{python_module parfive >= 1.2.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aioftp >= 0.17.1
Requires:       python-astropy >= 4.2
Requires:       python-numpy > 1.17.0
Requires:       python-packaging >= 19
Requires:       python-parfive >= 1.2.0
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib_metadata
%endif
# SECTION extras_require:asdf
Recommends:     python-asdf >= 2.6
# /SECTION
# SECTION extras_require:dask
Suggests:       python-dask-array >= 2.0
# /SECTION
# SECTION extras_require:database
Recommends:     python-SQLAlchemy >= 1.3.4
# /SECTION
# SECTION extras_require:image
Recommends:     python-scikit-image
Recommends:     python-scipy > 1.3.0
# /SECTION
# SECTION extras_require:jpeg2000
Recommends:     python-Glymur >= 0.8.18
# /SECTION
# SECTION extras_require:map
Recommends:     python-matplotlib >= 3.1.0
Recommends:     python-mpl-animators >= 1.0.0
Recommends:     python-reproject
# scipy
# /SECTION
# SECTION extras_require:net
Recommends:     python-beautifulsoup4 >= 4.0.0
Recommends:     python-drms >= 0.6.1
Recommends:     python-python-dateutil >= 2.8.0
Recommends:     python-tqdm >= 4.32.1
Recommends:     python-zeep >= 3.4.0
# /SECTION
# SECTION extras_require:timeseries
Recommends:     python-cdflib >= 0.3.19
Conflicts:      python-cdflib = 0.4.0
Recommends:     python-h5netcdf
Recommends:     python-h5py
Recommends:     python-pandas >= 1
#               matplotlib
# /SECTION
# SECTION test requirements (and extras)
# even although we do not use tox and doctestplus, there are tests in the suite checking their existence.
BuildRequires:  %{python_module Glymur >= 0.8.18}
BuildRequires:  %{python_module SQLAlchemy >= 1.3.4}
BuildRequires:  %{python_module beautifulsoup4 >= 4.0.0}
BuildRequires:  %{python_module cdflib >= 0.3.19}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module drms >= 0.6.1}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module h5netcdf}
BuildRequires:  %{python_module h5py >= 3.1.0}
BuildRequires:  %{python_module hypothesis >= 6.0.0}
BuildRequires:  %{python_module importlib_metadata if %python-base < 3.8}
BuildRequires:  %{python_module jplephem}
BuildRequires:  %{python_module matplotlib >= 3.1.0}
BuildRequires:  %{python_module mpl-animators >= 1.0.0}
BuildRequires:  %{python_module pandas >= 0.24.0}
BuildRequires:  %{python_module pytest-astropy >= 0.8}
BuildRequires:  %{python_module pytest-doctestplus >= 0.5}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-mpl >= 0.12}
BuildRequires:  %{python_module pytest-xdist >= 1.27}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module reproject}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-image >= 0.16.0}
BuildRequires:  %{python_module scipy >= 1.3.0}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module zeep >= 3.4.0}
# /SECTION
%python_subpackages

%description
SunPy is a Python library for solar physics data analysis and visualization.

%prep
%autosetup -p1 -n sunpy-%{version}
sed -i -e '/^#!\//, 1d' sunpy/extern/appdirs.py
chmod -x sunpy/data/test/cor1_20090615_000500_s4c1A.fts

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%{python_expand #
find %{buildroot}%{$python_sitearch} -name '*.h' -delete -print
rm -r %{buildroot}%{$python_sitearch}/benchmarks
%fdupes %{buildroot}%{$python_sitearch}
}

%check
mkdir testdir
pushd testdir
%pytest_arch --pyargs sunpy -ra -n auto
popd

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.rst licenses/*
%{python_sitearch}/sunpy
%{python_sitearch}/sunpy-%{version}*-info

%changelog
