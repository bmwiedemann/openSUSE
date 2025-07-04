#
# spec file for package gstreamer-plugins-good
#
# Copyright (c) 2025 SUSE LLC
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


%define gstreamer_req_version %(echo %{version} | sed -e "s/+.*//")

# aasink is just a toy. Once in future, we may want to disable aalib
# support completely: Disabled 25/12/17
%define ENABLE_AALIB 0
#
%define _name gst-plugins-good
%define gst_branch 1.0

# Disable Qt6 on aarch64 and %%arm since GLES is used and not compatible here
%ifarch aarch64 %arm
%bcond_with qt6
%else
%bcond_without qt6
%endif

Name:           gstreamer-plugins-good
Version:        1.26.3
Release:        0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{_name}-%{version}.tar.zst
Source1:        gstreamer-plugins-good.appdata.xml
Source99:       baselibs.conf

BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  Mesa-libGLESv3-devel
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libICE-devel
BuildRequires:  libQt5PlatformHeaders-devel
BuildRequires:  libSM-devel
# used by libgstvideo4linux2.so
BuildRequires:  libXv-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libbz2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  meson >= 1.4
BuildRequires:  nasm
BuildRequires:  orc >= 0.4.16
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  zlib-devel

%if %{with qt6}
BuildRequires:  qt6-gui-private-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6ShaderTools)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6Widgets)
%endif

BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-gobject) >= 1.10.0
BuildRequires:  pkgconfig(flac) >= 1.1.4
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.8.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-check-1.0)
BuildRequires:  pkgconfig(gstreamer-controller-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-gl-1.0)
BuildRequires:  pkgconfig(gstreamer-net-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.0
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.15.0
BuildRequires:  pkgconfig(gtk+-x11-3.0) >= 3.15.0
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(jack) >= 0.99.10
BuildRequires:  pkgconfig(libdv) >= 0.100
BuildRequires:  pkgconfig(libiec61883) >= 1.0.0
BuildRequires:  pkgconfig(libmpg123) >= 1.13
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libraw1394) >= 2.0.0
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.9
BuildRequires:  pkgconfig(opencore-amrwb) >= 0.1.3
BuildRequires:  pkgconfig(shout) >= 2.4.3
BuildRequires:  pkgconfig(speex) >= 1.1.6
BuildRequires:  pkgconfig(taglib) >= 1.5
BuildRequires:  pkgconfig(twolame) >= 0.3.10
BuildRequires:  pkgconfig(vpx) >= 1.3.0
BuildRequires:  pkgconfig(wavpack) >= 4.60.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
Requires:       gstreamer >= %{gstreamer_req_version}
Requires:       gstreamer-plugins-base >= %{gstreamer_req_version}
Recommends:     %{name}-gtk
Enhances:       gstreamer
Conflicts:      gstreamer-plugins-ugly < 1.24.0
# Generic name, never used in SuSE: I wish it had been used I would have used it then I wouldn't have to keep copy pasting and actually type it.
Provides:       gst-plugins-good = %{version}
%if 0%{?ENABLE_AALIB}
BuildRequires:  aalib-devel
%endif

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package extra
Summary:        Complementary plugins for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description extra
This package provides complementary plugins for
gstreamer-plugins-good.

%package jack
Summary:        Jack plugin for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description jack
This package provides the jack plugin for gstreamer-plugins-good.

%package gtk
Summary:        Gtksink plugin for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description gtk
This package provides the gtksink output plugin for gstreamer-plugins-good.

%if %{with qt6}
%package qtqml6
Summary:        Qml6glsink plugin for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description qtqml6
This package provides the qml6glsink output plugin for gstreamer-plugins-good.
%endif

%lang_package

%prep
%autosetup -n %{_name}-%{version} -p1

%build
%if 0%{?suse_version} < 1600
export CC=%{_bindir}/gcc-13
export CXX=%{_bindir}/g++-13
%endif
export PYTHON=%{_bindir}/python3
%meson \
	-Dpackage-name='openSUSE GStreamer-plugins-good package' \
	-Dpackage-origin='http://download.opensuse.org' \
%if ! 0%{?ENABLE_AALIB}
	-Daalib=disabled \
%endif
	-Ddoc=disabled \
	-Drpicamsrc=disabled \
	-Dv4l2-probe=true \
	-Dqt5=disabled \
%if %{with qt6}
	-Dqt6=enabled \
%else
	-Dqt6=disabled \
%endif
	-Dqt-egl=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{_name}-%{gst_branch}
if [ -f %{buildroot}%{_datadir}/appdata/gstreamer-plugins-good.appdata.xml ]; then
  echo "Please remove the added gstreamer-plugins-good.appdata.xml file from the sources - the tarball installs it"
  false
else
  mkdir -p %{buildroot}%{_datadir}/appdata
  cp %{SOURCE1} %{buildroot}%{_datadir}/appdata/
fi

%files
%license COPYING
%doc AUTHORS README.md RELEASE REQUIREMENTS NEWS
%dir %{_datadir}/appdata
%{_datadir}/appdata/gstreamer-plugins-good.appdata.xml
%{_datadir}/gstreamer-%{gst_branch}/presets/GstAmrnbEnc.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer10Bands.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer3Bands.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstQTMux.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstVP8Enc.prs
%{_libdir}/gstreamer-%{gst_branch}/libgstadaptivedemux2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalaw.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalphacolor.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalpha.so
%{_libdir}/gstreamer-%{gst_branch}/libgstamrnb.so
%{_libdir}/gstreamer-%{gst_branch}/libgstamrwbdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstapetag.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiofx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{gst_branch}/libgstauparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstautodetect.so
%{_libdir}/gstreamer-%{gst_branch}/libgstavi.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcutter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdebug.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdtmf.so
%{_libdir}/gstreamer-%{gst_branch}/libgsteffectv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstequalizer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflac.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflxdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgdkpixbuf.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgoom.so
%{_libdir}/gstreamer-%{gst_branch}/libgsticydemux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstid3demux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{gst_branch}/libgstinterleave.so
%{_libdir}/gstreamer-%{gst_branch}/libgstisomp4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstjpeg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlame.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlevel.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmatroska.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpg123.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmulaw.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultifile.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultipart.so
%{_libdir}/gstreamer-%{gst_branch}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{gst_branch}/libgstoss4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstossaudio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpng.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpulseaudio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstreplaygain.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtsp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstshapewipe.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsmpte.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsoup.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspectrum.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspeex.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttaglib.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttwolame.so
%{_libdir}/gstreamer-%{gst_branch}/libgstudp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideobox.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideocrop.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideofilter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideomixer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvpx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavpack.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstximagesrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstxingmux.so
%{_libdir}/gstreamer-%{gst_branch}/libgsty4menc.so

%files extra
%{_libdir}/gstreamer-%{gst_branch}/libgst1394.so
%if 0%{?ENABLE_AALIB}
%{_libdir}/gstreamer-%{gst_branch}/libgstaasink.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstcacasink.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcairo.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmonoscope.so
%{_libdir}/gstreamer-%{gst_branch}/libgstshout2.so

%files jack
%{_libdir}/gstreamer-%{gst_branch}/libgstjack.so

%files gtk
%{_libdir}/gstreamer-%{gst_branch}/libgstgtk.so

%if %{with qt6}
%files qtqml6
%{_libdir}/gstreamer-%{gst_branch}/libgstqml6.so
%endif

%files lang -f %{_name}-%{gst_branch}.lang

%changelog
