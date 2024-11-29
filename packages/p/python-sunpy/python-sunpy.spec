#
# spec file for package python-sunpy
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


%{?sle15_python_module_pythons}
Name:           python-sunpy
Version:        6.0.3
Release:        0
Summary:        SunPy core package: Python for Solar Physics
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/sunpy/sunpy
Source0:        https://files.pythonhosted.org/packages/source/s/sunpy/sunpy-%{version}.tar.gz
# PATCH-FIX-OPENSUSE use custom hypothesis profile for slow OBS executions
Patch1:         sunpy-obs-profile.patch
BuildRequires:  %{python_module aioftp}
BuildRequires:  %{python_module astropy >= 5.3}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module numpy-devel >= 1.25 with %python-numpy-devel < 2.3}
BuildRequires:  %{python_module packaging >= 19}
BuildRequires:  %{python_module parfive >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyerfa >= 2.0.0.1}
BuildRequires:  %{python_module requests >= 2.28}
BuildRequires:  %{python_module setuptools >= 62}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 5.3
Requires:       python-numpy > 1.24.5
Requires:       python-packaging >= 23
Requires:       python-parfive >= 2.0.0
Requires:       python-pyerfa >= 2.0.0.1
Requires:       python-requests >= 2.28.0
# pafived[ftp], ignore rpmlint's python-leftover-require
Requires:       python-aioftp >= 0.17.1
# SECTION project.optional-dependencies:asdf
Recommends:     python-asdf >= 2.13
Recommends:     python-asdf-astropy >= 0.4
# /SECTION
# SECTION project.optional-dependencies:dask
Suggests:       python-dask-array >= 2022.5.2
# /SECTION
# SECTION project.optional-dependencies:image
Recommends:     python-scipy >= 1.9
# /SECTION
# SECTION project.optional-dependencies:jpeg2000
Recommends:     python-Glymur >= 0.11
Recommends:     python-lxml >= 4.9
# /SECTION
# SECTION project.optional-dependencies:map
Recommends:     python-matplotlib >= 3.5.0
Recommends:     python-mpl-animators >= 1.0.0
Recommends:     python-reproject
# scipy
# /SECTION
# SECTION project.optional-dependencies:net
Recommends:     python-beautifulsoup4 >= 4.11.0
Recommends:     python-drms >= 0.7.1
Recommends:     python-python-dateutil >= 2.8.1
Recommends:     python-tqdm >= 4.64
Recommends:     python-zeep >= 4.1.0
# /SECTION
# SECTION project.optional-dependencies:opencv
Recommends:     python-opencv >= 4.6.0.66
# SECTION project.optional-dependencies:scikit-image
Recommends:     python-scikit-image >= 0.19
# /SECTION
# SECTION project.optional-dependencies:timeseries
Recommends:     python-cdflib >= 0.4.4
Recommends:     python-h5netcdf >= 1
Recommends:     python-h5py >= 3.7
Recommends:     python-pandas >= 1.4
#               matplotlib
# /SECTION
# SECTION project.optional-dependencies:visualization
#               matplotlib
#               mpl-animators
# /SECTION
# SECTION test requirements (and extras)
# even although we do not use tox and doctestplus, there are tests in the suite checking their existence.
BuildRequires:  %{python_module asdf >= 2.13}
BuildRequires:  %{python_module asdf-astropy >= 0.1.1}
BuildRequires:  %{python_module beautifulsoup4 >= 4.11.0}
BuildRequires:  %{python_module cdflib >= 0.4.4}
BuildRequires:  %{python_module dask-array >= 2022.5.2}
BuildRequires:  %{python_module drms >= 0.7.1}
BuildRequires:  %{python_module h5netcdf >= 1}
BuildRequires:  %{python_module h5py >= 3.7.0}
BuildRequires:  %{python_module hypothesis >= 6.0.0}
BuildRequires:  %{python_module jplephem >= 2.14}
BuildRequires:  %{python_module lxml >= 4.9}
BuildRequires:  %{python_module matplotlib >= 3.5.0}
BuildRequires:  %{python_module mpl-animators >= 1.0.0}
BuildRequires:  %{python_module pandas >= 1.4.0}
BuildRequires:  %{python_module pytest >= 7.1}
BuildRequires:  %{python_module pytest-astropy >= 0.11}
BuildRequires:  %{python_module pytest-mpl >= 0.16}
BuildRequires:  %{python_module pytest-xdist >= 3.0.2}
BuildRequires:  %{python_module reproject >= 0.9}
BuildRequires:  %{python_module scikit-image >= 0.19.0}
BuildRequires:  %{python_module scipy >= 1.9}
BuildRequires:  %{python_module zeep >= 4.1}
# opencv is not compiled with numpy2 yet
#BuildRequires:  python3-opencv
# /SECTION
%python_subpackages

%description
SunPy is a Python library for solar physics data analysis and visualization.

%prep
%autosetup -p1 -n sunpy-%{version}
sed -i -e '/^#!\//, 1d' sunpy/extern/appdirs.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
sed -i -e 's@^#!/usr/bin/env python@#!%__$python@' %{buildroot}%{$python_sitearch}/sunpy/extern/distro.py
chmod +x %{buildroot}%{$python_sitearch}/sunpy/extern/distro.py
%{$python_compile}
%fdupes %{buildroot}%{$python_sitearch}
}

%check
mkdir testdir
pushd testdir
%{python_expand # no opencv for non-primary python3
# if condition commented out: opencv is not compiled with numpy2 yet, disable for all
#if [ "%%{$python_provides}" != "python3" ]; then
  $python_donttest=" or opencv or (test_transform and (test_nans or test_clipping))"
#fi
}
# fails because it does not find any opencv-python dist metadata (even for python3-opencv installed)
donttest="test_self_test"
%ifarch aarch64
# invalid cast of type
donttest="$donttest or test_plot_unit8"
%endif
# spiceypy not available
%pytest_arch --pyargs sunpy -ra -n auto -k "not ($donttest ${$python_donttest})" --ignore %{buildroot}%{$python_sitearch}/sunpy/coordinates/tests/test_spice.py
popd

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.rst licenses/*
%{python_sitearch}/sunpy
%{python_sitearch}/sunpy-%{version}.dist-info

%changelog
