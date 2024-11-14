#
# spec file for package python-tokenizers
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


%if 0%{?suse_version} && 0%{?suse_version} < 1550
%global force_gcc_version 13
%endif

%{?sle15_python_module_pythons}
Name:           python-tokenizers
Version:        0.20.3
Release:        0
Summary:        Provides an implementation of today's most used tokenizers
License:        Apache-2.0
URL:            https://github.com/huggingface/tokenizers
Source0:        https://github.com/huggingface/tokenizers/archive/refs/tags/v%{version}.tar.gz#/tokenizers-%{version}.tar.gz
Source1:        registry.tar.zst
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}
Requires:       python-huggingface-hub
%python_subpackages

%description
Provides an implementation of today's most used tokenizers, with a focus on
performance and versatility.
* Train new vocabularies and tokenize, using today's most used tokenizers.
* Extremely fast (both training and tokenization), thanks to the Rust
  implementation. Takes less than 20 seconds to tokenize a GB of text on a
  server's CPU.
* Easy to use, but also extremely versatile.
* Designed for research and production.
* Normalization comes with alignments tracking. It's always possible to get the
  part of the original sentence that corresponds to a given token.
* Does all the pre-processing: Truncate, Pad, add the special tokens your model
  needs.

%prep
%autosetup -p1 -n tokenizers-%{version}
rm -rfv .cargo
tar xf %{S:1} -C $PWD

%build
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
pushd bindings/python
%pyproject_wheel
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%install
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
pushd bindings/python
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}/*

%check
export CARGO_HOME=$PWD/.cargo
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
# See https://doc.rust-lang.org/cargo/reference/config.html#hierarchical-structure
%{cargo_test} --manifest-path ./tokenizers/Cargo.toml --lib

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/tokenizers*

%changelog
