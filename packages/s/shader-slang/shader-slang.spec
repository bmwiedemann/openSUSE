#
# spec file for package shader-slang
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


%define lname libslang0_2026_18_3
Name:           shader-slang
Version:        2026.18.3
Release:        0
Summary:        A shading language compiler and tools
License:        Apache-2.0 WITH LLVM-exception
URL:            https://shader-slang.org/
#Git-Clone:     https://github.com/shader-slang/slang
Source:         https://github.com/shader-slang/slang/archive/refs/tags/v%version.tar.gz
Source8:        %name-rpmlintrc
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  cmark
BuildRequires:  dos2unix
BuildRequires:  fast_float-devel
BuildRequires:  glslang-devel
BuildRequires:  pkg-config
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools
BuildRequires:  vulkan-headers
BuildRequires:  cmake(unordered_dense)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(miniz)
Patch1:         0001-system.patch

%description
Slang is a shading language for building shader codebases in a
modular and extensible fashion. The Slang compiler can generate code
for a wide variety of targets (enabled on openSUSE: Vulkan), and even
generate code to run on a CPU. For textual targets, such as Metal
Shading Language (MSL) and CUDA, Slang produces readable code that
preserves original identifier names, as well as the type and call
structure.

%package -n %lname
Summary:        Slang shader language runtime
Group:          System/Libraries

%description -n %lname
Slang is a shading language for building shader codebases.
This package contains shared libraries for slang.

%package devel
Summary:        Headers for Slang shader libraries
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Conflicts:      slang-devel

%description devel
Slang is a shading language for building shader codebases.
This package contains files for the toolchain.

%package doc
Summary:        Documentation for Slang, a shader compiler
Group:          Documentation/Text
BuildArch:      noarch

%description doc
Slang is a shading language for building shader codebases.
This package contains the documentation.

%prep
%autosetup -p1 -n slang-%version

%build
%set_build_flags
export CXXFLAGS="$CXXFLAGS -I%_includedir/glslang"
%cmake \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	-DSLANG_VERSION_FULL="v%version" \
	-DSLANG_VERSION_NUMERIC="%version" \
	-DSLANG_ENABLE_CUDA=OFF \
	-DSLANG_ENABLE_OPTIX=OFF \
	-DSLANG_ENABLE_AFTERMATH=OFF \
	-DSLANG_ENABLE_SLANG_RHI=OFF \
	-DSLANG_ENABLE_DXIL=OFF \
	-DSLANG_ENABLE_TESTS=OFF \
	-DSLANG_ENABLE_EXAMPLES=OFF \
	-DSLANG_ENABLE_SLANG_PROXY:BOOL=OFF \
	-DSLANG_USE_SYSTEM_MINIZ=ON \
	-DSLANG_USE_SYSTEM_LZ4=ON \
	-DSLANG_USE_SYSTEM_VULKAN_HEADERS=ON \
	-DSLANG_USE_SYSTEM_SPIRV_HEADERS=ON \
	-DSLANG_USE_SYSTEM_UNORDERED_DENSE=ON \
	-DSLANG_USE_SYSTEM_SPIRV_TOOLS=ON \
	-DSLANG_USE_SYSTEM_GLSLANG=ON \
	-DSLANG_USE_SYSTEM_CMARK=ON \
	-DSLANG_SLANG_LLVM_FLAVOR=DISABLE \
	-DSLANG_EMBED_CORE_MODULE:BOOL=TRUE \
	-DSLANG_EMBED_CORE_MODULE_SOURCE:BOOL=FALSE

%cmake_build
make copy-gfx-slang-modules # unbreak cmake_install

%install
b="%buildroot"
%cmake_install
mkdir -pv "$b/%_defaultdocdir" "$b/%_libdir"
mv -v "$b/usr/share/doc/slang" "$b/%_defaultdocdir/%name/"
# sigh...
if [ "%_lib" != "lib" ]; then
	# Actually, the location does not really matter, because it is
	# included in libslang-compiler.so anyway (-DSLANG_EMBED_CORE_MODULE)
	mv -v "$b/usr/lib"/* "$b/%_libdir/"
	perl -i -pe 's{^libdir=\${prefix}/lib}{libdir=\${prefix}/%_lib}g' \
		"$b/%_libdir/pkgconfig"/*.pc
fi
# unexecutables
rm -fv "$b/%_bindir/gfx.slang" "$b/%_bindir/slang.slang"

%ldconfig_scriptlets -n %lname

%files
%_bindir/*slang*

%files -n %lname
%_libdir/lib*.so.*

%files devel
%_includedir/slang*
%_libdir/*.so
%_libdir/cmake/
%_libdir/pkgconfig/*.pc
%_libdir/slang-standard*

%files doc
%_defaultdocdir/%name/

%changelog
