#
# spec file for package python-sglang
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


Name:           python-sglang
Version:        0.5.18
Release:        0
Summary:        Fast serving framework for large language models
# Legal-Review-Notice: sgl-model-gateway and CUDA AOT kernels
# (python/sglang/kernels/aot) are in the GitHub tree but are not built
# or installed (aot excluded from the wheel). python/sglang/kernels/ops/
# attention/flash_attn/cute is a bundled FlashAttention CuTe DSL copy
# under BSD-3-Clause, shipped as Python package data.
# Rust PyO3 extensions (sglang-mm, sglang-grpc) are built from rust/
# against vendor.tar.zst. Re-derived with cargo tree --offline -e normal
# over those crates: BSD-2-Clause from numpy; BSD-3-Clause from
# subtle/matchit; Unicode-3.0 from icu_*/unicode-ident; ISC from
# rustls-webpki/untrusted; CDLA-Permissive-2.0 from webpki-roots.
# option-ext (MPL-2.0) reaches only sglang-server, but its sources ride
# along in vendor.tar.zst, which in the src.rpm satisfies MPL-2.0 §3.2.
# r-efi offers LGPL-2.1-or-later but is UEFI-target-only and absent from
# the Linux graph. sglang-server itself is not built: the CPU Python
# runtime does not use it and it drags in the whole dynamo stack.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND MIT AND MPL-2.0 AND Unicode-3.0
URL:            https://github.com/sgl-project/sglang
Source0:        https://github.com/sgl-project/sglang/archive/refs/tags/v%{version}.tar.gz#/sglang-%{version}.tar.gz
Source1:        vendor.tar.zst
# PATCH-FIX-OPENSUSE sglang-relax-cpu-requirements.patch -- >= floors (not exact pins), drop unpackaged CPU-inappropriate deps, name the dist sglang (not sglang-cpu)
Patch0:         sglang-relax-cpu-requirements.patch
# PATCH-FIX-OPENSUSE sglang-cpu-triton-stub.patch -- install upstream's triton stub when triton is not present so import sglang works
# The explicit importlib.machinery/importlib.util imports it also carries are upstream sgl-project/sglang PR 36215
Patch1:         sglang-cpu-triton-stub.patch
# PATCH-FIX-OPENSUSE sglang-cpu-rust-exts.patch -- build setuptools-rust PyO3 extensions (mm, grpc) from the CPU pyproject
Patch2:         sglang-cpu-rust-exts.patch
# PATCH-FIX-OPENSUSE sglang-grpc-system-protoc.patch -- use system protoc instead of protoc-bin-vendored
Patch3:         sglang-grpc-system-protoc.patch
BuildRequires:  %{python_module IPython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module SoundFile}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module anthropic >= 0.20.0}
BuildRequires:  %{python_module blobfile >= 3.0.0}
BuildRequires:  %{python_module compressed-tensors}
BuildRequires:  %{python_module datasets}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module easydict}
BuildRequires:  %{python_module einops}
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module gguf}
BuildRequires:  %{python_module interegular}
BuildRequires:  %{python_module llguidance >= 1.7.6}
BuildRequires:  %{python_module mistral-common >= 1.11.5}
BuildRequires:  %{python_module modelscope}
BuildRequires:  %{python_module msgspec}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module openai >= 2.6.1}
BuildRequires:  %{python_module openai-harmony >= 0.0.4}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module partial-json-parser}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module prometheus-client >= 0.20.0}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pybase64}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module python-multipart}
BuildRequires:  %{python_module pyzmq >= 25.1.2}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sentencepiece}
BuildRequires:  %{python_module setproctitle}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module setuptools-rust >= 1.10}
BuildRequires:  %{python_module setuptools-scm >= 8.0}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module tiktoken}
BuildRequires:  %{python_module timm >= 1.0.16}
BuildRequires:  %{python_module torch >= 2.12.0}
BuildRequires:  %{python_module torchaudio >= 2.11.0}
BuildRequires:  %{python_module torchvision >= 0.27.0}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module transformers >= 5.12.1}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module uvloop}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xgrammar >= 0.2.1}
BuildRequires:  %{python_module xxhash}
BuildRequires:  %{python_module zstandard}
BuildRequires:  alts
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
# import torch dlopens libopenblas.so.0 during %%check.
BuildRequires:  libopenblas_pthreads0
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  rust >= 1.92
BuildRequires:  zstd
BuildRequires:  pkgconfig(protobuf)
# pythondistdeps did not emit Requires-Dist from the uv-style wheel
# METADATA, so these manual Requires are load-bearing.
Requires:       alts
Requires:       python-Pillow
Requires:       python-SoundFile
Requires:       python-aiohttp
Requires:       python-anthropic >= 0.20.0
Requires:       python-blobfile >= 3.0.0
Requires:       python-compressed-tensors
Requires:       python-datasets
Requires:       python-easydict
Requires:       python-einops
Requires:       python-fastapi
Requires:       python-gguf
Requires:       python-interegular
Requires:       python-ipython
Requires:       python-llguidance >= 1.7.6
Requires:       python-mistral-common >= 1.11.5
Requires:       python-modelscope
Requires:       python-msgspec
Requires:       python-numpy
Requires:       python-openai >= 2.6.1
Requires:       python-openai-harmony >= 0.0.4
Requires:       python-orjson
Requires:       python-packaging
Requires:       python-partial-json-parser
Requires:       python-prometheus-client >= 0.20.0
Requires:       python-psutil
Requires:       python-pybase64
Requires:       python-pydantic
Requires:       python-python-multipart
Requires:       python-pyzmq >= 25.1.2
Requires:       python-requests
Requires:       python-scipy
Requires:       python-sentencepiece
Requires:       python-setproctitle
Requires:       python-tabulate
Requires:       python-tiktoken
Requires:       python-timm >= 1.0.16
Requires:       python-torch >= 2.12.0
Requires:       python-torchaudio >= 2.11.0
Requires:       python-torchvision >= 0.27.0
Requires:       python-tqdm
Requires:       python-transformers >= 5.12.1
Requires:       python-uvicorn
Requires:       python-uvloop
Requires:       python-xgrammar >= 0.2.1
Requires:       python-xxhash
Requires:       python-zstandard
# outlines 0.1.11 needs outlines_core 0.1.26 (fsm.guide); Factory/s:ml
# outlines_core is 0.2.14 (that module is gone) and vllm pins 0.2.14, so
# the 0.1.26 pin stays in the home cone only. Constrained decoding is
# optional — import sglang does not load outlines.
Suggests:       python-outlines
Suggests:       python-py-spy
Suggests:       python-smg-grpc-servicer
ExclusiveArch:  x86_64 aarch64
%python_subpackages

%description
SGLang is a fast serving framework for large language models and
vision language models.

This is a CPU build: inference uses PyTorch's native CPU operators.
The Rust PyO3 extensions (multimodal preprocess, native gRPC) are
built. The embedded Rust server is not. CUDA kernels, sgl-kernel
and flashinfer are not.

%prep
%autosetup -p1 -n sglang-%{version}
rm -f rust/rust-toolchain.toml
# vendor.tar.zst holds rust/.cargo/config.toml, rust/vendor and a
# regenerated rust/Cargo.lock (protoc-bin-vendored dropped).
tar -xf %{SOURCE1}
# setuptools-rust runs cargo from python/, which does not see rust/.cargo.
# CARGO_HOME is the reliable remap (same pattern as python-tokenizers).
mkdir -p .cargo-home
cat > .cargo-home/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$PWD/rust/vendor"
EOF

%build
%limit_build -m 2000
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export CARGO_HOME=$PWD/.cargo-home
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
# Upstream rust/Cargo.toml sets strip = true, which would empty debuginfo
export CARGO_PROFILE_RELEASE_STRIP=false
export PROTOC=%{_bindir}/protoc
pushd python
# pyproject_cpu.toml looks for LICENSE/README.md next to itself; they live
# at the repo root.
cp -f ../LICENSE ../README.md .
cp -f pyproject_cpu.toml pyproject.toml
%pyproject_wheel
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export CARGO_HOME=$PWD/.cargo-home
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
export PROTOC=%{_bindir}/protoc
pushd python
%pyproject_install
popd
%{python_expand \
rm -rf %{buildroot}%{$python_sitearch}/sglang/test \
       %{buildroot}%{$python_sitearch}/sglang/kernels/aot \
       %{buildroot}%{$python_sitearch}/sglang/multimodal_gen/test \
       %{buildroot}%{$python_sitelib}/sglang/test \
       %{buildroot}%{$python_sitelib}/sglang/kernels/aot \
       %{buildroot}%{$python_sitelib}/sglang/multimodal_gen/test
# CPU flavour never JIT-compiles these; shipping them scores
# devel-file-in-non-devel-package (badness 50 each) and fails rpmlint.
find %{buildroot} -type f \( \
  -name '*.h' -o -name '*.hpp' -o -name '*.c' -o -name '*.cc' \
  -o -name '*.cpp' -o -name '*.cxx' -o -name '*.cu' -o -name '*.cuh' \) -delete
# Triton autotune JSON dumps (and other data files) are mode 0755.
find %{buildroot}/%{$python_sitearch}/sglang %{buildroot}/%{$python_sitelib}/sglang \
  -type f -exec chmod a-x {} + 2>/dev/null || :
sed -i '1{/^#!/d}' %{buildroot}%{$python_sitearch}/sglang/cli/killall.py \
  %{buildroot}%{$python_sitelib}/sglang/cli/killall.py 2>/dev/null || :
$python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash \
  %{buildroot}%{$python_sitearch}/sglang %{buildroot}%{$python_sitelib}/sglang \
  2>/dev/null || :
}
%python_clone -a %{buildroot}%{_bindir}/sglang
%python_group_libalternatives sglang
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Full tests need model weights, a GPU and network. Smoke-test the import
# graph, the CLI, and that the Rust PyO3 extensions loaded.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch}:%{buildroot}%{$python_sitelib} $python -B -c "import sglang; print(sglang.__version__); import sglang.srt.rust_extensions._multimodal; import sglang.srt.rust_extensions._grpc"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch}:%{buildroot}%{$python_sitelib} %{buildroot}%{_bindir}/sglang-%{$python_bin_suffix} --help

%pre
%python_libalternatives_reset_alternative sglang

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/sglang
%{python_sitearch}/sglang
%{python_sitearch}/sglang-%{version}.dist-info

%changelog
