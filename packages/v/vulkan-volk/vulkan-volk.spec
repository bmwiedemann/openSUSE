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
%define lname libvolk-1_4_304
%define rev a776ece3fb71849ce220acaf3affea4df06cb587
Version:        1.4.304
Release:        0
Summary:        Meta loader for the Vulkan API
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/zeux/volk
Source:         https://github.com/zeux/volk/archive/%rev.tar.gz
Patch1:         shared.diff
BuildRequires:  c_compiler
BuildRequires:  cmake
BuildRequires:  python3-base
BuildRequires:  pkgconfig(vulkan) >= %version

%description
A meta loader for Vulkan.

%package -n %lname
Summary:        Meta loader for the Vulkan API
Group:          System/Libraries
Conflicts:      volk-devel

%description -n %lname
volk is a meta loader for Vulkan. It loads entrypoints required to
use Vulkan by means of dlopen-ing libvulkan.so.1. volk simplifies the
use of Vulkan extensions by loading all associated entrypoints. volk
enables loading Vulkan entrypoints directly from the driver which can
increase performance by skipping loader dispatch overhead.

%package devel
Summary:        Headers for the Vulkan meta loader
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release
# -lvolk is logically ambiguous, so block this package mix even
# if the filesets do not overlap at all times.
# https://github.com/zeux/volk/issues/166
Conflicts:      volk-devel

%description devel
Headers needed for programs to utilize the Vulkan VOLK meta loader.

%prep
%autosetup -p1 -n volk-%rev
perl -i -lpe 's{\@PACKAGE_VERSION\@}{%version}g' CMakeLists.txt

%build
%cmake -DVOLK_INSTALL=ON
%cmake_build

%install
%cmake_install
ln -s libvolk-%version.so "%buildroot/%_libdir/libvolk.so"

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libvolk-%version.so

%files devel
%_includedir/volk*
%_libdir/cmake/
%_libdir/libvolk.so
%doc LICENSE.md README.md

%changelog
