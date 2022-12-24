#
# spec file for package spirv-headers
#
# Copyright (c) 2022 SUSE LLC
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


# The git repo is a hodgepodge.
# Most recent tag is 1.5.4, but that is outdated.
# CMakeLists.txt's project() line contains 1.5.5, but this is outdated too.
# The SPIR-V version is 1.6.1 (include/spirv/unified1/spirv.core.grammar.json)
# They add "SDK" tags that reflect the Vulkan version (1.3),
# and the independently increasing toolchain release number (216).

Name:           spirv-headers
Version:        1.6.1+sdk236
Release:        0
Summary:        Machine-readable files from the SPIR-V registry
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Headers
Source:         https://github.com/KhronosGroup/SPIRV-Headers/archive/sdk-1.3.236.0.tar.gz
BuildArch:      noarch
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
This repository contains machine-readable files from the SPIR-V
registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file.

%prep
%autosetup -n SPIRV-Headers-sdk-1.3.236.0

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %buildroot/%_prefix

%files
%_includedir/spirv/
%_datadir/cmake/
%_datadir/pkgconfig/*.pc
%license LICENSE

%changelog
