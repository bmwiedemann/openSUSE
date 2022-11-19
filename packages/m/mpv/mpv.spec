#
# spec file for package mpv
#
# Copyright (c) 2022 SUSE LLC
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


%define _waf_ver 2.0.24
%define lname   libmpv2
Name:           mpv
Version:        0.35+git.20221118.d3a61cfe
Release:        0
Summary:        Advanced general-purpose multimedia player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            http://mpv.io
Source:         %{name}-%{version}.tar.xz
Source1:        https://waf.io/waf-%{_waf_ver}
Source2:        %{name}.changes
# PATCH-FIX-OPENSUSE do not require equal libav versions, obs rebuilds as needed
Patch0:         mpv-make-ffmpeg-version-check-non-fatal.patch
BuildRequires:  bash
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  linux-kernel-headers
%if 0%{?suse_version} > 1500
BuildRequires:  meson >= 0.60.3
%endif
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
BuildRequires:  pkgconfig(egl) >= 1.4
BuildRequires:  pkgconfig(ffnvcodec) >= 8.2.15.7
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libarchive) >= 3.4.0
BuildRequires:  pkgconfig(libass) >= 0.12.2
BuildRequires:  pkgconfig(libavcodec) >= 58.12.100
BuildRequires:  pkgconfig(libavdevice) >= 57.0.0
BuildRequires:  pkgconfig(libavfilter) >= 7.14.100
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libavformat) >= 59.27.100
BuildRequires:  pkgconfig(libavif) >= 0.11.1
BuildRequires:  pkgconfig(libavutil) >= 57.24.100
%else
BuildRequires:  pkgconfig(libavformat) >= 58.9.100
BuildRequires:  pkgconfig(libavutil) >= 56.12.100
%endif
BuildRequires:  pkgconfig(libbluray) >= 0.3.0
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdrm) >= 2.4.75
BuildRequires:  pkgconfig(libiso9660)
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libswresample) >= 3.0.100
BuildRequires:  pkgconfig(libswscale) >= 5.0.101
BuildRequires:  pkgconfig(libudf)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva) >= 1.1.0
BuildRequires:  pkgconfig(libva-x11) >= 1.1.0
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(openal) >= 1.13
# Testing framework: disabled for now as it runs just 1 test
# BuildRequires:  pkgconfig(cmocka) >= 0.4.1
BuildRequires:  pkgconfig(python3)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} > 150400
BuildRequires:  pkgconfig(libsixel) >= 1.5
%endif
BuildRequires:  pkgconfig(rubberband) >= 3.0.0
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(vapoursynth) >= 24
BuildRequires:  pkgconfig(vapoursynth-script) >= 23
BuildRequires:  pkgconfig(vdpau) >= 0.2
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xinerama) >= 1.0.0
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0
BuildRequires:  pkgconfig(xpresent) >= 1.0.0
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zimg) >= 2.9
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun):hicolor-icon-theme
Requires(postun):update-desktop-files
# Used via LUA scripts
Recommends:     yt-dlp
Conflicts:      mpv-plugin-mpris < 0.4
# Obsoletion of mplayer2 that is dead for 2 years now
Provides:       mplayer2 = 20140101
Obsoletes:      mplayer2 < 20140101
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} > 150300
BuildRequires:  pkgconfig(libplacebo) >= 4.157
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(mujs)
%endif
BuildRequires:  pkgconfig(libva-wayland) >= 1.1.0
BuildRequires:  pkgconfig(vulkan) >= 1.0.61
BuildRequires:  pkgconfig(wayland-client) >= 1.15.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.15.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.19
%endif
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
%setup -q
%patch0 -p1

# As we downloaded specific waf version we need to put and prepare it in place.
cp -f %{SOURCE1} waf
chmod a+x waf

# I hate UNKNOWN so lets put decent info there.
MODIFIED="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE2}")"
DATE="$(date -d "$MODIFIED" "+%%b %%e %%Y")"
sed -i "s|UNKNOWN|$DATE|g;s|VERSION|\"%{version}\"|g" common/version.c

%build
%if 0%{?suse_version} > 1500
# We don't want to rebuild all the time.
myopts=" -Dbuild-date=false"
# Disable pipwire for Leap because of build error
%if 0%{?suse_version} <= 1500
myopts+=" -Dpipewire=disabled"
%endif
%meson \
  -Dlibmpv=true \
  -Dmanpage-build=enabled \
  -Dcdda=enabled \
  -Ddvbin=enabled \
  -Ddvdnav=enabled \
  -Dopenal=enabled \
  -Dandroid-media-ndk=disabled \
  -Daudiounit=disabled \
  -Dcocoa=disabled \
  -Dcoreaudio=disabled \
  -Dd3d-hwaccel=disabled \
  -Dd3d11=disabled \
  -Dd3d9-hwaccel=disabled \
  -Ddirect3d=disabled \
  -Degl-android=disabled \
  -Degl-angle-lib=disabled \
  -Degl-angle-win32=disabled \
  -Degl-angle=disabled \
  -Dgl-cocoa=disabled \
  -Dgl-dxinterop-d3d9=disabled \
  -Dgl-dxinterop=disabled \
  -Dgl-win32=disabled \
  -Dios-gl=disabled \
  -Dmacos-10-11-features=disabled \
  -Dmacos-10-12-2-features=disabled \
  -Dmacos-10-14-features=disabled \
  -Dmacos-cocoa-cb=disabled \
  -Dmacos-media-player=disabled \
  -Dmacos-touchbar=disabled \
  -Dopensles=disabled \
  -Doss-audio=disabled \
  -Drpi-mmal=disabled \
  -Dsdl2-audio=disabled \
  -Dsdl2-gamepad=disabled \
  -Dsdl2-video=disabled \
  -Dsndio=disabled \
  -Dspirv-cross=disabled \
  -Dswift-build=disabled \
  -Dvideotoolbox-gl=disabled \
  -Dwasapi=disabled \
  -Dwin32-internal-pthreads=disabled \
  ${myopts}

%meson_build
%else
# SDL: disable as it is pointless to have on Linux, it is Windows/OS X fallback.
myopts="--disable-sdl2"
# We don't want to rebuild all the time.
myopts+=" --disable-build-date"
# Debug just adds -g and we do that over optflags anyway.
myopts+=" --disable-debug"
# Disable pipwire for Leap because of build error
%if 0%{?suse_version} <= 1500
myopts+=" --disable-pipewire"
%endif
# Vulkan support needs recent libplacebo
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} > 150300
myopts+=" --enable-vulkan"
%endif
export CFLAGS="%{optflags}"
python3 ./waf configure \
  --prefix="%{_prefix}"              \
  --bindir="%{_bindir}"              \
  --mandir="%{_mandir}"              \
  --libdir="%{_libdir}"              \
  --docdir="%{_docdir}/%{name}"      \
  --confdir="%{_sysconfdir}/%{name}" \
  --enable-cdda                      \
  --enable-dvdnav                    \
  --enable-libmpv-shared             \
  --enable-manpage-build             \
  --enable-libarchive                \
  --enable-dvbin                     \
  --enable-drm                       \
  --enable-x11                       \
  --enable-openal                    \
  --enable-wayland                   \
  --enable-gl-wayland                \
  --enable-gl-x11                    \
  --enable-egl-x11                   \
  --enable-egl-drm                   \
  --enable-zimg                      \
  ${myopts}

python3 ./waf build --verbose %{?_smp_mflags}
%endif

%install
%if 0%{?suse_version} > 1500
%meson_install
install -dm755 %{buildroot}%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/mpv %{buildroot}%{_defaultdocdir}/%{name}
%else
python3 ./waf --destdir=%{buildroot} install
%endif

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
