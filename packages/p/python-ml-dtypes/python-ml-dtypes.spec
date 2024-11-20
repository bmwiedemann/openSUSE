#
# spec file for package python-ml-dtypes
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-ml-dtypes
Version:        0.5.0
Release:        0
Summary:        stand-alone implementation of several NumPy dtype extensions
License:        Apache-2.0
URL:            https://github.com/jax-ml/ml_dtypes
Source:         https://files.pythonhosted.org/packages/source/m/ml-dtypes/ml_dtypes-%{version}.tar.gz
Source1:        https://github.com/jax-ml/ml_dtypes/archive/refs/tags/v%{version}.tar.gz#/ml-dtypes-%{version}-gh.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module abseil}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 2.0}
# /SECTION
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
Requires:       python-numpy >= 2.0
%python_subpackages

%description
`ml_dtypes` is a stand-alone implementation of several NumPy dtype extensions used in machine learning libraries, including:

- [`bfloat16`](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format):
  an alternative to the standard [`float16`](https://en.wikipedia.org/wiki/Half-precision_floating-point_format) format
- `float8_*`: several experimental 8-bit floating point representations
  including:
  * `float8_e3m4`
  * `float8_e4m3`
  * `float8_e4m3b11fnuz`
  * `float8_e4m3fn`
  * `float8_e4m3fnuz`
  * `float8_e5m2`
  * `float8_e5m2fnuz`
- Microscaling (MX) sub-byte floating point representations including:
  * `float4_e2m1fn`
  * `float6_e2m3fn`
  * `float6_e3m2fn`
- `int2`, `int4`, `uint2` and `uint4`: low precision integer types.

%prep
%autosetup -p1 -a1 -n ml_dtypes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest_arch -k "not testFInfo_float8_e8m0fnu"

%files %{python_files}
%{python_sitearch}/ml_dtypes
%{python_sitearch}/ml_dtypes-%{version}.dist-info

%changelog
