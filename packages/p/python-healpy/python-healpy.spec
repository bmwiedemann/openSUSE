#
# spec file for package python-healpy
#
# Copyright (c) 2020 SUSE LLC
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


# Builds on astropy, which is python >= 3.7 on TW
%define skip_python2 1
%define skip_python36 1
Name:           python-healpy
Version:        1.14.0
Release:        0
Summary:        Python library to handle pixelated data on the sphere based on HEALPix
License:        GPL-2.0-only
URL:            https://github.com/healpy/healpy
Source:         https://files.pythonhosted.org/packages/source/h/healpy/healpy-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE python-healpy-drop-pytest-runner.patch gh#healpy/healpy#649 badshah400@gmail.com -- Drop pytest-runner requirement for install: not required
Patch0:         python-healpy-drop-pytest-runner.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.13}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(healpix_cxx)
BuildRequires:  pkgconfig(libsharp)
Requires:       python-astropy >= 4.0
Requires:       python-matplotlib
Requires:       python-numpy >= 1.13
Requires:       python-scipy
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION Additional test requirements
# Symbol clashes with astropy < 4.0
BuildRequires:  %{python_module astropy >= 4.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
healpy is a Python package to handle pixelated data on the sphere. It is based
on the Hierarchical Equal Area isoLatitude Pixelization (HEALPix) scheme and
bundles the HEALPix C++ library.

healpy provides utilities to:
* convert between sky coordinates and pixel indices in HEALPix nested and ring schemes
* find pixels within a disk, a polygon or a strip in the sky
* apply coordinate transformations between Galactic, Ecliptic and Equatorial reference frames
* apply custom rotations either to vectors or full maps
* read and write HEALPix maps to disk in FITS format
* upgrade and downgrade the resolution of existing HEALPix maps
* visualize maps in Mollweide, Gnomonic and Cartographic projections
* transform maps to Spherical Harmonics space and back using multi-threaded C++ routines
* compute Auto and Cross Power Spectra from maps and create map realizations from spectra

%prep
%autosetup -p1 -n healpy-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a  %{buildroot}%{_bindir}/healpy_get_wmap_maps.sh
%python_expand %fdupes %{buildroot}%{$python_sitearch}
 

%check
# Skip tests requiring network access
%pytest_arch -k 'not (test_astropy_download_file or test_rotate_map_polarization or test_pixelweights_local_datapath)' %{buildroot}%{$python_sitearch}/healpy

%post
%python_install_alternative healpy_get_wmap_maps.sh

%postun
%python_uninstall_alternative healpy_get_wmap_maps.sh

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license COPYING
%python_alternative %{_bindir}/healpy_get_wmap_maps.sh
%{python_sitearch}/healpy/
%{python_sitearch}/healpy-%{version}-py%{python_version}.egg-info/

%changelog
