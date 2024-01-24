#
# spec file for package vulkan-volk
#
# Copyright (c) 2024 SUSE LLC
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


Name:           vulkan-volk
Version:        1.3.275.0
Release:        0
Summary:        Meta loader for the Vulkan API
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/zeux/volk
Source:         https://github.com/zeux/volk/archive/refs/tags/vulkan-sdk-%version.tar.gz
Patch1:         shared.diff
BuildRequires:  cmake
BuildRequires:  c_compiler
BuildRequires:  python3-base
BuildRequires:  pkgconfig(vulkan)

%description
A meta loader for Vulkan.

%package -n libvolk
Summary:        Meta loader for the Vulkan API
Group:          System/Libraries

%description -n libvolk
volk is a meta loader for Vulkan. It loads entrypoints required to
use Vulkan by means of dlopen-ing libvulkan.so.1. volk simplifies the
use of Vulkan extensions by loading all associated entrypoints. volk
enables loading Vulkan entrypoints directly from the driver which can
increase performance by skipping loader dispatch overhead.

%package devel
Summary:        Headers for the Vulkan meta loader
Group:          Development/Libraries/C and C++
Requires:       libvolk = %version-%release
Conflicts:      volk-devel

%description devel
Headers needed for programs to utilize the Vulkan VOLK meta loader.

%prep
%autosetup -p1 -n volk-vulkan-sdk-%version

%build
# Minimal re-versioning so rpm detects upgrades at least. Might change later.
sv="$PWD/lib.v"
ver=$(echo %version | cut -d+ -f1)
echo "VOLK_$ver { global: *; };" >"$sv"
%cmake -DVOLK_INSTALL=ON \
        -DCMAKE_SHARED_LINKER_FLAGS:STRING="-Wl,--version-script=$sv"
%cmake_build

%install
%cmake_install

%post   -n libvolk -p /sbin/ldconfig
%postun -n libvolk -p /sbin/ldconfig

%files -n libvolk
%_libdir/libvolk.so

%files devel
%_includedir/volk*
%_libdir/cmake/
%doc LICENSE.md README.md

%changelog
