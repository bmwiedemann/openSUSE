#
# spec file for package python-comfy-aimdo
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
Name:           python-comfy-aimdo
Version:        0.4.15
Release:        0
Summary:        AI Model Dynamic Offloader for ComfyUI (pure-Python fallback)
License:        GPL-3.0-only
URL:            https://github.com/Comfy-Org/comfy-aimdo
Source:         https://github.com/Comfy-Org/comfy-aimdo/archive/refs/tags/v%{version}.tar.gz#/comfy-aimdo-%{version}.tar.gz
# PATCH-FIX-UPSTREAM comfy-aimdo-detect-vendor-without-local-version.patch mpluskal@suse.com -- read torch's own cuda/hip attributes instead of the wheel-only version suffix, and skip quietly when there is no accelerator
Patch0:         comfy-aimdo-detect-vendor-without-local-version.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module setuptools-scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-torch >= 2.8.0
BuildArch:      noarch
%python_subpackages

%description
AIMDO (AI Model Dynamic Offloader) is a PyTorch VRAM allocator used by
ComfyUI to offload model weights under memory pressure. This build ships
the pure-Python fallback. The native CUDA/HIP allocator is not compiled:
it requires CUDA 12.8+ and a CUDA-enabled PyTorch, which Factory does
not provide. Without the native module, init() returns False and ComfyUI
continues without AIMDO.

%prep
%autosetup -p1 -n comfy-aimdo-%{version}

%build
# GitHub tag archives have no .git; pin the tagged version for setuptools-scm.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfy_aimdo
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No upstream test suite. The native aimdo.so is not built; confirm the
# Python modules import and the loader leaves lib unset.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import comfy_aimdo.control, comfy_aimdo.host_buffer, comfy_aimdo.model_mmap, comfy_aimdo.model_vbar, comfy_aimdo.vram_buffer; assert comfy_aimdo.control.lib is None"
# Patch0: without a CUDA or ROCm PyTorch, init() must report failure rather
# than guess a vendor, and it must not emit a warning while doing so.
cat > test_no_vendor.py <<'EOF'
import logging
import comfy_aimdo.control as c

seen = []


class Recorder(logging.Handler):
    def emit(self, record):
        seen.append(record)


logging.getLogger().addHandler(Recorder())
assert c.detect_vendor() is None, c.detect_vendor()
assert c.init() is False
assert c.lib is None
guesses = [r.getMessage() for r in seen
           if r.levelno >= logging.WARNING and "assuming Nvidia" in r.getMessage()]
assert not guesses, guesses
EOF
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B test_no_vendor.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/comfy_aimdo
%{python_sitelib}/comfy_aimdo-%{version}.dist-info

%changelog
