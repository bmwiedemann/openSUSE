#
# spec file for package python-uproot
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
%global modname uproot
Name:           python-uproot
Version:        5.7.5
Release:        0
Summary:        ROOT I/O in pure Python and Numpy
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scikit-hep/uproot5
Source0:        https://files.pythonhosted.org/packages/source/u/uproot/uproot-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-awkward >= 2.8.2
Requires:       python-cramjam >= 2.5.0
Requires:       python-fsspec
Requires:       python-numpy
Requires:       python-packaging
Requires:       python-xxhash
Suggests:       python-boost-histogram
Suggests:       python-cupy
Suggests:       python-hist
Suggests:       python-lz4
Suggests:       python-pandas
Suggests:       python-xrootd
Suggests:       python-zstandard
BuildArch:      noarch
# SECTION test requirements
# runtime
BuildRequires:  %{python_module awkward >= 2.8.2}
BuildRequires:  %{python_module cramjam >= 2.5.9}
BuildRequires:  %{python_module fsspec}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module xxhash}
# extras
BuildRequires:  %{python_module dask-array if %python-base >= 3.12}
BuildRequires:  %{python_module boost-histogram >= 0.13}
BuildRequires:  %{python_module dask-distributed if %python-base >= 3.12}
BuildRequires:  %{python_module pandas}
# test
BuildRequires:  %{python_module RangeHTTPServer}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-hep-testdata}
# /SECTION
# python-awkward no longer builds for 32-bit archs
ExcludeArch:    %{ix86} %{arm32}
%python_subpackages

%description
Uproot is a reader and a writer of the ROOT file format using only Python and
Numpy. Unlike the standard C++ ROOT implementation, Uproot is only an I/O
library, primarily intended to stream data into machine learning libraries in
Python. It uses Numpy to cast blocks of data from the ROOT file as Numpy
arrays.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export HOME=$PWD
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./)
# Network based tests
skip_network_tests=\
("-k" "not (test_0001_source_class or test_0006_notify_when_downloaded \
            or test_0007_single_chunk_interface or test_0692_fsspec_reading \
            or test_split_ranges_if_large_file_in_http \
            or test_descend_into_path_classname_of)" \
)
if [ $(getconf LONG_BIT) -eq 32 ]; then
# pandas tests assume 64bit types
skiptests32="(test_jagged_pandas or test_pandas_vector_TLorentzVector or test_iterate_pandas_2 or test_function_iterate_pandas_2 or test_0430)"
fi
# Skip test_decompression_executor_for_dask until we have dask-awkward packaged
# Skip test_1321_pandas_changed_api_again.py until we package awkward-pandas
%pytest "${skip_network_tests[@]} ${skiptests32} and not dask and not test_1321_pandas_changed_api_again"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
