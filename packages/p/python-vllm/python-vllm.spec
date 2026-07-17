#
# spec file for package python-vllm
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


# vllm is intentionally NOT built as a python-singlespec package: it is tied to
# the flavour python-torch is built for.  Bind to the single primary python3.
%define pythons python313
# CPU variant.  We build with VLLM_TARGET_DEVICE=empty: no CUDA/GPU kernels and
# no compiled CPU C++ kernels either -- inference runs through torch's native
# CPU operators.  vLLM's own optimised aarch64/x86 CPU kernels additionally need
# a from-source oneDNN build and a working libtorch CMake config; the latter is
# currently broken in Factory's python-torch (its Caffe2Targets.cmake points at
# the in-tree lib/ paths that the package moves to the system libdir), so
# find_package(Torch) fails for any downstream C++ consumer.  Enabling the
# compiled kernels is tracked as a follow-up once that is resolved.
%define vllm_target_device empty
Name:           python-vllm
Version:        0.25.0
Release:        0
Summary:        A high-throughput and memory-efficient inference and serving engine for LLMs
License:        Apache-2.0
URL:            https://github.com/vllm-project/vllm
Source0:        https://files.pythonhosted.org/packages/source/v/vllm/vllm-%{version}.tar.gz
# PATCH-FIX-OPENSUSE vllm-relax-cpu-requirements.patch -- relax exact pins to what Factory ships and drop optional torchvision/torchaudio/torchcodec/intel-openmp
Patch0:         vllm-relax-cpu-requirements.patch
# PATCH-FIX-OPENSUSE vllm-cpu-disable-rust-frontend.patch -- do not build the ~575-crate Rust frontend (unvendorable offline; runtime-optional)
Patch1:         vllm-cpu-disable-rust-frontend.patch
BuildRequires:  %{python_module Jinja2}
# Runtime modules imported eagerly by "import vllm" (needed for the %%check smoke test).
BuildRequires:  %{python_module cachetools}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module packaging >= 24.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyproject-metadata}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module setuptools >= 77.0.3}
# setup.py imports setuptools_rust unconditionally at module top even though the
# Rust frontend build itself is disabled (see vllm-cpu-disable-rust-frontend.patch).
BuildRequires:  %{python_module setuptools-rust >= 1.9.0}
BuildRequires:  %{python_module setuptools-scm >= 8.0}
# setup.py imports torch at module top to detect the target device.
BuildRequires:  %{python_module torch = 2.12.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
# import torch dlopens libopenblas.so.0 at build time.
BuildRequires:  libopenblas_pthreads0
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.13.3
Requires:       python-anthropic >= 0.71.0
Requires:       python-blake3
Requires:       python-cachetools
Requires:       python-cbor2
Requires:       python-cloudpickle
Requires:       python-compressed-tensors = 0.17.0
Requires:       python-depyf = 0.20.0
Requires:       python-diskcache = 5.6.3
Requires:       python-einops
Requires:       python-fastapi >= 0.133.0
Requires:       python-filelock >= 3.16.1
Requires:       python-huggingface-hub
Requires:       python-ijson
Requires:       python-jsonschema >= 4.23.0
Requires:       python-lark >= 1.2.2
Requires:       python-llguidance >= 1.7.0
Requires:       python-lm-format-enforcer = 0.11.3
Requires:       python-mcp
Requires:       python-mistral-common >= 1.11.5
Requires:       python-model-hosting-container-standards >= 0.1.14
Requires:       python-msgspec
Requires:       python-numba >= 0.65.0
Requires:       python-numpy
Requires:       python-openai >= 2.0.0
Requires:       python-openai-harmony >= 0.0.3
Requires:       python-opencv >= 4.13.0
Requires:       python-opentelemetry-api >= 1.27.0
Requires:       python-opentelemetry-exporter-otlp >= 1.27.0
Requires:       python-opentelemetry-sdk >= 1.27.0
Requires:       python-opentelemetry-semantic-conventions-ai >= 0.4.1
Requires:       python-outlines_core = 0.2.14
Requires:       python-partial-json-parser
Requires:       python-Pillow
Requires:       python-prometheus-fastapi-instrumentator >= 8.0.0
Requires:       python-prometheus-client >= 0.18.0
Requires:       python-protobuf >= 5.29.6
Requires:       python-psutil
Requires:       python-py-cpuinfo
Requires:       python-pybase64
Requires:       python-pydantic >= 2.12.0
Requires:       python-pydantic-extra-types
Requires:       python-python-json-logger
Requires:       python-PyYAML
Requires:       python-pyzmq >= 25.0.0
Requires:       python-regex
Requires:       python-requests >= 2.26.0
Requires:       python-safetensors >= 0.6.2
Requires:       python-sentencepiece
Requires:       python-setproctitle
Requires:       python-six >= 1.16.0
Requires:       python-starlette >= 1.0.1
Requires:       python-tiktoken >= 0.6.0
Requires:       python-tokenizers >= 0.21.1
Requires:       python-torch = 2.12.0
Requires:       python-tqdm
Requires:       python-transformers >= 5.5.3
Requires:       python-typing_extensions >= 4.10
Requires:       python-watchfiles
Requires:       python-xgrammar >= 0.2.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Pure-Python content (VLLM_TARGET_DEVICE=empty builds no compiled extension).
BuildArch:      noarch
# Limited to the arches python-torch is built for.
ExclusiveArch:  x86_64 aarch64
%python_subpackages

%description
vLLM is a fast and easy-to-use library for LLM inference and serving.

This build runs CPU inference through PyTorch's native CPU operators
(VLLM_TARGET_DEVICE=empty): the CUDA/GPU kernels, vLLM's optional compiled
CPU kernels, the audio/video (torchaudio/torchcodec/torchvision) helpers and
the optional Rust-accelerated tool parser are not included.

%prep
%autosetup -p1 -n vllm-%{version}

# Use the torch already installed in the build root (2.12.0) instead of the
# exact 2.11.0 pin, via vLLM's own helper.  Strips torch/torchvision/torchaudio
# pins from requirements/*.txt and pyproject.toml.
%python_expand $python use_existing_torch.py --prefix

%build
export VLLM_TARGET_DEVICE=%{vllm_target_device}
# Keep the wheel/dist-info version exactly the upstream version (setup.py
# otherwise appends a local-version tag, which would not match the files list).
export VLLM_VERSION_OVERRIDE=%{version}
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
# Skip the Rust frontend build (see vllm-cpu-disable-rust-frontend.patch); avoids
# cargo reaching out to the network in the offline build root.
export VLLM_DISABLE_RUST_FRONTEND=1
%pyproject_wheel

%install
export VLLM_TARGET_DEVICE=%{vllm_target_device}
export VLLM_VERSION_OVERRIDE=%{version}
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
# Drop non-runtime data files that upstream ships inside the package tree.
%python_expand rm -f %{buildroot}%{$python_sitelib}/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/hf3fs_utils.cpp
%python_expand rm -f %{buildroot}%{$python_sitelib}/vllm/distributed/kv_transfer/disagg_prefill_workflow.jpg
%python_expand rm -f %{buildroot}%{$python_sitelib}/vllm/vllm_flash_attn/.gitkeep
# These modules carry a #!/usr/bin/env python shebang but are imported, not run.
%python_expand sed -i '1{/^#!/d}' %{buildroot}%{$python_sitelib}/vllm/entrypoints/grpc_server.py
%python_expand sed -i '1{/^#!/d}' %{buildroot}%{$python_sitelib}/vllm/entrypoints/openai/dp_supervisor.py
%python_clone -a %{buildroot}%{_bindir}/vllm
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export VLLM_TARGET_DEVICE=%{vllm_target_device}
# Import smoke test validating the package and its metadata load.
# Full model/serving tests need model weights and are out of scope here.
%python_expand $python -c "import vllm; print(vllm.__version__)"

%post
%python_install_alternative vllm

%postun
%python_uninstall_alternative vllm

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/vllm
%{python_sitelib}/vllm
%{python_sitelib}/vllm-%{version}.dist-info

%changelog
