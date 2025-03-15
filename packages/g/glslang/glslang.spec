#
# spec file for package glslang
#
# Copyright (c) 2025 SUSE LLC
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


%define lname libglslang15
%if 0%{?suse_version} < 1600
%define gcc_version 13
%endif

Name:           glslang
Version:        15.2.0
Release:        0
Summary:        OpenGL and OpenGL ES shader front end and validator
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
#Git-URL:	https://github.com/KhronosGroup/glslang
# tag 15.2.0 missing in git as of 2025-03-13
%define rev 0018771b46c492e28ca916b00eda96093381a3b2
Source:         https://github.com/KhronosGroup/glslang/archive/%rev.tar.gz
Source3:        baselibs.conf
BuildRequires:  bison
BuildRequires:  cmake >= 3.14.0
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_version} >= 9
BuildRequires:  gcc%{?gcc_version}-c++ >= 9
BuildRequires:  python3-base
BuildRequires:  spirv-tools-devel >= 2025.1~rc1

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
Requires:       cmake(SPIRV-Tools-opt)
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

%package nonstd-devel
Summary:        Secondary set of header files for glslang
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
BuildArch:      noarch

%description nonstd-devel
glslang is a compiler front end for the OpenGL ES and OpenGL shading
languages. It implements a strict interpretation of the
specifications for these languages.

This package contains additional headers that are not officially installed,
but which some downstream packages rely on.

%prep
%autosetup -n glslang-%rev -p1

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
# (gh#3052 #3311 #3312 #3593) -- supposedly handled better in
# glslang-15 and onwards, do watch for ABI breaks
#echo "V_%version { global: *; };" >/tmp/z.sym
# Trim -Wl,--no-undefined for now (https://github.com/KhronosGroup/glslang/issues/1484)
%cmake -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
	-DCMAKE_C_COMPILER="gcc%{?gcc_version:-%{gcc_version}}" \
	-DCMAKE_CXX_COMPILER="g++%{?gcc_version:-%{gcc_version}}" \
	-DALLOW_EXTERNAL_SPIRV_TOOLS:BOOL=ON -DENABLE_OPT:BOOL=ON
%make_build

%install
%global _lto_cflags %_lto_cflags -ffat-lto-objects
od="$PWD"
%cmake_install

b="%buildroot"
cd "$b"
(
	find usr/include -mindepth 1 -type d -printf "%%%%dir /%p\n"
	find usr/include "(" -type f -o -type l ")" -printf "/%p\n"
) | sort >"$od/devel.files"
cd -

mkdir -p "$b/%_includedir/External/"
cp -a glslang "$b/%_includedir/"
cp -a SPIRV StandAlone "$b/%_includedir/External/"
find "$b/%_includedir/" -type f ! -iname "*.h" -a ! -iname "*.hpp" -print -delete
find "$b/%_includedir/" -type f -exec chmod a-x "{}" "+"

cd "$b"
(
	find usr/include -mindepth 1 -type d -printf "%%%%dir /%p\n"
	find usr/include "(" -type f -o -type l ")" -printf "/%p\n"
) | sort >"$od/devel_full.files"
cd -
comm -13 "$od/devel.files" "$od/devel_full.files" >"$od/devel2.files"

# 3rd party programs use -lOSDependent (because pristine glslang shipped .a
# files), so satisfy them under our shared build.
mkdir -p "$b/%_libdir"
for i in libOSDependent libGenericCodeGen libMachineIndependent; do
	ln -s libglslang.so "$b/%_libdir/$i.so"
	rm -f "$b/%_libdir/$i.a"
done
# Gone with glslang 14, redirect to main file
for i in libHLSL libOGLCompiler; do
	ln -s libglslang.so "$b/%_libdir/$i.so"
	rm -f "$b/%_libdir/$i.a"
done

%fdupes %buildroot/%_prefix

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/*.so.15*

%files devel -f devel.files
%_bindir/gls*
%_bindir/spirv*
%_libdir/cmake/
%_libdir/libGenericCodeGen.so
%_libdir/libHLSL.so
%_libdir/libMachineIndependent.so
%_libdir/libOGLCompiler.so
%_libdir/libOSDependent.so
%_libdir/libSPIRV.so
%_libdir/libSPVRemapper.so
%_libdir/libglslang.so
%_libdir/libglslang-default-resource-limits.so

%files nonstd-devel -f devel2.files

%changelog
