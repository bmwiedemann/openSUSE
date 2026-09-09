#
# spec file for package headroom
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


# Application, not a multi-flavour library: one /usr/bin/headroom against
# the distribution primary interpreter.
%define pythons %{primary_python}
Name:           headroom
Version:        0.37.0
Release:        0
Summary:        Context optimization layer for LLM applications
# Legal-Review-Notice: headroom-ai is Apache-2.0. The shipped artefact is
# the maturin cdylib from crates/headroom-py (cargo tree --offline
# -p headroom-py -e normal, 277 crates over 539 vendored). The only
# copyleft licence in that graph is MPL-2.0 from option-ext 0.2.0 (via
# hf-hub -> dirs -> dirs-sys). r-efi offers LGPL-2.1-or-later but is
# UEFI-target-only and is not in the Linux graph. aws-lc-sys is vendored
# with the workspace but is not linked into headroom-py. MPL-2.0 section
# 3.2 is satisfied because vendor.tar.zst ships in the src.rpm.
License:        Apache-2.0 AND MPL-2.0
URL:            https://github.com/headroomlabs-ai/headroom
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module click >= 8.3.3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module litellm >= 1.86.2}
BuildRequires:  %{python_module maturin >= 1.5}
BuildRequires:  %{python_module opentelemetry-api >= 1.24.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 13.0.0}
BuildRequires:  %{python_module tiktoken >= 0.5.0}
BuildRequires:  %{python_module tomlkit >= 0.13.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  memory-constraints
BuildRequires:  python-rpm-macros
BuildRequires:  rust >= 1.80
Requires:       %{primary_python}-PyYAML >= 6.0
Requires:       %{primary_python}-click >= 8.3.3
Requires:       %{primary_python}-litellm >= 1.86.2
Requires:       %{primary_python}-opentelemetry-api >= 1.24.0
Requires:       %{primary_python}-pydantic >= 2.0.0
Requires:       %{primary_python}-rich >= 13.0.0
Requires:       %{primary_python}-tiktoken >= 0.5.0
Requires:       %{primary_python}-tomlkit >= 0.13.0
# ast-grep-cli on PyPI is a wheel wrapping the sg/ast-grep binary; Factory
# ships the real ast-grep package. Headroom binaries.resolve() searches PATH.
Requires:       ast-grep
# PyPI name is headroom-ai; PyPI "headroom" 0.2.7 is a different project.
Provides:       python3dist(headroom-ai) = %{version}
ExclusiveArch:  %{rust_tier1_arches}

%description
Headroom is a context-optimization layer for LLM applications. It compresses
tool output and conversation context so requests use fewer tokens, and ships
a command-line interface plus a compiled pyo3 extension (headroom._core).

This package is the core CLI. The optional [proxy] extra lives in the
headroom-proxy subpackage; without it, "headroom proxy" / "headroom wrap"
exit because ensure_proxy_dependencies() hard-imports that set. Code-aware
slicing shells out to the distro ast-grep binary rather than the
ast-grep-cli PyPI wheel.

%package proxy
Summary:        HTTP/MCP proxy extra for Headroom
Requires:       %{name} = %{version}
Requires:       %{primary_python}-fastapi >= 0.100.0
# httpx[http2]: Factory python-httpx only Recommends python-h2
Requires:       %{primary_python}-h2 >= 3.0
Requires:       %{primary_python}-httpx >= 0.24.0
Requires:       %{primary_python}-magika >= 0.6.0
# Extra is mcp>=1.28.1,<2; Factory python-mcp is 1.28.1
Requires:       %{primary_python}-mcp >= 1.28.1
Requires:       %{primary_python}-onnxruntime >= 1.24.0
Requires:       %{primary_python}-openai >= 2.14.0
Requires:       %{primary_python}-orjson >= 3.9.14
Requires:       %{primary_python}-sqlite-vec >= 0.1.6
Requires:       %{primary_python}-transformers >= 5.5.0
Requires:       %{primary_python}-uvicorn >= 0.23.0
Requires:       %{primary_python}-watchdog >= 4.0.0
Requires:       %{primary_python}-websockets >= 13.0
Requires:       %{primary_python}-zstandard >= 0.20.0
BuildArch:      noarch

%description proxy
Runtime extra matching pip install headroom-ai[proxy]: FastAPI/uvicorn
HTTP+MCP proxy, Magika content routing, ONNX Runtime, and sqlite-vec
(--memory). Stock "headroom proxy" and "headroom wrap" refuse to start
without this set.

%prep
%autosetup -p1 -a1
# Upstream pins an exact toolchain via rustup; drop it so the distribution
# rust/cargo is used instead of trying to invoke rustup at build time.
rm -f rust-toolchain.toml
# Upstream's release profile sets strip = "symbols", which discards the DWARF
# that find-debuginfo.sh needs to build the -debuginfo/-debugsource packages.
sed -i 's/^strip = "symbols"/strip = "none"/' Cargo.toml

%build
# Cap parallel rustc jobs by RAM. The release profile uses lto=thin and
# codegen-units=1, so a single crate compile is already heavy.
%limit_build -m 2000
export CARGO_PROFILE_RELEASE_STRIP=none
export CARGO_NET_OFFLINE=true
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/headroom
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The compiled extension lives in sitearch. Do not pull [proxy] extras;
# those tests and the live/real_llm markers need network or unpackaged deps.
#
# PYTHONSAFEPATH: the source tree has a headroom/ package without _core.so.
# cwd is otherwise prepended to sys.path ahead of PYTHONPATH, so
# "import headroom" would bind the in-tree copy and then fail on _core.
export PYTHONSAFEPATH=1
export PYTHONPATH=%{buildroot}%{python_sitearch}
export PATH=%{buildroot}%{_bindir}:$PATH
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -P -c "import headroom, headroom._core; print(headroom.__version__)"
headroom --version
headroom --help
# Offline unit tests that only need the core runtime (click).
%pytest_arch tests/cli/test_utils.py

%files
%license LICENSE NOTICE
%doc README.md CHANGELOG.md
%{_bindir}/headroom
%{python_sitearch}/headroom
%{python_sitearch}/headroom_ai-%{version}.dist-info

%files proxy

%changelog
