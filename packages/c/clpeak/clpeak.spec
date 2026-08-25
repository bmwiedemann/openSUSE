#
# spec file for package clpeak
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2015-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           clpeak
Version:        2.1.3
Release:        0
Summary:        Find peak OpenCL capacities like bandwidth & compute
# Legal-Review-Notice: upstream relicensed from the Unlicense to Apache-2.0
# in commit 65e57245 (2023-12-22); LICENSE is the sole licence file in the
# tree, there is no bundled third-party code and no source carries a
# divergent SPDX header. Fedora declares Apache-2.0 as well.
License:        Apache-2.0
URL:            https://github.com/krrishnarraj/clpeak
Source:         https://github.com/krrishnarraj/clpeak/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM clpeak-version-override.patch gh#krrishnarraj/clpeak#206 mpluskal@suse.com
# -- let the builder pass the version in; tarball builds report "unknown" since 2.1.3
Patch0:         clpeak-version-override.patch
BuildRequires:  cmake >= 3.20
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  opencl-cpp-headers
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(vulkan)

%description
A tool which profiles OpenCL devices to find their peak capacities like
bandwidth & compute.

%prep
%autosetup -p1

%build
# Flutter GUI is optional upstream and skipped without an SDK; pin it off
# so a stray flutter in the buildroot cannot pull it in. CUDA/ROCm/Metal/
# oneAPI likewise auto-skip when their SDKs are absent — keep them off
# explicitly. Vulkan + OpenCL + CPU stay on (defaults).
%define __builder ninja
# GitHub archives carry no .git, so git-describe cannot run and 2.1.3 reports
# "unknown" -- in --version and in the clpeak_version field of every JSON/XML/
# CSV export. Our source is exactly the tag Version names, so state it (Patch0).
%cmake \
    -DCLPEAK_VERSION_OVERRIDE=%{version} \
    -DCLPEAK_ENABLE_GUI=OFF \
    -DCLPEAK_ENABLE_CUDA=OFF \
    -DCLPEAK_ENABLE_ROCM=OFF \
    -DCLPEAK_ENABLE_METAL=OFF \
    -DCLPEAK_ENABLE_ONEAPI=OFF
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/%{name}

%check
%ctest

%files
%license LICENSE
%doc README.md results
%{_bindir}/%{name}

%changelog
