#
# spec file for package rocm
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
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


%global rocm_release 7.2
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocm
Version:        %{rocm_version}
Release:        7%{?dist}
Summary:        ROCm tools for computing on AMD GPU
License:        MIT

Source0:        License.txt

# This is a meta package
%global debug_package %{nil}

# ROCm only working on x86_64
ExclusiveArch:  x86_64

Requires:       amdsmi >= %{rocm_release}
Requires:       hipblas >= %{rocm_release}
Requires:       hipcc
Requires:       hipfft-libs >= %{rocm_release}
Requires:       hiprand >= %{rocm_release}
Requires:       hipsolver-libs >= %{rocm_release}
Requires:       hipsparse >= %{rocm_release}
Requires:       hipsparselt
Requires:       rocalution-libs >= %{rocm_release}
Requires:       rocblas >= %{rocm_release}
Requires:       rocdecode-libs >= %{rocm_release}
Requires:       rocfft >= %{rocm_release}
Requires:       rocjpeg >= %{rocm_release}
Requires:       rocm-clang
Requires:       rocm-hip >= %{rocm_release}
Requires:       rocm-clinfo >= %{rocm_release}
Requires:       rocm-core >= %{rocm_release}
Requires:       rocm-opencl >= %{rocm_release}
Requires:       rocm-origami
Requires:       rocm-runtime >= %{rocm_release}
Requires:       rocm-smi >= %{rocm_release}
Requires:       rocminfo >= %{rocm_release}
Requires:       rocrand >= %{rocm_release}
Requires:       rocsolver >= %{rocm_release}
Requires:       rocsparse >= %{rocm_release}
Requires:       roctracer-libs >= %{rocm_release}
Requires:       hipblaslt >= %{rocm_release}
Requires:       miopen >= %{rocm_release}
#Requires:       rccl >= %{rocm_release}

%description
This is a collection of ROCm tools and libraries for programming
AMD graphics processing units.

%package devel
Summary:        Development environment for ROCm
Requires:       amdsmi-devel >= %{rocm_release}
Requires:       half-devel
Requires:       hipblas-common-devel >= %{rocm_release}
Requires:       hipblas-devel >= %{rocm_release}
Requires:       hipblaslt-devel >= %{rocm_release}
Requires:       hipcub-devel >= %{rocm_release}
Requires:       hipfft-devel >= %{rocm_release}
Requires:       hipify >= %{rocm_release}
Requires:       hiprand-devel >= %{rocm_release}
Requires:       hipsolver-devel >= %{rocm_release}
Requires:       hipsparse-devel >= %{rocm_release}
Requires:       hipsparselt-devel
Requires:       miopen-devel >= %{rocm_release}
#Requires:       rccl-devel >= %{rocm_release}
Requires:       rocalution-devel >= %{rocm_release}
Requires:       rocblas-devel >= %{rocm_release}
Requires:       rocdecode-devel >= %{rocm_release}
Requires:       rocfft-devel >= %{rocm_release}
Requires:       rocjpeg-devel >= %{rocm_release}
Requires:       rocm-clang-devel
Requires:       rocm-cmake >= %{rocm_release}
Requires:       rocm-compilersupport-macros
Requires:       rocm-core-devel >= %{rocm_release}
#Requires:       rocm-examples >= %{rocm_release}
Requires:       rocm-hip-devel >= %{rocm_release}
Requires:       rocm-opencl-devel >= %{rocm_release}
Requires:       rocm-origami-devel
Requires:       rocm-rpm-macros >= %{rocm_release}
Requires:       rocm-rpm-macros-modules >= %{rocm_release}
Requires:       rocm-runtime-devel >= %{rocm_release}
Requires:       rocm-smi-devel >= %{rocm_release}
Requires:       rocprim-devel >= %{rocm_release}
Requires:       rocrand-devel >= %{rocm_release}
Requires:       rocsolver-devel >= %{rocm_release}
Requires:       rocsparse-devel >= %{rocm_release}
Requires:       rocthrust-devel >= %{rocm_release}
Requires:       roctracer-devel >= %{rocm_release}
Requires:       rocwmma-devel >= %{rocm_release}

%description devel
This is a meta package for all of the ROCm devel packages.

%package test
Summary:        Tests for ROCm
Requires:       kfdtest             >= %{rocm_release}
Requires:       rocm-validation-suite >= %{rocm_release}

%description test
This is a meta package for all of the ROCm test packages.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .

%build

%install

%files
%license License.txt

%files devel
%license License.txt

%files test
%license License.txt

%changelog
