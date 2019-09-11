#
# spec file for package WindowMaker-applets
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           WindowMaker-applets
BuildRequires:  WindowMaker-devel
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  imake
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xxf86dga)
BuildRequires:  pkgconfig(xxf86vm)

%if 0%{?suse_version} >= 1210
BuildRequires:  libv4l-devel >= 0.8.4
%endif
%if 0%{?suse_version} >= 1220
BuildRequires:  xmessage
%endif
Obsoletes:      wmapps
Obsoletes:      wmweath
Provides:       wmapps
Provides:       wmweath
Version:        1.0.1
Release:        0
Summary:        Window Maker Applets
#
License:        GPL-2.0+
Group:          System/GUI/Other
%define wmcdplay_version	1.0-beta1
#http://www.geocities.com/SiliconValley/Vista/2471/wmcdplay.html
#
%define wmload_version		0.9.2
#
#
%define wmnet_version		1.06
#http://www.digitalkaos.net/linux/wmnet/
#
%define wmtune_version		1.1c
#http://soren.org/linux/wmtune/
#
%define WMMail_version 	0.64
#http://www.eecg.toronto.edu/cgi-bin/cgiwrap/chanb/index.cgi?wmmail
#http://vbeaud.free.fr/tools/patchs_en.html
#
%define wmmount_version 	1.0-beta2
#http://www.geocities.com/SiliconValley/Vista/2471/wmmount.html
#
%define wmmixer_version 	1.0-beta1
#http://www.geocities.com/SiliconValley/Vista/2471/wmmixer.html
#
%define wmtimer_version 	2.92
#http://www.darkops.net/wmtimer/
#
%define wmtime_version 		1.0b2
%define wmppp_version 		1.3.0
%define wmpalm_version 		0.11b
%define wmmp3_version 		0.12
#http://www.dotfiles.com/software/wmmp3/
#
%define wmmon_version 		1.0b2
%define wmint_version 		0.8
%define wminet_version 		2.0.3
#http://www.neotokyo.org/illusion/
#
%define wmifs_version 		1.3b1
%define wmgmon_version 		0.4.0
#http://www.logilab.org/wmgmon/
#
%define wmfire_version 		0.0.3.9pre4
#http://staff.xmms.org/zinx/misc/
#
%define wmcube_version 		0.98
#http://boombox.campus.luth.se/projects.html
#
%define wmbutton_version 	0.4
#http://members.access1.net/ehflora/
#
%define wmMatrix_version 	0.2
#http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
#
%define wmMand_version 		1.0
#http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
#
%define wmCalClock_version 	1.25
#http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
#
%define wmWeather_version 	2.4.3
#http://www.godisch.de/debian/wmweather/
#
%define WMAmpMenu_version 	0.27
%define wmswallow_version	0.6.1
%define wmtop_version 		0.83
%define wmGrabImage_version 	0.70
#http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
#
%define wmSpaceWeather_version 	1.04
#http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
#
%define wmSun_version 		1.03
#http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
#
%define wmrecord_version 	1.0.5
#http://www.bruhaha.demon.co.uk/
#
%define wmtv_version 		0.6.5
#http://www.student.uwa.edu.au/~wliang/
#
%define wmbiff_version		0.4.0
#http://sourceforge.net/projects/wmbiff/
#
%define pclock_version 		0.13.1
#http://kraanerg.apex-it.com/~awk/pclock/
#
%define wmNetscapeKiller_version 0.3
#http://pblumo.free.fr/wmNetscapeKiller/
#
%define wmSMPmon_version 	3.1
#http://lancre.ribbrock.org/binabit/wmSMPmon/
#
%define wmappl_version		0.6
#http://www.upl.cs.wisc.edu/~charkins/wmappl.html
#
%define wmnd_version		0.2.2
#http://www.wingeer.org/wmnd/
#
%define wmpinboard_version      1.0
#http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/
#
%define wmcliphist_version      1.0
#http://linux.nawebu.cz/wmcliphist/
#
%define wmisdn_version          1.8
#http://www.uni-bonn.de/~uzsymm/linux.html
#
Source0:        wmcdplay-%{wmcdplay_version}.tgz
Source1:        wmload-%{wmload_version}.tgz
Source2:        wmnet-%{wmnet_version}.tar.gz
Source3:        wmtune-%{wmtune_version}.tar.gz
Source4:        WMMail.app-%{WMMail_version}.tar.gz
Source5:        wmmount-%{wmmount_version}.tgz
Source6:        wmmixer-%{wmmixer_version}.tgz
Source7:        wmtimer-%{wmtimer_version}.tar.gz
Source8:        wmtime-%{wmtime_version}.tar.gz
Source9:        wmppp-%{wmppp_version}.tar.gz
Source10:       wmpalm-%{wmpalm_version}.tgz
Source11:       wmmp3-%{wmmp3_version}.tar.gz
Source12:       wmmon-%{wmmon_version}.tar.gz
Source13:       wmint-%{wmint_version}.tar.gz
Source14:       wminet-%{wminet_version}.tar.gz
Source15:       wmifs-%{wmifs_version}.tar.gz
Source16:       wmgmon-%{wmgmon_version}.tar.gz
Source18:       wmfire-%{wmfire_version}.tar.gz
Source19:       wmcube-%{wmcube_version}.tar.gz
Source20:       wmbutton-%{wmbutton_version}.tar.gz
Source21:       wmMatrix-%{wmMatrix_version}.tar.gz
Source22:       wmMand-%{wmMand_version}.tar.gz
Source23:       wmCalClock-%{wmCalClock_version}.tar.gz
Source24:       wmweather-%{wmWeather_version}.tar.gz
Source26:       WMAmpMenu-%{WMAmpMenu_version}.tar.gz
Source27:       wmswallow.tar.Z
Source28:       wmtop-%{wmtop_version}.tar.gz
Source29:       wmGrabImage-%{wmGrabImage_version}.tar.gz
Source30:       wmSpaceWeather-%{wmSpaceWeather_version}.tar.gz
Source31:       wmSun-%{wmSun_version}.tar.gz
Source32:       wmrecord-%{wmrecord_version}.tar.gz
Source33:       wmtv-%{wmtv_version}.tar.gz
Source34:       wmbiff-%{wmbiff_version}.tar.gz
Source35:       pclock-%{pclock_version}.tgz
Source36:       wmNetscapeKiller-%{wmNetscapeKiller_version}.tar.gz
Source37:       wmSMPmon-%{wmSMPmon_version}.tar.gz
Source38:       wmappl-%{wmappl_version}.tar.gz
Source39:       wmnd_%{wmnd_version}.tar.gz
Source40:       wmpinboard-%{wmpinboard_version}.tar.bz2
Source41:       wmcliphist-%{wmcliphist_version}.tar.gz
Source42:       wmisdn-%{wmisdn_version}.tgz
#
Source99:       README.SuSE
#
Source200:      SuSE_wmapps
#
Patch0:         wmcdplay-%{wmcdplay_version}.patch
Patch1:         wmload-%{wmload_version}.patch
Patch2:         wmnet-%{wmnet_version}.dif
Patch3:         wmtune-1.0.1-combined.dif
Patch4:         WMMail_patch_064_070.gz
Patch5:         wmmount-%{wmmount_version}.dif
Patch6:         wmmixer-%{wmmixer_version}.patch
Patch7:         wmtimer-2.9.patch
Patch8:         wmtime-%{wmtime_version}.patch
Patch9:         wmppp-%{wmppp_version}.dif
Patch11:        wmmp3-%{wmmp3_version}.dif
Patch12:        wmmon-%{wmmon_version}.patch
Patch15:        wmifs-%{wmifs_version}.patch
Patch16:        wmgmon.dif
Patch19:        wmcube-%{wmcube_version}.patch
Patch21:        wmMatrix.dif
Patch22:        wmMand-%{wmMand_version}.patch
Patch31:        wmSun-%{wmSun_version}.dif
Patch32:        wmrecord-%{wmrecord_version}.dif
Patch33:        wmtv-%{wmtv_version}.patch
Patch34:        wmtv-v4l-2.6.38.patch
Patch36:        wmNetscapeKiller-%{wmNetscapeKiller_version}.dif
Patch37:        wmSMPmon-%{wmSMPmon_version}.dif
Patch38:        wmappl-%{wmappl_version}.dif
Patch39:        wmnd_%{wmnd_version}.patch
Patch40:        wmpinboard-%{wmpinboard_version}.patch
Patch41:        wmcliphist-0.6-default.patch
Patch42:        wmisdn-%{wmisdn_version}.dif
Patch44:        WMMail-automake.patch
Patch45:        WMMail-fewargs.patch
Patch46:        wmSMPmon-Support-selecting-CPUs-to-display.patch
Patch47:        wmfire-%{wmfire_version}-configure_fix.diff
Patch48:        wmswallow-%{wmswallow_version}-ld_fix.diff
Patch49:        wmcliphist-%{wmcliphist_version}-ld_fix.diff
# PATCH-FIX-UPSTREAM mvetter@suse.com boo#707539 - ImageMagick convert parameter changed
Patch50:        wmgrabimage-0.70-boo-707539-fix-GrabImage.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Some small applications for Window Maker.



Authors:
--------
    Bryan Chan <bryan.chan@utoronto.ca>
    Michael G. Henderson <mghenderson@lanl.gov>
    Edward H. Flora <ehflora@ksu.edu>
    Sam Hawker <shawkie@geocities.com>
    Robert Kling <robkli-8@student.luth.se>
    Antti Takala <fragment@nic.fi>
    Martijn Pieterse <pieterse@xs4all.nl>
    Zinx Verituse <zinx@linuxfreak.com>
    Jerome Dumonteil <jerome.dumonteil@capway.com>
    Nicolas Chauvat <nico@caesium.fr>
    Antoine Nulle <warp@xs4all.nl>
    Dave Clark <clarkd@skynet.ca>
    Sébastien Liénard <slienard@worldnet.fr>
    Sam Hawker <shawkie@geocities.com>
    Patrick Crosby <xb@dotfiles.com>
    Jesse B. Off <joff@iastate.edu>
    <robertle@cube.net>
    Anthony Quinn <southgat@frontiernet.net>
    Josh King <jking@dwave.net>
    <soren@linuxwarez.com>
    Michael Pearson <alcaron@ozemail.com.au>
    Pontus Klang <c96pkg@cs.umu.se>
    Philippe Vigneron <vigneron@free.fr>
    Alexander Kourakos <alexander@kourakos.com>
    <lempinen@iki.fi>
    Gennady Belyakov <gb@ccat.elect.ru>
    Beat Christen <bchriste@iiic.ethz.ch>
    Pierre Olivier <pblumo@free.fr>
    <robertle@cube.net>
    Malcolm Cowe <malk@bruhaha.demon.co.uk>
    Friedrich Delgado Friedrichs <friedel@nomaden.org>
    Dan Piponi <dan@tanelorn.demon.co.uk>
    <wliang@tartarus.uwa.edu.au>
    <red_seb@yahoo.com>
    Casey Harkins <charkins@pobox.com>
    Reed Lai <reed@wingeer.org>
    Marco Goetze, <gomar@mindless.com>
    Michal Krause <michal@krause.cz>
    Thomas Ribbrock <emgaron@ribbrock.org>

%prep
%setup -n wmcdplay -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14 -b 15 -b 16 -b 18 -b 19 -b 20 -b 21 -b 22 -b 23 -b 24 -b 26 -b 27 -b 28 -b 29 -b 30 -b 31 -b 32 -b 33 -b 34 -b 35 -b 36 -b 37 -b 38 -b 39 -b 40 -b 41 -b 42
%patch0
touch wmcdplay.man
cd ../wmload-%{wmload_version}
%patch1
cd ../wmnet-%{wmnet_version}
%patch2
cd ../wmtune-1.0.1-combined
%patch3
cd ../WMMail.app*
%patch4
%patch44
%patch45
cd ../wmmount-%{wmmount_version}
%patch5
cd ../wmmixer
%patch6
cd ../wmtimer-%{wmtimer_version}
%patch7
cd ../wmtime.app
%patch8
cd ../wmppp.app
%patch9
cd ../wmmp3-%{wmmp3_version}
%patch11
cd ../wmmon.app
%patch12
cd ../wmifs.app
%patch15
cd ../wmgmon.app/src
%patch16
cd ../../wmcube
%patch19
cd ../wmMatrix-%{wmMatrix_version}
%patch21
cd ../wmMand-%{wmMand_version}
%patch22
cd ../wmSun-%{wmSun_version}
%patch31
cd ../wmrecord-%{wmrecord_version}
%patch32
cd ../wmtv
%patch33
%if 0%{?suse_version} >= 1210
%patch34 -p1
%endif
cd ../wmNetscapeKiller-%{wmNetscapeKiller_version}
%patch36
cd ../wmSMPmon-%{wmSMPmon_version}
%patch37
%patch46 -p1
cd ../wmappl-%{wmappl_version}
%patch38
cd ../wmnd_%{wmnd_version}
%patch39
cd ../wmpinboard-%{wmpinboard_version}
%patch40
cd ../wmcliphist
%patch41
cd ../wmisdn-%{wmisdn_version}
%patch42
cd ../wmfire-%{wmfire_version}
%patch47
cd ../wmswallow
%patch48
cd ../wmcliphist
%patch49
cd ../wmGrabImage-%{wmGrabImage_version}/wmGrabImage
%patch50 -p2

%build
RPM_OPT_FLAGS+=" -fgnu89-inline"
xmkmf -a
make CXXFLAGS="$RPM_OPT_FLAGS"
cd ../wmload-%{wmload_version}
xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS"
cd ../wmnet-%{wmnet_version}
xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS"
%ifarch %ix86 x86_64 alpha ia64 %arm
cd ../wmtune-1.0.1-combined
make CFLAGS="$RPM_OPT_FLAGS"
%endif
#wmmail uses proplist-compat.h needs to be fixed
#cd ../WMMail.app-%{WMMail_version}
#autoreconf --force --install -v
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/ --with-appspath=/usr/lib/GNUstep/Applications
#make
cd ../wmmount-%{wmmount_version}
xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS"
cd ../wmmixer
xmkmf -a
make CXXFLAGS="$RPM_OPT_FLAGS"
cd ../wmtimer-%{wmtimer_version}/wmtimer
rm -f ../wmgeneral/*.o
rm -f *.o
make CFLAGS="$RPM_OPT_FLAGS `pkg-config --cflags gtk+-2.0`"
cd ../../wmtime.app/wmtime
make CFLAGS="$RPM_OPT_FLAGS"
cd ../../wmppp.app/wmppp
rm -f example-scripts/getmodemspeed
mv getmodemspeed example-scripts
chmod 755 example-scripts/getmodemspeed
make CFLAGS="$RPM_OPT_FLAGS"
cd ../../wmpalm-%{wmpalm_version}
make FLAGS="-Wall -ansi $RPM_OPT_FLAGS" \
     LINK="-lX11 -lXpm -lXext"
cd ../wmmp3-%{wmmp3_version}
autoreconf --force --install -v
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/
make
cd ../wmmon.app/wmmon
make CFLAGS="$RPM_OPT_FLAGS"
cd ../../wmint.app/wmint
make FLAGS="$RPM_OPT_FLAGS"
cd ../../wminet.app/wminet
make FLAGS="$RPM_OPT_FLAGS"
cd ../../wmifs.app/wmifs
make  CFLAGS="$RPM_OPT_FLAGS"
#wmgmon uses proplist-compat.h needs to be fixed
#cd ../../wmgmon.app/src
#make FLAGS="$RPM_OPT_FLAGS -Wall -I/usr/include"
cd ../../wmfire-%{wmfire_version}
autoreconf -fi
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" ./configure --prefix=/usr/
make
cd ../wmcube/wmcube
make CFLAGS="$RPM_OPT_FLAGS -DLINUX"
cd ../../wmbutton-%{wmbutton_version}
make FLAGS="$RPM_OPT_FLAGS -I/usr/include/X11"
cd ../wmMatrix-%{wmMatrix_version}
rm -f *.o
make CFLAGS="$RPM_OPT_FLAGS"
cd ../wmMand-%{wmMand_version}/wmMand
rm -f *.o ../wmgeneral/*.o
make CFLAGS="$RPM_OPT_FLAGS"
cd ../../wmCalClock-%{wmCalClock_version}/Src
make CFLAGS="$RPM_OPT_FLAGS"
cd ..
cd ../wmweather-%{wmWeather_version}/src
autoreconf --force --install
CFLAGS="$RPM_OPT_FLAGS" \
  ./configure --prefix=/usr/
make
cd ..
cd ../wmswallow
make xfree CFLAGS="$RPM_OPT_FLAGS"
cd ../wmtop-%{wmtop_version}
make linux OPTS="$RPM_OPT_FLAGS"
cd ../wmGrabImage-%{wmGrabImage_version}/wmGrabImage
make CFLAGS="$RPM_OPT_FLAGS"
cd ../../wmSpaceWeather-%{wmSpaceWeather_version}/wmSpaceWeather
make clean
make COPTS="$RPM_OPT_FLAGS"
cd ../../wmSun-%{wmSun_version}/wmSun
make clean
make COPTS="$RPM_OPT_FLAGS"
cd ../../wmrecord-%{wmrecord_version}
make CFLAGS="$RPM_OPT_FLAGS"
cd ../wmtv
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
cd ../wmbiff-%{wmbiff_version}
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/ --mandir=%{_mandir}
make
cd ../pclock-%{pclock_version}
make CFLAGS="$RPM_OPT_FLAGS"
cd ../wmNetscapeKiller-%{wmNetscapeKiller_version}
make CFLAGS="$RPM_OPT_FLAGS"
cd ../wmSMPmon-%{wmSMPmon_version}/wmSMPmon
make CFLAGS="$RPM_OPT_FLAGS"
cd ../../wmappl-%{wmappl_version}
make CFLAGS="$RPM_OPT_FLAGS -I/usr/include/X11"
cd ../wmnd_%{wmnd_version}
make CFLAGS="$RPM_OPT_FLAGS"
cd ../wmpinboard-%{wmpinboard_version}
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --mandir=%{_mandir}
make
cd ../wmcliphist
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wall `pkg-config --cflags gtk+-2.0` -I. -Ifoodock"
#
cd ../wmisdn-%{wmisdn_version}
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/{%{_mandir}/man1,etc,usr/{lib/GNUstep/Applications,bin},usr/%_lib/xmms/Visualization}
#rm -f ../wmappsfiles
#touch ../wmappsfiles
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmbutton
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcalclock
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcdplay
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcube
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmload
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmnet
%ifarch %ix86 x86_64 alpha ia64 %arm
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtune
%endif
#wmmail uses proplist-compat.h needs to be fixed
#install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmail
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmand
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmount
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmatrix
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmixer
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmfire
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtimer
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtime
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmppp
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmpalm
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmp3
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmon
#wmgmon uses proplist-compat.h needs to be fixed
#install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmgmon
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmint
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wminet
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmifs
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmweather
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmampmenu
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmswallow
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtop
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmgrabimage
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmspaceweather
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmsun
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmrecord
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtv
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmbiff
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/pclock
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmnetscapekiller
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmsmpmon
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmappl
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmnd
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmpinboard
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcliphist
install -d -m 755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmisdn
#
install -m 0644 ${RPM_SOURCE_DIR}/README.SuSE $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}
#
install -m 0755 wmcdplay $RPM_BUILD_ROOT/usr/bin/
install -m 0644 ARTWORK COPYING README $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcdplay
cd ../wmload-%{wmload_version}
install -m 0755 wmload $RPM_BUILD_ROOT/usr/bin/
install -m 0644 README INSTALL $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmload
cd ../wmnet-%{wmnet_version}
install -m 0755 wmnet $RPM_BUILD_ROOT/usr/bin/
install -m 0644 wmnet.man $RPM_BUILD_ROOT%{_mandir}/man1/wmnet.1
install -m 0644 README Changelog $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmnet
%ifarch %ix86 x86_64 alpha ia64 %arm
cd ../wmtune-1.0.1-combined
install -m 0755 wmtune $RPM_BUILD_ROOT/usr/bin/
install -m 0644 README COPYING sample.wmtunerc $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtune/
install -m 0644 sample.wmtunerc $RPM_BUILD_ROOT/etc/wmtunerc
%endif
#wmmail uses proplist-compat.h needs to be fixed
#cd ../WMMail.app-%{WMMail_version}
#make DESTDIR=$RPM_BUILD_ROOT install
#install -m 0644 AUTHORS COPYING ChangeLog INSTALL README NEWS \
#		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmail/
#SAVE=$PWD; cd $RPM_BUILD_ROOT/usr/bin; rm -f wmmail; ln -s ../lib/GNUstep/Applications/WMMail.app/WMMail wmmail; cd $SAVE
cd ../wmmount-%{wmmount_version}
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib/X11/wmmount
install -m 0755 wmmount $RPM_BUILD_ROOT/usr/bin/
install -m 0644 COPYING README $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmount
install -m 0644 wmmount.SuSE $RPM_BUILD_ROOT/etc/wmmount
cd lib
for i in * ; do
  install -m 0644 $i $RPM_BUILD_ROOT/usr/lib/X11/wmmount/
done
cd ../../wmmixer
install -m 0755 wmmixer $RPM_BUILD_ROOT/usr/bin/
install -m 0644 home.wmmixer COPYING README $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmixer
cd ../wmtimer-%{wmtimer_version}/wmtimer
install -m 0755 wmtimer $RPM_BUILD_ROOT/usr/bin/
cd ..
install -m 0644 COPYING CREDITS Changelog INSTALL README \
                $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtimer
cd ../wmtime.app/wmtime
install -m 0755 wmtime $RPM_BUILD_ROOT/usr/bin
cd ..
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL README TODO \
                $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtime
cd ../wmppp.app/wmppp
install -m 0755 wmppp $RPM_BUILD_ROOT/usr/bin
install -m 0644 system.wmppprc user.wmppprc $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmppp
install -d -m 0755 $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmppp/example-scripts
install -m 0644 example-scripts/* $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmppp/example-scripts
cd ..
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL README TODO \
                $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmppp
cd ../wmpalm-%{wmpalm_version}
install -m 0755 wmpalm $RPM_BUILD_ROOT/usr/bin/
install -m 0644 README $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmpalm
cd ../wmmp3-%{wmmp3_version}
install -m 0755 wmmp3 $RPM_BUILD_ROOT/usr/bin/
install -m 0644 AUTHORS COPYING ChangeLog INSTALL NEWS README TODO sample.wmmp3\
                $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmp3
cd ../wmmon.app/wmmon
install -m 0755 wmmon $RPM_BUILD_ROOT/usr/bin
cd ..
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL README TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmon
cd ../wmint.app/wmint
install -m 0755 wmint $RPM_BUILD_ROOT/usr/bin
cd ..
install -m 0644 BUGS COPYING HINTS INSTALL README TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmint
cd ../wminet.app/wminet
install -m 0755 wminet $RPM_BUILD_ROOT/usr/bin
install -m 0644 wminetrc $RPM_BUILD_ROOT/etc/
cd ..
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL README TODO \
                $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wminet
cd ../wmifs.app/wmifs
install -m 0755 wmifs $RPM_BUILD_ROOT/usr/bin
install -m 0644 sample.wmifsrc $RPM_BUILD_ROOT/etc/wmifsrc
install -m 0644 sample.wmifsrc $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmifs
cd ..
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL README TODO \
                $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmifs
#wmgmon uses proplist-compat.h needs to be fixed
#cd ../wmgmon.app/src
#install -m 0755 wmgmon $RPM_BUILD_ROOT/usr/bin
#cd ..
#install -m 0644 README $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmgmon
#install -d $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmgmon/doc
#install -m 0644 doc/* $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmgmon/doc
cd ../wmfire-%{wmfire_version}
install -m 0755 wmfire $RPM_BUILD_ROOT/usr/bin
install -m 0755 fireload_cpu $RPM_BUILD_ROOT/usr/bin
install -m 0755 fireload_file $RPM_BUILD_ROOT/usr/bin
install -m 0644 AUTHORS COPYING CREDITS ChangeLog NEWS README \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmfire
cd ../wmcube/wmcube
install -m 0755 wmcube $RPM_BUILD_ROOT/usr/bin
cd ..
install -m 0644 COPYING INSTALL README TODO $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcube
install -d $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcube/3dObjects
install -m 0644 3dObjects/*  $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcube/3dObjects
cd ../wmbutton-%{wmbutton_version}
install -m 0755 wmbutton $RPM_BUILD_ROOT/usr/bin
install -m 0644 .wmbutton $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmbutton/sample.wmbutton
install -m 0644 COPYING README $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmbutton
cd ../wmMatrix-%{wmMatrix_version}
install -m 0755 wmMatrix $RPM_BUILD_ROOT/usr/bin/wmmatrix
cd ../wmMand-%{wmMand_version}/wmMand
install -m 0755 wmMand $RPM_BUILD_ROOT/usr/bin/wmmand
cd ..
install -m 0644 BUGS CHANGES COPYING $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmmand
cd ../wmCalClock-%{wmCalClock_version}/Src
install -m 0755 wmCalClock $RPM_BUILD_ROOT/usr/bin/wmcalclock
install -m 0644 wmCalClock.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmcalclock.1
cd ..
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL README TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcalclock
cd ../wmweather-%{wmWeather_version}/src
install -m 0755 wmweather $RPM_BUILD_ROOT/usr/bin/wmweather
install -m 0644 wmweather.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmweather.1
cd ..
install -m 0644 CHANGES COPYING README \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmweather
cd ../wmampmenu/src
install -m 0755 mp3launch wmampmenu $RPM_BUILD_ROOT/usr/bin/
cd ..
install -m 0644 COPYING Changes README  \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmampmenu
cd ../wmswallow
install -m 0755 wmswallow $RPM_BUILD_ROOT/usr/bin/
install -m 0644 CHANGELOG LICENCE README  \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmswallow
cd ../wmtop-%{wmtop_version}
install -m 0755 wmtop $RPM_BUILD_ROOT/usr/bin/
install -m 0644 wmtop.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 0644 BUGS CHANGES COPYING README TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtop
cd ../wmGrabImage-%{wmGrabImage_version}
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmgrabimage
cd wmGrabImage
install -m 0755 wmGrabImage $RPM_BUILD_ROOT/usr/bin/wmgrabimage
install -m 0755 GrabImage $RPM_BUILD_ROOT/usr/bin/
install -m 0644 wmGrabImage.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmgrabimage.1
cd ../../wmSpaceWeather-%{wmSpaceWeather_version}
install -m 0644 BUGS CHANGES COPYING HINTS INSTALL README \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmspaceweather
cd wmSpaceWeather
install -m 0755 wmSpaceWeather $RPM_BUILD_ROOT/usr/bin/wmspaceweather
install -m 0755 GetKp $RPM_BUILD_ROOT/usr/bin/
install -m 0644 wmSpaceWeather.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmspaceweather.1
cd ../../wmSun-%{wmSun_version}
install -m 0644 BUGS COPYING TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmsun
cd wmSun
install -m 0755 wmSun $RPM_BUILD_ROOT/usr/bin/wmsun
install -m 0644 wmSun.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmsun.1
cd ../../wmrecord-%{wmrecord_version}
install -m 0644 COPYING INSTALL README TODO  \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmrecord
install -m 0755 wmrecord $RPM_BUILD_ROOT/usr/bin/
install -m 0644 man/wmrecord.1 $RPM_BUILD_ROOT%{_mandir}/man1/
cd ../wmtv
install -m 0644 COPYING CHANGES CREDITS README wmtvrc.sample \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmtv
install -m 0755 wmtv $RPM_BUILD_ROOT/usr/bin/
cd ../wmbiff-%{wmbiff_version}
make DESTDIR=$RPM_BUILD_ROOT install
install -m 0644 README ChangeLog NEWS TODO README.licq wmbiff/sample.wmbiffrc \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmbiff
cd ../pclock-%{pclock_version}/src
install -m 0755 pclock $RPM_BUILD_ROOT/usr/bin/
cd ..
for i in demos/* ; do
  mv $i $i.orig
  sed -e "s|../src/||" $i.orig >$i
  rm -f $i.orig
done
chmod 755 demos/*
chmod 644 XPM/*
chmod 755 {demos,XPM}
install -m 0644 CHANGES COPYING CREDITS README TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/pclock
cp -pr demos XPM $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/pclock
cd ../wmNetscapeKiller-%{wmNetscapeKiller_version}
install -m 0755 wmNetscapeKiller $RPM_BUILD_ROOT/usr/bin/
install -m 0644 CHANGELOG README \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmnetscapekiller
cd ../wmSMPmon-%{wmSMPmon_version}/wmSMPmon
install -m 0755 wmSMPmon $RPM_BUILD_ROOT/usr/bin/wmSMPmon
install -m 0644 wmSMPmon.1 $RPM_BUILD_ROOT%{_mandir}/man1/
cd ..
install -m 0644 COPYING GREETINGS LISEZ-MOI Changelog \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmsmpmon
cd ../wmappl-%{wmappl_version}
install -m 0755 wmappl $RPM_BUILD_ROOT/usr/bin/
install -d $RPM_BUILD_ROOT/usr/share/icons/wmappl
install -m 644 -c icons/*.xpm $RPM_BUILD_ROOT/usr/share/icons/wmappl
install -m 0644 LICENSE README sample.wmapplrc \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmappl
cd ../wmnd_%{wmnd_version}
install -m 0755 wmnd $RPM_BUILD_ROOT/usr/bin/
install -m 0644 wmndrc CHANGELOGS COPYING HINTS INSTALL README TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmnd
install -m 0644 man/wmnd.1 $RPM_BUILD_ROOT%{_mandir}/man1
cd ../wmpinboard-%{wmpinboard_version}
make DESTDIR=$RPM_BUILD_ROOT install
install -m 0644 AUTHORS COPYING CREDITS NEWS README ChangeLog TODO \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmpinboard
cd ../wmcliphist
install -m 0755 wmcliphist $RPM_BUILD_ROOT/usr/bin/
install -m 0644 COPYING README ChangeLog wmcliphistrc \
		$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmcliphist
cd ../wmisdn-%{wmisdn_version}
install -m 0755 wmisdn $RPM_BUILD_ROOT/usr/bin/
install -m 0644 README CHANGES COPYING \
                $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/wmisdn
#
mkdir -p $RPM_BUILD_ROOT/etc/X11/WindowMaker
install -m 644 %{S:200} $RPM_BUILD_ROOT/etc/X11/WindowMaker/SuSE_wmapps
#
%fdupes $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/X11/wmmount/
%docdir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}
%doc %{_mandir}/man1/wmnet.1.gz
%doc %{_mandir}/man1/wmcalclock.1.gz
%doc %{_mandir}/man1/wmbiff.1.gz
%doc %{_mandir}/man1/wmSMPmon.1.gz
%doc %{_mandir}/man5/wmbiffrc.5.gz
%dir /usr/lib/GNUstep/Applications
#wmmail uses proplist-compat.h needs to be fixed
#/usr/lib/GNUstep/Applications/WMMail.app
#/usr/bin/wmmail
/usr/bin/wmmand
/usr/bin/wmmatrix
/usr/bin/wmbutton
/usr/bin/wmcdplay
/usr/bin/wmcube
/usr/bin/wmcalclock
/usr/bin/wmload
/usr/bin/wmfire
/usr/bin/fireload_cpu
/usr/bin/fireload_file
/usr/bin/wmint
/usr/bin/wmifs
/usr/bin/wminet
/usr/bin/wmnet
/usr/bin/wmmon
#wmgmon uses proplist-compat.h needs to be fixed
#/usr/bin/wmgmon
/usr/bin/wmmount
/usr/bin/wmmp3
/usr/bin/wmmixer
/usr/bin/wmtimer
/usr/bin/wmtime
/usr/bin/wmpalm
/usr/bin/wmppp
%ifarch %ix86 x86_64 alpha ia64 %arm
/usr/bin/wmtune
%config /etc/wmtunerc
%endif
%config /etc/wminetrc
%config /etc/wmifsrc
%config /etc/wmmount
/usr/bin/wmweather
/usr/bin/mp3launch
/usr/bin/wmampmenu
/usr/bin/wmswallow
/usr/bin/wmtop
/usr/bin/wmgrabimage
/usr/bin/GrabImage
/usr/bin/wmspaceweather
/usr/bin/GetKp
/usr/bin/wmsun
/usr/bin/wmrecord
/usr/bin/wmtv
/usr/bin/wmbiff
/usr/share/wmbiff
/usr/bin/pclock
/usr/bin/wmNetscapeKiller
/usr/bin/wmSMPmon
/usr/bin/wmappl
/usr/share/icons/wmappl
/usr/bin/wmnd
/usr/bin/wmpinboard
/usr/bin/wmcliphist
/usr/bin/wmisdn
%doc %{_mandir}/man1/wmweather.1.gz
%doc %{_mandir}/man1/wmtop.1.gz
%doc %{_mandir}/man1/wmgrabimage.1.gz
%doc %{_mandir}/man1/wmspaceweather.1.gz
%doc %{_mandir}/man1/wmsun.1.gz
%doc %{_mandir}/man1/wmrecord.1.gz
%doc %{_mandir}/man1/wmpinboard.1.gz
%doc %{_mandir}/man1/wmnd.1.gz
%dir /etc/X11/WindowMaker
%config /etc/X11/WindowMaker/SuSE_wmapps

%changelog
