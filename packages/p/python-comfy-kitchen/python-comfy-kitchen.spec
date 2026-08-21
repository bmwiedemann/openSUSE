#
# spec file for package python-comfy-kitchen
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
Name:           python-comfy-kitchen
Version:        0.2.31
Release:        0
Summary:        Fast kernel library for ComfyUI (CPU/eager backend)
# Legal-Review-Notice: NOTICE names the NVIDIA CUDA runtime EULA for a
# statically linked cudart used only by the CUDA backend. This build does
# not compile or ship that backend. BSD-3-Clause is from torchao-derived
# Python in the eager backend (quantization.py, float_utils.py).
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/Comfy-Org/comfy-kitchen
Source:         https://github.com/Comfy-Org/comfy-kitchen/archive/refs/tags/v%{version}.tar.gz#/comfy-kitchen-%{version}.tar.gz
# PATCH-FIX-OPENSUSE comfy-kitchen-cpu-only-build.patch mpluskal@suse.com -- honour COMFY_KITCHEN_BUILD_NO_CUDA for PEP 517 and drop CUDA/HIP-only build-system requires
Patch0:         comfy-kitchen-cpu-only-build.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module torch >= 2.5.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-torch >= 2.5.0
BuildArch:      noarch
# Match Factory python-torch (ExcludeArch: %%ix86 %%{arm})
ExcludeArch:    %{ix86} %{arm}
%python_subpackages

%description
Comfy Kitchen is a kernel library for diffusion-model inference used
by ComfyUI. This build ships the pure-Python eager (CPU) backend.
Native CUDA and HIP extensions are not compiled: Factory python-torch
is CPU-only and has no CUDA flavor.

%prep
%autosetup -p1 -n comfy-kitchen-%{version}

%build
# Factory python-torch is CPU-only. --no-cuda is a setup.py argv flag that
# PEP 517 does not pass at import time; the env var is the pep517 path.
export COMFY_KITCHEN_BUILD_NO_CUDA=1
export COMFY_KITCHEN_BUILD_NO_HIP=1
%pyproject_wheel

%install
%pyproject_install
# CUDA headers are setuptools package-data for native wheels. This CPU
# build does not compile that backend (devel-file-in-non-devel-package).
find %{buildroot} -type f \( -name '*.h' -o -name '*.cuh' \) -delete
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfy_kitchen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Upstream pytest is GPU-oriented (cuda/cupy/slow markers). Smoke-test the
# installed eager backend, which is what this CPU-only build ships.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import comfy_kitchen as ck; assert ck.list_backends()['eager']['available']"

%files %{python_files}
%license LICENSE NOTICE
%doc README.md
%{python_sitelib}/comfy_kitchen
%{python_sitelib}/comfy_kitchen-%{version}.dist-info

%changelog
