#
# spec file for package python-sunpy
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define skip_python311 1
Name:           python-sunpy
Version:        7.1.0
Release:        0
Summary:        SunPy core package: Python for Solar Physics
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/sunpy/sunpy
Source0:        https://files.pythonhosted.org/packages/source/s/sunpy/sunpy-%{version}.tar.gz
# PATCH-FIX-OPENSUSE use custom hypothesis profile for slow OBS executions
Patch1:         sunpy-obs-profile.patch
BuildRequires:  %{python_module aioftp}
BuildRequires:  %{python_module astropy >= 6.1}
BuildRequires:  %{python_module devel >= 3.12}
BuildRequires:  %{python_module extension-helpers >= 1.3 with %python-extension-helpers < 2}
BuildRequires:  %{python_module fsspec >= 2023.6.0}
BuildRequires:  %{python_module numpy-devel >= 2}
BuildRequires:  %{python_module packaging >= 23.2}
BuildRequires:  %{python_module parfive >= 2.1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyerfa >= 2.0.1.1}
BuildRequires:  %{python_module requests >= 2.32}
BuildRequires:  %{python_module setuptools >= 62}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 6.1
Requires:       python-fsspec >= 2023.6.0
Requires:       python-numpy >= 1.26
Requires:       python-packaging >= 23.2
Requires:       python-parfive >= 2.1.0
Requires:       python-pyerfa >= 2.0.1.1
Requires:       python-requests >= 2.32.1
# parfive[ftp], ignore rpmlint's python-leftover-require
Requires:       python-aioftp >= 0.17.1
# SECTION project.optional-dependencies:asdf
Recommends:     python-asdf >= 3
Recommends:     python-asdf-astropy >= 0.5
# /SECTION
# SECTION project.optional-dependencies:dask
Suggests:       python-dask-array >= 2023.6
# /SECTION
# SECTION project.optional-dependencies:image
Recommends:     python-scipy >= 1.12
# /SECTION
# SECTION project.optional-dependencies:jpeg2000
Recommends:     python-Glymur >= 0.11
Recommends:     python-lxml >= 5.0.1
# /SECTION
# SECTION project.optional-dependencies:map
Recommends:     python-matplotlib >= 3.8.0
Recommends:     python-mpl-animators >= 1.2.0
Recommends:     python-reproject >= 0.13.0
# scipy
# /SECTION
# SECTION project.optional-dependencies:net
Recommends:     python-beautifulsoup4 >= 4.13.0
Recommends:     python-drms >= 0.7.1
Recommends:     python-python-dateutil >= 2.9.0
Recommends:     python-tqdm >= 4.66
Recommends:     python-zeep >= 4.3.0
# /SECTION
# SECTION project.optional-dependencies:opencv
Recommends:     python-opencv >= 4.8.0.74
# SECTION project.optional-dependencies:scikit-image
Recommends:     python-scikit-image >= 0.21
# /SECTION
# SECTION project.optional-dependencies:timeseries
Recommends:     python-cdflib >= 1.3.2
Recommends:     python-h5netcdf >= 1.2
Recommends:     python-h5py >= 3.10
Recommends:     python-pandas >= 2.2
#               matplotlib
# /SECTION
# SECTION project.optional-dependencies:visualization
#               matplotlib
#               mpl-animators
# /SECTION
# SECTION project.optional-dependencies:jupyter
Recommends:     python-itables >= 2.2.4
Recommends:     python-ipywidgets >= 8.1.0
# /SECTION
# SECTION test requirements (and extras)
BuildRequires:  %{python_module asdf >= 3}
BuildRequires:  %{python_module asdf-astropy >= 0.5}
BuildRequires:  %{python_module beautifulsoup4 >= 4.13.0}
BuildRequires:  %{python_module cdflib >= 1.3.2}
BuildRequires:  %{python_module dask-array >= 2023.6}
BuildRequires:  %{python_module drms >= 0.7.1}
BuildRequires:  %{python_module h5netcdf >= 1.2}
BuildRequires:  %{python_module h5py >= 3.10}
BuildRequires:  %{python_module hypothesis >= 6.0.0}
BuildRequires:  %{python_module ipywidgets >= 8.1.0}
#BuildRequires: %%{python_module itables >= 2.2.4}
BuildRequires:  %{python_module jplephem >= 2.19}
#BuildRequires:  %%{python_module pytest-mpl >= 0.18}
BuildRequires:  %{python_module pytest-mpl >= 0.17}
BuildRequires:  %{python_module lxml >= 5.0.1}
BuildRequires:  %{python_module matplotlib >= 3.8.0}
BuildRequires:  %{python_module mpl-animators >= 1.2.0}
BuildRequires:  %{python_module pandas >= 2.2}
BuildRequires:  %{python_module pytest >= 7.1}
BuildRequires:  %{python_module pytest-asdf-plugin >= 0.1.1}
BuildRequires:  %{python_module pytest-astropy >= 0.11}
BuildRequires:  %{python_module pytest-xdist >= 3.0.2}
BuildRequires:  %{python_module reproject >= 0.13}
BuildRequires:  %{python_module scikit-image >= 0.21}
BuildRequires:  %{python_module scipy >= 1.12}
BuildRequires:  %{python_module zeep >= 4.3}
BuildRequires:  python3-opencv
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
if [ "%{$python_provides}" != "python3" ]; then
  $python_donttest=" or opencv or (test_transform and (test_nans or test_clipping))"
fi
}
# fails because it does not find any opencv-python dist metadata (even for python3-opencv installed)
donttest="test_self_test"
# max age: not online for IERS updates
donttest="$donttest or test_print_params"
# FutureWarning of type cast in astropy. Don't bother here.
donttest="$donttest or (test_sxt_source and test_wcs)"
# spiceypy not available
%python_expand ignore="$ignore --ignore %{buildroot}%{$python_sitearch}/sunpy/coordinates/tests/test_spice.py"
%ifarch aarch64
# invalid cast of type
donttest="$donttest or test_plot_unit8"
%endif
%pytest_arch --pyargs sunpy -ra -n auto -k "not ($donttest ${$python_donttest})" $ignore
popd

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.rst licenses/*
%{python_sitearch}/sunpy
%{python_sitearch}/sunpy-%{version}.dist-info

%changelog
