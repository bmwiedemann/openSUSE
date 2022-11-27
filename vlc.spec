#
# spec file for package vlc
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Dominique Leuenberger, Amsterdam, The Netherlands
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


%define libvlc 5
%define libvlccore 9
%define conflicts vlc-beta
%ifarch %{arm}
%bcond_without opengles
%else
%bcond_with opengles
%endif
%bcond_without gstreamer
# Fluidsynth plugin is known to cause strange crashes here and there - disable it for now (2014-10-07, DimStar)
%bcond_with fluidsynth
# VNC support - the module is not really usable in most cases tested so far (e.g. against qemu-kvm -vnc :xx)
%bcond_with vnc
%bcond_with faad
%bcond_with fdk_aac
Name:           vlc
Version:        3.0.18
Release:        0
Summary:        Graphical media player
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            http://www.videolan.org
Source:         http://download.videolan.org/%{name}/%{version}/%{name}-%{version}.tar.xz
Source2:        %{name}-rpmlintrc
Source98:       http://download.videolan.org/%{name}/%{version}/%{name}-%{version}.tar.xz.asc
Source99:       vlc.keyring
# PATCH-FIX-UPSTREAM vlc.a52.patch https://trac.videolan.org/vlc/ticket/3731 dimstar@opensuse.org -- Support new version of liba52
Patch0:         vlc.a52.patch
# PATCH-FIX-UPSTREAM vlc-allow-deprecated-fribidi.patch dimstar@opensuse.org -- Allow usage of deprecated fribidi functions
Patch1:         vlc-allow-deprecated-fribidi.patch
# PATCH-FIX-UPSTREAM vlc-lua-5.3.patch dimstar@opensuse.org -- Replace lua_optlong with lua_optinteger
Patch2:         vlc-lua-5.3.patch
# PATCH-FIX-UPSTREAM fix-build-with-fdk-2.0.patch -- Fix building vlc with libfdk-aac v2
Patch4:         fix-build-with-fdk-2.0.patch
# PATCH-FIX-UPSTREAM -- Backport libplacebo v5 compatibility patch to vlc v3
Patch5:         vlc-libplacebo-5.patch
# PATCH-FEATURE-OPENSUSE vlc-projectM-qt5.patch -- Build against projectM-qt5; openSUSE provides projectM as -qt and -qt5 variant
Patch100:       vlc-projectM-qt5.patch
# PATCH-FIX-UPSTREAM -- Use OpenCV C++ API
Patch103:       0001-Port-OpenCV-facedetect-example-to-C-API.patch
BuildRequires:  Mesa-devel
BuildRequires:  aalib-devel
BuildRequires:  alsa-devel >= 1.0.24
BuildRequires:  avahi-devel >= 0.6
BuildRequires:  dirac-devel
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  flac-devel
BuildRequires:  freetype2
BuildRequires:  fribidi-devel
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gettext-devel
#BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  liba52-devel
BuildRequires:  libavc1394-devel >= 0.5.3
BuildRequires:  libcddb-devel >= 0.9.5
BuildRequires:  libcdio-devel >= 0.78.2
BuildRequires:  libdc1394-devel >= 2.1.0
BuildRequires:  libdvbpsi-devel >= 1.0.0
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  libjack-devel >= 1.9.7
BuildRequires:  libjpeg-devel
BuildRequires:  libkate-devel >= 0.3.0
BuildRequires:  libmad-devel
BuildRequires:  libmatroska-devel
BuildRequires:  libogg-devel >= 1.0
BuildRequires:  libopus-devel >= 1.0.3
BuildRequires:  libraw1394 >= 2.0.1
BuildRequires:  librsvg-devel >= 2.9.0
BuildRequires:  libsamplerate-devel
BuildRequires:  libshout-devel >= 2.1
BuildRequires:  libssh2-devel
BuildRequires:  libtheora-devel >= 1.0
BuildRequires:  libtool
BuildRequires:  libv4l-devel
BuildRequires:  libvorbis-devel >= 1.1
BuildRequires:  libvpx-devel >= 1.5.0
BuildRequires:  libxml2-devel >= 2.5
BuildRequires:  lirc-devel
BuildRequires:  live555-devel >= 2015.01.27
BuildRequires:  mpg123-devel
BuildRequires:  pkgconfig
BuildRequires:  posix_cc
BuildRequires:  schroedinger-devel >= 1.0.10
BuildRequires:  (lua >= 5.1 with lua < 5.4)
BuildRequires:  (lua-devel >= 5.1 with lua-devel < 5.4)
BuildConflicts: lua >= 5.4
BuildRequires:  pkgconfig(libudev) >= 142
BuildRequires:  pkgconfig(smbclient)
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libplacebo)
%endif
#BuildRequires:  slang-devel
BuildRequires:  speex-devel >= 1.0.5
BuildRequires:  update-desktop-files
BuildRequires:  vcdimager-devel
BuildRequires:  xosd-devel
BuildRequires:  (pkgconfig(libavcodec) >= 57.37.100 with pkgconfig(libavcodec) < 59)
BuildRequires:  (pkgconfig(libavformat) >= 53.21.0 with pkgconfig(libavformat) < 59)
BuildRequires:  (pkgconfig(libavutil) >= 52.4.0 with pkgconfig(libavutil) < 57)
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(caca) >= 0.99.beta20
BuildRequires:  pkgconfig(dbus-1) >= 1.6.0
BuildRequires:  pkgconfig(dvdnav) > 4.9.0
BuildRequires:  pkgconfig(dvdread) > 4.9.0
BuildRequires:  pkgconfig(gnutls) >= 3.2.0
BuildRequires:  pkgconfig(libarchive) >= 3.1.0
BuildRequires:  pkgconfig(libass) >= 0.9.8
BuildRequires:  pkgconfig(libbluray) >= 0.6.2
BuildRequires:  pkgconfig(libgme)
#BuildRequires:  pkgconfig(libmodplug) >= 0.8.9
BuildRequires:  pkgconfig(libmpeg2) > 0.3.2
BuildRequires:  pkgconfig(libmtp) >= 1.0.0
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libnfs)
%endif
BuildRequires:  (pkgconfig(libswscale) with pkgconfig(libswscale) < 6)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(protobuf-lite) >= 2.5.0
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(soxr)
%endif
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vdpau) >= 0.6
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:  pkgconfig(xcb-randr) >= 1.3
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xv) >= 1.1.90.1
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28
Requires:       %{name}-noX = %{version}-%{release}
Requires:       %{name}-qt = %{version}-%{release}
# FIXME: use proper Requires(pre/post/preun/...)
# We need the noX package first, as it contains vlc-cache-gen
PreReq:         %{name}-noX
Conflicts:      %{conflicts}
Obsoletes:      %{name}-gnome <= %{version}
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(dav1d)
%ifarch x86_64
BuildRequires:  pkgconfig(libmfx)
%endif
%endif
%if 0%{?suse_version} > 1500 && 0%{?is_opensuse}
BuildRequires:  pkgconfig(srt)
%endif
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version} >= 1500 && 0%{?is_opensuse}
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(wayland-protocols)
%endif
%if %{with gstreamer}
BuildRequires:  pkgconfig(gstreamer-app-1.0)
%endif
%if 0%{?suse_version} != 1315 || 0%{?is_opensuse}
BuildRequires:  pkgconfig(Qt5X11Extras)
# for some reason libXi-devel is explicitly needed on Leap 42.1, otherwise the build fails...
BuildRequires:  pkgconfig(xi)
%endif
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(opencv) > 2.0
%ifarch %{ix86} x86_64
%if 0%{?suse_version} > 1320 && 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
BuildRequires:  pkgconfig(libprojectM-qt5) >= 2.0.0
%else
BuildRequires:  pkgconfig(libprojectM) >= 2.0.0
%endif
%endif
%endif
%if 0%{?suse_version} < 1330 && ( 0%{?sle_version} < 120200 || 0%{?is_opensuse} < 1 )
BuildRequires:  pkgconfig(freerdp) >= 1.0.1
%endif
%if %{with vnc}
BuildRequires:  pkgconfig(libvncclient) >= 0.9.9
%endif
%if %{with fluidsynth}
BuildRequires:  pkgconfig(fluidsynth) >= 1.1.2
%endif
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libchromaprint) >= 0.6.0
%endif
%if 0%{?suse_version} >= 1320
BuildRequires:  pkgconfig(ncursesw)
%endif
# Those are dependencies which are NOT provided in openSUSE, mostly for legal reasons.
%if 0%{?BUILD_ORIG}
BuildRequires:  libxvidcore-devel
BuildRequires:  pkgconfig(libdca) >= 0.0.5
BuildRequires:  pkgconfig(x264) >= 0.8.6
BuildRequires:  pkgconfig(x265)
%if %{with faad}
BuildRequires:  libfaad-devel
%endif
%if %{with fdk_aac}
BuildRequires:  pkgconfig(fdk-aac)
%endif
%endif

%description
VLC media player is a multimedia player for many
audio and video files and formats (such as MPEG, DivX, mp3, ogg, ...)
as well as DVDs, VCDs, and various streaming protocols.
It can also be used as a server to stream in unicast or multicast
in IPv4 or IPv6 on a high-bandwidth network.

%if 0%{?BUILD_ORIG}
Note that the actual support is provided through ffmpeg and gstreamer
libraries, which may not have all codecs enabled that were just named.
%endif

%package devel
Summary:        Development files for the VLC media player system
Group:          Development/Libraries/C and C++
Requires:       %{name}-jack = %{version}
Requires:       %{name}-noX = %{version}
Requires:       %{name}-vdpau = %{version}

%description devel
These development headers are required if you plan on coding against VLC.

%package -n libvlc%{libvlc}
Summary:        Shared code for the VLC media player program
Group:          System/Libraries

%description -n libvlc%{libvlc}
This subpackage contains libraries that are part of VLC.

%package -n libvlccore%{libvlccore}
Summary:        Shared code for the VLC media player program
Group:          System/Libraries

%description -n libvlccore%{libvlccore}
This subpackage contains libraries that are part of VLC.

%package noX
Summary:        VLC without X dependencies
Group:          Productivity/Multimedia/Video/Players
Requires:       libvlc%{libvlc} = %{version}-%{release}
Requires:       libvlccore%{libvlccore} = %{version}-%{release}
# This is a hack only due to libbluray not having versioned symbols as well as
# having a strange ABI/API break between 0.3 and 0.7
%requires_ge    libbluray1
Recommends:     %{name}-codecs
# lang subpackage
Recommends:     %{name}-lang
Recommends:     libdvdcss
Conflicts:      %{conflicts}-noX
# The lang-package was renamed to vlc-lang to assist AppStream building
Obsoletes:      %{name}-noX-lang

%description noX
This package of VLC contains the bare requirements you need to install.
There is no graphical user interface included, thus it is also perfectly
suitable for server installations, for example, to run a streaming server.

Should you decide to install the GUI modules, %{name}-noX will stay
installed as a dependency.

%package lang
# we can't use %%lang_package, as we need a different dependency
# boo#1012556
# but the package name has to stay vlc-lang, as otherise the software centers
# (AppStream based) can't see vlc being translated (vlc is the one listed in SC
# not vlc-noX)
Summary:        Translations for package %{name}
# We do not want to require vlc, which is GUI based, but only vlc-noX
Group:          System/Localization
Requires:       %{name}-noX = %{version}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations for the "%{name}" package.

%package codec-gstreamer
Summary:        GStreamer integration for the VLC media player
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name}-noX = %{version}
# We need the noX package first, as it contains vlc-cache-gen
Requires(post): %{name}-noX
Supplements:    packageand(%{name}-noX:%(rpm --qf "%%{name}" -qf $(readlink -f %{_libdir}/libgstapp-1.0.so)))

%description codec-gstreamer
This package enhances the functionality of the VLC media player by
using GStreamer and its submodules as a backend to decode streams.

%package jack
Summary:        Jack integration for the VLC media player
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name}-noX = %{version}
# We need the noX package first, as it contains vlc-cache-gen
Requires(post): %{name}-noX

%description jack
This package adds jack support to vlc via plugins.

%if 0%{?BUILD_ORIG}
%package codecs
Summary:        Additional codecs for the VLC media player
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name}-noX = %{version}
# We require the unrestricted libavcodec - same ABI version we linked
Requires:       %(rpm --qf "%%{name}" -qf $(readlink -f %{_libdir}/libavcodec.so))(unrestricted)
# We need the noX package first, as it contains vlc-cache-gen
Requires(post): %{name}-noX
Supplements:    %{name}-noX

%description codecs
This package enhances the functionality of the VLC media player by
codecs that are not available in the stock openSUSE distribution.

%endif

%package vdpau
Summary:        Additional vdpau codecs for the VLC media player
# We require the unrestricted libavcodec - same ABI version we linked
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name}-noX = %{version}
# We need the noX package first, as it contains vlc-cache-gen
Requires(post): %{name}-noX
Supplements:    %{name}

%description vdpau
This package enhances the functionality of the VLC media player by
vdpau codecs that are not available in the stock openSUSE distribution.

%package qt
Summary:        Qt interface for the VLC media player
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name}-noX = %{version}-%{release}
# We need the noX package first, as it contains vlc-cache-gen
Requires(post): %{name}-noX
Supplements:    packageand(%{name}-noX:libqt5)
Conflicts:      %{conflicts}-qt

%description qt
This subpackage provides a Qt interface for VLC and selects it by
default when `vlc` is invoked from an X session.

%package opencv
Summary:        OpenCV plugins for VLC media player
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name}-noX = %{version}-%{release}
# We need the noX package first, as it contains vlc-cache-gen
Requires(post): %{name}-noX
# Package split
Provides:       %{name}:%{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
Conflicts:      %{name} < %{version}-%{release}
Supplements:    packageand(%{name}-noX:opencv3)
# Data required for face detection
Recommends:     opencv3

%description opencv
This subpackage provides a wrapper plugin for OpenCV for
OpenCV based video filters and a face detection example.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch4 -p1
%if 0%{?suse_version} > 1320 && 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
%patch100 -p1
%endif
%patch103 -p1

### And LUA 5.3.1 has some more API changes
if pkg-config --atleast-version 5.3.1 lua; then
%patch2 -p1
fi

if pkg-config --atleast-version 5 libplacebo; then
%patch5 -p1
fi

# We do not rely on contrib but make use of system libraries
rm -rf contrib

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%if 0%{?suse_version} < 1500
export CC=%{_bindir}/gcc-7
export CXX=%{_bindir}/g++-7
%endif
autoreconf -fiv
%configure \
   --disable-dependency-tracking        \
   --disable-oss                        \
   --disable-svgdec                     \
   --enable-a52                         \
   --enable-aa                          \
   --enable-alsa                        \
   --enable-avcodec                     \
   --enable-chromecast                  \
   --enable-dvbpsi                      \
   --enable-dvdnav                      \
   --enable-dvdread                     \
   --enable-fast-install                \
   --enable-flac                        \
   --enable-freetype                    \
   --enable-fribidi                     \
   --enable-gnutls                      \
   --enable-jack                        \
   --enable-kate                        \
   --enable-libass                      \
   --enable-libcddb                     \
   --enable-libmpeg2                    \
%if 0%{?is_opensuse}
   --enable-libplacebo                  \
%endif
   --enable-lirc                        \
   --enable-live555                     \
   --enable-lua                         \
   --enable-mad                         \
   --disable-mod                        \
   --enable-ogg                         \
   --enable-optimizations               \
   --enable-postproc                    \
   --enable-pulse                       \
   --enable-realrtsp                    \
   --enable-sftp                        \
   --enable-sout                        \
   --enable-speex                       \
   --enable-swscale                     \
   --enable-taglib                      \
   --enable-theora                      \
   --enable-twolame                     \
   --enable-v4l2                        \
   --enable-vcd                         \
   --enable-vdpau                       \
   --enable-vorbis                      \
   --enable-xcb                         \
   --enable-xvideo                      \
   --with-default-font=%{_datadir}/fonts/truetype/FreeSerifBold.ttf \
   --with-default-monospace-font=%{_datadir}/fonts/truetype/FreeMono.ttf \
%if %{with opengles}
  --enable-gles2                        \
%endif
%if 0%{?is_opensuse}
   --enable-opencv                      \
%endif
%if 0%{?suse_version} >= 1500 && 0%{?is_opensuse}
  --enable-wayland                      \
%else
  --disable-wayland                     \
%endif
%if 0%{?BUILD_ORIG}
%if %{with fdk_aac}
   --enable-fdkaac                      \
%endif
%if %{with faad}
   --enable-faad                        \
%endif
   --enable-dca                         \
   --enable-x265                        \
%else
   --disable-faad                       \
   --disable-fdkaac                     \
   --disable-dca                        \
   --disable-x265                       \
%endif
	%{nil}

# make sure the build hostname is not embedded in the binaries -- or we'll
# continuously republish packages -- seife
### ONLY REMOVE THIS IF YOU KNOW WHAT YOU ARE DOING!
sed -i 's/^#define.*VLC_COMPILE_HOST.*/#define VLC_COMPILE_HOST "obs-build"/' config.h

%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/pixmaps
# We need a full copy, as the pixmap icon goes to the -noX package
cp %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/vlc.png %{buildroot}/%{_datadir}/pixmaps/vlc.png
#Make vlc available in Plasma 5 device notifier
mkdir %{buildroot}%{_datadir}/solid
mkdir %{buildroot}%{_datadir}/solid/actions
cp %{buildroot}%{_datadir}/kde4/apps/solid/actions/vlc-open*.desktop %{buildroot}%{_datadir}/solid/actions/
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file vlc AudioVideo Audio Video Player
%fdupes %{buildroot}%{_datadir}/vlc
# remove duplicate file
rm %{buildroot}/%{_datadir}/vlc/lua/http/requests/README.txt
# add missing manfiles
for i in ?vlc; do
    pushd %{buildroot}/%{_mandir}/man1
    ln -s vlc.1 $i.1
    popd
done

# clean up some lang issues...
for lang in ach an cgg co ff tet ks_IN; do
  rm -rf %{buildroot}%{_datadir}/locale/$lang
done
%find_lang vlc

# ensure the ghost file has constant length for reproducibility
dd if=/dev/zero bs=1M count=1 of=%{buildroot}/%{_libdir}/vlc/plugins/plugins.dat

%post
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins

%post -n %{name}-noX
/sbin/ldconfig
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins

%postun -n %{name}-noX -p /sbin/ldconfig
%post -n libvlc%{libvlc} -p /sbin/ldconfig
%postun -n libvlc%{libvlc} -p /sbin/ldconfig
%post -n libvlccore%{libvlccore} -p /sbin/ldconfig
%postun -n libvlccore%{libvlccore} -p /sbin/ldconfig

%post -n %{name}-qt
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%if %{with gstreamer}
%post -n %{name}-codec-gstreamer
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%postun -n %{name}-codec-gstreamer
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi
%endif

%post -n %{name}-jack
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%postun -n %{name}-jack
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%if 0%{?BUILD_ORIG}
%post -n %{name}-codecs
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%postun -n %{name}-codecs
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi
%endif

%post -n %{name}-vdpau
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%postun -n %{name}-vdpau
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%post -n %{name}-opencv
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%postun -n %{name}-opencv
if [ -x %{_libdir}/vlc/vlc-cache-gen ]; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
fi

%files
%exclude %{_libdir}/vlc/libcompat.a
# The presence of the .desktop file is what gives AppStream the
# hint of which package to add in the appstore... 'vlc' is the place to be
%{_datadir}/applications/vlc.desktop
%{_datadir}/icons/hicolor/*/apps/vlc*
%{_datadir}/kde4/apps/solid
%if 0%{?suse_version} < 1500
%dir %{_datadir}/metainfo
%endif
%{_datadir}/metainfo/%{name}.appdata.xml
# The icon is the one referenced by the .desktop file
%{_datadir}/pixmaps/vlc.png
%{_datadir}/solid
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/apps
%{_libdir}/vlc/libvlc_pulse.so
%{_libdir}/vlc/libvlc_pulse.so.0
%{_libdir}/vlc/libvlc_pulse.so.0.0.0
%{_libdir}/vlc/libvlc_xcb_events.so
%{_libdir}/vlc/libvlc_xcb_events.so.0
%{_libdir}/vlc/libvlc_xcb_events.so.0.0.0
%{_libdir}/vlc/plugins/access/libavio_plugin.so
%{_libdir}/vlc/plugins/access/libpulsesrc_plugin.so
%{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
%{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so
%{_libdir}/vlc/plugins/codec/libavcodec_plugin.so
%{_libdir}/vlc/plugins/codec/liblibass_plugin.so
%{_libdir}/vlc/plugins/control/libxcb_hotkeys_plugin.so
%{_libdir}/vlc/plugins/demux/libavformat_plugin.so
%{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%{_libdir}/vlc/plugins/notify/libnotify_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_avparser_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_av1_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libpulselist_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libxcb_apps_plugin.so
%if 0%{?is_opensuse}
%{_libdir}/vlc/plugins/stream_out/libstream_out_chromaprint_plugin.so
%endif
%{_libdir}/vlc/plugins/text_renderer/libfreetype_plugin.so
%{_libdir}/vlc/plugins/text_renderer/libsvg_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libswscale_plugin.so
%{_libdir}/vlc/plugins/video_output/libaa_plugin.so
%{_libdir}/vlc/plugins/video_output/libcaca_plugin.so
%{_libdir}/vlc/plugins/video_output/libegl_x11_plugin.so
%if 0%{?suse_version} >= 1500 && 0%{?is_opensuse}
%{_libdir}/vlc/plugins/video_output/libegl_wl_plugin.so
%{_libdir}/vlc/plugins/video_output/libglconv_vaapi_wl_plugin.so
%endif
%if %{with opengles}
%{_libdir}/vlc/plugins/video_output/libgles2_plugin.so
%endif
%{_libdir}/vlc/plugins/video_output/libglx_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_xv_plugin.so
%{_libdir}/vlc/plugins/video_splitter/libpanoramix_plugin.so
%{_libdir}/vlc/plugins/visualization/libglspectrum_plugin.so
%if 0%{?is_opensuse}
%ifarch %{ix86} x86_64
%{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
%endif
%endif

%files lang -f vlc.lang

%files noX
%doc %{_datadir}/doc/vlc/
%license COPYING
%doc NEWS AUTHORS THANKS README
%{_bindir}/cvlc
%if 0%{?suse_version} >= 1320
%{_bindir}/nvlc
%{_mandir}/man1/nvlc*
%endif
%{_bindir}/rvlc
%{_bindir}/svlc
%{_bindir}/vlc
%{_bindir}/vlc-wrapper
%{_datadir}/vlc/
%{_mandir}/man1/cvlc*
%{_mandir}/man1/svlc.1%{?ext_man}
%{_mandir}/man1/rvlc*
%{_mandir}/man1/vlc*
# Own the file.. but it's an auto-generated file, so ghost it.
%ghost %{_libdir}/vlc/plugins/plugins.dat
%dir %{_libdir}/vlc
%dir %{_libdir}/vlc/lua
%dir %{_libdir}/vlc/lua/extensions
%dir %{_libdir}/vlc/lua/intf
%dir %{_libdir}/vlc/lua/intf/modules
%dir %{_libdir}/vlc/lua/meta
%dir %{_libdir}/vlc/lua/meta/art
%dir %{_libdir}/vlc/lua/meta/reader
%dir %{_libdir}/vlc/lua/modules
%dir %{_libdir}/vlc/lua/playlist
%dir %{_libdir}/vlc/lua/sd
%dir %{_libdir}/vlc/plugins
%dir %{_libdir}/vlc/plugins/access
%dir %{_libdir}/vlc/plugins/access_output
%dir %{_libdir}/vlc/plugins/audio_filter
%dir %{_libdir}/vlc/plugins/audio_mixer
%dir %{_libdir}/vlc/plugins/audio_output
%dir %{_libdir}/vlc/plugins/codec
%dir %{_libdir}/vlc/plugins/control
%dir %{_libdir}/vlc/plugins/demux
%dir %{_libdir}/vlc/plugins/gui
%dir %{_libdir}/vlc/plugins/keystore
%dir %{_libdir}/vlc/plugins/logger
%dir %{_libdir}/vlc/plugins/lua
%dir %{_libdir}/vlc/plugins/meta_engine
%dir %{_libdir}/vlc/plugins/misc
%dir %{_libdir}/vlc/plugins/mux
%dir %{_libdir}/vlc/plugins/notify
%dir %{_libdir}/vlc/plugins/packetizer
%dir %{_libdir}/vlc/plugins/services_discovery
%dir %{_libdir}/vlc/plugins/spu
%dir %{_libdir}/vlc/plugins/stream_extractor
%dir %{_libdir}/vlc/plugins/stream_filter
%dir %{_libdir}/vlc/plugins/stream_out
%dir %{_libdir}/vlc/plugins/text_renderer
%dir %{_libdir}/vlc/plugins/video_chroma
%dir %{_libdir}/vlc/plugins/video_filter
%dir %{_libdir}/vlc/plugins/video_output
%dir %{_libdir}/vlc/plugins/video_splitter
%dir %{_libdir}/vlc/plugins/visualization
%dir %{_libdir}/vlc/plugins/vaapi
# Files explicitly listed... so we are in full control of what goes to -noX, -codec or the X-depending pkg.
%{_libdir}/vlc/lua/extensions/VLSub.luac
%{_libdir}/vlc/lua/intf/cli.luac
%{_libdir}/vlc/lua/intf/dummy.luac
%{_libdir}/vlc/lua/intf/dumpmeta.luac
%{_libdir}/vlc/lua/intf/http.luac
%{_libdir}/vlc/lua/intf/luac.luac
%{_libdir}/vlc/lua/intf/modules/host.luac
%{_libdir}/vlc/lua/intf/modules/httprequests.luac
%{_libdir}/vlc/lua/intf/telnet.luac
%{_libdir}/vlc/lua/meta/art/00_musicbrainz.luac
%{_libdir}/vlc/lua/meta/art/01_googleimage.luac
%{_libdir}/vlc/lua/meta/art/02_frenchtv.luac
%{_libdir}/vlc/lua/meta/art/03_lastfm.luac
%{_libdir}/vlc/lua/meta/reader/filename.luac
%{_libdir}/vlc/lua/modules/common.luac
%{_libdir}/vlc/lua/modules/dkjson.luac
%{_libdir}/vlc/lua/modules/sandbox.luac
%{_libdir}/vlc/lua/modules/simplexml.luac
%{_libdir}/vlc/lua/playlist/anevia_streams.luac
%{_libdir}/vlc/lua/playlist/anevia_xml.luac
%{_libdir}/vlc/lua/playlist/appletrailers.luac
%{_libdir}/vlc/lua/playlist/bbc_co_uk.luac
%{_libdir}/vlc/lua/playlist/cue.luac
%{_libdir}/vlc/lua/playlist/dailymotion.luac
%{_libdir}/vlc/lua/playlist/jamendo.luac
%{_libdir}/vlc/lua/playlist/koreus.luac
%{_libdir}/vlc/lua/playlist/liveleak.luac
%{_libdir}/vlc/lua/playlist/newgrounds.luac
%{_libdir}/vlc/lua/playlist/rockbox_fm_presets.luac
%{_libdir}/vlc/lua/playlist/soundcloud.luac
%{_libdir}/vlc/lua/playlist/twitch.luac
%{_libdir}/vlc/lua/playlist/vimeo.luac
%{_libdir}/vlc/lua/playlist/vocaroo.luac
%{_libdir}/vlc/lua/playlist/youtube.luac
%{_libdir}/vlc/lua/sd/icecast.luac
%{_libdir}/vlc/lua/sd/jamendo.luac
%{_libdir}/vlc/plugins/access/libaccess_alsa_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_concat_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_imem_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_mms_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_mtp_plugin.so
%{_libdir}/vlc/plugins/access/libaccess_realrtsp_plugin.so
%{_libdir}/vlc/plugins/access/libattachment_plugin.so
%{_libdir}/vlc/plugins/access/libcdda_plugin.so
%{_libdir}/vlc/plugins/access/libdc1394_plugin.so
%{_libdir}/vlc/plugins/access/libdtv_plugin.so
%{_libdir}/vlc/plugins/access/libdv1394_plugin.so
%{_libdir}/vlc/plugins/access/libdvb_plugin.so
%{_libdir}/vlc/plugins/access/libdvdnav_plugin.so
%{_libdir}/vlc/plugins/access/libdvdread_plugin.so
%{_libdir}/vlc/plugins/access/libfilesystem_plugin.so
%{_libdir}/vlc/plugins/access/libftp_plugin.so
%{_libdir}/vlc/plugins/access/libhttp_plugin.so
%{_libdir}/vlc/plugins/access/libhttps_plugin.so
%{_libdir}/vlc/plugins/access/libidummy_plugin.so
%{_libdir}/vlc/plugins/access/libimem_plugin.so
%{_libdir}/vlc/plugins/access/liblibbluray_plugin.so
%{_libdir}/vlc/plugins/access/liblinsys_hdsdi_plugin.so
%{_libdir}/vlc/plugins/access/liblinsys_sdi_plugin.so
%{_libdir}/vlc/plugins/access/liblive555_plugin.so
%if 0%{?suse_version} >= 1500
%{_libdir}/vlc/plugins/access/libnfs_plugin.so
%endif
%if 0%{?suse_version} < 1330 && ( 0%{?sle_version} < 120200 || 0%{?is_opensuse} < 1 )
%{_libdir}/vlc/plugins/access/librdp_plugin.so
%endif
%{_libdir}/vlc/plugins/access/librist_plugin.so
%{_libdir}/vlc/plugins/access/librtp_plugin.so
%{_libdir}/vlc/plugins/access/libsatip_plugin.so
%{_libdir}/vlc/plugins/access/libsdp_plugin.so
%{_libdir}/vlc/plugins/access/libsftp_plugin.so
%{_libdir}/vlc/plugins/access/libshm_plugin.so
%{_libdir}/vlc/plugins/access/libsmb_plugin.so
%if 0%{?suse_version} > 1500 && 0%{?is_opensuse}
%{_libdir}/vlc/plugins/access/libaccess_srt_plugin.so
%endif
%{_libdir}/vlc/plugins/access/libtcp_plugin.so
%{_libdir}/vlc/plugins/access/libtimecode_plugin.so
%{_libdir}/vlc/plugins/access/libudp_plugin.so
%{_libdir}/vlc/plugins/access/libv4l2_plugin.so
%{_libdir}/vlc/plugins/access/libvcd_plugin.so
%{_libdir}/vlc/plugins/access/libvdr_plugin.so
%if %{with vnc}
%{_libdir}/vlc/plugins/access/libvnc_plugin.so
%endif
%{_libdir}/vlc/plugins/access_output/libaccess_output_dummy_plugin.so
%{_libdir}/vlc/plugins/access_output/libaccess_output_file_plugin.so
%{_libdir}/vlc/plugins/access_output/libaccess_output_http_plugin.so
%{_libdir}/vlc/plugins/access_output/libaccess_output_livehttp_plugin.so
%{_libdir}/vlc/plugins/access_output/libaccess_output_rist_plugin.so
%{_libdir}/vlc/plugins/access_output/libaccess_output_shout_plugin.so
%if 0%{?suse_version} > 1500 && 0%{?is_opensuse}
%{_libdir}/vlc/plugins/access_output/libaccess_output_srt_plugin.so
%endif
%{_libdir}/vlc/plugins/access_output/libaccess_output_udp_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libaudio_format_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libcompressor_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libequalizer_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libgain_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libkaraoke_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libmad_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libmono_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libnormvol_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libparam_eq_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libremap_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libsamplerate_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libscaletempo_pitch_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libscaletempo_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libsimple_channel_mixer_plugin.so
%if 0%{?suse_version} >= 1500
%{_libdir}/vlc/plugins/audio_filter/libsoxr_plugin.so
%endif
%{_libdir}/vlc/plugins/audio_filter/libspatializer_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libspeex_resampler_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libstereo_widen_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libtospdif_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libtrivial_channel_mixer_plugin.so
%{_libdir}/vlc/plugins/audio_filter/libugly_resampler_plugin.so
%{_libdir}/vlc/plugins/audio_mixer/libfloat_mixer_plugin.so
%{_libdir}/vlc/plugins/audio_mixer/libinteger_mixer_plugin.so
%{_libdir}/vlc/plugins/audio_output/libadummy_plugin.so
%{_libdir}/vlc/plugins/audio_output/libafile_plugin.so
%{_libdir}/vlc/plugins/audio_output/libalsa_plugin.so
%{_libdir}/vlc/plugins/audio_output/libamem_plugin.so
%{_libdir}/vlc/plugins/codec/liba52_plugin.so
%{_libdir}/vlc/plugins/codec/libadpcm_plugin.so
%{_libdir}/vlc/plugins/codec/libaes3_plugin.so
%{_libdir}/vlc/plugins/codec/libaom_plugin.so
%{_libdir}/vlc/plugins/codec/libaraw_plugin.so
%{_libdir}/vlc/plugins/codec/libcc_plugin.so
%{_libdir}/vlc/plugins/codec/libcdg_plugin.so
%{_libdir}/vlc/plugins/codec/libcvdsub_plugin.so
%if 0%{?suse_version} >= 1550
%{_libdir}/vlc/plugins/codec/libdav1d_plugin.so
%ifarch x86_64
%{_libdir}/vlc/plugins/codec/libqsv_plugin.so
%endif
%endif
%{_libdir}/vlc/plugins/codec/libddummy_plugin.so
%{_libdir}/vlc/plugins/codec/libdvbsub_plugin.so
%{_libdir}/vlc/plugins/codec/libedummy_plugin.so
%{_libdir}/vlc/plugins/codec/libflac_plugin.so
%if %{with fluidsynth}
%{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%endif
%{_libdir}/vlc/plugins/codec/libg711_plugin.so
%{_libdir}/vlc/plugins/codec/libjpeg_plugin.so
%{_libdir}/vlc/plugins/codec/libkate_plugin.so
%{_libdir}/vlc/plugins/codec/liblibmpeg2_plugin.so
%{_libdir}/vlc/plugins/codec/liblpcm_plugin.so
%{_libdir}/vlc/plugins/codec/libmpg123_plugin.so
%{_libdir}/vlc/plugins/codec/liboggspots_plugin.so
%{_libdir}/vlc/plugins/codec/libopus_plugin.so
%{_libdir}/vlc/plugins/codec/libpng_plugin.so
%{_libdir}/vlc/plugins/codec/librawvideo_plugin.so
%{_libdir}/vlc/plugins/codec/librtpvideo_plugin.so
%{_libdir}/vlc/plugins/codec/libschroedinger_plugin.so
%{_libdir}/vlc/plugins/codec/libscte18_plugin.so
%{_libdir}/vlc/plugins/codec/libscte27_plugin.so
%{_libdir}/vlc/plugins/codec/libspdif_plugin.so
%{_libdir}/vlc/plugins/codec/libspeex_plugin.so
%{_libdir}/vlc/plugins/codec/libspudec_plugin.so
%{_libdir}/vlc/plugins/codec/libstl_plugin.so
%{_libdir}/vlc/plugins/codec/libsubsdec_plugin.so
%{_libdir}/vlc/plugins/codec/libsubstx3g_plugin.so
%{_libdir}/vlc/plugins/codec/libsubsusf_plugin.so
%{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so
%{_libdir}/vlc/plugins/codec/libt140_plugin.so
%{_libdir}/vlc/plugins/codec/libtelx_plugin.so
%{_libdir}/vlc/plugins/codec/libtextst_plugin.so
%{_libdir}/vlc/plugins/codec/libtheora_plugin.so
%{_libdir}/vlc/plugins/codec/libttml_plugin.so
%{_libdir}/vlc/plugins/codec/libtwolame_plugin.so
%{_libdir}/vlc/plugins/codec/libuleaddvaudio_plugin.so
%{_libdir}/vlc/plugins/codec/libvorbis_plugin.so
%{_libdir}/vlc/plugins/codec/libvpx_plugin.so
%{_libdir}/vlc/plugins/codec/libvaapi_drm_plugin.so
%{_libdir}/vlc/plugins/codec/libvaapi_plugin.so
%{_libdir}/vlc/plugins/codec/libwebvtt_plugin.so
%{_libdir}/vlc/plugins/codec/libxwd_plugin.so
%{_libdir}/vlc/plugins/codec/libzvbi_plugin.so
%{_libdir}/vlc/plugins/control/libdbus_plugin.so
%{_libdir}/vlc/plugins/control/libdummy_plugin.so
%{_libdir}/vlc/plugins/control/libgestures_plugin.so
%{_libdir}/vlc/plugins/control/libhotkeys_plugin.so
%{_libdir}/vlc/plugins/control/liblirc_plugin.so
%{_libdir}/vlc/plugins/control/libmotion_plugin.so
%{_libdir}/vlc/plugins/control/libnetsync_plugin.so
%{_libdir}/vlc/plugins/control/liboldrc_plugin.so
%{_libdir}/vlc/plugins/demux/libadaptive_plugin.so
%{_libdir}/vlc/plugins/demux/libaiff_plugin.so
%{_libdir}/vlc/plugins/demux/libasf_plugin.so
%{_libdir}/vlc/plugins/demux/libau_plugin.so
%{_libdir}/vlc/plugins/demux/libavi_plugin.so
%{_libdir}/vlc/plugins/demux/libcaf_plugin.so
%{_libdir}/vlc/plugins/demux/libdemux_cdg_plugin.so
%{_libdir}/vlc/plugins/demux/libdemux_chromecast_plugin.so
%{_libdir}/vlc/plugins/demux/libdemuxdump_plugin.so
%{_libdir}/vlc/plugins/demux/libdemux_stl_plugin.so
%{_libdir}/vlc/plugins/demux/libdiracsys_plugin.so
%{_libdir}/vlc/plugins/demux/libdirectory_demux_plugin.so
%{_libdir}/vlc/plugins/demux/libes_plugin.so
%{_libdir}/vlc/plugins/demux/libflacsys_plugin.so
%{_libdir}/vlc/plugins/demux/libgme_plugin.so
%{_libdir}/vlc/plugins/demux/libh26x_plugin.so
%{_libdir}/vlc/plugins/demux/libimage_plugin.so
%{_libdir}/vlc/plugins/demux/libmjpeg_plugin.so
%{_libdir}/vlc/plugins/demux/libmkv_plugin.so
#%{_libdir}/vlc/plugins/demux/libmod_plugin.so
%{_libdir}/vlc/plugins/demux/libmp4_plugin.so
%{_libdir}/vlc/plugins/demux/libmpgv_plugin.so
%{_libdir}/vlc/plugins/demux/libnoseek_plugin.so
%{_libdir}/vlc/plugins/demux/libnsc_plugin.so
%{_libdir}/vlc/plugins/demux/libnsv_plugin.so
%{_libdir}/vlc/plugins/demux/libnuv_plugin.so
%{_libdir}/vlc/plugins/demux/libogg_plugin.so
%{_libdir}/vlc/plugins/demux/libplaylist_plugin.so
%{_libdir}/vlc/plugins/demux/libps_plugin.so
%{_libdir}/vlc/plugins/demux/libpva_plugin.so
%{_libdir}/vlc/plugins/demux/librawaud_plugin.so
%{_libdir}/vlc/plugins/demux/librawdv_plugin.so
%{_libdir}/vlc/plugins/demux/librawvid_plugin.so
%{_libdir}/vlc/plugins/demux/libreal_plugin.so
%{_libdir}/vlc/plugins/demux/libsmf_plugin.so
%{_libdir}/vlc/plugins/demux/libsubtitle_plugin.so
%{_libdir}/vlc/plugins/demux/libts_plugin.so
%{_libdir}/vlc/plugins/demux/libtta_plugin.so
%{_libdir}/vlc/plugins/demux/libty_plugin.so
%{_libdir}/vlc/plugins/demux/libvc1_plugin.so
%{_libdir}/vlc/plugins/demux/libvobsub_plugin.so
%{_libdir}/vlc/plugins/demux/libvoc_plugin.so
%{_libdir}/vlc/plugins/demux/libwav_plugin.so
%{_libdir}/vlc/plugins/demux/libxa_plugin.so
%if 0%{?suse_version} >= 1320
%{_libdir}/vlc/plugins/gui/libncurses_plugin.so
%endif
%{_libdir}/vlc/plugins/keystore/libfile_keystore_plugin.so
%{_libdir}/vlc/plugins/keystore/libkwallet_plugin.so
%{_libdir}/vlc/plugins/keystore/libmemory_keystore_plugin.so
%{_libdir}/vlc/plugins/keystore/libsecret_plugin.so
%{_libdir}/vlc/plugins/logger/libconsole_logger_plugin.so
%{_libdir}/vlc/plugins/logger/libfile_logger_plugin.so
%{_libdir}/vlc/plugins/logger/libsd_journal_plugin.so
%{_libdir}/vlc/plugins/logger/libsyslog_plugin.so
%{_libdir}/vlc/plugins/lua/liblua_plugin.so
%{_libdir}/vlc/plugins/meta_engine/libfolder_plugin.so
%{_libdir}/vlc/plugins/meta_engine/libtaglib_plugin.so
%{_libdir}/vlc/plugins/misc/libaddonsfsstorage_plugin.so
%{_libdir}/vlc/plugins/misc/libaddonsvorepository_plugin.so
%{_libdir}/vlc/plugins/misc/libaudioscrobbler_plugin.so
%{_libdir}/vlc/plugins/misc/libdbus_screensaver_plugin.so
%{_libdir}/vlc/plugins/misc/libexport_plugin.so
%{_libdir}/vlc/plugins/misc/libfingerprinter_plugin.so
%{_libdir}/vlc/plugins/misc/libgnutls_plugin.so
%{_libdir}/vlc/plugins/misc/liblogger_plugin.so
%{_libdir}/vlc/plugins/misc/libstats_plugin.so
%{_libdir}/vlc/plugins/misc/libvod_rtsp_plugin.so
%{_libdir}/vlc/plugins/misc/libxdg_screensaver_plugin.so
%{_libdir}/vlc/plugins/misc/libxml_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_asf_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_avi_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_dummy_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_mp4_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_mpjpeg_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_ogg_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_ps_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_ts_plugin.so
%{_libdir}/vlc/plugins/mux/libmux_wav_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_a52_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_copy_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_dirac_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_dts_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_h264_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_hevc_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegaudio_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so
%{_libdir}/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libavahi_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libmediadirs_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libmtp_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libpodcast_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libsap_plugin.so
%{_libdir}/vlc/plugins/services_discovery/libudev_plugin.so
%if 0%{?is_opensuse}
%{_libdir}/vlc/plugins/services_discovery/libupnp_plugin.so
%endif
%{_libdir}/vlc/plugins/spu/libaudiobargraph_v_plugin.so
%{_libdir}/vlc/plugins/spu/libdynamicoverlay_plugin.so
%{_libdir}/vlc/plugins/spu/liblogo_plugin.so
%{_libdir}/vlc/plugins/spu/libmarq_plugin.so
%{_libdir}/vlc/plugins/spu/libmosaic_plugin.so
%{_libdir}/vlc/plugins/spu/libremoteosd_plugin.so
%{_libdir}/vlc/plugins/spu/librss_plugin.so
%{_libdir}/vlc/plugins/spu/libsubsdelay_plugin.so
%{_libdir}/vlc/plugins/stream_extractor/libarchive_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libadf_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libcache_block_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libcache_read_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libdecomp_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libhds_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libinflate_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libprefetch_plugin.so
%{_libdir}/vlc/plugins/stream_filter/librecord_plugin.so
%{_libdir}/vlc/plugins/stream_filter/libskiptags_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_bridge_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_chromecast_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_cycle_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_delay_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_description_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_display_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_dummy_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_es_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_gather_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_record_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_rtp_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_setid_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_smem_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_standard_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_stats_plugin.so
%{_libdir}/vlc/plugins/stream_out/libstream_out_transcode_plugin.so
%{_libdir}/vlc/plugins/text_renderer/libtdummy_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libchain_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_10_p010_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_nv12_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_rgb_plugin.so
%ifarch %{ix86} x86_64
%{_libdir}/vlc/plugins/video_chroma/libi420_rgb_mmx_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_rgb_sse2_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_mmx_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_sse2_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_mmx_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_sse2_plugin.so
%endif
%ifarch ppc ppc64 ppc64le
%{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_altivec_plugin.so
%endif
%{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi422_i420_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_plugin.so
%{_libdir}/vlc/plugins/video_chroma/librv32_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuvp_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
%{_libdir}/vlc/plugins/video_chroma/libyuy2_i422_plugin.so
%{_libdir}/vlc/plugins/video_filter/libadjust_plugin.so
%{_libdir}/vlc/plugins/video_filter/libalphamask_plugin.so
%{_libdir}/vlc/plugins/video_filter/libanaglyph_plugin.so
%{_libdir}/vlc/plugins/video_filter/libantiflicker_plugin.so
%{_libdir}/vlc/plugins/video_filter/libball_plugin.so
%{_libdir}/vlc/plugins/video_filter/libblendbench_plugin.so
%{_libdir}/vlc/plugins/video_filter/libblend_plugin.so
%{_libdir}/vlc/plugins/video_filter/libbluescreen_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcanvas_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcolorthres_plugin.so
%{_libdir}/vlc/plugins/video_filter/libcroppadd_plugin.so
%{_libdir}/vlc/plugins/video_filter/libdeinterlace_plugin.so
%{_libdir}/vlc/plugins/video_filter/libedgedetection_plugin.so
%{_libdir}/vlc/plugins/video_filter/liberase_plugin.so
%{_libdir}/vlc/plugins/video_filter/libextract_plugin.so
%{_libdir}/vlc/plugins/video_filter/libfps_plugin.so
%{_libdir}/vlc/plugins/video_filter/libfreeze_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgaussianblur_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgradfun_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgradient_plugin.so
%{_libdir}/vlc/plugins/video_filter/libgrain_plugin.so
%{_libdir}/vlc/plugins/video_filter/libhqdn3d_plugin.so
%{_libdir}/vlc/plugins/video_filter/libinvert_plugin.so
%{_libdir}/vlc/plugins/video_filter/libmagnify_plugin.so
%{_libdir}/vlc/plugins/video_filter/libmirror_plugin.so
%{_libdir}/vlc/plugins/video_filter/libmotionblur_plugin.so
%{_libdir}/vlc/plugins/video_filter/libmotiondetect_plugin.so
%{_libdir}/vlc/plugins/video_filter/liboldmovie_plugin.so
%{_libdir}/vlc/plugins/video_filter/libposterize_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpostproc_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpsychedelic_plugin.so
%{_libdir}/vlc/plugins/video_filter/libpuzzle_plugin.so
%{_libdir}/vlc/plugins/video_filter/libripple_plugin.so
%{_libdir}/vlc/plugins/video_filter/librotate_plugin.so
%{_libdir}/vlc/plugins/video_filter/libscale_plugin.so
%{_libdir}/vlc/plugins/video_filter/libscene_plugin.so
%{_libdir}/vlc/plugins/video_filter/libsepia_plugin.so
%{_libdir}/vlc/plugins/video_filter/libsharpen_plugin.so
%{_libdir}/vlc/plugins/video_filter/libtransform_plugin.so
%{_libdir}/vlc/plugins/video_filter/libvhs_plugin.so
%{_libdir}/vlc/plugins/video_filter/libwave_plugin.so
%if 0%{?suse_version} >= 1500 && 0%{?is_opensuse}
%{_libdir}/vlc/plugins/video_output/libwl_shell_plugin.so
%{_libdir}/vlc/plugins/video_output/libwl_shm_plugin.so
%{_libdir}/vlc/plugins/video_output/libxdg_shell_plugin.so
%endif
%{_libdir}/vlc/plugins/video_output/libfb_plugin.so
%{_libdir}/vlc/plugins/video_output/libflaschen_plugin.so
%{_libdir}/vlc/plugins/video_output/libglconv_vaapi_drm_plugin.so
%{_libdir}/vlc/plugins/video_output/libglconv_vaapi_x11_plugin.so
%{_libdir}/vlc/plugins/video_output/libgl_plugin.so
%{_libdir}/vlc/plugins/video_output/libvdummy_plugin.so
%{_libdir}/vlc/plugins/video_output/libvmem_plugin.so
%{_libdir}/vlc/plugins/video_output/libyuv_plugin.so
%{_libdir}/vlc/plugins/video_splitter/libclone_plugin.so
%{_libdir}/vlc/plugins/video_splitter/libwall_plugin.so
%{_libdir}/vlc/plugins/visualization/libvisual_plugin.so
%{_libdir}/vlc/plugins/vaapi/libvaapi_filters_plugin.so
%ifarch %{arm}
%dir %{_libdir}/vlc/plugins/arm_neon
%{_libdir}/vlc/plugins/arm_neon/libchroma_yuv_neon_plugin.so
%{_libdir}/vlc/plugins/arm_neon/libvolume_neon_plugin.so
%{_libdir}/vlc/plugins/arm_neon/libyuv_rgb_neon_plugin.so
%endif
%{_libdir}/vlc/vlc-cache-gen

%files jack
%{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so
%{_libdir}/vlc/plugins/audio_output/libjack_plugin.so

%if %{with gstreamer}
%files codec-gstreamer
%{_libdir}/vlc/plugins/codec/libgstdecode_plugin.so
%endif

%files vdpau
%dir %{_libdir}/vlc/plugins/vdpau
%{_libdir}/vlc/libvlc_vdpau.so.0
%{_libdir}/vlc/libvlc_vdpau.so.0.0.0
%{_libdir}/vlc/plugins/vdpau/libvdpau_adjust_plugin.so
%{_libdir}/vlc/plugins/vdpau/libvdpau_avcodec_plugin.so
%{_libdir}/vlc/plugins/vdpau/libvdpau_chroma_plugin.so
%{_libdir}/vlc/plugins/vdpau/libvdpau_deinterlace_plugin.so
%{_libdir}/vlc/plugins/vdpau/libvdpau_display_plugin.so
%{_libdir}/vlc/plugins/vdpau/libvdpau_sharpen_plugin.so
%{_libdir}/vlc/plugins/video_output/libglconv_vdpau_plugin.so

%if 0%{?is_opensuse}
%files opencv
%{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
%endif

%files -n libvlc%{libvlc}
%{_libdir}/libvlc.so.%{libvlc}*

%files -n libvlccore%{libvlccore}
%{_libdir}/libvlccore.so.%{libvlccore}*

%files qt
%{_bindir}/qvlc
%{_mandir}/man1/qvlc*
%{_libdir}/vlc/plugins/gui/libqt_plugin.so

%files devel
%{_includedir}/vlc/
%{_libdir}/libvlccore.so
%{_libdir}/libvlc.so
%{_libdir}/pkgconfig/libvlc.pc
%{_libdir}/pkgconfig/vlc-plugin.pc
%{_libdir}/vlc/libcompat.a
%{_libdir}/vlc/libvlc_vdpau.so

%if 0%{?BUILD_ORIG}
%files codecs
%{_libdir}/vlc/plugins/codec/libdca_plugin.so
%if %{with faad}
%{_libdir}/vlc/plugins/codec/libfaad_plugin.so
%endif
%if %{with fdk_aac}
%{_libdir}/vlc/plugins/codec/libfdkaac_plugin.so
%endif
%{_libdir}/vlc/plugins/codec/libx264_plugin.so
%{_libdir}/vlc/plugins/codec/libx26410b_plugin.so
%{_libdir}/vlc/plugins/codec/libx265_plugin.so
%endif

%changelog
