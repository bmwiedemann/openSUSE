#
# spec file for package python-pytest-arraydiff-test
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python36 1
Name:           python-pytest-arraydiff%{psuffix}
Version:        0.3
Release:        0
Summary:        Pytest plugin to help with comparing array output from tests
License:        BSD-2-Clause
URL:            https://github.com/astropy/pytest-arraydiff
Source:         https://files.pythonhosted.org/packages/source/p/pytest-arraydiff/pytest-arraydiff-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-pytest
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module astropy if %python-base > 3}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
This is a py.test plugin to facilitate the generation and comparison of
data arrays produced during tests.

The basic idea is that you can write a test that generates a Numpy array (or
other related objects depending on the format). You can then either run the
tests in a mode to generate reference files from the arrays, or you can run
the tests in comparison mode, which will compare the results of the tests to
the reference ones within some tolerance.

At the moment, the supported file formats for the reference files are:

-  A plain text-based format (baSed on Numpy loadtxt output)
-  The FITS format (requires astropy). With this format, tests
   can return either a Numpy array for a FITS HDU object.

%prep
%setup -q -n pytest-arraydiff-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%{python_expand # u-a controlled pytest executable for nested pytest calls within tests
mkdir -p build/bin
ln -sf %{_bindir}/pytest-%{$python_bin_suffix} build/bin/pytest
}
export PATH="$PWD/build/bin:$PATH"
# not installed in :test multiflavor
export PYTHONPATH="$PWD"
# generate, default_format, test_fails, test_succeeds_func_fits_hdu tests need astropy that is python3 only, so skip
python2_donttest=" or test_generate or test_default_format or test_fails or test_succeeds_func_fits_hdu"
%pytest -k "not (donttestdummyprefix ${$python_donttest})"
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE
%{python_sitelib}/pytest_arraydiff
%{python_sitelib}/pytest_arraydiff-%{version}*-info
%endif

%changelog
