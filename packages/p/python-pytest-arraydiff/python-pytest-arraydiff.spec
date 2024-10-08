#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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

Name:           python-pytest-arraydiff%{psuffix}
Version:        0.6.1
Release:        0
Summary:        Pytest plugin to help with comparing array output from tests
License:        BSD-2-Clause
URL:            https://github.com/astropy/pytest-arraydiff
Source:         https://files.pythonhosted.org/packages/source/p/pytest-arraydiff/pytest-arraydiff-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-pytest >= 4.6
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest >= 4.6}
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

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# not installed in :test multiflavor
export PYTHONPATH="$PWD"
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE
%{python_sitelib}/pytest_arraydiff
%{python_sitelib}/pytest_arraydiff-%{version}*-info
%endif

%changelog
