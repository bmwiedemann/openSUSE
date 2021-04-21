#
# spec file for package python-astropy-test
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%define binaries fitsdiff fitsheader fitscheck fitsinfo fits2bitmap samp_hub showtable volint wcslint

%if 0%{suse_version} <= 1500
# Use the bundled libraries for Leap 15.X, because the versions in the repos are too old
%bcond_with systemlibs
%else
%bcond_without systemlibs
%endif
%if %{with systemlibs}
%define unbundle_libs export ASTROPY_USE_SYSTEM_CFITSIO=1 \
                      export ASTROPY_USE_SYSTEM_EXPAT=1 \
                      export ASTROPY_USE_SYSTEM_WCSLIB=1
%endif

%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
# upcoming python3 multiflavor: minimum supported python is 3.7
%define         skip_python36 1
Name:           python-astropy%{psuffix}
Version:        4.2.1
Release:        0
Summary:        Community-developed python astronomy tools
License:        BSD-3-Clause
URL:            https://astropy.org
Source:         https://files.pythonhosted.org/packages/source/a/astropy/astropy-%{version}.tar.gz
# belongs to Patch1 --  gh/astropy/astropy#11260
Source1:        https://github.com/dhomeier/astropy/raw/wcs-distortion-headers/astropy/wcs/tests/data/dss.14.29.56-62.41.05.fits.gz
# Mark wcs headers as false positives for devel-file-in-non-devel-package
# These are used by the python files so they must be available.
Source100:      python-astropy-rpmlintrc
# PATCH-FIX-UPSTREAM astropy-pr11260-wcsfailures.patch -- gh/astropy/astropy#11260
Patch1:         astropy-pr11260-wcsfailures.patch
# https://docs.astropy.org/en/v4.1/install.html#requirements
BuildRequires:  %{python_module Cython >= 0.21}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module numpy-devel >= 1.17}
BuildRequires:  %{python_module pyerfa}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       python-dbm
Requires:       python-numpy >= 1.17
Requires:       python-pyerfa
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     libxml2-tools
Recommends:     python-Bottleneck
Recommends:     python-PyYAML >= 3.13
Recommends:     python-asdf >= 2.6
Recommends:     python-beautifulsoup4
Recommends:     python-bleach
Recommends:     python-h5py
Recommends:     python-html5lib
Recommends:     python-jplephem
Recommends:     python-matplotlib >= 3
Recommends:     python-mpmath
Recommends:     python-pandas
Recommends:     python-scipy >= 1.1
Recommends:     python-setuptools
Recommends:     python-sortedcontainers
Conflicts:      perl-Data-ShowTable
%if %{with systemlibs}
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(wcslib) >= 7
%endif
%if %{with test}
# SECTION Optional requirements
BuildRequires:  %{python_module Bottleneck}
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module asdf >= 2.6}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module jplephem}
BuildRequires:  %{python_module matplotlib >= 3}
BuildRequires:  %{python_module mpmath}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module scipy >= 1.1}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  libxml2-tools
# /SECTION
# SECTION test requirements
# We need the compiled package for testing
BuildRequires:  %{python_module astropy = %{version}}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module objgraph}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module sgp4}
BuildRequires:  %{python_module skyfield}
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
%autosetup -p1 -n astropy-%{version}

cp %{SOURCE1} astropy/wcs/tests/data/

%if %{with systemlibs}
# Make sure bundled libs are not used
rm -rf cextern/cfitsio
rm -rf cextern/expat
rm -rf cextern/wcslib
rm licenses/EXPAT_LICENSE.rst
rm licenses/WCSLIB_LICENSE.rst
%endif

# Disable test failure on DeprecationWarnings
sed -i "/enable_deprecations_as_exceptions(/,/)/ d" astropy/conftest.py
# increase test deadline for slow obs executions (e.g. on s390x)
echo "
import hypothesis
hypothesis.settings.register_profile('obs', deadline=2000)
" >> astropy/conftest.py

%build
%{?unbundle_libs}
%python_build

%install
%{?unbundle_libs}
%python_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done

%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%ifarch aarch64
# doctest failure because of precision errors
  donttest+=" or bayesian_info_criterion_lsq"
%endif
testselect_expr="${donttest:+-k \"not (${donttest# or })\"}"
# http://docs.astropy.org/en/latest/development/testguide.html#running-tests
# running pytest directly would require building the extensions inplace
%{python_exec -B -c "
import sys, astropy
pytestargs = ('-v '
              '-n auto ' # pytest-xdist
              '-p no:cacheprovider '
              '--hypothesis-profile=obs '
              '$testselect_expr')
returncode = astropy.test(args=pytestargs)
sys.exit(returncode)
"}
%endif

%if !%{with test}
%post
%{expand:%(for b in %{binaries}; do echo "%%python_install_alternative $b"; done)}

%postun
%{expand:%(for b in %{binaries}; do echo "%%python_uninstall_alternative $b"; done)}

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst licenses/*
%{expand:%(for b in %{binaries}; do echo "%%python_alternative %%{_bindir}/$b"; done)}
%{python_sitearch}/astropy/
%{python_sitearch}/astropy-%{version}*-info
%endif

%changelog
