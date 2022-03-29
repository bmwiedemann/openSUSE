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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
%define skip_python2 1
Name:           python-construct%{?psuffix}
Version:        2.10.68
Release:        0
Summary:        A declarative parser/builder for binary data
License:        MIT
URL:            https://github.com/construct/construct
Source:         https://github.com/construct/construct/archive/v%{version}.tar.gz#/construct-%{version}.tar.gz
Patch0:         split_debug.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-arrow
Recommends:     python-cloudpickle
Recommends:     python-lz4
Recommends:     python-numpy
Recommends:     python-ruamel.yaml
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
%endif
%python_subpackages

%description
Construct is a declarative parser (and builder) for binary data.

Instead of writing imperative code to parse a piece of data, a data
structure that describes the data is declared. As this data structure is not
code, it can be used in one direction to parse data into Pythonic objects,
and in the other direction to convert ("build") objects into binary data.

%prep
%setup -q -n construct-%{version}
%patch0 -p1

# remove gallery tests that require in place stuff
rm -rf tests/gallery
rm -rf tests/deprecated_gallery

%build
%if %{without test}
%python_build
%endif

%install
%if %{without test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# local source dir is needed for tests
export PYTHONPATH=$(pwd)
# Don't test with NumPy in the python36 flavor, because python36-numpy is not in TW anymore
python36_donttest="numpy or test_overall_parse or test_overall_build or test_compiled_example_benchmark or test_compiled_example_integrity"
%pytest --benchmark-disable ${$python_donttest:+ -k "not (${$python_donttest})"}
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/construct
%{python_sitelib}/construct-%{version}-py%{python_version}.egg-info
%endif

%changelog
