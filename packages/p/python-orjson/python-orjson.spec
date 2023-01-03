#
# spec file for package python-orjson
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-orjson
Version:        3.8.3
Release:        0
Summary:        Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:        Apache-2.0 OR MIT
URL:            https://github.com/ijl/orjson
Source:         https://files.pythonhosted.org/packages/source/o/orjson/orjson-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  %{python_module maturin >= 0.12.19}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pendulum}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module xxhash}
BuildRequires:  timezone
# /SECTION
%python_subpackages

%description
orjson is a fast JSON library for Python.
It benchmarks as the fastest Python library for JSON.

%prep
%autosetup -a1 -n orjson-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test_numpy_array_d1_uintp and test_numpy_array_d1_intp fail on 32bit
# test_memory_loads_keys occasionally fails on crashes on ppc64le
%pytest_arch -k "not (test_numpy_array_d1_intp or test_numpy_array_d1_uintp or test_memory_loads_keys)"

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE-APACHE LICENSE-MIT
%{python_sitearch}/orjson*

%changelog
