#
# spec file for package xawtv
#
# Copyright (c) 2020 SUSE LLC
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


%ifarch %arm aarch64
%define _lto_cflags %{nil}
%endif

Name:           xawtv
Version:        3.103
Release:        0
Summary:        Video4Linux TV application (Athena)
License:        GPL-2.0-or-later
Group:          Hardware/TV
URL:            http://www.kraxel.org/blog/linux/xawtv/
Source0:        http://linuxtv.org/downloads/xawtv/%{name}-%{version}.tar.bz2
Source1:        xawtv.desktop
Source2:        motv.desktop
# PATCH-FIX-OPENSUSE v4l-conf_non-position-independent-executable_fix.patch asterios.dramis@gmail.com -- Fix non-position-independent-executable rpmlint warning for v4l-conf
Patch0:         v4l-conf_non-position-independent-executable_fix.patch
# PATCH-SENT-UPSTREAM to hdegoede
Patch1:         xawtv-fixblitframesegfault.patch
# PATCH-FIX-UPSTREAM
Patch2:         fix-build-with-recent-glibc.patch
Patch3:         v4l-conf-fix-CVE-2020-13696.patch
Patch4:         gcc-10.patch
BuildRequires:  aalib-devel
BuildRequires:  alsa-devel
BuildRequires:  gcc-c++
BuildRequires:  libdv-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libquicktime-devel
BuildRequires:  libv4l-devel
BuildRequires:  lirc-devel
BuildRequires:  ncurses-devel
BuildRequires:  openmotif-devel
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11
BuildRequires:  zvbi-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86dga)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       tv-common
Requires:       tv-fonts
Requires:       v4l-conf
Recommends:     pia
Suggests:       lirc
Conflicts:      xaw3dd
%if 0%{?suse_version} > 1210
BuildRequires:  desktop-file-utils
%else
BuildRequires:  update-desktop-files
%endif

%description
xawtv is an X11 application for watching TV with your Linux box. It supports
video4linux devices (for example bttv cards, various USB webcams, ...). It uses
the Athena widgets.

%package -n motv
Summary:        Video4Linux TV application (Motif)
Group:          Hardware/TV
Requires:       tv-common
Requires:       tv-fonts
Requires:       v4l-conf
Recommends:     pia
Suggests:       lirc
Provides:       xawtv:%{_bindir}/motv

%description -n motv
motv is a X11 application for watching TV with your Linux box. It supports
video4linux devices (for example bttv cards, various USB webcams, ...).	It's
based on xawtv's code, but uses Motif to provide a better GUI.

Also includes the teletext/videotext viewer mtt.

%package -n tv-common
Summary:        Frequency tables and some Tools for motv and xawtv
Group:          Hardware/TV
Provides:       xawtv:%{_prefix}/X11R6/lib/X11/fonts/misc/led-iso8859-1.bdf

%description -n tv-common
This package includes frequency tables for various countries and some utilities
for xawtv and motv (xawtv-remote, for example).

%package -n v4l-conf
Summary:        Video4linux Configuration Tool
Group:          Hardware/TV
Requires(post): permissions
Provides:       xawtv:%{_bindir}/v4l-conf

%description -n v4l-conf
This is a small utility used to configure video4linux device drivers
(bttv, for example). xawtv, motv, and fbtv need it.

%package -n v4l-tools
Summary:        Video4linux terminal / command line utilities
Group:          Hardware/TV
Requires:       tv-common
Requires:       v4l-conf
Provides:       xawtv:%{_bindir}/v4lctl

%description -n v4l-tools
This package includes a bunch of command line utilities: v4lctl to
control video4linux devices; streamer to record movies; fbtv to watch
TV on the framebuffer console; ttv to watch tv on any ttv (powered by
aalib), webcam for capturing and uploading images, a curses radio
application, ...

%package -n alevtd
Summary:        HTTP server for Teletext pages
Group:          Productivity/Networking/Web/Servers

%description -n alevtd
alevtd reads the teletext pages from /dev/vbi and allows to fetch them
via http, i.e. you can read the teletext pages with a web browser.

%package -n pia
Summary:        Simple Movie Player
Group:          Productivity/Multimedia/Video/Players
Requires:       tv-common

%description -n pia
pia is a simple movie player which can playback AVI and QuickTime
movies recorded by xawtv, motv, and streamer. Other movies might work
as well.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure
make verbose=yes %{?_smp_mflags}

%install
%make_install SUID_ROOT=""

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pm 0644 contrib/xawtv48x48.xpm  %{buildroot}%{_datadir}/pixmaps/xawtv.xpm
install -pm 0644 contrib/xawtv48x48.xpm  %{buildroot}%{_datadir}/pixmaps/motv.xpm

%if 0%{?suse_version} > 1210
desktop-file-install %{SOURCE1}
desktop-file-install %{SOURCE2}
%else
%suse_update_desktop_file -i xawtv
%suse_update_desktop_file -i motv
%endif

%verifyscript -n v4l-conf
%verify_permissions -e %{_bindir}/v4l-conf

%post -n v4l-conf
%if 0%{?set_permissions:1} > 0
  %{set_permissions %{_bindir}/v4l-conf}
%else
  %run_permissions
%endif

%files
%license COPYING
%doc Changes README README.* TODO
%doc contrib/frequencies* contrib/vdr.config
%{_bindir}/xawtv
%{_bindir}/rootv
%{_mandir}/man1/xawtv.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/xawtv.1%{ext_man}
%doc %lang(fr) %{_mandir}/fr/man1/xawtv.1%{ext_man}
%{_mandir}/man1/rootv.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/rootv.1%{ext_man}
%{_datadir}/X11/app-defaults/Xawtv
%{_datadir}/applications/xawtv.desktop
%{_datadir}/pixmaps/xawtv.xpm

%files -n motv
%license COPYING
%doc Changes README README.* TODO
%doc contrib/frequencies* contrib/vdr.config
%{_bindir}/motv
%{_mandir}/man1/motv.1%{?ext_man}
%{_datadir}/X11/app-defaults/MoTV
%dir %{_datadir}/X11/de_DE.UTF-8
%dir %{_datadir}/X11/fr_FR.UTF-8
%dir %{_datadir}/X11/it_IT.UTF-8
%lang(de) %{_datadir}/X11/de_DE.UTF-8/app-defaults
%lang(fr) %{_datadir}/X11/fr_FR.UTF-8/app-defaults
%lang(it) %{_datadir}/X11/it_IT.UTF-8/app-defaults
%{_bindir}/mtt
%{_mandir}/man1/mtt.1%{?ext_man}
%{_datadir}/X11/app-defaults/mtt
%{_datadir}/applications/motv.desktop
%{_datadir}/pixmaps/motv.xpm

%files -n tv-common
%license COPYING
%{_bindir}/subtitles
%{_mandir}/man1/subtitles.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/subtitles.1%{ext_man}
%{_bindir}/xawtv-remote
%{_mandir}/man1/xawtv-remote.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/xawtv-remote.1%{ext_man}
%{_bindir}/propwatch
%{_mandir}/man1/propwatch.1%{?ext_man}
%{_mandir}/man5/xawtvrc.5%{?ext_man}
%doc %lang(es) %{_mandir}/es/man5/xawtvrc.5.gz
%{_libdir}/xawtv
%{_datadir}/xawtv

%files -n v4l-conf
%license COPYING
%verify(not mode) %attr(4750,root,video) %{_bindir}/v4l-conf
%{_mandir}/man8/v4l-conf.8%{?ext_man}
%doc %lang(es) %{_mandir}/es/man8/v4l-conf.8.gz

%files -n v4l-tools
%license COPYING
%{_bindir}/radio
%{_mandir}/man1/radio.1%{?ext_man}
%{_bindir}/fbtv
%{_mandir}/man1/fbtv.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/fbtv.1%{ext_man}
%{_bindir}/ttv
%{_mandir}/man1/ttv.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/ttv.1%{ext_man}
%{_bindir}/streamer
%{_mandir}/man1/streamer.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/streamer.1%{ext_man}
%{_bindir}/v4lctl
%{_mandir}/man1/v4lctl.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/v4lctl.1%{ext_man}
%{_bindir}/record
%{_mandir}/man1/record.1%{?ext_man}
%{_bindir}/dump-mixers
%{_mandir}/man1/dump-mixers.1%{?ext_man}
%{_bindir}/showriff
%{_mandir}/man1/showriff.1%{?ext_man}
%{_bindir}/showqt
%{_bindir}/scantv
%{_mandir}/man1/scantv.1%{?ext_man}
%doc %lang(es) %{_mandir}/es/man1/scantv.1%{ext_man}
%{_bindir}/ntsc-cc
%{_mandir}/man1/ntsc-cc.1%{?ext_man}
%{_bindir}/webcam
%{_mandir}/man1/webcam.1%{?ext_man}
%{_bindir}/v4l-info
%{_mandir}/man1/v4l-info.1%{?ext_man}

%files -n alevtd
%license COPYING
%{_bindir}/alevtd
%{_mandir}/man1/alevtd.1%{?ext_man}

%files -n pia
%license COPYING
%doc Changes README
%{_bindir}/pia
%{_mandir}/man1/pia.1%{?ext_man}

%changelog
