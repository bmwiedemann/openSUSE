#
# spec file for package darktable
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_with clang

%if 0%{?fedora_version} >= 33
%bcond_without use_intree_lua
%else
%bcond_with    use_intree_lua
%endif

%if %{with use_intree_lua}
%define _dont_use_intree_lua OFF
%else
%define _dont_use_intree_lua ON
%endif

%if 0%{?suse_version} || 0%{?fedora_version} >= 33
%bcond_without cmake_macros
%else
%bcond_with    cmake_macros
%endif

%if 0%{?suse_version} || 0%{?fedora_version} >= 33
%bcond_without cmake_macros
%else
%bcond_with    cmake_macros
%endif

%if 0%{?is_opensuse} || 0%{?fedora_version} >= 26
%bcond_without osmgpsmap
%bcond_without flickcurl
%bcond_without translated_manpages
%else
%bcond_with    osmgpsmap
%bcond_with    flickcurl
%bcond_with    translated_manpages
%endif

%if 0%{?suse_version} >= 1550 || 0%{?fedora_version} >= 33
%bcond_without avif
%else
%bcond_with    avif
%endif

%if 0%{?suse_version} >= 1550
%bcond_without gmic
%else
%bcond_with    gmic
%endif

%ifarch ppc64le
# The OpenCL kernels don't compile on ppc64le and if you get
# them compiled there are funny runtime issues.
%bcond_with     opencl
%else
%bcond_without  opencl
%endif

%bcond_without  openmp

%if %{with openmp}
%global _use_openmp "ON"
%else
%global _use_openmp "OFF"
%endif

%if %{with opencl}
%global _use_opencl "ON"
%else
%global _use_opencl "OFF"
%endif

%if %{with gmic}
%global _use_gmic "ON"
%else
%global _use_gmic "OFF"
%endif

%if %{with avif}
%global _use_avif "ON"
%else
%global _use_avif "OFF"
%endif

%if 0%{?suse_version} && 0%{?suse_version} < 1550
%define force_gcc_version 7
%endif

Name:           darktable
Version:        3.4.1
Release:        0
%define pkg_name darktable
%define pkg_version %{version}
URL:            http://www.darktable.org/
Source0:        https://github.com/darktable-org/darktable/releases/download/release-%{version}/%{pkg_name}-%{version}.tar.xz
Source1:        https://github.com/darktable-org/darktable/releases/download/release-%{version}/%{pkg_name}-%{version}.tar.xz.asc
Source2:        %{pkg_name}-rpmlintrc
#
Source10:       https://github.com/darktable-org/darktable/releases/download/release-3.4.0/darktable-usermanual.pdf
Source11:       https://github.com/darktable-org/darktable/releases/download/release-3.0.0/darktable-usermanual-de.pdf
Source12:       https://github.com/darktable-org/darktable/releases/download/release-3.0.0/darktable-usermanual-it.pdf
Source13:       https://github.com/darktable-org/darktable/releases/download/release-3.0.0/darktable-usermanual-fr.pdf
# This is not online yet?
Source14:       darktable-lua-api.pdf
#
Source97:       darktable.dsc
Source98:       debian.tar.xz
Source99:       README.openSUSE
#
Patch0:         darktable-old-glib.patch
#
ExclusiveArch:  x86_64 aarch64 ppc64le
# build time tools
BuildRequires:  clang
BuildRequires:  cmake >= 3.4
BuildRequires:  fdupes
BuildRequires:  llvm-devel
%if 0%{?fedora_version}
BuildRequires:  llvm-static
%endif
%if %{without clang}
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 5
%if 0%{?force_gcc_version}
#!BuildIgnore:  libgcc_s1
%endif
%endif
BuildRequires:  intltool
BuildRequires:  libxslt
%if %{with translated_manpages}
BuildRequires:  po4a
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  xz
# libraries deps
BuildRequires:  cups-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
#
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(lua5.3)
%else
BuildRequires:  pkgconfig(lua)
%endif
%if 0%{?fedora_version} == 31
BuildRequires:  pugixml-devel
%else
BuildRequires:  pkgconfig(pugixml)
%endif
#
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libopenjp2)
%if %{with flickcurl}
BuildRequires:  pkgconfig(flickcurl)
%endif
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libwebp)
%if %{with osmgpsmap}
BuildRequires:  pkgconfig(osmgpsmap-1.0)
%endif
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sqlite3)
%if %{with opencl}
BuildRequires:  opencl-headers
%endif
%if %{with gmic}
%if 0%{?is_opensuse}
BuildRequires:  libgmic-devel
%else
BuildRequires:  gmic-devel
%endif
# /gmic
%endif
%if %{with avif}
BuildRequires:  libavif-devel
%endif

# for the sake of simplicity we do not enforce the version here
# the package is small enough that installing it doesnt hurt
Requires:       iso-codes
#
# Some CSS themes suggest to use the the Roboto font family
# https://github.com/darktable-org/darktable/releases/tag/release-3.0.0
%if 0%{?fedora_version}
Recommends:     roboto-fontface-fonts
%else
Recommends:     google-roboto-fonts
%endif
#
Summary:        A virtual Lighttable and Darkroom
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers

%description
darktable is a virtual lighttable and darkroom for photographers: it manages
digital negatives in a database and can show them through a zoomable
lighttable. It also enables developing raw images and enhance them.

%package tools-basecurve
Summary:        The basecurve tool from tools/basecurve/
Group:          Productivity/Graphics/Viewers
Requires:       /usr/bin/convert
Requires:       dcraw
Requires:       exiftool

%description tools-basecurve
darktable is a virtual lighttable and darkroom for photographers: it manages
digital negatives in a database and can show them through a zoomable
lighttable. It also enables developing raw images and enhance them.

This package provides the basecurve tool from tools/basecurve/.
Another option to solve the same problem might be the darktable-chart module
from the darktable package.

%package tools-noise
Summary:        Noise profiling tools to support new cameras
Group:          Productivity/Graphics/Viewers
Requires:       /usr/bin/convert
Requires:       ghostscript
Requires:       gnuplot

%description tools-noise
darktable is a virtual lighttable and darkroom for photographers: it manages
digital negatives in a database and can show them through a zoomable
lighttable. It also enables developing raw images and enhance them.

This package provides the noise profiling tools to add support for new cameras.

%package doc
Summary:        Documentation for Darktable
Group:          Documentation/Other
BuildArch:      noarch

%description doc
darktable is a virtual lighttable and darkroom for photographers: it manages
digital negatives in a database and can show them through a zoomable
lighttable. It also enables developing raw images and enhance them.

This package provides the user manual in PDF format.

%prep
%autosetup -p1 -n %{pkg_name}-%{version}

cp %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} .
cp %{SOURCE99} .

# Remove bundled OpenCL headers.
rm -rf src/external/CL src/external/OpenCL
sed -i -e 's, \"external/CL/\*\.h\" , ,' src/CMakeLists.txt

# Remove bundled lua
%if %{without use_intree_lua}
rm -rf src/external/lua/
%endif

%build
%global cmake_options \\\
   -DCMAKE_INSTALL_LIBDIR=%{_lib} \\\
   -DCMAKE_SKIP_RPATH:BOOL=OFF \\\
   -DCMAKE_INSTALL_DATAROOTDIR="share" \\\
   -DCMAKE_INSTALL_LIBEXECDIR="%{_libexecdir}" \\\
   -DCMAKE_INSTALL_DOCDIR="%{_defaultdocdir}/%{pkg_name}" \\\
   -DBINARY_PACKAGE_BUILD=1 \\\
   -DRAWSPEED_ENABLE_LTO=ON \\\
   -DUSE_OPENCL="%{_use_opencl}" \\\
   -DUSE_OPENMP="%{_use_openmp}" \\\
   -DUSE_GMIC="%{_use_gmic}" \\\
   -DUSE_AVIF="%{_use_avif}" \\\
   -DBUILD_NOISE_TOOLS=ON \\\
   -DBUILD_CURVE_TOOLS=ON

%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%if %{with clang}
export CC="/usr/bin/clang"
export CXX="/usr/bin/clang++"
%endif
export _OPENCL_INCLUDE_DIR=$(clang -print-search-dirs | awk -F= '/^libra/ {print $2}' | awk -F: '{print $1 "/include"}')

%if %{with cmake_macros}
#suse branch
%cmake \
  -DCLANG_OPENCL_INCLUDE_DIR=${_OPENCL_INCLUDE_DIR} \
  -DDONT_USE_INTERNAL_LUA=%{_dont_use_intree_lua} \
  %ifarch aarch64
  -DTESTBUILD_OPENCL_PROGRAMS=OFF \
  %endif
  %{cmake_options} \
%if "%{optimization_architecture}" == "asan"
  -DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" -DCMAKE_SHARED_LINKER_FLAGS="" -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
%endif
   || cat CMakeFiles/CMakeError.log
%cmake_build
#/ suse branch
%else
#fedora branch
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake \
  -DDONT_USE_INTERNAL_LUA=%{_dont_use_intree_lua} \
  %ifarch aarch64
  -DTESTBUILD_OPENCL_PROGRAMS=OFF \
  %endif
  %{cmake_options} ..
make %{_smp_mflags} VERBOSE=1

#/ with cmake_macros
%endif

%install
%if %{with cmake_macros}
%cmake_install

%if 0%{?suse_version}
%suse_update_desktop_file darktable
%endif
#/ cmake macros branch
%else
# fedora branch
%make_install -C %{_target_platform}
#/ fedora branch
%endif

%find_lang darktable

cp -av %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} doc/TODO \
  %{buildroot}%{_defaultdocdir}/%{pkg_name}
rm %{buildroot}%{_defaultdocdir}/%{pkg_name}/LICENSE

%fdupes %{buildroot}/%{_prefix}

%if ! 0%{?suse_version}
%post
touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || :

%postun
update-desktop-database >/dev/null 2>/dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || :
%endif

%files -f darktable.lang
%doc %{_defaultdocdir}/%{pkg_name}
%license LICENSE
%exclude %{_defaultdocdir}/%{pkg_name}/*.pdf
%exclude %{_defaultdocdir}/%{pkg_name}/README.tools.basecurve.md
%{_bindir}/darktable
%if %{with opencl}
%{_bindir}/darktable-cltest
%endif
%{_bindir}/darktable-cli
%{_bindir}/darktable-generate-cache
%{_bindir}/darktable-chart
%{_bindir}/darktable-cmstest
%{_bindir}/darktable-rs-identify
%{_libdir}/darktable
%{_datadir}/applications/darktable.desktop
%{_datadir}/darktable
%exclude %{_datadir}/%{pkg_name}/tools/basecurve/
%dir %{_datadir}/appdata
%{_datadir}/appdata/darktable.appdata.xml
%{_datadir}/icons/hicolor/*/apps/darktable*
%{_mandir}/man1/darktable*.1*
%if %{with translated_manpages}
%{_mandir}/*/man1/darktable*.1*
%endif
%dir %{_libexecdir}/darktable
%dir %{_libexecdir}/darktable/tools

%files tools-basecurve
%{_libexecdir}/darktable/tools/darktable-curve-tool
%{_libexecdir}/darktable/tools/darktable-curve-tool-helper
%{_datadir}/%{pkg_name}/tools/basecurve/
%doc %{_defaultdocdir}/%{pkg_name}/README.tools.basecurve.md

%files tools-noise
%{_libexecdir}/darktable/tools/darktable-gen-noiseprofile
%{_libexecdir}/darktable/tools/darktable-noiseprofile
%{_libexecdir}/darktable/tools/profiling-shot.xmp
%{_libexecdir}/darktable/tools/subr.sh

%files doc
%{_defaultdocdir}/%{pkg_name}/*.pdf

%changelog
