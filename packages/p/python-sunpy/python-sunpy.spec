#
# spec file for package python-sunpy
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python2 1
# Astropy, SciPy, NumPy require python >= 3.7
%define         skip_python36 1
Name:           python-sunpy
Version:        2.1.4
Release:        0
Summary:        SunPy: Python for Solar Physics
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/sunpy/sunpy
Source0:        https://files.pythonhosted.org/packages/source/s/sunpy/sunpy-%{version}.tar.gz
Source100:      python-sunpy-rpmlintrc
BuildRequires:  %{python_module aioftp}
BuildRequires:  %{python_module asdf}
BuildRequires:  %{python_module astropy >= 4.1}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel > 1.16.0}
BuildRequires:  %{python_module parfive >= 1.2.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aioftp >= 0.17.1
Requires:       python-astropy >= 4.1
Requires:       python-numpy > 1.16.0
Requires:       python-parfive >= 1.2.0
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib_metadata
%endif
# SECTION extras_require:asdf
Recommends:     python-asdf
# /SECTION
# SECTION extras_require:dask
Suggests:       python-dask-array
# /SECTION
# SECTION extras_require:database
Recommends:     python-SQLAlchemy
# /SECTION
# SECTION extras_require:instr
Recommends:     python-matplotlib >= 3.1.0
Recommends:     python-pandas >= 0.24.0
Recommends:     python-scipy > 1.3.0
# /SECTION
# SECTION extras_require:image
Recommends:     python-scikit-image
#               scipy
# /SECTION
# SECTION extras_require:jpeg2000
Recommends:     python-Glymur
# /SECTION
# SECTION extras_require:map
#               matlotlib, scipy
# /SECTION
# SECTION extras_require:net
Recommends:     python-beautifulsoup4
Recommends:     python-drms
Recommends:     python-python-dateutil
Recommends:     python-tqdm
Recommends:     python-zeep
# /SECTION
# SECTION extras_require:timeseries
Recommends:     python-h5netcdf
#               matlotlib, pandas
# /SECTION
# SECTION test requirements (and extras)
BuildRequires:  %{python_module Glymur}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module drms}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module h5netcdf}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module importlib_metadata}
BuildRequires:  %{python_module matplotlib >= 3.1.0}
BuildRequires:  %{python_module pandas >= 0.24.0}
BuildRequires:  %{python_module pytest-astropy >= 0.8}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy >= 1.3.0}
BuildRequires:  %{python_module zeep}
# /SECTION
%python_subpackages

%description
SunPy is a Python library for solar physics data analysis.

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
find  %{buildroot}%{$python_sitearch} -name '*.h' -delete -print
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
%{python_sitearch}/sunpy-%{version}-py*.egg-info

%changelog
