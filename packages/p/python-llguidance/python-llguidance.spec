#
# spec file for package python-llguidance
#
# Copyright (c) 2026 SUSE LLC
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
Name:           python-llguidance
Version:        1.7.6
Release:        0
Summary:        Low-level Guidance (llguidance) bindings for constrained decoding
License:        Apache-2.0 AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND MIT AND MPL-2.0 AND Unicode-3.0
URL:            https://github.com/guidance-ai/llguidance
Source0:        https://github.com/guidance-ai/llguidance/archive/refs/tags/v%{version}.tar.gz#/llguidance-%{version}.tar.gz
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
%python_subpackages

%description
Bindings for the Low-level Guidance (llguidance) Rust library, providing
super-fast structured outputs and constrained decoding for large language
models. It supports context-free grammars, JSON schemas and Lark-style
syntax to constrain token generation.

%prep
%autosetup -p1 -n llguidance-%{version}
rm -rfv .cargo
tar xf %{SOURCE1} -C $PWD
# gbnf_to_lark is an importable library module, not an entry point; drop its
# spurious shebang and executable bit so it is treated as a plain module
sed -i '1{/^#!/d}' python/llguidance/gbnf_to_lark.py
chmod -x python/llguidance/gbnf_to_lark.py

%build
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true
%pyproject_install
# maturin only strips debuginfo (Cargo.toml profile); strip the symbol table
# from the extension module so it is not flagged as unstripped
%python_expand strip %{buildroot}%{$python_sitearch}/llguidance/_lib.abi3.so
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The upstream torch_tests suite requires torch, transformers, tiktoken and
# huggingface_hub which are not available in this build; fall back to an
# import smoke test of the compiled extension module.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "import llguidance"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/llguidance
%{python_sitearch}/llguidance-%{version}.dist-info

%changelog
