#
# spec file for package glslang
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define version_unconverted 7.11.3276.git10
%define lname libglslang-suse6

Name:           glslang
Version:        7.11.3276.git10
Release:        0
Summary:        OpenGL and OpenGL ES shader front end and validator
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
#Git-URL:	https://github.com/KhronosGroup/glslang

Source:         %name-%version.tar.xz
Patch1:         ver.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  python3-base

%description
glslang is a compiler front end for the OpenGL ES and OpenGL shading
languages. It implements a strict interpretation of the
specifications for these languages.

%package -n %lname
Summary:        OpenGL and OpenGL ES shader front end implementation
Group:          System/Libraries

%description -n %lname
glslang is a compiler front end for the OpenGL ES and OpenGL shading
languages. It implements a strict interpretation of the
specifications for these languages.

%package devel
Summary:        OpenGL and OpenGL ES shader front end and validator
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
glslang is a compiler front end for the OpenGL ES and OpenGL shading
languages. It implements a strict interpretation of the
specifications for these languages.

spirv-remap is a utility to improve compression of SPIR-V binary
files via entropy reduction, plus optional stripping of debug
information and load/store optimization. It transforms SPIR-V to
SPIR-V, remapping IDs. The resulting modules have an increased ID
range (IDs are not as tightly packed around zero), but will compress
better when multiple modules are compressed together, since
compressor's dictionary can find better cross module commonality.

%prep
%autosetup -p1

%build
# Trim -Wl,--no-undefined for now (https://github.com/KhronosGroup/glslang/issues/1484)
%cmake -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"
make %{?_smp_mflags}

%install
b="%buildroot"
%cmake_install
mkdir -p "$b/%_includedir"
cp -a SPIRV glslang "$b/%_includedir/"
find "$b/%_includedir/" -type f ! -iname "*.h" -a ! -iname "*.hpp" -print -delete
ln -s SPIRV/spirv.hpp "$b/%_includedir/"
find "$b/%_includedir/" -type f -exec chmod a-x "{}" "+"
cp build/StandAlone/libglslang-default-resource-limits.so "$b/%_libdir/"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/*.so.suse6*

%files devel
%defattr(-,root,root)
%_bindir/gls*
%_bindir/spirv*
%_libdir/*.a
%_libdir/*resource*.so
%_libdir/libHLSL.so
%_libdir/libSPIRV.so
%_libdir/libSPVRemapper.so
%_libdir/libglslang.so
%_includedir/*

%changelog
