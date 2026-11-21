#
# spec file for package python-array-api-compat
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


%define one_dot_version 1.16
Name:           python-array-api-compat
Version:        1.16.0
Release:        0
Summary:        Wrapper around NumPy and other array libraries
License:        MIT
URL:            https://data-apis.org/array-api-compat/
Source:         https://github.com/data-apis/array-api-compat/archive/refs/tags/%{one_dot_version}.tar.gz#/array_api_compat-%{version}.tar.gz
BuildRequires:  %{python_module meson-python}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.22}
BuildRequires:  %{python_module dask >= 2024.9.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
This is a small wrapper around common array libraries that is compatible with
the [Array API standard](https://data-apis.org/array-api/latest/). Currently,
NumPy, CuPy, PyTorch, Dask, JAX, ndonnx and `sparse` are supported. If you want
support for other array libraries, or if you encounter any issues, please [open
an issue](https://github.com/data-apis/array-api-compat/issues).

See the documentation for more details https://data-apis.org/array-api-compat/

%prep
%autosetup -p1 -n array-api-compat-%{one_dot_version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/array_api_compat
%{python_sitelib}/array_api_compat-%{version}.dist-info

%changelog
