#
# spec file for package python-ormsgpack
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%{?sle15_python_module_pythons}
Name:           python-ormsgpack
Version:        1.12.2
Release:        0
Summary:        Fast Python msgpack library supporting dataclasses, datetimes, and numpy
License:        Apache-2.0 OR MIT
URL:            https://github.com/ormsgpack/ormsgpack
Source0:        https://files.pythonhosted.org/packages/source/o/ormsgpack/ormsgpack-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  rust
BuildRequires:  zstd
%python_subpackages

%description
ormsgpack is a fast msgpack library for Python. It is a fork of orjson's
msgpack support and serializes faster than other Python msgpack libraries.
It supports serializing dataclasses, datetimes, numpy arrays and pydantic
models natively.

%prep
%autosetup -a1 -n ormsgpack-%{version}

%build
export RUSTFLAGS=%{rustflags}
%pyproject_wheel

%install
export RUSTFLAGS=%{rustflags}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} python%{$python_bin_suffix} -B -c "import ormsgpack; print(ormsgpack.__version__)"

%files %{python_files}
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{python_sitearch}/ormsgpack
%{python_sitearch}/ormsgpack-%{version}.dist-info

%changelog
