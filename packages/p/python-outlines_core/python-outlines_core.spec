#
# spec file for package python-outlines_core
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
Name:           python-outlines_core
Version:        0.2.14
Release:        0
Summary:        Structured Text Generation in Rust
License:        Apache-2.0
URL:            https://github.com/dottxt-ai/outlines-core
Source0:        https://files.pythonhosted.org/packages/source/o/outlines_core/outlines_core-%{version}.tar.gz
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
Core functionality of the Outlines project for structured text generation,
implemented in Rust. Provides the building blocks used to guide language
model generation with regular expressions and JSON schemas, including the
regular-expression to finite-state-machine index, a vocabulary type and a
guide that constrains token-by-token generation.

%prep
%autosetup -p1 -n outlines_core-%{version}
rm -rfv .cargo
tar xf %{SOURCE1} -C $PWD

%build
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}/*
# The singlespec install loop stamps a _current_flavor bookkeeping marker into
# the site-packages dirs; drop every copy so none is shipped and the
# installed-but-unpackaged check passes (tolerant of which flavours have it).
find %{buildroot} -name _current_flavor -delete

%check
# The upstream pytest suite pulls unpackaged deps (torch, numba, asv,
# pytest-benchmark, ...) and downloads models from HuggingFace, so it is not
# runnable in the build root. Fall back to an import smoke test that exercises
# the compiled Rust extension and its re-exported symbols. Run it from a fresh
# empty directory (not the source tree, whose outlines_core/ package would
# shadow the extension, and not the buildroot sitearch, which the singlespec
# loop would then pollute with a _current_flavor marker) with the installed
# module on PYTHONPATH.
%python_expand d=$(mktemp -d) && cd "$d" && PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "import outlines_core; from outlines_core import Guide, Index, Vocabulary; from outlines_core.json_schema import build_regex_from_schema; assert callable(build_regex_from_schema)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/outlines_core
%{python_sitearch}/outlines_core-%{version}.dist-info

%changelog
