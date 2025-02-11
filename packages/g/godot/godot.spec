#
# spec file for package godot
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017 Luke Jones, luke.nukem.jones@gmail.com
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


# faster_build only builds the editor to speed up the build.
%define faster_build 0

%define _buildshell /bin/bash
# not needed anymore since 4.1
%define ca_bundle %{_localstatedir}/lib/ca-certificates/ca-bundle.pem

# building with default gcc 7.5 fails since 4.1 on Leap
# https://github.com/godotengine/godot/issues/79352
%define compiler_version_leap 10

Name:           godot
Version:        4.3
Release:        0
Summary:        Cross-Platform Game Engine with an Integrated Editor
License:        MIT
Group:          Development/Tools/Other
URL:            https://godotengine.org/
Source0:        https://downloads.tuxfamily.org/godotengine/%{version}/%{name}-%{version}-stable.tar.xz
Source1:        https://downloads.tuxfamily.org/godotengine/%{version}/%{name}-%{version}-stable.tar.xz.sha256
BuildRequires:  Mesa-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
%if %{suse_version} > 1500
BuildRequires:  gcc
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc%{compiler_version_leap}
BuildRequires:  gcc%{compiler_version_leap}-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  scons
BuildRequires:  update-desktop-files
BuildRequires:  yasm-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

%if 0%{?suse_version} > 1500
# Does not work currently:
# BuildRequires:  embree-devel-static >= 3.13.0

# https://github.com/godotengine/godot/issues/64090 :
#   unbundled freetype needs to be build with brotli decompression support
#   to load build in WOFF2 editor fonts since godot version 3.5.
# This was added according to
#   https://build.opensuse.org/package/view_file/M17N/freetype2/freetype2.changes
#   in freetype2 version 2.10.2
# By default this seems to be currently only available in Tumbleweed (v2.12.1).
# As of 20220808 Leap 15.2, .3 and .4 report freetype2 version as 2.10.1
BuildRequires:  pkgconfig(freetype2) >= 2.10.2
# Using bundled freetype2 throws build errors, if
#   we don't use bundled libpng and zlib as well.
BuildRequires:  pkgconfig(libpng)
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libwslay)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(zlib)
%else
%if 0%{?is_opensuse}
# SLES seems not to have wslay and miniupnpc
BuildRequires:  libminiupnpc-devel
BuildRequires:  pkgconfig(libwslay)
%if 0%{?sle_version} >= 150200
BuildRequires:  mbedtls-devel
%endif
%endif
%endif

Requires:       ca-certificates
Recommends:     ca-certificates-mozilla
Requires(post): update-desktop-files
Requires(postun):update-desktop-files
Suggests:       %{name}-runner = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# The following "Provides: bundled()" and comments were taken from the
# Fedora Godot specfile.
# Link: https://src.fedoraproject.org/rpms/godot/blob/master/f/godot.spec

# Has some modifications for IPv6 support, upstream enet is unresponsive
# Should not be unbundled.
Provides:       bundled(enet) = 1.3.18

# Has custom changes to support seeking in zip archives
# Should not be unbundled.
Provides:       bundled(minizip) = 1.3.1

Provides:       bundled(FastLZ)
Provides:       bundled(JetBrainsMono_Regular)
Provides:       bundled(RVO2-3D)
Provides:       bundled(Tangent_Space_Normal_Maps)
Provides:       bundled(amd-fsr) = 1.0.2
Provides:       bundled(amd-fsr2) = 2.2.1
Provides:       bundled(angle)
Provides:       bundled(astcenc) = 4.8.0
Provides:       bundled(basis_universal) = 1.16.4
Provides:       bundled(clipper2) = 1.3.0
Provides:       bundled(cvtt)
Provides:       bundled(d3d12ma) = 2.1.0
Provides:       bundled(directx_headers) = 1.611.1
Provides:       bundled(doctest) = 2.4.11
Provides:       bundled(etcpak) = 1.0
Provides:       bundled(glad) = 2.0.4
# same version for glslang, spirv-reflect, volk and vulkan needed
Provides:       bundled(glslang) = sdk-1.3.283.0
Provides:       bundled(google-droid-fonts)
Provides:       bundled(icu4c) = 75.1
Provides:       bundled(ifaddrs-android)
Provides:       bundled(jpeg-compressor) = 2.00
Provides:       bundled(libbacktrace)
Provides:       bundled(libktx) = 4.3.2
Provides:       bundled(meshoptimizer) = 0.20
Provides:       bundled(mingw-std-threads)
Provides:       bundled(minimp3)
Provides:       bundled(msdfgen) = 1.11
Provides:       bundled(noise) = 1.1.0
Provides:       bundled(noto-sans-fonts)
Provides:       bundled(nvapi) = R525
Provides:       bundled(openxr) = 1.0.34
Provides:       bundled(pcg)
Provides:       bundled(polyclipping)
Provides:       bundled(polypartition)
Provides:       bundled(pvrtccompressor)
Provides:       bundled(qoa)
Provides:       bundled(smaz)
Provides:       bundled(spirv-reflect) = sdk-1.3.283.0
Provides:       bundled(stb)
Provides:       bundled(thorvg) = 0.14.2
Provides:       bundled(tinyexr) = 1.0.8
Provides:       bundled(ufbx) = 0.14.0
Provides:       bundled(vhacd)
Provides:       bundled(volk) = sdk-1.3.283.0
Provides:       bundled(vulkan) = sdk-1.3.283.0
Provides:       bundled(wayland) = 1.22.0
Provides:       bundled(wayland-protocols) = 1.33
Provides:       bundled(yuv2rgb)

# Can be unbundled if packaged
Provides:       bundled(recastnavigation) = 1.6.0
Provides:       bundled(squish) = 1.15
Provides:       bundled(xatlas)

# Embree 3.13.0+ supports both x86_64 and aarch64.
# per 20211108 Factory is at 3.13.0, Leap at 3.8 .
# Currently build fails with Distro (unbundled) embree on Tumbleweed although
# the required version is available.
# Perhaps because it is build with special flags (static) for blender.
Provides:       bundled(embree) = 4.3.1

%if 0%{?suse_version} > 1500
%else
Provides:       bundled(brotli) = 1.1.0

# see comments for freetype2, libpng and zlib Factory BuildRequires
Provides:       bundled(freetype2) = 2.13.2
Provides:       bundled(graphite) = 1.3.14
Provides:       bundled(harfbuzz) = 8.5.0
Provides:       bundled(libpng) = 1.6.43
Provides:       bundled(libzstd) = 1.5.6
Provides:       bundled(zlib) = 1.3.1
%if 0%{?sle_version} < 150200
Provides:       bundled(mbedtls) = 3.6.0
%endif
%if !0%{?is_opensuse}
# SLES seems not to have miniupnpc and wslay
Provides:       bundled(libwslay) = 1.1.1
Provides:       bundled(miniupnpc) = 2.2.7
%endif
%endif

# Build currently fails on armv7l
ExcludeArch:    %arm

%description
Godot is a game engine. It provides a set of tools and a visually
oriented workflow that can export games to PC, Mobile and Web
platforms.

%if !0%{?faster_build}
%package runner
Summary:        Shared binary to play games developed with the Godot engine
Group:          Amusements/Games/Other
Requires:       ca-certificates
Recommends:     ca-certificates-mozilla
Suggests:       %{name}-bash-completion

%description runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.
%endif

%package bash-completion
Summary:        Godot command line completion for Bash
Group:          Amusements/Games/Other
BuildArch:      noarch
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
Enhances:       (%{name}-runner and bash-completion)

%description bash-completion
Bash command line completion support for %{name} and %{name}-runner

%prep
%autosetup -p1 -n %{name}-%{version}-stable

cp thirdparty/README.md thirdparty_README.md

# actual doc location in openSUSE
sed -i 's/\/usr\/share\/doc\/godot\//\/usr\/share\/doc\/packages\/godot\//' misc/dist/linux/godot.6

if [[ -z "$(desktop-file-validate misc/dist/linux/org.godotengine.Godot.desktop)" ]];
 then
  # desktop-file-utils version >= 0.25
  echo desktop-file-utils is up to date and recognizes PrefersNonDefaultGPU.
  # rpmlint complains nevertheless with older rpmlint-mini.
  # Tumbleweed is fixed with update of rpmlint-mini.
  # see https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#recognized-keys
  # Perhaps because rpmlint-mini includes as of today (18.09.2020)
  # desktop-file-utils-0.24 while we checked for available default version >= 0.25
 else
  echo PrefersNonDefaultGPU not recognized.
  # rpmlint considers file invalid without "X-" prefix
  sed -i 's/PrefersNonDefaultGPU=true/X-PrefersNonDefaultGPU=true/' misc/dist/linux/org.godotengine.Godot.desktop
fi

# disarm shebang
sed -i '1s/#!/##/' misc/dist/shell/godot.bash-completion

# bash completion for sub package
cp misc/dist/shell/godot.bash-completion misc/dist/shell/godot-runner
sed -i '$s/_complete_godot_bash godot/_complete_godot_bash godot-runner/' misc/dist/shell/godot-runner

# set update check default to disabled
sed -i 's/EngineUpdateLabel::UpdateMode default_update_mode = EngineUpdateLabel::UpdateMode::NEWEST_UNSTABLE;/EngineUpdateLabel::UpdateMode default_update_mode = EngineUpdateLabel::UpdateMode::DISABLED;/' editor/editor_settings.cpp
sed -i 's/default_update_mode = EngineUpdateLabel::UpdateMode::NEWEST_STABLE;/default_update_mode = EngineUpdateLabel::UpdateMode::DISABLED;/' editor/editor_settings.cpp

%build
# Configuring build to use some distribution libraries
unbundle_libs=('certs' 'libogg' 'libtheora' 'libvorbis' \
               'libwebp' 'pcre2')

# Adding distribution name to build name
%if 0%{?suse_version}
  %if 0%{?is_opensuse}
    # Unbundle more libs for openSUSE
    unbundle_libs+=('miniupnpc' 'wslay')
    export BUILD_NAME="openSUSE"
  %else
    export BUILD_NAME="SUSE"
  %endif
%endif

# Unbundle more libs for Tumbleweed
%if %{suse_version} > 1500
unbundle_libs+=('brotli' 'freetype' 'graphite' 'harfbuzz' 'libpng' 'mbedtls' 'zlib' 'zstd')
%else
# Unbundle more libs for coming Leap
%if 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
unbundle_libs+=('mbedtls')
%endif
%endif

system_libs=""
for thirdparty in "${unbundle_libs[@]}"; do
  system_libs="$system_libs builtin_$thirdparty=no"
  rm -rf thirdparty/$thirdparty
done

# Keep empty certificates file needed as "source" by
# function "make_certs_header" in core/core_builders.py
mkdir -pv thirdparty/certs
touch thirdparty/certs/ca-certificates.crt

use_sowrap="use_sowrap=no "
rm -rf thirdparty/linuxbsd_headers

%if %{suse_version} > 1500
%define ccflags %{optflags}
compiler=""
linkflags=""
%else
%define ccflags %{optflags} -fPIE
compiler="CC=gcc-%{compiler_version_leap}  CXX=g++-%{compiler_version_leap}"
linkflags="linkflags=-pie"
%endif

%define build_args_common %{?_smp_mflags} \\\
        progress=no verbose=yes udev=yes use_lto=1 \\\
        use_static_cpp=no ccflags='%{ccflags}' $linkflags $compiler \\\
        engine_update_check=no steamapi=no \\\
        system_certs_path=%{ca_bundle} $use_sowrap $system_libs

%ifarch aarch64 %arm
# Disable unsupported features - https://github.com/godotengine/godot/issues/48297#issuecomment-829165296
%define build_args %{build_args_common} module_denoise_enabled=no
%else
%define build_args %{build_args_common}
%endif

# Build graphical editor
scons %{build_args} platform=linuxbsd target=editor

%if !0%{?faster_build}
# Build game runner
scons %{build_args} platform=linuxbsd target=template_release production=yes
%endif

%install
# build binary suffix
%ifarch riscv64
suffix=rv64
%else
%ifarch aarch64
suffix=arm64
%else
%ifarch ppc64 ppc64le
suffix=ppc64
%else
suffix=%{__isa_name}_%{__isa_bits}
%endif
%endif
%endif

# Installing the editor
install -D -p -m 755 bin/%{name}.linuxbsd.editor.$suffix %{buildroot}%{_bindir}/%{name}

install -D -p -m 644 misc/dist/linux/godot.6 %{buildroot}/%{_mandir}/man6/%{name}.6%{?ext_man}
install -D -p -m 644 icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -D -p -m 644 icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -p -m 644 misc/dist/linux/org.godotengine.Godot.appdata.xml  %{buildroot}%{_datadir}/metainfo/org.godotengine.Godot.appdata.xml
%suse_update_desktop_file -i org.godotengine.Godot

%if !0%{?faster_build}
# Installing the runner
install -D -p -m 755 bin/%{name}.linuxbsd.template_release.$suffix %{buildroot}%{_bindir}/%{name}-runner
%endif

# Installing bash-completion
install -D -p -m 644 misc/dist/shell/godot.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -p -m 644 misc/dist/shell/godot-runner %{buildroot}%{_datadir}/bash-completion/completions/%{name}-runner

%fdupes -s %{buildroot}/%{_prefix}

%files
%license LICENSE.txt LOGO_LICENSE.txt COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md logo.svg
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_bindir}/%{name}
%{_datadir}/metainfo/org.godotengine.Godot.appdata.xml
%{_datadir}/applications/org.godotengine.Godot.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6%{?ext_man}

%if !0%{?faster_build}
%files runner
%license LICENSE.txt LOGO_LICENSE.txt COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md logo.svg
%{_bindir}/%{name}-runner
%endif

%files bash-completion
%license LICENSE.txt COPYRIGHT.txt
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/bash-completion/completions/%{name}-runner

%changelog
