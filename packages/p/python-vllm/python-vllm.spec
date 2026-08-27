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
#
# Two multibuild flavours, differing only in VLLM_TARGET_DEVICE:
#
#   (default)  VLLM_TARGET_DEVICE=empty -- pure Python, no compiled extension.
#              Inference runs through torch's native CPU operators.  noarch.
#   cpu        VLLM_TARGET_DEVICE=cpu   -- vLLM's own optimised C++ CPU kernels,
#              which need a from-source static oneDNN (plus the Arm Compute
#              Library as oneDNN's backend on aarch64).  Arch-specific.
#
# The two are mutually exclusive: both provide the same importable vllm module,
# so the cpu flavour Conflicts with the default one and users pick exactly one.
%global         flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "cpu"
%define         psuffix -cpu
%define         vllm_target_device cpu
%bcond_without  cpu_kernels
%else
%define         psuffix %{nil}
%define         vllm_target_device empty
%bcond_with     cpu_kernels
%endif
# Upstream's exact pins from cmake/cpu_extension.cmake -- bump these together
# with any vllm update, they are version-locked to the kernel sources.
%define         onednn_aarch64_commit 9c5be1cc59e368aebf0909e6cf20f981ea61462a
%define         onednn_aarch64_commit_short 9c5be1cc
%define         onednn_x86_version 3.13
%define         acl_version 52.6.0
%bcond_without  libalternatives
Name:           python-vllm%{psuffix}
Version:        0.28.0
Release:        0
Summary:        A high-throughput and memory-efficient inference and serving engine for LLMs
License:        Apache-2.0
URL:            https://github.com/vllm-project/vllm
Source0:        https://files.pythonhosted.org/packages/source/v/vllm/vllm-%{version}.tar.gz
# cmake/cpu_extension.cmake builds oneDNN from source at an exact pin and, on
# aarch64, the Arm Compute Library as oneDNN's backend -- both via FetchContent
# straight from git, which the offline build root cannot do.  Ship them as
# Sources and point vLLM at the unpacked trees with the environment overrides
# it already honours (FETCHCONTENT_SOURCE_DIR_ONEDNN and ACL_ROOT_DIR).
# The two oneDNN pins are upstream's, and they genuinely differ per arch: the
# aarch64/ACL path needs a post-3.10 snapshot, x86_64 uses the 3.10 tag.
Source10:       https://github.com/oneapi-src/oneDNN/archive/%{onednn_aarch64_commit}.tar.gz#/oneDNN-%{onednn_aarch64_commit_short}.tar.gz
Source11:       https://github.com/oneapi-src/oneDNN/archive/refs/tags/v%{onednn_x86_version}.tar.gz#/oneDNN-%{onednn_x86_version}.tar.gz
Source12:       https://github.com/ARM-software/ComputeLibrary/archive/refs/tags/v%{acl_version}.tar.gz#/ComputeLibrary-%{acl_version}.tar.gz
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
BuildRequires:  %{python_module torch >= 2.12.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
# import torch dlopens libopenblas.so.0 at build time.
BuildRequires:  libopenblas_pthreads0
BuildRequires:  python-rpm-macros
Requires:       alts
# Several of upstream's requirements/*.txt entries are exact "== X.Y.Z" pins.
# Those describe upstream's own pinned developer/CI environment, not a proven
# incompatibility, and an exact RPM pin is actively harmful: it couples two
# independently released packages, so every update of either leaves the other
# uninstallable.  Nothing catches that -- the build still succeeds, because the
# breakage only happens at install time -- so it surfaces as a broken package in
# the target project.  Carry floors at the version upstream actually asks for
# instead; vllm-relax-cpu-requirements.patch relaxes the same pins in the wheel
# metadata so the RPM dependencies and the dist-info agree.
Requires:       python-Pillow
Requires:       python-PyYAML
Requires:       python-aiohttp >= 3.13.3
Requires:       python-anthropic >= 0.71.0
Requires:       python-blake3
Requires:       python-cachetools
Requires:       python-cbor2
Requires:       python-cloudpickle
# Upstream pins compressed-tensors == 0.17.0, but an exact RPM pin breaks the
# package every time the devel project moves.  Every symbol vllm imports from
# compressed_tensors exists unchanged in both 0.17.1 and 0.18.0 (the only delta
# on that surface is an added TransformConfig.merge()), so carry a floor.
Requires:       python-compressed-tensors >= 0.17.1
# Optional torch.compile debugging helper, imported lazily inside
# vllm/compilation only when compilation debug dumps are enabled.
Requires:       python-depyf >= 0.20.0
Requires:       python-einops
Requires:       python-fastapi >= 0.133.0
Requires:       python-filelock >= 3.16.1
Requires:       python-huggingface-hub >= 1.27.0
Requires:       python-ijson
Requires:       python-jsonschema >= 4.23.0
Requires:       python-lark >= 1.2.2
Requires:       python-llguidance >= 1.7.0
# One of the optional structured-output backends, LazyLoader-imported only when
# a request selects it.
Requires:       python-lm-format-enforcer >= 0.11.3
Requires:       python-mcp
Requires:       python-mistral-common >= 1.11.6
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
# Optional structured-output backend, also LazyLoader-imported.  Its on-disk
# index cache is keyed on importlib.metadata.version("outlines_core") and is
# cleared whenever that changes, so the code handles version drift by design.
Requires:       python-outlines_core >= 0.2.14
Requires:       python-partial-json-parser
Requires:       python-prometheus-client >= 0.18.0
Requires:       python-prometheus-fastapi-instrumentator >= 8.0.0
Requires:       python-protobuf >= 5.29.6
Requires:       python-psutil
Requires:       python-py-cpuinfo
Requires:       python-pybase64
Requires:       python-pydantic >= 2.12.0
Requires:       python-pydantic-extra-types
Requires:       python-python-json-logger
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
# The default flavour is pure Python and only uses torch's Python API.  The cpu
# flavour additionally links the compiled kernels against libtorch, and that
# coupling is already expressed by the automatic libtorch.so / libtorch_cpu.so /
# libc10.so dependencies rpm generates from the extension -- which is also what
# makes OBS rebuild this package when torch moves.  An exact pin adds nothing
# there and only makes the package uninstallable until it is bumped by hand.
Requires:       python-torch >= 2.12.0
Requires:       python-tqdm
Requires:       python-transformers >= 5.5.3
Requires:       python-typing_extensions >= 4.10
Requires:       python-watchfiles
Requires:       python-xgrammar >= 0.2.1
# Limited to the arches python-torch is built for.
ExclusiveArch:  x86_64 aarch64
%if %{with cpu_kernels}
# The compiled kernels need a C++ toolchain and torch's CMake package config,
# which ships in the -devel subpackage (find_package(Torch)).
BuildRequires:  %{python_module torch-devel >= 2.12.0}
BuildRequires:  cmake >= 3.26
BuildRequires:  gcc-c++
BuildRequires:  libnuma-devel
BuildRequires:  ninja
# torch's own Caffe2Config.cmake does find_package(Protobuf) and hard-fails
# without it, so find_package(Torch) needs protobuf present at build time.
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(zlib)
Conflicts:      python-vllm
# Both flavours install the same importable vllm module, so exactly one of them
# may be installed at a time.
Provides:       python-vllm = %{version}-%{release}
%endif
%if %{without cpu_kernels}
# Pure-Python content (VLLM_TARGET_DEVICE=empty builds no compiled extension).
BuildArch:      noarch
%endif
%python_subpackages

%description
vLLM is a fast and easy-to-use library for LLM inference and serving.

%if %{with cpu_kernels}
This build includes vLLM's optimised C++ CPU kernels (VLLM_TARGET_DEVICE=cpu),
backed by a statically linked oneDNN -- and, on aarch64, the Arm Compute
Library. The CUDA/GPU kernels, the audio/video (torchaudio/torchcodec/
torchvision) helpers and the optional Rust-accelerated tool parser are not
included. It conflicts with the plain python-vllm package; install one or the
other.
%else
This build runs CPU inference through PyTorch's native CPU operators
(VLLM_TARGET_DEVICE=empty): the CUDA/GPU kernels, vLLM's optional compiled
CPU kernels, the audio/video (torchaudio/torchcodec/torchvision) helpers and
the optional Rust-accelerated tool parser are not included. For the compiled
CPU kernels install python-vllm-cpu instead.
%endif

%prep
%autosetup -p1 -n vllm-%{version}
%if %{with cpu_kernels}
# Unpack the pinned oneDNN (and ACL, its aarch64 backend) beside the source
# tree; %%build points vLLM's FetchContent at them instead of letting it clone.
%ifarch aarch64
tar -xf %{SOURCE10} -C ..
tar -xf %{SOURCE12} -C ..
%else
tar -xf %{SOURCE11} -C ..
%endif
%endif

# Build against whatever torch the build root provides instead of upstream's
# exact 2.13.0 pin, via vLLM's own helper.  Strips torch/torchvision/torchaudio
# pins from requirements/*.txt and pyproject.toml.
%python_expand $python use_existing_torch.py --prefix

%build
export VLLM_TARGET_DEVICE=%{vllm_target_device}
%if %{with cpu_kernels}
# Point cpu_extension.cmake at the unpacked trees (both overrides are upstream's
# own, see cmake/cpu_extension.cmake) so no FetchContent clone is attempted.
%ifarch aarch64
export FETCHCONTENT_SOURCE_DIR_ONEDNN="$(readlink -f ../oneDNN-%{onednn_aarch64_commit})"
export ACL_ROOT_DIR="$(readlink -f ../ComputeLibrary-%{acl_version})"
%else
export FETCHCONTENT_SOURCE_DIR_ONEDNN="$(readlink -f ../oneDNN-%{onednn_x86_version})"
%endif
export CMAKE_GENERATOR=Ninja
export MAX_JOBS=%{?jobs:%{jobs}}%{!?jobs:4}
# cpu_extension.cmake does a bare find_library(OPEN_MP NAMES gomp REQUIRED),
# but only libgomp.so.1 lives in the default library path -- the unversioned
# link ships inside gcc's own version directory.  Ask gcc where it is instead
# of hardcoding a compiler version into the path.
export CMAKE_LIBRARY_PATH="$(dirname "$(gcc -print-file-name=libgomp.so)")${CMAKE_LIBRARY_PATH:+:$CMAKE_LIBRARY_PATH}"
# The x86 kernel variants (_C, _C_AVX2, _C_AVX512) link assembler objects that
# carry no .note.GNU-stack, so the linker conservatively marks the whole shared
# object's stack executable -- rpmlint scores that 10000 badness each and fails
# the build. Force a non-executable stack at link time; CMake seeds
# CMAKE_*_LINKER_FLAGS from $LDFLAGS on the first configure, and setup.py has no
# CMAKE_ARGS hook to pass it through instead.
export LDFLAGS="${LDFLAGS:-} -Wl,-z,noexecstack"
%endif
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
# The default flavour is pure Python and lands in sitelib; the cpu flavour
# builds a compiled extension and lands in sitearch.  Detect which one
# %%pyproject_install actually used rather than branching every line below.
%{python_expand # post-install cleanup
sd=%{buildroot}%{$python_sitelib}
[ -d "$sd/vllm" ] || sd=%{buildroot}%{$python_sitearch}
# Drop non-runtime data files that upstream ships inside the package tree.
rm -f $sd/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/hf3fs_utils.cpp
rm -f $sd/vllm/distributed/kv_transfer/disagg_prefill_workflow.jpg
rm -f $sd/vllm/vllm_flash_attn/.gitkeep
# These modules carry a #!/usr/bin/env python shebang but are imported, not run.
sed -i '1{/^#!/d}' $sd/vllm/entrypoints/grpc_server.py
sed -i '1{/^#!/d}' $sd/vllm/entrypoints/openai/dp_supervisor.py
%fdupes $sd
}
%python_clone -a %{buildroot}%{_bindir}/vllm
%python_group_libalternatives vllm

%check
export VLLM_TARGET_DEVICE=%{vllm_target_device}
# Import smoke test validating the package and its metadata load.
# Full model/serving tests need model weights and are out of scope here.
%python_expand $python -c "import vllm; print(vllm.__version__)"

%pre
# Migrate an install that still carries the old update-alternatives symlink.
%python_libalternatives_reset_alternative vllm

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/vllm
%if %{with cpu_kernels}
%{python_sitearch}/vllm
%{python_sitearch}/vllm-%{version}.dist-info
%else
%{python_sitelib}/vllm
%{python_sitelib}/vllm-%{version}.dist-info
%endif

%changelog
