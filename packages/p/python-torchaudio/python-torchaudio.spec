#
# spec file for package python-torchaudio
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
Name:           python-torchaudio
Version:        2.11.0
Release:        0
Summary:        Audio signal processing for PyTorch
# Legal-Review-Notice: third_party/cuctc (BSD-2-Clause / BSD-3-Clause /
# Apache-2.0) is CUDA-only and is not built (USE_CUDA=0).
License:        BSD-2-Clause
URL:            https://github.com/pytorch/audio
Source:         https://github.com/pytorch/audio/archive/refs/tags/v%{version}.tar.gz#/torchaudio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module torch-devel}
BuildRequires:  %{python_module torch}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
# setup.py install_requires is empty; declare the runtime torch dep by hand.
Requires:       python-torch
# Match Factory python-torch (ExcludeArch: %%ix86 %%{arm})
ExcludeArch:    %{ix86} %{arm}
%python_subpackages

%description
TorchAudio applies PyTorch to the audio domain: GPU-optional
autograd-friendly transforms and a small set of C++ extensions
(lfilter, RNNT loss, forced alignment, overdrive). This build is
CPU-only against Factory python-torch 2.12 (CUDA disabled). Upstream
2.11.0 is the latest release and is documented as compatible with
later torch versions; there is no 2.12.0 torchaudio tag.

%prep
%autosetup -p1 -n audio-%{version}
# Upstream pyproject.toml has no [build-system] (only black/usort).
cat >> pyproject.toml <<'EOF'

[build-system]
requires = ["setuptools", "wheel", "torch"]
build-backend = "setuptools.build_meta"
EOF

%build
# Factory python-torch is CPU-only (standard/openmpi4, CUDA bcond off).
export USE_CUDA=0
export USE_ROCM=0
export BUILD_CUDA_CTC_DECODER=0
export BUILD_VERSION=%{version}
# PEP 517 exec of setup.py does not put the source dir on sys.path, so
# "from tools import setup_helpers" fails without this.
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
%pyproject_wheel

%install
export USE_CUDA=0
export USE_ROCM=0
export BUILD_CUDA_CTC_DECODER=0
export BUILD_VERSION=%{version}
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/torchaudio
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
cd %{_tmppath}
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -B -c "import torchaudio; assert torchaudio.__version__ == '%{version}', torchaudio.__version__"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/torchaudio
%{python_sitearch}/torchaudio-%{version}.dist-info

%changelog
