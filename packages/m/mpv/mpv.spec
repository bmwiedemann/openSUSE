#
# spec file for package mpv
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.38.0+git20240706.00f43e0916fa
Release:        0
Summary:        Advanced general-purpose multimedia player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            http://mpv.io
Source:         %{name}-%{version}.tar.xz
Source2:        %{name}.changes
# PATCH-FIX-OPENSUSE do not require equal libav versions, obs rebuilds as needed
Patch0:         mpv-make-ffmpeg-version-check-non-fatal.patch
# Install docs in proper directory
Patch2:         fix-docs-path.patch
BuildRequires:  bash
BuildRequires:  hicolor-icon-theme
BuildRequires:  linux-kernel-headers
BuildRequires:  meson >= 0.60.3
# Needed any lua to convert the bash-completion
BuildRequires:  lua
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa) >= 1.0.18
BuildRequires:  pkgconfig(caca) >= 0.99.beta18
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(dvdnav) >= 4.2.0
BuildRequires:  pkgconfig(dvdread) >= 4.1.0
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
BuildRequires:  pkgconfig(libavif) >= 0.11.1
BuildRequires:  pkgconfig(libavutil) >= 58.29.100
BuildRequires:  pkgconfig(libbluray) >= 0.3.0
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdrm) >= 2.4.105
BuildRequires:  pkgconfig(libiso9660)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libsixel) >= 1.5
BuildRequires:  pkgconfig(libswresample) >= 4.12.100
BuildRequires:  pkgconfig(libswscale) >= 7.5.100
BuildRequires:  pkgconfig(libva) >= 1.1.0
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(openal) >= 1.13
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(rubberband) >= 3.0.0
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(vapoursynth) >= 56
BuildRequires:  pkgconfig(vapoursynth-script) >= 56
BuildRequires:  pkgconfig(vdpau) >= 0.2
BuildRequires:  pkgconfig(x11) >= 1.0.0
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0
BuildRequires:  pkgconfig(xpresent) >= 1.0.0
BuildRequires:  pkgconfig(xrandr) >= 1.4.0
BuildRequires:  pkgconfig(xscrnsaver) >= 1.0.0
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zimg) >= 2.9
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
# Used via LUA scripts
Recommends:     yt-dlp
Conflicts:      mpv-plugin-mpris < 0.4
# Obsoletion of mplayer2 that is dead for 2 years now
Provides:       mplayer2 = 20140101
Obsoletes:      mplayer2 < 20140101
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.48
BuildRequires:  pkgconfig(libplacebo) >= 6.338.2
BuildRequires:  pkgconfig(libva-wayland) >= 1.1.0
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(vulkan) >= 1.1.70
BuildRequires:  pkgconfig(wayland-client) >= 1.20.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.20.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
# JIT for lua.
%ifarch aarch64 %{ix86} x86_64
BuildRequires:  pkgconfig(luajit)
%else
BuildRequires:  pkgconfig(lua5.1)
%endif

%description
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name} = %{version}
Requires:       bash-completion
Recommends:     xrandr
Supplements:    (mpv and bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name} = %{version}
Supplements:    (mpv and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%package devel
Summary:        A library to link together with mpv player
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

This package contains all the development files.

%package -n %{lname}
Summary:        A library to link together with mpv player
Group:          System/Libraries

%description -n %{lname}
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

This package contains a library that can other apps use to utilize the mpv
features.

%prep
%autosetup -p1

# I hate UNKNOWN so lets put decent info there.
MODIFIED="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE2}")"
DATE="$(date -d "$MODIFIED" "+%%b %%e %%Y")"
sed -i "s|UNKNOWN|$DATE|g;s|VERSION|\"%{version}\"|g" common/version.c

%build
# We don't want to rebuild all the time.
myopts=" -Dbuild-date=false"
%meson \
  --auto-features=auto       \
  -Dcdda=enabled             \
  -Dlibmpv=true              \
  -Ddvbin=enabled            \
  -Ddvdnav=enabled           \
  -Dopenal=enabled           \
  ${myopts}                  \
  %{?nil}
%meson_build

%install
%meson_install

install -D -m 0644 etc/input.conf %{buildroot}%{_sysconfdir}/%{name}/input.conf
install -D -m 0644 etc/mpv.conf %{buildroot}%{_sysconfdir}/%{name}/mpv.conf
# remove shebang
sed -i -e '1d' %{buildroot}%{_datadir}/bash-completion/completions/mpv

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSE.GPL
%doc Copyright README.md RELEASE_NOTES
%doc %{_defaultdocdir}/%{name}/input.conf
%doc %{_defaultdocdir}/%{name}/mplayer-input.conf
%doc %{_defaultdocdir}/%{name}/mpv.conf
%doc %{_defaultdocdir}/%{name}/restore-old-bindings.conf
%dir %{_sysconfdir}/%{name}/
%ghost %dir %{_sysconfdir}/%{name}/scripts/
%config %{_sysconfdir}/%{name}/encoding-profiles.conf
%config %{_sysconfdir}/%{name}/input.conf
%config %{_sysconfdir}/%{name}/mpv.conf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/mpv.metainfo.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

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
