#
# spec file for package blender
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019-2023 LISA GmbH, Bingen, Germany.
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


%define _dwz_low_mem_die_limit  40000000
%define _dwz_max_die_limit     200000000

%bcond_with is_snapshot

%ifarch x86_64
%bcond_without embree
%bcond_without oidn
%else
%bcond_with embree
%bcond_with oidn
%endif

%ifarch x86_64 aarch64
%bcond_without openpgl
%else
%bcond_with openpgl
%endif

%bcond_with optix
%define optix_version 7.4

%if 0%{?suse_version} >= 1550
%bcond_without system_audaspace
%else
%bcond_without system_audaspace
%global force_boost_version 1_75_0
%global force_gcc_version 14
%endif

%bcond_with clang

%bcond_with blender_ua

# Set this to 1 for fixing bugs.
%define debugbuild 0

# Define the version of python3 that blender is going to build against.
%if 0%{?suse_version} >= 1550
%define py3ver 3.13
%define py3pkg python313
%else
%define py3ver 3.11
%define py3pkg python311
%endif
# this is mostly needed on leap for PySound.cpp as we build the intree audaspace
%if %{without system_audaspace}
%if 0%{?suse_version} >= 1600
%define numpy_include_path %{_libdir}/python%{py3ver}/site-packages/numpy/_core/include/
%else
%define numpy_include_path %{_libdir}/python%{py3ver}/site-packages/numpy/core/include/
%endif
%endif

# Blender version: source/blender/blenkernel/BKE_blender_version.h
# blender has versions like x.xxy which have x.xx (notice the missing
# trailing y) in the directory path. This makes this additional variable
# necessary.
%define _version %(echo %{version} | cut -b 1-3)
%define _suffix %(echo %{_version} | tr -d '.')

%bcond_without alembic
%bcond_without collada
%bcond_without opensubdiv
%bcond_without openvdb
%bcond_without osl
%bcond_without system_glew
# TBD: contributions welcome
%bcond_with usd
%bcond_with openxr

%global pkg_name blender

Name:           blender
Version:        4.4.0
Release:        0
Summary:        A 3D Modelling And Rendering Package
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/3D Editors
URL:            https://www.blender.org/
# Please leave the source url intact
%if %{with is_snapshot}
Source0:        %{pkg_name}-%{version}.tar.xz
%else
Source0:        https://download.blender.org/source/%{pkg_name}-%{version}.tar.xz
Source1:        https://download.blender.org/source/%{pkg_name}-%{version}.tar.xz.md5sum
%endif
# Unfortunately, the "Essentials" library is only availabe using GIT LFS. https://projects.blender.org/blender/blender/issues/128359
Source2:        blender-assets-%{version}.tar.xz
Source4:        geeko.blend
Source5:        geeko.README
Source6:        geeko_example_scene.blend
Source7:        geeko_example_scene.README
Source8:        %{pkg_name}-sample
Source9:        SUSE-NVIDIA-GPU-rendering.txt
Source10:       SUSE-NVIDIA-OptiX-rendering.txt
Source99:       series
# PATCH-FIX-UPSTREAM https://projects.blender.org/blender/blender/pulls/115320
Patch1:         cmake_manpage_fix.patch
%if %{with mold}
BuildRequires:  mold
%endif
BuildRequires:  %{py3pkg}-devel
BuildRequires:  %{py3pkg}-numpy-devel
BuildRequires:  %{py3pkg}-requests
BuildRequires:  OpenColorIO-devel >= 2.0
BuildRequires:  OpenEXR-devel
BuildRequires:  OpenImageIO < 3
BuildRequires:  OpenImageIO-devel < 3
BuildRequires:  SDL2-devel
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  distribution-release
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gettext-tools
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libboost_atomic%{?force_boost_version}-devel
BuildRequires:  libboost_date_time%{?force_boost_version}-devel
BuildRequires:  libboost_filesystem%{?force_boost_version}-devel
BuildRequires:  libboost_iostreams%{?force_boost_version}-devel
BuildRequires:  libboost_locale%{?force_boost_version}-devel
%if "%{?force_boost_version}" == ""
BuildRequires:  libboost_numpy3-devel
BuildRequires:  libboost_python3-devel
%else
BuildRequires:  libboost_numpy-py3-%{?force_boost_version}-devel
BuildRequires:  libboost_python-py3-%{?force_boost_version}-devel
%endif
BuildRequires:  libboost_program_options%{?force_boost_version}-devel
BuildRequires:  libboost_regex%{?force_boost_version}-devel
BuildRequires:  libboost_serialization%{?force_boost_version}-devel
BuildRequires:  libboost_system%{?force_boost_version}-devel
BuildRequires:  libboost_thread%{?force_boost_version}-devel
BuildRequires:  libboost_wave%{?force_boost_version}-devel
BuildRequires:  libharu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libomp-devel
BuildRequires:  libpng-devel
BuildRequires:  libpulse-devel
BuildRequires:  libspnav-devel
BuildRequires:  libtiff-devel
BuildRequires:  llvm-devel
BuildRequires:  lzo-devel
BuildRequires:  ninja
BuildRequires:  openal-soft-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-Text-Iconv
BuildRequires:  pkgconfig
BuildRequires:  potrace-devel
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  cmake(pugixml)
BuildRequires:  cmake(zstd)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(level-zero)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
%ifarch x86_64
# oneVPL only available on x86_64 atm
BuildRequires:  pkgconfig(vpl)
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
Requires:       %{py3pkg}-base
Requires:       %{py3pkg}-numpy
Requires:       %{py3pkg}-requests
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme
Recommends:     %name-demo = %version
# current locale handling doesn't create locale(..) provides correctly
Recommends:     %name-lang = %version
Provides:       %{pkg_name}-%{_suffix} = %{version}
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  pkgconfig(OpenEXR)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(gmpxx)
%else
BuildRequires:  gmp-devel
%endif
# conditional requirements
%if 0%{?debugbuild} == 1
BuildRequires:  pkgconfig(valgrind)
%endif
%if 0%{?is_opensuse} == 1
BuildRequires:  pkgconfig(jemalloc)
%endif
%if %{with alembic}
BuildRequires:  alembic-devel
%endif
%if %{with collada}
BuildRequires:  openCOLLADA-devel
%endif
%if %{with embree}
BuildRequires:  cmake(embree)
%endif
%if %{with oidn}
BuildRequires:  OpenImageDenoise-devel >= 2
%endif
%if %{with openpgl}
BuildRequires:  openpgl-devel >= 0.5
%endif
%if %{with opensubdiv}
BuildRequires:  OpenSubdiv-devel
%endif
%if %{with openvdb}
BuildRequires:  openvdb-devel
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(blosc)
%endif
%if %{with optix}
BuildRequires:  nvidia-optix-headers
%endif
%if %{with osl}
BuildRequires:  OpenShadingLanguage-devel > 1.13
%endif
%if %{with system_audaspace}
BuildRequires:  pkgconfig(audaspace) >= 1.6
Requires:       audaspace-deviceplugin
Requires:       audaspace-fileplugin
%endif
%ifarch x86_64
Obsoletes:      %{pkg_name}-cycles-devel = %{version}
Provides:       %{pkg_name}-cycles-devel = %{version}
%endif
ExcludeArch:    %{ix86} %{arm}
%if %{with blender_ua}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

%description
Blender is a 3D modelling and rendering package. It is the in-house
software of a high quality animation studio, Blender has proven to
be an extremely fast and versatile design instrument. The software
has a personal touch, offering a unique approach to the world of
Three Dimensions. Use Blender to create TV commercials, to make
technical visualizations, business graphics, to do some morphing,
or design user interfaces. You can easy build and manage complex
environments. The renderer is versatile and extremely fast. All
basic animation principles (curves & keys) are well implemented.It
includes tools for modeling, sculpting, texturing (painting,
node-based shader materials, or UV mapped), UV mapping, rigging and
constraints, weight painting, particle systems, simulation (fluids,
physics, and soft body dynamics and an external crowd simulator),
rendering, node-based compositing, and non linear video editing,
as well as an integrated game engine for real-time interactive 3D
and game creation and playback with cross-platform compatibility.

%if %{with optix}
This build has enabled support for OptiX Version %{optix_version}.
Check %{_docdir}/SUSE-NVIDIA-OptiX-rendering.txt.
%endif

%package demo
Summary:        Some Blender demo files
License:        CC-BY-4.0
Group:          Productivity/Graphics/3D Editors
BuildArch:      noarch

%description demo
Some Blender demo scenes

geeko_example_scene: showing raytracing, rigging, animation, curves,
                     shading, texturing, vertex groups and rendering.

%lang_package

%prep
%if %{without is_snapshot}
pushd "%{_sourcedir}"
md5sum -c %{SOURCE1}
popd
%endif

%autosetup -p1 -n %{pkg_name}-%{version}
%setup -T -D -a 2 -q -n %{pkg_name}-%{version}
mv blender-assets-%{version} release/datafiles/assets

rm -rf extern/libopenjpeg
%if %{with system_glew}
rm -rf extern/glew
# silence warning about missing includedir
mkdir -p extern/glew/include
sed -i 's|NOT WITH_SYSTEM_GLEW|WITH_SYSTEM_GLEW|' source/blender/gpu/CMakeLists.txt
%endif

for i in $(grep -rl "%{_bindir}/env python"); do sed -i '1s@^#!.*@#!%{_bindir}/python%{py3ver}@' ${i}; done

%build
export SUSE_ASNEEDED=0
%if %{with clang}
export CC="clang"
export CXX="clang++"
%define _lto_cflags -flto=full
%else
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%endif
%if %{with mold}
%define build_ldflags -fuse-ld=mold
%endif

echo "optflags: " %{optflags}
mkdir -p build && pushd build

# lean against build_files/cmake/config/blender_release.cmake
%define __builder %__ninja
cmake ../ \
      -GNinja \
%if 0%{?debugbuild} == 1
      -DCMAKE_BUILD_TYPE:STRING=Debug \
      -DCMAKE_C_FLAGS_DEBUG:STRING="-fsanitize=address -ggdb" \
      -DCMAKE_CXX_FLAGS_DEBUG:STRING="-fsanitize=address -ggdb" \
      -DWITH_MEM_VALGRIND:BOOL=ON \
      -DWITH_ASSERT_ABORT:BOOL=ON \
%else
      -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIC -fopenmp %{?numpy_include_path:-I%{numpy_include_path}}" \
      -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIC -fopenmp %{?numpy_include_path:-I%{numpy_include_path}}" \
      -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now" \
      -DCMAKE_MODULE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed" \
      -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now" \
      -DWITH_MEM_VALGRIND:BOOL=OFF \
      -DWITH_ASSERT_ABORT:BOOL=OFF \
%endif
      -DCMAKE_CXX_STANDARD=17 \
      -DWITH_CLANG:BOOL=ON \
      -DWITH_LLVM:BOOL=ON \
      -DLLVM_LIBRARY:FILE=%{_libdir}/libLLVM.so \
      -DCMAKE_VERBOSE_MAKEFILE=ON \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DCMAKE_EXE_LINKER_FLAGS:STRING="-pie" \
      -DBUILD_SHARED_LIBS:BOOL=OFF \
      -DWITH_INSTALL_PORTABLE:BOOL=OFF \
%if 0%{?is_opensuse} == 1
      -DWITH_MEM_JEMALLOC:BOOL=ON \
%endif
%if %{with alembic}
      -DWITH_ALEMBIC:BOOL=ON \
%endif
      -DWITH_AUDASPACE:BOOL=ON \
%if %{with system_audaspace}
      -DWITH_SYSTEM_AUDASPACE:BOOL=ON \
%endif
      -DWITH_BUILDINFO:BOOL=OFF \
      -DWITH_BULLET:BOOL=ON \
      -DWITH_CODEC_FFMPEG:BOOL=ON \
      -DFFMPEG_ROOT_DIR:PATH=%{_includedir}/ffmpeg \
      -DWITH_CODEC_SNDFILE:BOOL=ON \
      -DLIBSNDFILE_ROOT_DIR:FILE=%{_prefix} \
%ifarch ppc ppc64 ppc64le
      -DWITH_CYCLES:BOOL=OFF \
      -DWITH_CYCLES_EMBREE:BOOL=OFF \
%else
      -DWITH_CYCLES:BOOL=ON \
%if %{with osl}
      -DWITH_CYCLES_OSL:BOOL=ON \
      -DOSL_SHADER_HINT:PATH=%{_datadir}/OpenShadingLanguage \
%endif
%if %{with embree}
      -DWITH_CYCLES_EMBREE:BOOL=ON \
%else
      -DWITH_CYCLES_EMBREE:BOOL=OFF \
%endif
%endif
      -DWITH_DRACO:BOOL=ON \
      -DWITH_FFTW3:BOOL=ON \
      -DWITH_FREESTYLE:BOOL=ON \
      -DWITH_GMP:BOOL=ON \
      -DWITH_HARU:BOOL=ON \
      -DWITH_IK_ITASC:BOOL=ON \
      -DWITH_IK_SOLVER:BOOL=ON \
      -DWITH_IMAGE_CINEON:BOOL=ON \
      -DWITH_IMAGE_OPENEXR:BOOL=ON \
      -DWITH_IMAGE_OPENJPEG:BOOL=ON \
      -DWITH_INPUT_NDOF:BOOL=ON \
      -DWITH_INTERNATIONAL:BOOL=ON \
      -DWITH_LIBMV:BOOL=ON \
      -DWITH_LIBMV_SCHUR_SPECIALIZATIONS:BOOL=ON \
      -DWITH_LZMA:BOOL=ON \
      -DWITH_LZO:BOOL=ON \
      -DWITH_SYSTEM_EIGEN3:BOOL=ON \
      -DWITH_SYSTEM_LZO:BOOL=ON \
      -DWITH_MOD_FLUID:BOOL=ON \
%ifnarch x86_64
      -DWITH_MOD_OCEANSIM:BOOL=OFF \
%else
      -DWITH_MOD_OCEANSIM:BOOL=ON \
%endif
      -DWITH_MOD_REMESH:BOOL=ON \
      -DWITH_NANOVDB:BOOL=ON \
      -DWITH_OPENAL:BOOL=ON \
%if %{with collada}
      -DWITH_OPENCOLLADA:BOOL=ON \
%else
      -DWITH_OPENCOLLADA:BOOL=OFF \
%endif
      -DWITH_OPENCOLORIO:BOOL=ON \
%if %{with oidn}
      -DWITH_OPENIMAGEDENOISE:BOOL=ON \
%endif
      -DWITH_OPENMP:BOOL=ON \
%if %{with opensubdiv}
      -DWITH_OPENSUBDIV:BOOL=ON \
      -DOPENSUBDIV_OSDGPU_LIBRARY:FILE=%{_libdir}/libosdGPU.so \
%endif
%if %{with openvdb}
      -DWITH_OPENVDB:BOOL=ON \
      -DWITH_OPENVDB_BLOSC:BOOL=ON \
%endif
      -DWITH_POTRACE:BOOL=ON \
      -DWITH_PUGIXML:BOOL=ON \
      -DWITH_PYTHON:BOOL=ON \
      -DWITH_PYTHON_INSTALL:BOOL=OFF \
      -DPYTHON_VERSION=%{py3ver} \
      -DPYTHON_LIBPATH=%{_libexecdir} \
      -DPYTHON_LIBRARY=python%{py3ver} \
      -DPYTHON_INCLUDE_DIRS=%{_includedir}/python%{py3ver} \
      -DWITH_PYTHON_INSTALL_NUMPY=OFF \
      -DPYTHON_NUMPY_PATH:PATH=%{_libdir}/python%{py3ver}/site-packages \
      -DWITH_QUADRIFLOW:BOOL=ON \
      -DWITH_SDL:BOOL=ON \
      -DWITH_TBB:BOOL=ON \
%if %{with usd}
      -DWITH_USD:BOOL=ON \
%else
      -DWITH_USD:BOOL=OFF \
%endif
      -DWITH_MATERIALX:BOOL=OFF \
%if 0%{?is_opensuse} == 1
      -DWITH_MEM_JEMALLOC:BOOL=ON \
%endif
      -DWITH_JACK:BOOL=ON \
      -DWITH_DOC_MANPAGE:BOOL=ON \
      -DWITH_GHOST_XDND:BOOL=ON \
      -DWITH_GHOST_SDL:BOOL=OFF \
      -DWITH_X11_XINPUT:BOOL=ON \
      -DWITH_X11_XF86VMODE:BOOL=ON \
      -DWITH_INPUT_IME:BOOL=ON \
%if %{with openxr}
      -DWITH_XR_OPENXR:BOOL=ON \
%else
      -DWITH_XR_OPENXR:BOOL=OFF \
%endif
%if %{with optix}
      -DWITH_CYCLES_DEVICE_OPTIX:BOOL=ON \
      -DOPTIX_INCLUDE_DIR:PATH=%{_includedir}/optix/include \
      -DOPTIX_ROOT_DIR:PATH=/opt/nvidia/optix \
%endif
      -DWITH_CYCLES_CUDA_BINARIES:BOOL=OFF \
      -DWITH_CYCLES_HIP_BINARIES:BOOL=ON \
      -DWITH_CYCLES_DEVICE_HIPRT:BOOL=ON \
      -DWITH_CYCLES_DEVICE_ONEAPI:BOOL=ON \
      -DWITH_CYCLES_ONEAPI_BINARIES:BOOL=ON

%cmake_build

%install
echo "release version = %{_version}"
# make install
%cmake_install

# tidy some .dot {files,dirs} installation
# Fix any .py files with shebangs and wrong permissions.
find %{buildroot} -name "*.py" -perm 0644 -print0 | \
	xargs -0r grep -l '^#!' | xargs -d'\n' chmod -f 0755;
# Copy text files to correct place.
mkdir -p %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}
mv -v %{buildroot}%{_datadir}/doc/blender/* %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}/
rmdir %{buildroot}%{_datadir}/doc/blender
# install blender sample.
install -D -m 0644 %{SOURCE4} %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}/
install -D -m 0644 %{SOURCE5} %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}/
install -D -m 0644 %{SOURCE6} %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}/
install -D -m 0644 %{SOURCE7} %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}/
install -D -m 0755 %{SOURCE8} %{buildroot}%{_bindir}/
# GPU and OptiX rendering texts
install -D -m 0644 %{SOURCE9} %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}/
install -D -m 0644 %{SOURCE10} %{buildroot}%{_docdir}/%{pkg_name}-%{_suffix}/

chmod -f 0644 %{buildroot}%{_datadir}/%{pkg_name}/%{_version}/scripts/modules/console_python.py

%fdupes %{buildroot}%{_datadir}/%{pkg_name}/%{_version}/
%find_lang %{pkg_name} %{?no_lang_C}
rm -rf %{buildroot}%{_datadir}/locale/languages

%ifnarch x86_64
find %{buildroot}%{_datadir}/%{pkg_name}/%{_version}/scripts/ -name "*.h" -print -delete
%endif

# distinguishable menu entry
perl -p -i -e 's/^Name=Blender$/Name=Blender %{_version}/g ; s/^((Exec|Icon)=blender)/$1-%{_version}/g' \
  %{buildroot}%{_datadir}/applications/%{pkg_name}.desktop

%if 0%{?sles_version}
%suse_update_desktop_file -i -n %{pkg_name}
%else
# Validate blender.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{pkg_name}.desktop
%endif

mv %{buildroot}%{_bindir}/blender{,-%{_version}}
mv %{buildroot}%{_bindir}/blender-sample{,-%{_version}}
mv %{buildroot}%{_bindir}/blender-thumbnailer{,-%{_version}}
mv %{buildroot}%{_datadir}/applications/blender{,-%{_version}}.desktop
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/blender{,-%{_version}}.svg
mv %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/blender-symbolic{,-%{_version}}.svg
mv %{buildroot}%{_mandir}/man1/blender{,-%{_version}}.1
mv %{buildroot}%{_datadir}/metainfo/org.blender.Blender{,-%{_version}}.metainfo.xml

%if "%{name}" == "blender" && %{without blender_ua}
ln %{buildroot}%{_bindir}/blender{-%{_version},}
ln %{buildroot}%{_bindir}/blender-sample{-%{_version},}
ln %{buildroot}%{_bindir}/blender-thumbnailer{-%{_version},}
ln %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/blender{-%{_version},}.svg
ln %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/blender-symbolic{-%{_version},}.svg
ln %{buildroot}%{_mandir}/man1/blender{-%{_version},}.1
ln %{buildroot}%{_datadir}/metainfo/org.blender.Blender{-%{_version},}.metainfo.xml
%endif

%if %{with blender_ua}
mkdir -p %{buildroot}/etc/alternatives/

%if %{with self_ghosting}
ln -s blender                          %{buildroot}/etc/alternatives/blender
ln -s blender-sample                   %{buildroot}/etc/alternatives/blender-sample
ln -s blender-thumbnailer              %{buildroot}/etc/alternatives/blender-thumbnailer
ln -s blender.desktop                  %{buildroot}/etc/alternatives/blender.desktop
ln -s blender.svg                      %{buildroot}/etc/alternatives/blender.svg
ln -s blender-symbolic.svg             %{buildroot}/etc/alternatives/blender-symbolic.svg
ln -s blender.1.gz                     %{buildroot}/etc/alternatives/blender.1.gz
ln -s org.blender.Blender.metainfo.xml %{buildroot}/etc/alternatives/org.blender.Blender.metainfo.xml
%endif

ln -s /etc/alternatives/blender                          %{buildroot}%{_bindir}/blender
ln -s /etc/alternatives/blender-sample                   %{buildroot}%{_bindir}/blender-sample
ln -s /etc/alternatives/blender-thumbnailer              %{buildroot}%{_bindir}/blender-thumbnailer
ln -s /etc/alternatives/blender.desktop                  %{buildroot}%{_datadir}/applications/blender.desktop
ln -s /etc/alternatives/blender.svg                      %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/blender.svg
ln -s /etc/alternatives/blender-symbolic.svg             %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/blender-symbolic.svg
ln -s /etc/alternatives/blender.1.gz                     %{buildroot}%{_mandir}/man1/blender.1.gz
ln -s /etc/alternatives/org.blender.Blender.metainfo.xml %{buildroot}%{_datadir}/metainfo/org.blender.Blender.metainfo.xml

%post
/usr/sbin/update-alternatives --quiet --install \
  %{_bindir}/blender                                                     blender                          %{_bindir}/blender-%{_version} %{_suffix} \
    --slave %{_bindir}/blender-sample                                    blender-sample                   %{_bindir}/blender-sample-%{_version} \
    --slave %{_bindir}/blender-thumbnailer                               blender-thumbnailer              %{_bindir}/blender-thumbnailer-%{_version} \
    --slave %{_datadir}/applications/blender.desktop                     blender.desktop                  %{_datadir}/applications/blender-%{_version}.desktop \
    --slave %{_datadir}/icons/hicolor/scalable/apps/blender.svg          blender.svg                      %{_datadir}/icons/hicolor/scalable/apps/blender-%{_version}.svg \
    --slave %{_datadir}/icons/hicolor/symbolic/apps/blender-symbolic.svg blender-symbolic.svg             %{_datadir}/icons/hicolor/symbolic/apps/blender-symbolic-%{_version}.svg \
    --slave %{_mandir}/man1/blender.1.gz                                 blender.1.gz                     %{_mandir}/man1/blender-%{_version}.1.gz \
    --slave %{_datadir}/metainfo/org.blender.Blender.metainfo.xml        org.blender.Blender.metainfo.xml %{_datadir}/metainfo/org.blender.Blender-%{_version}.metainfo.xml

%postun
if [ ! -f %{_bindir}/blender-%{_version} ] ; then
  /usr/sbin/update-alternatives --quiet --remove blender %{_bindir}/blender-%{_version}
fi
%endif

%files lang -f %{pkg_name}.lang
%dir %{_datadir}/%{pkg_name}/%{_version}/datafiles/locale
%dir %{_datadir}/%{pkg_name}/%{_version}/datafiles/locale/*
%dir %{_datadir}/%{pkg_name}/%{_version}/datafiles/locale/*/LC_MESSAGES
%{_datadir}/%{pkg_name}/%{_version}/datafiles/locale/languages

%files
%{_bindir}/*-%{_version}
%{_mandir}/man1/%{pkg_name}-%{_version}.1.gz
%dir %{_datadir}/%{pkg_name}/
%dir %{_datadir}/%{pkg_name}/%{_version}/
%dir %{_datadir}/%{pkg_name}/%{_version}/datafiles/
%{_datadir}/%{pkg_name}/%{_version}/extensions/
%{_datadir}/%{pkg_name}/%{_version}/scripts/
%{_datadir}/%{pkg_name}/%{_version}/datafiles/assets/
%{_datadir}/%{pkg_name}/%{_version}/datafiles/colormanagement/
%{_datadir}/%{pkg_name}/%{_version}/datafiles/fonts/
%{_datadir}/%{pkg_name}/%{_version}/datafiles/icons/
%{_datadir}/%{pkg_name}/%{_version}/datafiles/studiolights/
%{_datadir}/applications/%{pkg_name}-%{_version}.desktop
%{_datadir}/icons/hicolor/*/apps/%{pkg_name}*-%{_version}.svg
%{_datadir}/metainfo/org.%{pkg_name}.Blender-%{_version}.metainfo.xml
%doc %{_docdir}/%{pkg_name}-%{_suffix}
%exclude %{_docdir}/%{pkg_name}-%{_suffix}/geeko_example_scene.*
%if %{with blender_ua}
%ghost /etc/alternatives/blender
%ghost /etc/alternatives/blender-sample
%ghost /etc/alternatives/blender-thumbnailer
%ghost /etc/alternatives/blender.desktop
%ghost /etc/alternatives/blender.svg
%ghost /etc/alternatives/blender-symbolic.svg
%ghost /etc/alternatives/blender.1.gz
%ghost /etc/alternatives/org.blender.Blender.metainfo.xml
%endif
%if %{with blender_ua} || "%{name}" == "blender"
%{_bindir}/blender
%{_bindir}/blender-sample
%{_bindir}/blender-thumbnailer
%{_datadir}/icons/hicolor/scalable/apps/blender.svg
%{_datadir}/icons/hicolor/symbolic/apps/blender-symbolic.svg
%{_mandir}/man1/blender.1.gz
%{_datadir}/metainfo/org.blender.Blender.metainfo.xml
%endif

%files demo
%doc %{_docdir}/%{pkg_name}-%{_suffix}/geeko_example_scene.*

%changelog
