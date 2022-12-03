#
# spec file for package xine-ui
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xine-ui
%bcond_without distributable
BuildRequires:  aalib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  gawk
BuildRequires:  libjpeg-devel
BuildRequires:  perl-DateTime
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxine)
%if !%{with distributable}
BuildRequires:  libxine2-codecs
%endif
BuildRequires:  lirc-devel
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
Summary:        Video player with plugins
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Productivity/Multimedia/Video/Players
Version:        0.99.13
Release:        0
URL:            http://xine.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       xine:/usr/bin/xine
Source:         http://sourceforge.net/projects/xine/files/xine-ui/%{version}/xine-ui-%{version}.tar.xz
Source1:        xine-ui.png
Source2:        xine-ui-crippled.png
# extra skins
Source11:       caramel.tar.bz2
Source12:       CelomaChrome.tar.bz2
Source13:       lcd.tar.bz2
Source99:       baselibs.conf
# *** xine-lib: Bugfixes
Patch0:         xine-ui-various.diff
#PATCH_FIX-OPENSUSE xine-ui-desktop.patch davejplater@gmail.com - remove desktop file errors
Patch1:         xine-ui-desktop.patch
# PATCH-FIX-UPSTREAM
Patch2:         Fix-build.patch
# *** SUSE only changes
Patch50:        xine-ui-crippled-LOCAL.diff
Patch60:        xine-ui-AUTOMAKE.diff

%description
xine is a free multimedia player. It plays back CDs, DVDs, and VCDs. It
also decodes multimedia files like AVI, MOV, WMV, and MP3 from local
disk drives, and displays multimedia streamed over the Internet. It
interprets many of the most common multimedia formats available - and
some of the most uncommon formats, too.



Authors:
--------
    Guenter Bartsch <guenter@sourceforge.net>

%prep
echo %{with distributable}
%setup -q
%patch2 -p1
%patch0
%patch50 -p0
%patch60
%patch1
install -m 0644 %SOURCE1 misc/splash-default/xine-ui_logo.png
install -m 0644 %SOURCE2 misc/splash-default/xine-ui_logo-crippled.png
%ifarch x86_64
sed -i -e "s/lirc_libprefix=\"\$LIRC_PREFIX\/lib\"/lirc_libprefix=\"\$LIRC_PREFIX\/lib64\"/g" \
       -e "s/for llirc in \$lirc_libprefix \/lib \/usr\/lib \/usr\/local\/lib; do/for llirc in \$lirc_libprefix \/lib64 \/usr\/lib64 \/usr\/local\/lib64; do/g" m4/_xine.m4
%endif

%build
%if 1 == 0
%define gcc_version 7
export CC=gcc-7
export CPP=cpp-7
export CXX=g++-7
%endif
export CFLAGS="%{optflags} -fno-strict-aliasing"
%if 0%{?gcc_version} > 5
export CFLAGS="$CFLAGS -Werror=date-time"
%endif
# ignore nonupdated automake+co files
rm -f missing ; touch missing
export XINE_DOCPATH=%{_datadir}/doc/packages/xine-ui

NO_CONFIGURE=1 ./autogen.sh

%configure \
	--enable-vdr-keys \
	--with-pic \
	--disable-static \
	--without-caca \
	--disable-silent-rules
make %{_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/xitk %{buildroot}%{_defaultdocdir}/xine-ui
mkdir -p %{buildroot}%{_datadir}/applications/
rm -rf %{buildroot}%{_datadir}/xine/desktop
install -m 0644 %SOURCE2 %{buildroot}%{_datadir}/xine/skins/xine-ui_logo-crippled.png
# extra skins
install -d -m755 %{buildroot}%{_datadir}/xine/skins/
for i in %SOURCE11 %SOURCE12 %SOURCE13 ; do
  tar xfvj $i -C %buildroot%{_datadir}/xine/skins/
done
#
%find_lang %{name}
%find_lang xitk %{name}.lang
find . -name "xine-bugreport.1*" -print -delete
%fdupes -s %{buildroot}%{_datadir}/xine
%if 0
%fdupes -s %{buildroot}%{_mandir}
%endif

%post
%mime_database_post
%desktop_database_post

%postun
%mime_database_postun
%desktop_database_postun

%files -f %{name}.lang
%defattr(-,root,root,0755)
%dir %_mandir/??
%dir %_mandir/??/man1
%doc %_mandir/*/man1/xine.1.gz
%doc %_mandir/*/man1/xine-check.1.gz
%doc %_mandir/*/man1/xine-remote.1.gz
%doc %_mandir/*/man1/aaxine*
%doc %_mandir/man1/aaxine*
%doc %_mandir/man1/xine.1.gz
%doc %_mandir/man1/xine-check.1.gz
%doc %_mandir/man1/xine-remote.1.gz
%doc %_mandir/*/man1/xine-bugreport.1.gz
%doc %_mandir/man1/xine-bugreport.1.gz
%{_bindir}/aaxine
%{_bindir}/fbxine
%{_bindir}/xine
%{_bindir}/xine-check
%{_bindir}/xine-remote
%{_bindir}/xine-bugreport
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/xine.png
%{_datadir}/icons/hicolor/scalable/apps/xine.svgz
%dir %{_datadir}/xine
%dir %{_datadir}/xine/skins
%{_datadir}/xine/skins/missing.png
%{_datadir}/xine/skins/xine-ui_logo.mpg
%{_datadir}/xine/skins/xine-ui_logo.png
%{_datadir}/xine/skins/xine-ui_logo-crippled.png
%{_datadir}/xine/skins/xine_64.png
%{_datadir}/xine/skins/xine_splash.png
%{_datadir}/xine/skins/xinetic
%{_datadir}/xine/skins/CelomaChrome
%{_datadir}/xine/skins/caramel
%{_datadir}/xine/skins/lcd
%dir %{_datadir}/xine/visuals
%{_datadir}/xine/visuals/default.mpv
%{_datadir}/applications/xine.desktop
%{_datadir}/xine/oxine
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/xine-ui.xml
%_defaultdocdir/xine-ui

%changelog
