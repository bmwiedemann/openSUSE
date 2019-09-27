#
# spec file for package blender
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 LISA GMbH, Bingen, Germany.
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


%bcond_without alembic
%bcond_without collada
%ifarch x86_64
%bcond_without embree
%else
%bcond_with embree
%endif
%bcond_without opensubdiv
%bcond_without openvdb
%bcond_without osl
%bcond_without system_audaspace
%bcond_with wplayer

# Set this to 1 for fixing bugs.
%define debugbuild 0
# Find the version of python3 that blender is going to build against.
%define py3version %(pkg-config python3 --modversion)
# blender has versions like x.xxy which have x.xx (notice the missing
# trailing y) in the directory path. This makes this additional variable
# necessary.
%define _version %(echo %{version} | cut -b 1-4)

Name:           blender
Version:        2.80
Release:        0
Summary:        A 3D Modelling And Rendering Package
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/3D Editors
Url:            http://www.blender.org/
# http://download.blender.org/source/
Source0:        http://download.blender.org/source/%{name}-%{version}.tar.gz
Source1:        http://download.blender.org/source/%{name}-%{version}.tar.gz.md5sum
Source2:        geeko.blend
Source3:        geeko.README
Source4:        blender-sample
Source8:        %{name}.appdata.xml
#!BuildIgnore:  libGLwM1
BuildRequires:  OpenColorIO-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  OpenImageIO-devel
BuildRequires:  SDL2-devel
BuildRequires:  binutils-gold
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  distribution-release
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libboost_wave-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libspnav-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  llvm-devel
BuildRequires:  lzo-devel
BuildRequires:  memory-constraints
BuildRequires:  openal-soft-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-Text-Iconv
BuildRequires:  pkg-config
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-requests
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  cmake(pugixml)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(glw)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python3) >= 3.7
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
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
BuildRequires:  embree-devel-static
%endif
%if %{with opensubdiv}
BuildRequires:  OpenSubdiv-devel
%endif
%if %{with openvdb}
BuildRequires:  openvdb-devel
BuildRequires:  cmake(TBB)
BuildRequires:  pkgconfig(blosc)
%endif
%if %{with osl}
BuildRequires:  OpenShadingLanguage-devel
%endif
%if %{with system_audaspace}
BuildRequires:  pkgconfig(audaspace) >= 1.3
Requires:       audaspace-plugins
%endif
%ifarch x86_64
Requires:       %{name}-cycles-devel = %{version}
%endif
Requires:       python3-base >= %{py3version}
Requires:       python3-numpy
Requires:       python3-requests
Requires:       python3-xml
Requires(post):    hicolor-icon-theme
Requires(postun):  hicolor-icon-theme

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

%ifarch x86_64
%package cycles-devel
Summary:        Headers for cycles rendering
#This package is for blender with cycles OSL
License:        Apache-2.0
Group:          Development/Sources
Obsoletes:      blender-devel <= %{version}
BuildArch:      noarch

%description cycles-devel
These are the cycles headers that blender uses for rendering with
specific gpus
%endif

%lang_package

%prep
pushd "%{_sourcedir}"
md5sum -c %{SOURCE1}
popd

%setup -q
%autopatch -p1

rm -rf extern/glew
rm -rf extern/libopenjpeg
for i in `grep -rl "/usr/bin/env python3"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done

%build
%limit_build -m 1500
#The limit_build macro fails to give the same value to -flto= as it gives to -j
#resulting in link time crashes
echo $_threads
%define _lto_cflags -flto=$_threads
echo %{optflags}
# sse options only on supported archs
%ifarch %{ix86} x86_64
sseflags='-msse -msse2'
%endif
# Find python3 version and abiflags
export psver=$(pkg-config python3 --modversion)
export pver=$(pkg-config python3 --modversion)$(python3-config --abiflags)
mkdir -p build && pushd build

# FIXME: This comes from a stupid osc spec formatter
# blender's flags are complex enough already without %%cmake macro spamming the build log.
# It also puts _smp_mflags where it shouldn't, I had to write make -j1 to stop it.
# NOTE: Don't use cmake macro.
#
# lean against build_files/cmake/config/blender_release.cmake
cmake ../ \
%if 0%{?debugbuild} == 1
      -DCMAKE_BUILD_TYPE:STRING=Debug \
      -DCMAKE_C_FLAGS_DEBUG:STRING="-fsanitize=address -ggdb" \
      -DCMAKE_CXX_FLAGS_DEBUG:STRING="-fsanitize=address -ggdb" \
      -DWITH_MEM_VALGRIND:BOOL=ON \
      -DWITH_ASSERT_ABORT:BOOL=ON \
%else
      -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIC ${sseflags} -fopenmp" \
      -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIC ${sseflags} -fopenmp" \
%endif
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
      -DWITH_BUILDINFO:BOOL=ON \
      -DWITH_BULLET:BOOL=ON \
      -DWITH_CODEC_AVI:BOOL=ON \
      -DWITH_CODEC_FFMPEG:BOOL=ON \
      -DWITH_CODEC_SNDFILE:BOOL=ON \
      -DLIBSNDFILE_ROOT_DIR:FILE=%{_prefix} \
%ifarch ppc ppc64 ppc64le
      -DWITH_CYCLES:BOOL=OFF \
%else
      -DWITH_CYCLES:BOOL=ON \
%if %{with osl}
      -DWITH_CYCLES_OSL:BOOL=ON \
%endif
%if %{with embree}
      -DWITH_CYCLES_EMBREE:BOOL=ON \
%endif
      -DWITH_LLVM:BOOL=ON \
      -DLLVM_LIBRARY:FILE=%{_libdir}/libLLVM.so \
%endif
      -DWITH_DRACO:BOOL=ON \
      -DWITH_FFTW3:BOOL=ON \
      -DWITH_LIBMV:BOOL=ON \
      -DWITH_LIBMV_SCHUR_SPECIALIZATIONS:BOOL=ON \
      -DWITH_COMPOSITOR:BOOL=ON \
      -DWITH_FREESTYLE:BOOL=ON \
      -DWITH_GHOST_XDND:BOOL=ON \
      -DWITH_IK_SOLVER:BOOL=ON \
      -DWITH_IK_ITASC:BOOL=ON \
      -DWITH_IMAGE_CINEON:BOOL=ON \
      -DWITH_IMAGE_DDS:BOOL=ON \
      -DWITH_IMAGE_HDR:BOOL=ON \
      -DWITH_IMAGE_OPENEXR:BOOL=ON \
      -DWITH_IMAGE_OPENJPEG:BOOL=ON \
      -DOPENJPEG_LIBRARY:FILE=%{_libdir}/libopenjp2.so \
      -DWITH_IMAGE_TIFF:BOOL=ON \
      -DWITH_INPUT_NDOF:BOOL=ON \
      -DWITH_INTERNATIONAL:BOOL=ON \
      -DWITH_JACK:BOOL=ON \
      -DWITH_JACK_DYNLOAD:BOOL=ON \
      -DWITH_LZMA:BOOL=ON \
      -DWITH_LZO:BOOL=ON \
      -DWITH_SYSTEM_LZO:BOOL=ON \
      -DWITH_MOD_FLUID:BOOL=ON \
      -DWITH_MOD_REMESH:BOOL=ON \
      -DWITH_MOD_SMOKE:BOOL=ON \
%ifnarch x86_64
      -DWITH_MOD_OCEANSIM:BOOL=OFF \
%else
      -DWITH_MOD_OCEANSIM:BOOL=ON \
%endif
      -DWITH_AUDASPACE:BOOL=ON \
%if %{with system_audaspace}
      -DWITH_SYSTEM_AUDASPACE:BOOL=ON \
%endif
      -DWITH_OPENAL:BOOL=ON \
%if %{with collada}
      -DWITH_OPENCOLLADA:BOOL=ON \
%else
      -DWITH_OPENCOLLADA:BOOL=OFF \
%endif
      -DWITH_OPENCOLORIO:BOOL=ON \
      -DWITH_OPENIMAGEIO:BOOL=ON \
      -DWITH_OPENMP:BOOL=ON \
%if %{with opensubdiv}
      -DWITH_OPENSUBDIV:BOOL=ON \
      -DOPENSUBDIV_OSDGPU_LIBRARY:FILE=%{_libdir}/libosdGPU.so \
%endif
%if %{with openvdb}
      -DWITH_OPENVDB:BOOL=ON \
      -DWITH_OPENVDB_BLOSC:BOOL=ON \
%endif
      -DWITH_PYTHON:BOOL=ON \
      -DWITH_PYTHON_INSTALL:BOOL=OFF \
      -DPYTHON_VERSION=$psver \
      -DPYTHON_LIBPATH=%{_libexecdir} \
      -DPYTHON_LIBRARY=python$pver \
      -DPYTHON_INCLUDE_DIRS=%{_includedir}/python$pver \
      -DWITH_PYTHON_INSTALL_NUMPY=OFF \
%ifnarch x86_64
      -DWITH_RAYOPTIMIZATION:BOOL=OFF \
%else
      -DWITH_RAYOPTIMIZATION:BOOL=ON \
%endif
      -DWITH_SDL:BOOL=ON \
      -DWITH_SYSTEM_GLEW:BOOL=ON \
      -DWITH_X11_XINPUT:BOOL=ON \
      -DWITH_X11_XF86VMODE:BOOL=ON \
      -DWITH_DOC_MANPAGE:BOOL=ON \
      -DCYCLES_CUDA_BINARIES_ARCH="sm_30;sm_35;sm_37;sm_50;sm_52;sm_60;sm_61;sm_70;sm_75"

#Build at all costs
if ! make %{?_smp_mflags}
then \
%define _lto_cflags %{nil}
cmake ../ \
%if 0%{?debugbuild} == 1
      -DCMAKE_BUILD_TYPE:STRING=Debug \
      -DCMAKE_C_FLAGS_DEBUG:STRING="-fsanitize=address -ggdb" \
      -DCMAKE_CXX_FLAGS_DEBUG:STRING="-fsanitize=address -ggdb" \
      -DWITH_MEM_VALGRIND:BOOL=ON \
      -DWITH_ASSERT_ABORT:BOOL=ON \
%else
      -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIC ${sseflags} -fopenmp" \
      -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIC ${sseflags} -fopenmp" \
%endif
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
      -DWITH_BUILDINFO:BOOL=ON \
      -DWITH_BULLET:BOOL=ON \
      -DWITH_CODEC_AVI:BOOL=ON \
      -DWITH_CODEC_FFMPEG:BOOL=ON \
      -DWITH_CODEC_SNDFILE:BOOL=ON \
      -DLIBSNDFILE_ROOT_DIR:FILE=%{_prefix} \
%ifarch ppc ppc64 ppc64le
      -DWITH_CYCLES:BOOL=OFF \
%else
      -DWITH_CYCLES:BOOL=ON \
%if %{with osl}
      -DWITH_CYCLES_OSL:BOOL=ON \
%endif
%if %{with embree}
      -DWITH_CYCLES_EMBREE:BOOL=ON \
%endif
      -DWITH_LLVM:BOOL=ON \
      -DLLVM_LIBRARY:FILE=%{_libdir}/libLLVM.so \
%endif
      -DWITH_DRACO:BOOL=ON \
      -DWITH_FFTW3:BOOL=ON \
      -DWITH_LIBMV:BOOL=ON \
      -DWITH_LIBMV_SCHUR_SPECIALIZATIONS:BOOL=ON \
      -DWITH_COMPOSITOR:BOOL=ON \
      -DWITH_FREESTYLE:BOOL=ON \
      -DWITH_GHOST_XDND:BOOL=ON \
      -DWITH_IK_SOLVER:BOOL=ON \
      -DWITH_IK_ITASC:BOOL=ON \
      -DWITH_IMAGE_CINEON:BOOL=ON \
      -DWITH_IMAGE_DDS:BOOL=ON \
      -DWITH_IMAGE_HDR:BOOL=ON \
      -DWITH_IMAGE_OPENEXR:BOOL=ON \
      -DWITH_IMAGE_OPENJPEG:BOOL=ON \
      -DOPENJPEG_LIBRARY:FILE=%{_libdir}/libopenjp2.so \
      -DWITH_IMAGE_TIFF:BOOL=ON \
      -DWITH_INPUT_NDOF:BOOL=ON \
      -DWITH_INTERNATIONAL:BOOL=ON \
      -DWITH_JACK:BOOL=ON \
      -DWITH_JACK_DYNLOAD:BOOL=ON \
      -DWITH_LZMA:BOOL=ON \
      -DWITH_LZO:BOOL=ON \
      -DWITH_SYSTEM_LZO:BOOL=ON \
      -DWITH_MOD_FLUID:BOOL=ON \
      -DWITH_MOD_REMESH:BOOL=ON \
      -DWITH_MOD_SMOKE:BOOL=ON \
%ifnarch x86_64
      -DWITH_MOD_OCEANSIM:BOOL=OFF \
%else
      -DWITH_MOD_OCEANSIM:BOOL=ON \
%endif
      -DWITH_AUDASPACE:BOOL=ON \
%if %{with system_audaspace}
      -DWITH_SYSTEM_AUDASPACE:BOOL=ON \
%endif
      -DWITH_OPENAL:BOOL=ON \
%if %{with collada}
      -DWITH_OPENCOLLADA:BOOL=ON \
%else
      -DWITH_OPENCOLLADA:BOOL=OFF \
%endif
      -DWITH_OPENCOLORIO:BOOL=ON \
      -DWITH_OPENIMAGEIO:BOOL=ON \
      -DWITH_OPENMP:BOOL=ON \
%if %{with opensubdiv}
      -DWITH_OPENSUBDIV:BOOL=ON \
      -DOPENSUBDIV_OSDGPU_LIBRARY:FILE=%{_libdir}/libosdGPU.so \
%endif
%if %{with openvdb}
      -DWITH_OPENVDB:BOOL=ON \
      -DWITH_OPENVDB_BLOSC:BOOL=ON \
%endif
      -DWITH_PYTHON:BOOL=ON \
      -DWITH_PYTHON_INSTALL:BOOL=OFF \
      -DPYTHON_VERSION=$psver \
      -DPYTHON_LIBPATH=%{_libexecdir} \
      -DPYTHON_LIBRARY=python$pver \
      -DPYTHON_INCLUDE_DIRS=%{_includedir}/python$pver \
      -DWITH_PYTHON_INSTALL_NUMPY=OFF \
%ifnarch x86_64
      -DWITH_RAYOPTIMIZATION:BOOL=OFF \
%else
      -DWITH_RAYOPTIMIZATION:BOOL=ON \
%endif
      -DWITH_SDL:BOOL=ON \
      -DWITH_SYSTEM_GLEW:BOOL=ON \
      -DWITH_X11_XINPUT:BOOL=ON \
      -DWITH_X11_XF86VMODE:BOOL=ON \
      -DWITH_DOC_MANPAGE:BOOL=ON \
      -DCYCLES_CUDA_BINARIES_ARCH="sm_30;sm_35;sm_37;sm_50;sm_52;sm_60;sm_61;sm_70;sm_75"
make
fi

%install
echo "release version = %{_version}"
# make install
%cmake_install

# Remove folder, it's not supposed to be installed here.
rm -rf %{buildroot}%{_datadir}/%{name}/%{_version}/datafiles/fonts
rm -f %{buildroot}%{_datadir}/%{name}/%{_version}/scripts/addons/.gitignore
# Fix any .py files with shebangs and wrong permissions.
find %{buildroot} -name "*.py" -perm 0644 -print0 | \
	xargs -0r grep -l '#!' | xargs -d'\n' chmod -f 0755;
# Copy text files to correct place.
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -rv %{buildroot}%{_datadir}/doc/blender/* %{buildroot}%{_docdir}/%{name}/
rm -rf %{buildroot}%{_datadir}/doc/blender
# install blender sample.
install -D -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/
install -D -m 0644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}/
install -D -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/

# install appdata file
mkdir -p %{buildroot}%{_datadir}/appdata/
install -D -m 0644 %{SOURCE8} %{buildroot}%{_datadir}/appdata/

find %{buildroot} -empty -print -delete
chmod -f 0644 %{buildroot}%{_datadir}/%{name}/%{_version}/scripts/modules/console_python.py

find %{buildroot}%{_docdir}/%{name} -name "*.py" -perm 0755 -print0 | \
	xargs -0r grep -l '#!' | xargs -d'\n' -r chmod -f 0644
%fdupes %{buildroot}%{_datadir}/%{name}/%{_version}/
%find_lang %{name} %{?no_lang_C}
rm -rf %{buildroot}%{_datadir}/locale/languages

%ifnarch x86_64
find %{buildroot}%{_datadir}/%{name}/%{_version}/scripts/ -name "*.h" -print -delete
%endif

# Factory is now of the opinion that every /usr/bin file needs a man page,
%if %{with wplayer}
# Create man1 directory if it doesn't exist.
mkdir -p %{buildroot}%{_mandir}/man1
# Generate man page with help2man
pushd %{buildroot}%{_mandir}/man1
cp -v %{buildroot}%{_bindir}/blenderplayer ./
help2man \
	--version-string="%{version}" \
	--help-option="-h" -n "a utility for previewing .blend files" \
	-s 1 -m "User Commands" -S "Stichting Blender Foundation" -N -o blenderplayer.1 ./'blenderplayer -h ""'
rm blenderplayer
popd
#cp -v %%{SOURCE5} %%{buildroot}%%{_mandir}/man1
%endif

# don't package thumbnailer
rm %{buildroot}%{_bindir}/%{name}-thumbnailer.py

%if 0%{?sles_version}
%suse_update_desktop_file -i -n %{name}
%else
# Validate blender.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

%post
%mime_database_post
%desktop_database_post
%icon_theme_cache_post

%postun
%mime_database_postun
%desktop_database_postun
%icon_theme_cache_post

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/%{_version}/datafiles/locale
%{_datadir}/%{name}/%{_version}/datafiles/locale/

%files
%{_bindir}/*
%{_mandir}/man1/%{name}.1.gz
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{_version}
%dir %{_datadir}/%{name}/%{_version}/datafiles
%exclude %{_datadir}/%{name}/%{_version}/datafiles/locale
%ifarch x86_64
%exclude %{_datadir}/%{name}/%{_version}/scripts/addons/cycles
%endif
%{_datadir}/%{name}/%{_version}/scripts/
%{_datadir}/%{name}/%{_version}/datafiles/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%doc %{_docdir}/%{name}

%ifarch x86_64
%files cycles-devel
%{_datadir}/%{name}/%{_version}/scripts/addons/cycles
%endif

%changelog
