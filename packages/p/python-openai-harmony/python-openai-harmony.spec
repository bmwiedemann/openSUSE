#
# spec file for package python-openai-harmony
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
Name:           python-openai-harmony
Version:        0.0.8
Release:        0
Summary:        Renderer for the OpenAI harmony response format
License:        Apache-2.0
URL:            https://github.com/openai/harmony
Source0:        https://github.com/openai/harmony/archive/refs/tags/v%{version}.tar.gz#/harmony-%{version}.tar.gz
Source1:        registry.tar.zst
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2.11.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
Requires:       python-pydantic >= 2.11.7
ExclusiveArch:  %{rust_tier1_arches} riscv64
%python_subpackages

%description
Harmony is the response format used by OpenAI's open-weight gpt-oss model
series. It structures conversations into typed messages, roles and channels
and provides the tokenizer encodings the models expect.

This package provides the Python bindings, a thin typed convenience layer
backed by a compiled Rust extension, for rendering and parsing harmony
formatted conversations.

%prep
%autosetup -p1 -n harmony-%{version}
rm -rfv .cargo
tar xf %{SOURCE1} -C $PWD

%build
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
# Keep the debug symbols in the shared object so rpm's find-debuginfo can
# extract them into the -debugsource/-debuginfo packages instead of them
# being stripped by cargo (which leaves an unstrippable object).
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}/*

%check
# The upstream test-suite (tests/test_harmony.py) downloads the tiktoken
# encoding vocabularies from the network at import of load_harmony_encoding,
# which is unavailable in the build sandbox. Fall back to an import smoke
# test of the compiled extension plus the Python convenience layer.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -Bc "import openai_harmony; from openai_harmony import Message, Conversation, load_harmony_encoding"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/openai_harmony
%{python_sitearch}/openai_harmony-%{version}.dist-info

%changelog
