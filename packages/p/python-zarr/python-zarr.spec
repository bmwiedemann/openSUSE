#
# spec file for package python-zarr
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-zarr
Version:        3.4.1
Release:        0
Summary:        An implementation of chunked, compressed, N-dimensional arrays for Python
License:        MIT
URL:            https://github.com/zarr-developers/zarr-python
Source:         https://files.pythonhosted.org/packages/source/z/zarr/zarr-%{version}.tar.gz
# Needs full python stdlib, base is not enough
BuildRequires:  %{pythons}
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling >= 1.29.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python >= 3.12
Requires:       python-donfig >= 0.8
Requires:       python-google-crc32c >= 1.5
Requires:       python-msgspec >= 0.19
Requires:       python-numcodecs >= 0.16
Requires:       python-numpy >= 2.0
Requires:       python-packaging >= 22
Requires:       python-typing_extensions >= 4.14
Suggests:       python-dbm
Suggests:       python-ipytree
BuildArch:      noarch
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module packaging >= 22}
BuildRequires:  %{python_module donfig >= 0.8}
BuildRequires:  %{python_module google-crc32c >= 1.5}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module msgspec >= 0.19}
BuildRequires:  %{python_module numcodecs >= 0.16}
BuildRequires:  %{python_module numpy >= 2.0}
BuildRequires:  %{python_module numpydoc}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module typing_extensions >= 4.14}
# /SECTION
%python_subpackages

%description
An implementation of chunked, compressed, N-dimensional arrays for Python.

%prep
%autosetup -p1 -n zarr-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/zarr
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -v tests/test_examples.py
# https://pytest-xdist.readthedocs.io/en/stable/known-limitations.html
donttestparallel="test_docstring_consistent_parameters"
# 32-bit failures in tests: not able to allocate that much memory
if [ $(getconf LONG_BIT) -eq 32 ]; then
  donttest+=" or (test_e2e and (test_read_array or test_write_array) and batched)"
  donttest+=" or test_sparse_selections_on_arrays_with_many_chunks"
  donttest+=" or test_sparse_indexer_projection_reconstructs_coordinates"
  donttest+=" or test_coordinate_indexer_many_chunks"
fi
# these take long
donttest+=" or (test_indexing and test_sharded_morton and memory)"
donttest+=" or test_basic_indexing_complex_rectilinear"
%pytest -n auto -k "not ($donttestparallel $donttest)" --ignore src/zarr
%pytest -k "$donttestparallel" --ignore src/zarr

%pre
%python_libalternatives_reset_alternative zarr

%post
%python_install_alternative zarr

%postun
%python_uninstall_alternative zarr

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/zarr
%{python_sitelib}/zarr
%{python_sitelib}/zarr-%{version}.dist-info

%changelog
