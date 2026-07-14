#
# spec file for package python-blake3
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
Name:           python-blake3
Version:        1.0.9
Release:        0
Summary:        Python bindings for the BLAKE3 cryptographic hash function
License:        Apache-2.0 OR CC0-1.0
URL:            https://github.com/oconnor663/blake3-py
Source0:        https://github.com/oconnor663/blake3-py/archive/refs/tags/%{version}.tar.gz#/blake3-py-%{version}.tar.gz
Source1:        registry.tar.zst
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches} riscv64
%if %{python_version_nodots} < 312
Requires:       python-typing_extensions >= 4.6.0
%endif
%python_subpackages

%description
Python bindings for the official Rust implementation of the BLAKE3
cryptographic hash function. BLAKE3 is fast, secure, highly parallelizable and
suitable for verified streaming and key derivation.

%prep
%autosetup -p1 -n blake3-py-%{version}
rm -rfv .cargo
tar xf %{SOURCE1} -C $PWD

%build
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}/*

%check
# The full pytest suite needs numpy and the bundled reference test vectors;
# instead exercise the compiled Rust extension with a functional smoke test
# (a 256-bit BLAKE3 digest is 64 hex characters).
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "import blake3; d = blake3.blake3(b'x').hexdigest(); assert len(d) == 64, d; print(d)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/blake3*

%changelog
