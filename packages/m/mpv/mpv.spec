#
# spec file for package mpv
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2015 Packman Team <packman@links2linux.de>
# Copyright (c) 2012 Jiri Slaby <jslaby@suse.de>
# Copyright (c) 2011-2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define lname   libmpv2
Name:           mpv
Version:        0.40.0+git20251010.67330ba2de
Release:        0
Summary:        Advanced general-purpose multimedia player
License:        GPL-2.0-or-later
URL:            https://mpv.io
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE do not require equal libav versions, obs rebuilds as needed
Patch0:         mpv-make-ffmpeg-version-check-non-fatal.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  linux-kernel-headers
BuildRequires:  meson >= 1.3.0
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(alsa) >= 1.0.18
BuildRequires:  pkgconfig(caca) >= 0.99.beta18
BuildRequires:  pkgconfig(dvdnav) >= 4.2.0
BuildRequires:  pkgconfig(egl) >= 1.4
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libarchive) >= 3.4.0
BuildRequires:  pkgconfig(libass) >= 0.12.2
BuildRequires:  pkgconfig(libavcodec) >= 60.31.102
BuildRequires:  pkgconfig(libavdevice) >= 60.3.100
BuildRequires:  pkgconfig(libavfilter) >= 9.12.100
BuildRequires:  pkgconfig(libavformat) >= 60.16.100
BuildRequires:  pkgconfig(libavutil) >= 58.29.100
BuildRequires:  pkgconfig(libbluray) >= 0.5.0
BuildRequires:  pkgconfig(libcdio) >= 0.90
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdisplay-info) >= 0.1.1
BuildRequires:  pkgconfig(libdrm) >= 2.4.105
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.57
BuildRequires:  pkgconfig(libplacebo) >= 6.338.2
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libsixel) >= 1.5
BuildRequires:  pkgconfig(libswresample) >= 4.12.100
BuildRequires:  pkgconfig(libswscale) >= 7.5.100
BuildRequires:  pkgconfig(libva) >= 1.1.0
BuildRequires:  pkgconfig(libva-wayland) >= 1.1.0
BuildRequires:  pkgconfig(mujs) >= 1.0.0
BuildRequires:  pkgconfig(openal) >= 1.13
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(rubberband) >= 3.0.0
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(vapoursynth) >= 56
BuildRequires:  pkgconfig(vapoursynth-script) >= 56
BuildRequires:  pkgconfig(vdpau) >= 0.2
BuildRequires:  pkgconfig(vulkan) >= 1.3.238
BuildRequires:  pkgconfig(wayland-client) >= 1.21.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.21.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.31
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11) >= 1.0.0
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0
BuildRequires:  pkgconfig(xpresent) >= 1.0.0
BuildRequires:  pkgconfig(xrandr) >= 1.4.0
BuildRequires:  pkgconfig(xscrnsaver) >= 1.0.0
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zimg) >= 2.9
BuildRequires:  pkgconfig(zlib)
# Used via Lua scripts
Recommends:     yt-dlp
Conflicts:      mpv-plugin-mpris < 0.4
BuildSystem:    meson
BuildOption:    --auto-features=auto
BuildOption:    -Dcdda=enabled
BuildOption:    -Dlibmpv=true
BuildOption:    -Ddvbin=enabled
BuildOption:    -Ddvdnav=enabled
BuildOption:    -Dopenal=enabled
BuildOption:    -Dtests=true
# We don't want to rebuild all the time.
BuildOption:    -Dbuild-date=false
# These tests need more FFmpeg than ffmpeg-mini provides
BuildOption(check): --no-suite=libmpv
# JIT for Lua.
%ifarch aarch64 %{ix86} x86_64 riscv64
BuildRequires:  pkgconfig(luajit)
BuildOption:    -Dlua=luajit
%else
BuildRequires:  pkgconfig(lua5.1)
BuildOption:    -Dlua=lua5.1
%endif

%description
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Recommends:     xrandr
Supplements:    (mpv and bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (mpv and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (mpv and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package devel
Summary:        A library to link together with mpv player
Requires:       %{lname} = %{version}

%description devel
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

This package contains all the development files.

%package -n %{lname}
Summary:        A library to link together with mpv player

%description -n %{lname}
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

This package contains a library that can other apps use to utilize the mpv
features.

%prep
%autosetup -p1
echo '%{version}' > MPV_VERSION

%install -a
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
mv %{buildroot}/%{_datadir}/doc/%{name}/* %{buildroot}/%{_defaultdocdir}/%{name}/

%ldconfig_scriptlets -n %{lname}

%files
%license LICENSE.GPL Copyright
%doc README.md RELEASE_NOTES
%doc %{_defaultdocdir}/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/mpv.metainfo.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/mpv.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_mpv

%files bash-completion
%{_datadir}/bash-completion/completions/mpv

%files -n %{lname}
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
