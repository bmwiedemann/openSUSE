#
# spec file for package godot
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.2.2
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
BuildRequires:  Mesa-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  scons
BuildRequires:  update-desktop-files
BuildRequires:  yasm-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
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
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1500
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig(bullet)
BuildRequires:  pkgconfig(libwslay)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(miniupnpc)
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
Requires(postun): update-desktop-files
Recommends:     %{name}-bash-completion
Suggests:       %{name}-headless = %{version}
Suggests:       %{name}-runner = %{version}
Suggests:       %{name}-server = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# The following "Provides: bundled()" and comments were taken from the 
# Fedora Godot specfile. 
# Link: https://src.fedoraproject.org/rpms/godot/blob/master/f/godot.spec

# Has some modifications for IPv6 support, upstream enet is unresponsive
# Should not be unbundled.
Provides:       bundled(enet) = 1.3.15

# Has custom changes to support seeking in zip archives
# Should not be unbundled.
Provides:       bundled(minizip) = 1.2.11

Provides:       bundled(FastLZ)
Provides:       bundled(Tangent_Space_Normal_Maps)
Provides:       bundled(cvtt)
Provides:       bundled(easing)
Provides:       bundled(etc2comp)
Provides:       bundled(glad)
Provides:       bundled(google-droid-fonts)
Provides:       bundled(hack-fonts)
Provides:       bundled(hqx)
Provides:       bundled(ifaddrs-android)
Provides:       bundled(jpeg-compressor)
Provides:       bundled(libsimplewebm)
Provides:       bundled(noto-sans-fonts)
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

## Need to update in Factory ##
# Possibility to unbundle disabled in 3.2.1
Provides:       bundled(assimp)

%if 0%{?suse_version} > 1500
%else
Provides:       bundled(bullet) = 2.90
Provides:       bundled(libzstd)
%if 0%{?sle_version} < 150200
Provides:       bundled(mbedtls) = 2.16.6
%endif
%if !0%{?is_opensuse}
# SLES seems not to have miniupnpc and wslay
Provides:       bundled(libwslay) = 1.1.0
Provides:       bundled(miniupnpc)
%endif
%endif

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

cp thirdparty/README.md thirdparty_README.md

# actual doc location in openSUSE
sed -i 's/\/usr\/share\/doc\/godot\//\/usr\/share\/doc\/packages\/godot\//' misc/dist/linux/godot.6

# rpmlint considers file invalid without "X-" prefix
sed -i 's/PrefersNonDefaultGPU=true/X-PrefersNonDefaultGPU=true/' misc/dist/linux/org.godotengine.Godot.desktop

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
unbundle_libs=('certs' 'freetype' 'libogg' 'libpng' 'libtheora' 'libvorbis' \
               'libwebp' 'opus' 'pcre2' 'zlib')

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
unbundle_libs+=('bullet' 'mbedtls' 'zstd')
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

%define build_args %{?_smp_mflags} \\\
        progress=yes verbose=yes udev=yes use_lto=1 \\\
        CCFLAGS='%{optflags}' \\\
        system_certs_path=%{ca_bundle} $system_libs

# Build graphical editor (tools)
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
install -D -p -m 755 bin/%{name}.x11.opt.tools.%{__isa_bits} %{buildroot}%{_bindir}/%{name}

install -D -p -m 644 misc/dist/linux/godot.6 %{buildroot}/%{_mandir}/man6/%{name}.6%{?ext_man}
install -D -p -m 644 icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -D -p -m 644 icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -p -m 644 misc/dist/linux/org.godotengine.Godot.appdata.xml  %{buildroot}%{_datadir}/appdata/org.godotengine.Godot.appdata.xml
%suse_update_desktop_file -i org.godotengine.Godot

%if !0%{?faster_build}
# Installing the headless editor
install -D -p -m 755 bin/%{name}_server.x11.opt.tools.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-headless

# Installing the runner
install -D -p -m 755 bin/%{name}.x11.opt.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-runner

# Installing the server
install -D -p -m 755 bin/%{name}_server.x11.opt.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-server
%endif

# Installing bash-completion
install -D -p -m 644 misc/dist/shell/godot.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -p -m 644 misc/dist/shell/godot-headless %{buildroot}%{_datadir}/bash-completion/completions/%{name}-headless
install -D -p -m 644 misc/dist/shell/godot-runner %{buildroot}%{_datadir}/bash-completion/completions/%{name}-runner
install -D -p -m 644 misc/dist/shell/godot-server %{buildroot}%{_datadir}/bash-completion/completions/%{name}-server

%fdupes -s %{buildroot}/%{_prefix}

%files
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md CODE_OF_CONDUCT.md
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_bindir}/%{name}
%{_datadir}/appdata/org.godotengine.Godot.appdata.xml
%{_datadir}/applications/org.godotengine.Godot.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6%{?ext_man}

%if !0%{?faster_build}
%files headless
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md CODE_OF_CONDUCT.md
%{_bindir}/%{name}-headless

%files runner
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md CODE_OF_CONDUCT.md
%{_bindir}/%{name}-runner

%files server
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md README.md CODE_OF_CONDUCT.md
%{_bindir}/%{name}-server
%endif

%files bash-completion
%license LICENSE.txt COPYRIGHT.txt
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/bash-completion/completions/%{name}-headless
%{_datadir}/bash-completion/completions/%{name}-runner
%{_datadir}/bash-completion/completions/%{name}-server

%changelog
