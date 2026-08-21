#
# spec file for package python-torchvision
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
Name:           python-torchvision
Version:        0.27.0
Release:        0
Summary:        Image datasets, models and transforms for PyTorch
# Legal-Review-Notice: ships a bundled giflib 5.2.2 (MIT) under
# torchvision/csrc/io/image/cpu/giflib/, compiled into torchvision.image.
License:        BSD-3-Clause AND MIT
URL:            https://github.com/pytorch/vision
Source0:        https://github.com/pytorch/vision/archive/refs/tags/v%{version}.tar.gz#/torchvision-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-gif-decoder-oob.patch gh#pytorch/vision#9520
# Backport of 4e05dc22f5 (0.28): GIF decoder heap OOB read/write. GHSA-vp9x-48wq-4wc3.
Patch0:         fix-gif-decoder-oob.patch
BuildRequires:  %{python_module Pillow >= 5.3.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module torch-devel}
BuildRequires:  %{python_module torch}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
# The auto Python dep generator does not pick up Requires-Dist from this
# setuptools wheel; declare them by hand.
Requires:       python-Pillow
Requires:       python-numpy
Requires:       python-torch
# Match Factory python-torch (ExcludeArch: %%ix86 %%{arm})
ExcludeArch:    %{ix86} %{arm}
%python_subpackages

%description
The torchvision package consists of popular datasets, model
architectures, and common image transformations for computer vision
on top of PyTorch. This build is CPU-only, matching Factory
python-torch (CUDA disabled).

%prep
%autosetup -p1 -n vision-%{version}
# Keep DWARF for the debuginfo package; upstream strips it for wheels.
sed -i 's/extra_compile_args\["cxx"\].append("-g0")/extra_compile_args["cxx"].append("-g")/' setup.py
# Factory ships libpng16-config, not the unversioned libpng-config name
# that setup.py looks up via shutil.which.
sed -i 's/"libpng-config"/"libpng16-config"/g' setup.py

%build
# Factory python-torch is CPU-only (standard/openmpi4, CUDA bcond off).
export FORCE_CUDA=0
export TORCHVISION_USE_NVJPEG=0
export TORCHVISION_USE_PNG=1
export TORCHVISION_USE_JPEG=1
export TORCHVISION_USE_WEBP=1
# Stop setup.py appending +gitsha when git is in the buildroot.
export BUILD_VERSION=%{version}
%pyproject_wheel

%install
export FORCE_CUDA=0
export TORCHVISION_USE_NVJPEG=0
export BUILD_VERSION=%{version}
%pyproject_install
# imported modules, not scripts (rpmlint non-executable-script)
find %{buildroot} -name '*.py' ! -perm /111 -exec sed -i '1{/^#!/d}' {} +
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/torchvision
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The source tree contains a torchvision/ package without the compiled
# _C.so; importing from cwd would skip the installed extension.
cd %{_tmppath}
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -B -c "import torchvision; assert torchvision.__version__ == '%{version}', torchvision.__version__; from torchvision import ops, transforms, io"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/torchvision
%{python_sitearch}/torchvision-%{version}.dist-info

%changelog
