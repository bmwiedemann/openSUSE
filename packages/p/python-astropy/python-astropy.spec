#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%define binaries fitsdiff fitsheader fitscheck fitsinfo fits2bitmap samp_hub showtable volint wcslint

# backwards compatibility for --without systemlibs
%bcond_without systemlibs

%if %{with systemlibs}
%bcond_without system_cfitsio
%bcond_without system_expat
%bcond_without system_wcslib
%else
%bcond_with system_cfitsio
%bcond_with system_expat
%bcond_with system_wcslib
%endif

%if %{with system_cfitsio}
%define unbundle_cfitsio export ASTROPY_USE_SYSTEM_CFITSIO=1
%endif
%if %{with system_expat}
%define unbundle_expat   export ASTROPY_USE_SYSTEM_EXPAT=1
%endif
%if %{with system_wcslib}
%define unbundle_wcs     export ASTROPY_USE_SYSTEM_WCSLIB=1
%endif
%define unbundle_libs %{?unbundle_cfitsio} \
                      %{?unbundle_expat} \
                      %{?unbundle_wcs}

Name:           python-astropy%{psuffix}
Version:        5.2
Release:        0
Summary:        Community-developed python astronomy tools
License:        BSD-3-Clause
URL:            https://astropy.org
Source:         https://files.pythonhosted.org/packages/source/a/astropy/astropy-%{version}.tar.gz
# SourceRepository: https://github.com/astropy/astropy
# Mark wcs headers as false positives for devel-file-in-non-devel-package
# These are used by the python files so they must be available.
Source100:      python-astropy-rpmlintrc
# PATCH-FIX-UPSTREAM
Patch1:         https://github.com/astropy/astropy/pull/14194.patch#/astropy-pr14194-numpy1.24.patch
# https://docs.astropy.org/en/v5.2/install.html#requirements
BuildRequires:  %{python_module Cython >= 0.29.30}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module numpy-devel >= 1.20}
BuildRequires:  %{python_module packaging >= 19.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyerfa >= 2.0}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.13
Requires:       python-dbm
Requires:       python-numpy >= 1.20
Requires:       python-packaging >= 19.0
Requires:       python-pyerfa >= 2.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     libxml2-tools
Recommends:     python-Bottleneck
Recommends:     python-asdf >= 2.9.2
Recommends:     python-asdf-astropy
Recommends:     python-beautifulsoup4
Recommends:     python-bleach
Recommends:     python-h5py
Recommends:     python-html5lib
Recommends:     python-jplephem
Recommends:     python-matplotlib >= 3.1
Recommends:     python-mpmath
Recommends:     python-pandas
Recommends:     python-pyarrow >= 5
Recommends:     python-scipy >= 1.5
Recommends:     python-setuptools
Recommends:     python-sortedcontainers
Recommends:     python-typing_extensions >= 3.10.0.1
Conflicts:      perl-Data-ShowTable
Conflicts:      python-matplotlib = 3.4.0
Conflicts:      python-matplotlib = 3.5.2
%if %{with system_cfitsio}
BuildRequires:  pkgconfig(cfitsio)
%endif
%if %{with system_expat}
BuildRequires:  pkgconfig(expat)
%endif
%if %{with system_wcslib}
BuildRequires:  pkgconfig(wcslib) >= 7
%endif
%if %{with test}
# SECTION Optional requirements
BuildRequires:  %{python_module Bottleneck}
BuildRequires:  %{python_module asdf >= 2.10.0}
BuildRequires:  %{python_module asdf-astropy}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module jplephem}
BuildRequires:  %{python_module matplotlib >= 3.1}
BuildRequires:  %{python_module mpmath}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module scipy >= 1.3}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module typing_extensions >= 3.10.0.1}
BuildRequires:  libxml2-tools
# /SECTION
# SECTION test requirements
# We need the compiled package for testing
BuildRequires:  %{python_module astropy = %{version}}
BuildRequires:  %{python_module ipython >= 4.2}
BuildRequires:  %{python_module objgraph}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module pytest-astropy >= 0.10}
BuildRequires:  %{python_module pytest-astropy-header >= 0.2.1}
BuildRequires:  %{python_module pytest-doctestplus >= 0.12}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module sgp4 >= 2.3}
BuildRequires:  %{python_module skyfield >= 1.20}
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
# avoid rpmlint zero-length error for empty module
echo '# empty module' > astropy/samp/setup_package.py

# Make sure bundled libs are not used
%if %{with system_cfitsio}
rm -rf cextern/cfitsio
%endif
%if %{with system_expat}
rm -rf cextern/expat
rm licenses/EXPAT_LICENSE.rst
%endif
%if %{with system_wcslib}
rm -rf cextern/wcslib
rm licenses/WCSLIB_LICENSE.rst
%endif

# increase test deadline for slow obs executions (e.g. on s390x)
echo "
import hypothesis
hypothesis.settings.register_profile(
    'obs',
    deadline=5000,
    suppress_health_check=[hypothesis.HealthCheck.too_slow]
)
" >> astropy/conftest.py
sed -i 's/--color=yes//' setup.cfg

%build
%{?unbundle_libs}
%pyproject_wheel

%install
%{?unbundle_libs}
%pyproject_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done

%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# these are flaky on obs
donttest="test_color_print3"
donttest+=" or test_ignore_sigint"
donttest+=" or (test_wcs and test_spectra)"
donttest+=" or (test_standard_profile and test_main)"
# segfaults on obs, but are okay when run on live system -- gh#astropy/astropy/13286
donttest+=" or test_celprm or test_prjprm"
# gh#astropy/astropy#13805 -- requires fix in matplotlib
donttest+=" or test_units"
%ifarch aarch64
# doctest failure because of precision errors
  donttest+=" or bayesian_info_criterion_lsq"
%endif
%ifarch %arm32
  # gh#astropy/astropy#12017
  donttest+=" or test_stats"
%endif
%ifarch %ix86 %arm
  donttest+=" or (test_models_quantities and test_models_fitting and LevMarLSQFitter)"
%endif
# http://docs.astropy.org/en/latest/development/testguide.html#running-tests
# running pytest directly would require building the extensions inplace
%{python_exec -B -c "
import sys, astropy
pytestargs = ('-v '
              '-n auto ' # pytest-xdist
              '-p no:cacheprovider '
              '--hypothesis-profile=obs '
              '-k \"not ($donttest)\"')
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
%{python_sitearch}/astropy-%{version}.dist-info
%endif

%changelog
