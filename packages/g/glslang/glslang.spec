#
# spec file for package glslang
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


%define lname libglslang11
Name:           glslang
Version:        11.13.0
Release:        0
Summary:        OpenGL and OpenGL ES shader front end and validator
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
#Git-URL:	https://github.com/KhronosGroup/glslang
Source:         https://github.com/KhronosGroup/glslang/archive/%version.tar.gz
Source3:        baselibs.conf
Patch1:         0001-build-set-SOVERSION-on-all-libraries.patch
Patch2:         abibreak_bump.diff
BuildRequires:  bison
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
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
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
echo "V_%version { global: *; };" >/tmp/z.sym
# Trim -Wl,--no-undefined for now (https://github.com/KhronosGroup/glslang/issues/1484)
%cmake -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"
%make_build

%install
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake_install
b="%buildroot"
mkdir -p "$b/%_includedir"
cp -a SPIRV glslang "$b/%_includedir/"
find "$b/%_includedir/" -type f ! -iname "*.h" -a ! -iname "*.hpp" -print -delete
ln -s SPIRV/spirv.hpp "$b/%_includedir/"
find "$b/%_includedir/" -type f -exec chmod a-x "{}" "+"
cp build/StandAlone/libglslang-default-resource-limits.so "$b/%_libdir/"

# 3rd party programs use -lOGLCompiler (because pristine glslang shipped .a files),
# so satisfy them under our shared build.
for i in libOGLCompiler libOSDependent libGenericCodeGen libMachineIndependent; do
	ln -s libglslang.so "$b/%_libdir/$i.so"
	rm -f "$b/%_libdir/$i.a"
done

%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/*.so.11*

%files devel
%_bindir/gls*
%_bindir/spirv*
%_libdir/cmake/
%_libdir/*resource*.so
%_libdir/libGenericCodeGen.so
%_libdir/libHLSL.so
%_libdir/libMachineIndependent.so
%_libdir/libOGLCompiler.so
%_libdir/libOSDependent.so
%_libdir/libSPIRV.so
%_libdir/libSPVRemapper.so
%_libdir/libglslang.so
%_includedir/*

%changelog
