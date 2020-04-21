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
%define         skip_python2 1
Name:           python-astropy
Version:        4.0.1.post1
Release:        0
Summary:        Community-developed python astronomy tools
License:        BSD-3-Clause
URL:            https://astropy.org
Source:         https://files.pythonhosted.org/packages/source/a/astropy/astropy-%{version}.tar.gz
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
Recommends:     libxml2-tools
Recommends:     python-Jinja2
Recommends:     python-PyYAML
Recommends:     python-asdf >= 2.5
Recommends:     python-beautifulsoup4
Recommends:     python-Bottleneck
Recommends:     python-bleach
Recommends:     python-h5py
Recommends:     python-ipython
Recommends:     python-jplephem
Recommends:     python-matplotlib >= 2.1
Recommends:     python-pandas
Recommends:     python-scikit-image
Recommends:     python-scipy >= 0.18
Conflicts:      perl-Data-ShowTable
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
BuildRequires:  %{python_module mpmath}
BuildRequires:  %{python_module objgraph}
BuildRequires:  %{python_module pytest >= 3.1}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest-mpl}
# /SECTION
%python_subpackages

%description
Astropy is a package intended to contain core functionality and some
common tools needed for performing astronomy and astrophysics research with
Python. It also provides an index for other astronomy packages and tools for
managing them.

%prep
%setup -q -n astropy-%{version}

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

%check
export PYTHONDONTWRITEBYTECODE=1
# http://docs.astropy.org/en/latest/development/testguide.html#running-tests
%python_exec setup.py build_ext --inplace --offline
%ifarch aarch64 
# doctest failure because of precision errors
  %define skippytest -k 'not bayesian_info_criterion_lsq'
%endif
%{pytest_arch -W "ignore:the imp module is deprecated:DeprecationWarning" \
              -W "ignore:Unknown pytest.mark.openfiles_ignore:pytest.PytestUnknownMarkWarning" \
              --ignore "docs/whatsnew" %{?skippytest}
}

%files %{python_files}
%doc CHANGES.rst README.rst
%license licenses/*
%python3_only %{_bindir}/fitsdiff
%python3_only %{_bindir}/fitsheader
%python3_only %{_bindir}/fitscheck
%python3_only %{_bindir}/fitsinfo
%python3_only %{_bindir}/fits2bitmap
%python3_only %{_bindir}/samp_hub
%python3_only %{_bindir}/showtable
%python3_only %{_bindir}/volint
%python3_only %{_bindir}/wcslint
%{python_sitearch}/astropy/
%{python_sitearch}/astropy-%{version}-py*.egg-info

%changelog
