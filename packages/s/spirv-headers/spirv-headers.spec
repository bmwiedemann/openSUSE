#
# spec file for package spirv-headers
#
# Copyright (c) 2025 SUSE LLC and contributors
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
# The SPIR-V version is 1.6.4 (include/spirv/unified1/spirv.core.grammar.json)
# They add "SDK" tags that reflect the Vulkan version (1.4),
# and the independently increasing toolchain release number (335).

# Leap 15 and SLES 15 defaults to GCC 7, which does not have stable C++17 ABI.
# See https://bugzilla.suse.com/show_bug.cgi?id=1235697
%if 0%{?suse_version} < 1600
%define gcc_version 13
%endif

Name:           spirv-headers
Version:        1.6.4+sdk335+gb824a46
%define innerver 1.4.335
%define rev b824a462d4256d720bebb40e78b9eb8f78bbb305
Release:        0
Summary:        Machine-readable files from the SPIR-V registry
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Headers
Source:         https://github.com/KhronosGroup/SPIRV-Headers/archive/%rev.tar.gz
BuildArch:      noarch
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_version} >= 9
BuildRequires:  gcc%{?gcc_version}-c++ >= 9
BuildRequires:  pkg-config

%description
This repository contains machine-readable files from the SPIR-V
registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file.

%prep
%autosetup -n SPIRV-Headers-%rev -p1

%build
%cmake \
	-DCMAKE_C_COMPILER="gcc%{?gcc_version:-%{gcc_version}}" \
	-DCMAKE_CXX_COMPILER="g++%{?gcc_version:-%{gcc_version}}"
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
