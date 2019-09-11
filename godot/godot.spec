#
# spec file for package godot
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _buildshell /bin/bash
%define ca_bundle /var/lib/ca-certificates/ca-bundle.pem

Name:           godot
Version:        3.1.1
Release:        0
Summary:        Cross-Platform Game Engine with an Integrated Editor
License:        MIT
Group:          Development/Tools/Other
URL:            https://godotengine.org/
Source0:        https://downloads.tuxfamily.org/godotengine/%{version}/%{name}-%{version}-stable.tar.xz
Source1:        https://downloads.tuxfamily.org/godotengine/%{version}/%{name}-%{version}-stable.tar.xz.sha256
Source2:        export_presets.cfg
Source3:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE Allows building all files with -lpie
Patch0:         fix-pie-warning.patch
# Use system certificates as fallback for project certificates
Patch1:         project_certs_fallback.patch
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
BuildRequires:  pkgconfig(openssl)
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
%if %{suse_version} > 1500
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig(miniupnpc)
%endif
Requires:       ca-certificates
Recommends:     ca-certificates-mozilla
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
Suggests:       godot-headless = %{version}
Suggests:       godot-runner = %{version}
Suggests:       godot-server = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# The following "Provides: bundled()" and comments were taken from the 
# Fedora Godot specfile. 
# Link: https://src.fedoraproject.org/rpms/godot/blob/master/f/godot.spec

# Git commit slightly newer than 2.87
# Can be unbundled if bullet 2.88+ is available
Provides:       bundled(bullet) = 2.88

# Has some modifications for IPv6 support, upstream enet is unresponsive
# Should not be unbundled.
Provides:       bundled(enet) = 1.3.13

# Upstream commit from 2016, newer than 1.0.0.27 which is last tag
# Could be unbundled if packaged.
# Godot upstream will soon deprecate this "libsimplewebm" module.
Provides:       bundled(libwebm) = 1.0.2

# Has custom changes to support seeking in zip archives
# Should not be unbundled.
Provides:       bundled(minizip) = 1.2.11

# Could be unbundled if packaged.
# Version: git (c1f6e20, 2018)
Provides:       bundled(nanosvg)

# Could be unbundled if packaged.
Provides:       bundled(squish) = 1.15

# Can't be unbundled out-of-the-box as it uses experimental APIs available
# only to static linking. They're not critical features though and could
# maybe be patched away to link against a shared zstd.
Provides:       bundled(zstd) = 1.3.8

# Has custom changes made to library to aid in build configurations
Provides:       bundled(libwebsockets) = 3.1.0

%description
Godot is a game engine. It provides a set of tools and a visually
oriented workflow that can export games to PC, Mobile and Web
platforms.

%package headless
Summary:        Headless version of Godot editor useful for command line
Group:          Development/Tools/Other
Requires:       godot-rpm-macros
Requires:       godot-runner

%description headless
This package is the headless version of the Godot editor that is suited for 
exporting Godot games on the command line.

%package runner
Summary:        Shared binary to play games developed with the Godot engine
Group:          Amusements/Games/Other
Requires:       ca-certificates
Recommends:     ca-certificates-mozilla

%description runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.

%package server
Summary:        Godot headless binary for servers
Group:          Amusements/Games/Other

%description server
This package contains the headless binary for the Godot game engine
particularly suited for running dedicated servers.

%prep
%setup -q -n %{name}-%{version}-stable
%patch0 -p1
%patch1 -p1

%build
# Adding distribution name to build name
%if 0%{?suse_version}
  %if 0%{?is_opensuse}
    export BUILD_NAME="openSUSE"
  %else
    export BUILD_NAME="SUSE"
  %endif
%endif

# Configuring build to use some distribution libraries
unbundle_libs=('certs' 'freetype' 'libogg' 'libpng' 'libtheora' 'libvorbis' \
               'libwebp' 'opus' 'pcre2' 'zlib')

# Unbundle more libs for Tumbleweed
%if %{suse_version} > 1500
unbundle_libs+=('mbedtls' 'miniupnpc')
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

# Removing extra thirdparty libraries as they are either not needed or are
# provided by the distribution.
rm -rf thirdparty/rtaudio

# Keep empty certificates file needed as "source" by
# function "make_certs_header" in core/core_builders.py
mkdir -pv thirdparty/certs
touch thirdparty/certs/ca-certificates.crt

# Common build arguments for all targets
%if %{suse_version} >= 1500
%define use_lto use_lto=1
%else
%define use_lto use_lto=0
%endif

%define build_args %{?_smp_mflags} \\\
        progress=yes verbose=yes udev=yes %{use_lto} \\\
        CCFLAGS='%{optflags}' system_certs_path=%{ca_bundle} \\\
        $system_libs

# Build graphical editor (tools)
scons %{build_args} platform=x11 tools=yes target=release_debug

# Build headless version of the editor (with tools)
scons %{build_args} platform=server tools=yes target=release_debug

# Build game runner (without tools)
scons %{build_args} platform=x11 tools=no target=release

# Build server version (without tools)
scons %{build_args} platform=server tools=no target=release

%install
# Installing the editor
install -D -p -m 755 bin/%{name}.x11.opt.tools.%{__isa_bits} %{buildroot}%{_bindir}/%{name}

# Installing the headless editor
install -D -p -m 755 bin/%{name}_server.x11.opt.tools.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-headless

# Installing the runner
install -D -p -m 755 bin/%{name}.x11.opt.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-runner

# Installing the server
install -D -p -m 755 bin/%{name}_server.x11.opt.%{__isa_bits} %{buildroot}%{_bindir}/%{name}-server

install -D -p -m 644 %{S:2} %{buildroot}%{_datadir}/%{name}/export_presets.cfg
install -D -p -m 644 misc/dist/linux/godot.6 %{buildroot}/%{_mandir}/man6/%{name}.6%{?ext_man}
install -D -p -m 644 icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -D -p -m 644 icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -p -m 644 misc/dist/linux/org.godotengine.Godot.appdata.xml  %{buildroot}%{_datadir}/appdata/org.godotengine.Godot.appdata.xml
%suse_update_desktop_file -i org.godotengine.Godot

cp thirdparty/README.md thirdparty_README.md
%fdupes -s %{buildroot}/%{_prefix}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%if 0%{?suse_version} < 1500
%doc LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%else
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%endif
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md ISSUE_TEMPLATE.md README.md
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

%files headless
%defattr(-,root,root)
%if 0%{?suse_version} < 1500
%doc LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%else
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%endif
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md ISSUE_TEMPLATE.md README.md
%dir %{_datadir}/%{name}
%{_bindir}/%{name}-headless
%{_datadir}/%{name}/export_presets.cfg

%files runner
%defattr(-,root,root)
%if 0%{?suse_version} < 1500
%doc LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%else
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%endif
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md ISSUE_TEMPLATE.md README.md
%{_bindir}/%{name}-runner

%files server
%defattr(-,root,root)
%if 0%{?suse_version} < 1500
%doc LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%else
%license LICENSE.txt LOGO_LICENSE.md COPYRIGHT.txt thirdparty_README.md
%endif
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md DONORS.md ISSUE_TEMPLATE.md README.md
%{_bindir}/%{name}-server

%changelog
