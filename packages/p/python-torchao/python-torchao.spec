#
# spec file for package python-torchao
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
Name:           python-torchao
Version:        0.17.0
Release:        0
Summary:        PyTorch native quantization and sparsity
# Legal-Review-Notice: root LICENSE is BSD-3-Clause. prototype/paretoq
# models/configuration_llama.py and modeling_llama_quant.py are Apache-2.0
# HuggingFace/EleutherAI Llama configs; prototype/spinquant/hadamard_utils.py
# is adapted from QuaRot (Apache-2.0). The empty third_party/cutlass git
# submodule is not built (CPU, USE_CPP=0).
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/pytorch/ao
Source:         https://github.com/pytorch/ao/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module torch}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# setup.py does not declare install_requires; pythondistdeps sees no
# Requires-Dist in the wheel METADATA
Requires:       python-torch
BuildArch:      noarch
%python_subpackages

%description
TorchAO is a PyTorch-native library for quantization and sparsity of
model weights and activations, for both training and inference. It
integrates with torch.compile and FSDP2. This package is the CPU,
pure-Python build (no CUDA kernels).

%prep
%autosetup -p1 -n ao-%{version}

%build
# CPU/no-CUDA cone. setup.py defaults to USE_CPP=1, but on Linux that
# compiles nothing without CUDA_HOME or USE_CPU_KERNELS=1 (and the
# latter injects -march=native). USE_CPP=0 is the documented
# pure-Python fallback, matching the PyPI py3-none-any wheel.
# VERSION_SUFFIX must be empty: otherwise setup.py appends +git and
# the dist-info version no longer matches %%{version}.
export USE_CPP=0
export VERSION_SUFFIX=
export USE_SYSTEM_LIBS=1
%pyproject_wheel

%install
%pyproject_install
# find_packages() also picks up the top-level test/ tree
%python_expand rm -rf %{buildroot}%{$python_sitelib}/test
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/torchao
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Full pytest is huge and pulls HuggingFace checkpoints over the
# network. Smoke-test the import SGLang uses.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import torchao; from torchao.quantization import quantize_; assert torchao.__version__ == '%{version}'"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/torchao
%{python_sitelib}/torchao-%{version}.dist-info

%changelog
