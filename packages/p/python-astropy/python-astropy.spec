#
# spec file for package python-astropy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define binaries fitsdiff fitsheader fitscheck fitsinfo fits2bitmap samp_hub showtable volint wcslint
%define         skip_python2 1
Name:           python-astropy
Version:        4.0.2
Release:        0
Summary:        Community-developed python astronomy tools
License:        BSD-3-Clause
URL:            https://astropy.org
Source:         https://files.pythonhosted.org/packages/source/a/astropy/astropy-%{version}.tar.gz
# PATCH-FIX-UPSTREAM astropy-pr10545-remove-newline-3d_cd_hdr.patch gh#astropy/astropy#10545 -- clean up newlines after pytest output
Patch0:         astropy-pr10545-remove-newline-3d_cd_hdr.patch
# Mark wcs headers as false positives for devel-file-in-non-devel-package
# These are used by the python files so they must be available.
Source100:      python-astropy-rpmlintrc
BuildRequires:  %{python_module Cython >= 0.21}
BuildRequires:  %{python_module astropy-helpers}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.16}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(erfa) >= 1.7.0
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(wcslib)
Requires:       hdf5
Requires:       liberfa1 >= 1.7.0
Requires:       python-dbm
Requires:       python-matplotlib >= 2.1
Requires:       python-numpy >= 1.7.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     libxml2-tools
Recommends:     python-Bottleneck
Recommends:     python-Jinja2
Recommends:     python-PyYAML
Recommends:     python-asdf >= 2.5
Recommends:     python-beautifulsoup4
Recommends:     python-bleach
Recommends:     python-h5py
Recommends:     python-ipython
Recommends:     python-jplephem
Recommends:     python-matplotlib >= 2.1
Recommends:     python-pandas
Recommends:     python-scikit-image
Recommends:     python-scipy >= 0.18
Conflicts:      perl-Data-ShowTable
%if %{with test}
# SECTION Optional requirements
BuildRequires:  %{python_module Bottleneck}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module asdf >= 2.5}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jplephem}
BuildRequires:  %{python_module matplotlib >= 2.1}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy >= 0.18}
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module astropy = %{version}}
BuildRequires:  %{python_module mpmath}
BuildRequires:  %{python_module objgraph}
BuildRequires:  %{python_module pytest >= 3.1}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-doctestplus >= 0.6}
BuildRequires:  %{python_module pytest-mpl}
# /SECTION
%endif
%python_subpackages

%description
Astropy is a package intended to contain core functionality and some
common tools needed for performing astronomy and astrophysics research with
Python. It also provides an index for other astronomy packages and tools for
managing them.

%if !%{with test}
%prep
%setup -q -n astropy-%{version}
%autopatch -p1

# Disable test failure on DeprecationWarnings
sed -i "/enable_deprecations_as_exceptions(/,/)/ d" astropy/conftest.py

# Make sure bundled libs are not used
rm -rf cextern/expat
rm -rf cextern/erfa
rm -rf cextern/cfitsio
rm -rf cextern/wcslib

echo "[build]" >> setup.cfg
echo "use_system_libraries=1" >> setup.cfg

%build
%python_build --use-system-libraries --offline

%install
%python_install --use-system-libraries --offline
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
chmod a-x %{buildroot}%{python_sitearch}/astropy/wcs/tests/data/header_with_time.fits

# Deduplicating files can generate a RPMLINT warning for pyc mtime
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
rm -rf %{buildroot}%{$python_sitearch}/astropy/io/misc/tests/__pycache__/__init__.*.pyc
rm -rf %{buildroot}%{$python_sitearch}/astropy/io/votable/tests/__pycache__/*_test.*.pyc
rm -rf %{buildroot}%{$python_sitearch}/astropy/io/votable/tests/__pycache__/__init__.*.pyc
rm -rf %{buildroot}%{$python_sitearch}/astropy/wcs/tests/__pycache__/__init__.*.pyc
rm -rf %{buildroot}%{$python_sitearch}/astropy/wcs/tests/extension/__pycache__/__init__.*.pyc
$python    -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/io/misc/tests/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/io/misc/tests/
$python    -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/io/votable/tests/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/io/votable/tests/
$python    -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/stats/bls/tests/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/stats/bls/tests/
$python    -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/wcs/tests/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/astropy/wcs/tests/
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%if %{with test}
%check
# test matrix is ill-conditioned and fails occasionally
# https://github.com/astropy/astropy/issues/10675
donttest="compound_fitting_with_units"
%ifarch aarch64
# doctest failure because of precision errors
  donttest+=" or bayesian_info_criterion_lsq"
%endif
# http://docs.astropy.org/en/latest/development/testguide.html#running-tests
# running pytest directly would require building the extensions inplace
%python_exec -B -c "import astropy, sys; sys.exit(astropy.test(args=\"-v -k \\\"not ($donttest)\\\"\"))"
%endif

%if !%{with test}
%post
%{expand:%(for b in %{binaries}; do echo "%%python_install_alternative $b"; done)}

%postun
%{expand:%(for b in %{binaries}; do echo "%%python_uninstall_alternative $b"; done)}

%files %{python_files}
%doc CHANGES.rst README.rst
%license licenses/*
%{expand:%(for b in %{binaries}; do echo "%%python_alternative %%{_bindir}/$b"; done)}
%{python_sitearch}/astropy/
%{python_sitearch}/astropy-%{version}-py*.egg-info
%endif

%changelog
