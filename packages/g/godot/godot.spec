#
# spec file for package godot
#
# Copyright (c) 2022 SUSE LLC
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
%define ca_bundle %{_localstatedir}/lib/ca-certificates/ca-bundle.pem

Name:           godot
Version:        3.5.1
Release:        0
Summary:        Cross-Platform Game Engine with an Integrated Editor
License:        MIT
Group:          Development/Tools/Other
URL:            https://godotengine.org/
Source0:        https://downloads.tuxfamily.org/godotengine/%{version}/%{name}-%{version}-stable.tar.xz
Source1:        https://downloads.tuxfamily.org/godotengine/%{version}/%{name}-%{version}-stable.tar.xz.sha256
# Project policy does not allow "-no-pie"
Patch0:         linker_pie_flag.patch
# Use system certificates as fallback for certificates
Patch1:         certs_fallback.patch
# Heap-buffer-overflow in bundled tinyexr
Patch2:         tinyexr_thirdparty_upstream.patch
BuildRequires:  Mesa-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  scons
BuildRequires:  update-desktop-files
BuildRequires:  yasm-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

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
BuildRequires:  pkgconfig(bullet) >= 2.90
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
Suggests:       %{name}-headless = %{version}
Suggests:       %{name}-runner = %{version}
Suggests:       %{name}-server = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# The following "Provides: bundled()" and comments were taken from the
# Fedora Godot specfile.
# Link: https://src.fedoraproject.org/rpms/godot/blob/master/f/godot.spec

# Has some modifications for IPv6 support, upstream enet is unresponsive
# Should not be unbundled.
Provides:       bundled(enet) = 1.3.17

# Has custom changes to support seeking in zip archives
# Should not be unbundled.
Provides:       bundled(minizip) = 1.2.12

Provides:       bundled(FastLZ)
Provides:       bundled(RVO2-3D)
Provides:       bundled(Tangent_Space_Normal_Maps)
Provides:       bundled(brotli)
Provides:       bundled(cvtt)
Provides:       bundled(etc2comp)
Provides:       bundled(glad)
Provides:       bundled(google-droid-fonts)
Provides:       bundled(hack-fonts)
Provides:       bundled(hqx)
Provides:       bundled(ifaddrs-android)
Provides:       bundled(jpeg-compressor)
Provides:       bundled(libsimplewebm)
Provides:       bundled(minimp3)
Provides:       bundled(noto-sans-fonts)
Provides:       bundled(oidn)
Provides:       bundled(open-simplex-noise-in-c)
Provides:       bundled(pcg)
Provides:       bundled(polyclipping)
Provides:       bundled(polypartition)
Provides:       bundled(pvrtccompressor)
Provides:       bundled(smaz)
Provides:       bundled(stb)
Provides:       bundled(tinyexr)
Provides:       bundled(vhacd)
Provides:       bundled(yuv2rgb)

# Can be unbundled if packaged
Provides:       bundled(nanosvg)
Provides:       bundled(recastnavigation)
Provides:       bundled(squish) = 1.15
Provides:       bundled(xatlas)

# Embree 3.13.0+ supports both x86_64 and aarch64.
# per 20211108 Factory is at 3.13.0, Leap at 3.8 .
# Currently build fails with Distro (unbundled) embree on Tumbleweed although
# the required version is available.
# Perhaps because it is build with special flags (static) for blender.
Provides:       bundled(embree) = 3.13.0

%if 0%{?suse_version} > 1500
%else
Provides:       bundled(bullet) = 3.24
# see comments for freetype2, libpng and zlib Factory BuildRequires
Provides:       bundled(freetype2)
Provides:       bundled(libpng) = 1.6.38
Provides:       bundled(libzstd)
Provides:       bundled(zlib)
%if 0%{?sle_version} < 150200
Provides:       bundled(mbedtls) = 2.18.1
%endif
%if !0%{?is_opensuse}
# SLES seems not to have miniupnpc and wslay
Provides:       bundled(libwslay) = 1.1.1
Provides:       bundled(miniupnpc)
%endif
%endif

# Build currently fails on armv7l
ExcludeArch:    %arm

%description
Godot is a game engine. It provides a set of tools and a visually
oriented workflow that can export games to PC, Mobile and Web
platforms.

%if !0%{?faster_build}

%package headless
Summary:        Headless version of Godot editor useful for command line
Group:          Development/Tools/Other
Requires:       ca-certificates
Recommends:     ca-certificates-mozilla
Suggests:       %{name}-bash-completion

%description headless
This package is the headless version of the Godot editor that is suited for
exporting Godot games on the command line.

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

%package server
Summary:        Godot headless binary for servers
Group:          Amusements/Games/Other
Requires:       ca-certificates
Recommends:     ca-certificates-mozilla
Suggests:       %{name}-bash-completion

%description server
This package contains the headless binary for the Godot game engine
particularly suited for running dedicated servers.

%endif

%package bash-completion
Summary:        Godot command line completion for Bash
Group:          Amusements/Games/Other
BuildArch:      noarch
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
Enhances:       (%{name}-headless and bash-completion)
Enhances:       (%{name}-runner and bash-completion)
Enhances:       (%{name}-server and bash-completion)

%description bash-completion
Bash command line completion support for %{name}, %{name}-headless,
%{name}-runner and %{name}-server

%prep
%setup -q -n %{name}-%{version}-stable
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp thirdparty/README.md thirdparty_README.md

# actual doc location in openSUSE
sed -i 's/\/usr\/share\/doc\/godot\//\/usr\/share\/doc\/packages\/godot\//' misc/dist/linux/godot.6

if [[ -z "$(desktop-file-validate misc/dist/linux/org.godotengine.Godot.desktop)" ]];
 then
  # desktop-file-utils version >= 0.25
  echo desktop-file-utils is up to date and recognizes PrefersNonDefaultGPU.
  # rpmlint complains nevertheless (on Tumbleweed). A false negative?
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

# bash completion for sub packages
cp misc/dist/shell/godot.bash-completion misc/dist/shell/godot-headless
cp misc/dist/shell/godot.bash-completion misc/dist/shell/godot-runner
cp misc/dist/shell/godot.bash-completion misc/dist/shell/godot-server

sed -i '$s/_complete_godot_bash godot/_complete_godot_bash godot-headless/' misc/dist/shell/godot-headless
sed -i '$s/_complete_godot_bash godot/_complete_godot_bash godot-runner/' misc/dist/shell/godot-runner
sed -i '$s/_complete_godot_bash godot/_complete_godot_bash godot-server/' misc/dist/shell/godot-server

%build
# Configuring build to use some distribution libraries
unbundle_libs=('certs' 'libogg' 'libtheora' 'libvorbis' \
               'libwebp' 'opus' 'pcre2')

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
unbundle_libs+=('bullet' 'freetype' 'libpng' 'mbedtls' 'zlib' 'zstd')
%else
# Unbundle more libs for coming Leap
%if 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
unbundle_libs+=('mbedtls')
%endif
%endif

# Unbundle libvpx only if it doesn't meet the minimum requirement.
# See: https://github.com/godotengine/godot/tree/master/thirdparty#libvpx
vpx_version_min=1.6.0
vpx_version=$(pkg-config --modversion vpx)
if [[ $vpx_version = $vpx_version_min || $vpx_version > $vpx_version_min ]]; then
  unbundle_libs+=('libvpx')
fi

system_libs=""
for thirdparty in "${unbundle_libs[@]}"; do
  system_libs="$system_libs builtin_$thirdparty=no"
  rm -rf thirdparty/$thirdparty
done

# Keep empty certificates file needed as "source" by
# function "make_certs_header" in core/core_builders.py
mkdir -pv thirdparty/certs
touch thirdparty/certs/ca-certificates.crt

%define build_args_common %{?_smp_mflags} \\\
        progress=no verbose=yes udev=yes use_lto=1 \\\
        use_static_cpp=no CCFLAGS='%{optflags}' \\\
        system_certs_path=%{ca_bundle} $system_libs

%ifarch aarch64 %arm
# Disable unsupported features - https://github.com/godotengine/godot/issues/48297#issuecomment-829165296
%define build_args %{build_args_common} module_denoise_enabled=no
%else
%define build_args %{build_args_common}
%endif

# Build graphical editor (tools)
# rename x11 to linuxbsd ?
scons %{build_args} platform=x11 tools=yes target=release_debug

%if !0%{?faster_build}
# Build headless version of the editor (with tools)
scons %{build_args} platform=server tools=yes target=release_debug

# Build game runner (without tools)
scons %{build_args} platform=x11 tools=no target=release

# Build server version (without tools)
scons %{build_args} platform=server tools=no target=release
%endif

%install
# Installing the editor
%ifarch riscv64
suffix=rv64
%else
suffix=%{__isa_bits}
%endif
install -D -p -m 755 bin/%{name}.x11.opt.tools.$suffix %{buildroot}%{_bindir}/%{name}

install -D -p -m 644 misc/dist/linux/godot.6 %{buildroot}/%{_mandir}/man6/%{name}.6%{?ext_man}
install -D -p -m 644 icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -D -p -m 644 icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -p -m 644 misc/dist/linux/org.godotengine.Godot.appdata.xml  %{buildroot}%{_datadir}/metainfo/org.godotengine.Godot.appdata.xml
%suse_update_desktop_file -i org.godotengine.Godot

%if !0%{?faster_build}
# Installing the headless editor
install -D -p -m 755 bin/%{name}_server.x11.opt.tools.$suffix %{buildroot}%{_bindir}/%{name}-headless

# Installing the runner
install -D -p -m 755 bin/%{name}.x11.opt.$suffix %{buildroot}%{_bindir}/%{name}-runner

# Installing the server
install -D -p -m 755 bin/%{name}_server.x11.opt.$suffix %{buildroot}%{_bindir}/%{name}-server
%endif

# Installing bash-completion
install -D -p -m 644 misc/dist/shell/godot.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -p -m 644 misc/dist/shell/godot-headless %{buildroot}%{_datadir}/bash-completion/completions/%{name}-headless
install -D -p -m 644 misc/dist/shell/godot-runner %{buildroot}%{_datadir}/bash-completion/completions/%{name}-runner
install -D -p -m 644 misc/dist/shell/godot-server %{buildroot}%{_datadir}/bash-completion/completions/%{name}-server

%fdupes -s %{buildroot}/%{_prefix}

%files
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
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
%files headless
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md logo.svg
%{_bindir}/%{name}-headless

%files runner
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md logo.svg
%{_bindir}/%{name}-runner

%files server
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md logo.svg
%{_bindir}/%{name}-server
%endif

%files bash-completion
%license LICENSE.txt COPYRIGHT.txt
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/bash-completion/completions/%{name}-headless
%{_datadir}/bash-completion/completions/%{name}-runner
%{_datadir}/bash-completion/completions/%{name}-server

%changelog
