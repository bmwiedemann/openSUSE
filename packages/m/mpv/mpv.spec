#
# spec file for package mpv
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _waf_ver 2.0.9
%define _mbc_ver 3.3.17
%define _mpv_ver 0.30.0+git.1573301895.cb2d7c1534
%define lname   libmpv1

Name:           mpv
Version:        %{_mpv_ver}
Release:        0
Summary:        Advanced general-purpose multimedia player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            http://mpv.io/
Source:         %{name}-%{_mpv_ver}.tar.xz
Source1:        https://waf.io/waf-%{_waf_ver}
Source2:        %{name}.changes
# mpv-bash-completion is licensed with GPL-3.0+
Source3:        https://github.com/2ion/mpv-bash-completion/archive/%{_mbc_ver}.tar.gz#/mpv-bash-completion-%{_mbc_ver}.tar.gz
# PATCH-FIX-OPENSUSE do not require equal libav versions, obs rebuilds as needed
Patch0:         mpv-make-ffmpeg-version-check-non-fatal.patch
BuildRequires:  bash
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  linux-kernel-headers
# Needed any lua to convert the bash-completion
BuildRequires:  lua
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(caca) >= 0.99.beta18
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(dvdnav) >= 4.2.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libarchive) >= 3.0.0
BuildRequires:  pkgconfig(libass) >= 0.12.1
BuildRequires:  pkgconfig(libavcodec) >= 58.7.100
BuildRequires:  pkgconfig(libavdevice) >= 57.0.0
BuildRequires:  pkgconfig(libavfilter) >= 7.0.101
BuildRequires:  pkgconfig(libavformat) >= 58.0.102
BuildRequires:  pkgconfig(libavutil) >= 56.6.100
BuildRequires:  pkgconfig(libbluray) >= 0.3.0
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libiso9660)
BuildRequires:  pkgconfig(libkms)
BuildRequires:  pkgconfig(libplacebo) >= 1.18.0
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libswresample) >= 3.0.100
BuildRequires:  pkgconfig(libswscale) >= 5.0.101
BuildRequires:  pkgconfig(libudf)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva) >= 0.36.0
BuildRequires:  pkgconfig(libva-x11) >= 0.36.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(vapoursynth-script)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xinerama) >= 1.0.0
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
# Used via LUA scripts
Recommends:     youtube-dl
# Obsoletion of mplayer2 that is dead for 2 years now
Provides:       mplayer2 = 20140101
Obsoletes:      mplayer2 < 20140101
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(lua5.1)
%else
BuildRequires:  pkgconfig(lua)
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libva-wayland) >= 0.36.0
BuildRequires:  pkgconfig(vulkan) >= 1.0.61
BuildRequires:  pkgconfig(wayland-client) >= 1.6.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.6.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
%endif
# JIT for lua.
%if 0%{?suse_version} >= 1500
%ifarch aarch64 %{ix86} x86_64
BuildRequires:  pkgconfig(luajit)
%else
BuildRequires:  pkgconfig(lua5.1)
%endif
%else
BuildRequires:  pkgconfig(lua)
%endif
# Testing framework: disabled for now as it runs just 1 test
# BuildRequires:  pkgconfig(cmocka) >= 0.4.1

%description
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

%package bash-completion
Version:        %{_mbc_ver}
Release:        0
Summary:        Bash Completion for %{name}
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name} = %{_mpv_ver}
Requires:       bash-completion
Recommends:     xrandr
Supplements:    packageand(mpv:bash)
BuildArch:      noarch

%description bash-completion
A Bash completion script for the mpv video player. It features
  * Completion for all --options,
  * Type-based completion for --option arguments for choices, flags,
    integers and floats,
  * Completion for upper/lower bounds for integer- and float-type
    argument ranges where applicable,
  * Completion of filter lists as arguments to --vf and --af style
    options as well as completion of filter parameters while composing
    filter lists,
  * Similarly, parameter completion for video and audio outputs (--vo, --ao),
  * Regular file name completion.

%package zsh-completion
Summary:        ZSH Completion for %{name}
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name} = %{_mpv_ver}
Supplements:    packageand(mpv:zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%package devel
Summary:        A library to link together with mpv player
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{_mpv_ver}

%description devel
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

This package contains all the development files.

%package -n %{lname}
Summary:        A library to link together with mpv player
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{lname}
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

This package contains a library that can other apps use to utilize the mpv
features.

%prep
%setup -q -a 3
%patch0 -p1

# As we downloaded specific waf version we need to put and prepare it in place.
cp -f %{SOURCE1} waf
chmod a+x waf

# I hate UNKNOWN so lets put decent info there.
MODIFIED="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE2}")"
DATE="$(date -d "$MODIFIED" "+%%b %%e %%Y")"
sed -i "s|UNKNOWN|$DATE|g;s|VERSION|\"%{_mpv_ver}\"|g" common/version.c

%build
# SDL: disable as it is pointless to have on Linux, it is Windows/OS X fallback.
myopts="--disable-sdl2"
# We don't want to rebuild all the time.
myopts+=" --disable-build-date"
# Debug just adds -g and we do that over optflags anyway.
myopts+=" --disable-debug"
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
  --enable-libsmbclient              \
  --enable-libmpv-shared             \
  --enable-manpage-build             \
  --enable-libarchive                \
  --enable-dvbin                     \
  --enable-drm                       \
  --enable-x11                       \
%if 0%{?suse_version} > 1500
  --enable-wayland                   \
  --enable-gl-wayland                \
  --enable-vulkan                    \
%endif
  --enable-gl-x11                    \
  --enable-egl-x11                   \
  --enable-egl-drm                   \
  --enable-zimg                      \
  ${myopts}

python3 ./waf build --verbose %{?_smp_mflags}

pushd mpv-bash-completion-%{_mbc_ver}
export MPV_BASHCOMPGEN_MPV_CMD=../build/mpv
make %{?_smp_mflags}
popd

%install
python3 ./waf --destdir=%{buildroot} install

pushd mpv-bash-completion-%{_mbc_ver}
%make_install
popd

install -D -m 0644 etc/input.conf %{buildroot}%{_sysconfdir}/%{name}/input.conf
install -D -m 0644 etc/mpv.conf %{buildroot}%{_sysconfdir}/%{name}/mpv.conf
# remove shebang
sed -i -e '1d' %{buildroot}%{_datadir}/bash-completion/completions/mpv

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

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
%{_mandir}/man?/%{name}.?%{?ext_man}

%files zsh-completion
%{_datadir}/zsh/site-functions/_mpv

%files bash-completion
%license mpv-bash-completion-%{_mbc_ver}/LICENSE
%doc mpv-bash-completion-%{_mbc_ver}/README.mkd
%{_datadir}/bash-completion/completions/mpv

%files -n %{lname}
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
