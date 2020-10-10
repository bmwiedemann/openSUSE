#
# spec file for package spirv-headers
#
# Copyright (c) 2020 SUSE LLC
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


Name:           spirv-headers
Version:        1.5.3.g22
Release:        0
Summary:        Machine-readable files from the SPIR-V registry
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Headers

#Source:         https://github.com/KhronosGroup/SPIRV-Headers/archive/%version.tar.gz
Source:         SPIRV-Headers-%version.tar.xz
BuildArch:      noarch
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++

%description
This repository contains machine-readable files from the SPIR-V
registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file.

%prep 
%autosetup -n SPIRV-Headers-%version

%build
# Because Khronos does not know what DESTDIR is.
%cmake -DCMAKE_INSTALL_PREFIX="%buildroot/%_prefix"
%cmake_build

%install
pushd build/
make install-headers
popd
%fdupes %buildroot/%_prefix

%files
%_includedir/spirv/
%license LICENSE

%changelog
