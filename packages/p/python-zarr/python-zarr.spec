#
# spec file for package python-zarr
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-zarr
Version:        2.18.4
Release:        0
Summary:        An implementation of chunked, compressed, N-dimensional arrays for Python
License:        MIT
URL:            https://github.com/zarr-developers/zarr-python
Source:         https://files.pythonhosted.org/packages/source/z/zarr/zarr-%{version}.tar.gz
# PATCH-FIX-OPENSUSE zarr-numcodecs-zstd-test.patch code@bnavigator.de -- Allow numcodecs < 0.13 for zstd tests, overrides gh#zarr-developers/zarr-python#2114
Patch0:         zarr-numcodecs-zstd-test.patch
# Needs full python stdlib, base is not enough
BuildRequires:  %{pythons}
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm > 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python >= 3.10
Requires:       python-asciitree
Requires:       python-fasteners
Requires:       python-numcodecs >= 0.10.0
Requires:       python-numpy >= 1.24
Conflicts:      (python-numcodecs >= 0.14.0 with python-numcodecs < 0.14.2)
Suggests:       python-dbm
Suggests:       python-ipytree
Suggests:       python-msgpack
Suggests:       python-notebook
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module asciitree}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module fasteners}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module numcodecs >= 0.14.2}
BuildRequires:  %{python_module numpy >= 1.24}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
An implementation of chunked, compressed, N-dimensional arrays for Python.

%prep
%autosetup -p1 -n zarr-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Numcodecs error, unknown
donttest="test_object_arrays_vlen_bytes"
# avoid broken tests in s390x, gh#zarr-developers/zarr-python#1375
%if "%_arch" == "s390x"
donttest+=" or test_hexdigest or test_nbytes_stored"
donttest+=" or test_array_1d or test_array_1d_fill_value or test_array_1d_selections"
donttest+=" or test_array_2d or test_array_2d_edge_case or test_array_order"
donttest+=" or test_resize_2d or test_append_2d or test_append_2d_axis"
donttest+=" or test_np_ufuncs or test_iter or test_islice or test_non_cont"
donttest+=" or test_read_nitems_less_than_blocksize_from_multiple_chunks"
donttest+=" or test_read_from_all_blocks"
donttest+=" or test_format_compatibility"
%endif
%pytest -n auto -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/zarr
%{python_sitelib}/zarr-%{version}.dist-info

%changelog
