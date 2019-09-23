#
# spec file for package i4l-base
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           i4l-base
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  groff
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libpcap-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  ppp-devel
BuildRequires:  sgmltool
#!BuildIgnore:  systemd
BuildRequires:  systemd-mini
BuildRequires:  tcl-devel
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-devel
Url:            http://www.isdn4linux.de
Provides:       i4l = %{version}
Obsoletes:      i4l <= %{version}
Version:        2011.8.29
Release:        0
Summary:        ISDN for Linux Basic Utilities
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Hardware/ISDN
Source:         isdn4k-utils.v3.13.tar.bz2
Source1:        i4l_suse.tar.bz2
Source2:        firmware.tar.bz2
Source3:        divactrl_2.1.tar.bz2
Source4:        45-isdn.rules
Source5:        isdn.sh
Source6:        baselibs.conf
Source7:        i4l.conf
Source8:        i4l-base-postprocess
Source9:        i4l-base-sysconfig
Source10:       libcapi20-3.0.7.tar.bz2
Source99:       i4l-base-rpmlintrc
Patch:          isdn4k-utils.dif
Patch1:         capi20_3.0.7.patch
Patch2:         isdn4k-utils-gcc5-fixes.patch
Patch31:        divactrl_2.1-gcc.diff
Patch32:        divactrl_2.1-fix.diff
Patch33:        divactrl_2.1-dprintf.diff
Patch34:        vboxbeep-pie.patch
Patch35:        isdnctrl-pie.patch
Patch36:        divactrl_2.1-dialog.patch
Patch37:        isdn4k-ncurses-6.0-accessors.patch
Patch38:        isdn4k-utils-perl526.diff
Patch39:        divactrl_2.1-sysmacros.diff
# fix build with newer automake
Patch50:        isdn4k-utils-automake-1_13.diff
Patch51:        isdn4k-utils-initialize-memory.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         /bin/cat
PreReq:         fileutils
PreReq:         %fillup_prereq
PreReq:         permissions
PreReq:         systemd
Requires(post): group(uucp)
#Excludearch:  s390 s390x
%define _xorg7_prefix /usr
%define _xorg7_app /usr/share
%define ppp_version %(rpm -q ppp --qf '%%{VERSION}')
%define ppp_version_short %(rpm -q ppp --qf '%%{VERSION}' | sed -e "s@\.git.*@@")

%description
These utilities are needed for configuring and using ISDN devices. This
package includes special tools for network connections via ISDN. Other
tools for setup of various ISDN cards and for monitoring ISDN
connections are also included.

%package -n ppp-userpass
Summary:        Password plugin for pppd
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/PPP
Requires:       ppp = %ppp_version

%description -n ppp-userpass
This package provides a plugin for pppd to allow setting the password
as a pppd option instead of placing it in the pap-secrets or
chap-secrets files. It is particularly useful to define ppp connections
in a single pppd options file under /etc/ppp/peers .

%package -n libcapi20-2
Summary:        CAPI 2.0 library
License:        LGPL-2.1-or-later
Group:          Hardware/ISDN

%description -n libcapi20-2
This package contains the CAPI 2.0 runtime library files.

%package -n libcapi20-3
Summary:        CAPI 2.0 library
License:        LGPL-2.1-or-later
Group:          Hardware/ISDN

%description -n libcapi20-3
This package contains the CAPI 2.0 runtime library files.

%package -n capi4linux
Summary:        CAPI 2.0 tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Hardware/ISDN
Provides:       i4l:/usr/bin/capiinfo
Requires:       i4l-base
Requires:       ppp = %ppp_version
Requires:       ppp-userpass
# bug437293
%ifarch ppc64
Obsoletes:      capi4linux-64bit
%endif
#

%description -n capi4linux
This package contains the CAPI 2.0 library, which is needed for all
CAPI applications.  It also contains programs to show information about
installed CAPI controllers and for the receiving and sending of FAX
messages. CAPI 2.0 drivers for Linux are available for a growing number
of ISDN devices.

%package -n capi4linux-devel
Summary:        CAPI 2.0 library files for development
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Hardware/ISDN
Requires:       capi4linux = %version
Requires:       libcapi20-2 = %version
Requires:       libcapi20-3 = %version
# bug437293
%ifarch ppc64
Obsoletes:      capi4linux-devel-64bit
%endif
#

%description -n capi4linux-devel
This package contains the CAPI 2.0 library files needed for
development.

%package -n i4lfirm
Summary:        ISDN firmware for active ISDN cards
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          Hardware/ISDN
Requires:       i4l-base

%description -n i4lfirm
ISDN firmware for active ISDN cards.

%package -n i4l-vbox
Obsoletes:      vbox
Provides:       i4l:/usr/bin/vbox
Provides:       vbox
Provides:       vbox2b4
Requires:       i4l-base
PreReq:         permissions
Summary:        A Voice Answering Machine for isdn4linux
License:        GPL-2.0-or-later
Group:          Hardware/ISDN

%description -n i4l-vbox
i4l-vbox is a voice answering machine for isdn4linux. It is a
collection of tools for answering phone calls, recording messages via
an ISDN card, and replaying recorded messages. It is also possible to
send the recorded messages to an email account. The recording and
playing of messages on the phone line is controlled via a Tcl script,
and it is possible to control additional functions via touch-tone. The
calling number can be used to select between various messages. The
answering machine configuration is controlled by a number of variable
configuration files.

%package -n ant-phone
Summary:        A telephone application
License:        GPL-2.0-or-later
Group:          Hardware/ISDN

%description -n ant-phone
ANT is a telephone application written for GNU/Linux, I4L (ISDN4Linux,
integrated in the kernel), GTK+ (GIMP Toolkit) and OSS (Open Sound
System).

%package -n i4l-isdnlog
Summary:        An ISDN line logging and control utility
License:        GPL-2.0-or-later
Group:          Hardware/ISDN
Provides:       i4l:/usr/sbin/isdnlog

%description -n i4l-isdnlog
Isdnlog is a very powerful tool to log calls on your ISDN line. It can
analyze the D-channel messages and start programs based on various
phone call events. It can make summaries of phone call costs and
translate known numbers to names. It has its own database for areacodes
and phone call costs for many phone network providers and can help you
to take care of your phone bill.

%prep
%setup -q -n isdn4k-utils -b 1 -b 2 -b 3
rm -rf capi20
tar -xjf %{S:10}
%patch
%patch34 -p1
%patch35 -p1
%patch1 -p0
%patch2 -p2
chmod a+x */configure
mv -f eicon/firmware/eicon_firm.tgz eicon/firmware/firmware.tgz
mv -f eicon/firmware ../divactrl_2.1/
pushd ../divactrl_2.1/
%patch31 -p1
%patch32 -p1
%patch33 -p0
%patch36
%patch39 -p1
popd
pushd ../isdn4k-utils
%patch37 -p1
%patch38 -p1
popd
%patch50 -p1
%patch51 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
for i in capi20 capiinfo capiinit capifax rcapid ; do
 cd $i
 rm -f lt* libto*
 rm -f missing
 aclocal
 libtoolize --force --automake --copy
 automake --add-missing --copy
 autoconf
 cd ..
done
for i in ant-phone avmb1 eicon isdnctrl isdnlog ipppd act2000 hisax icn pcbit; do
 cd $i
 autoconf
 cd ..
done
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fgnu89-inline"
make CFLAGS="$RPM_OPT_FLAGS  -fno-strict-aliasing -fgnu89-inline" LIBDIR=/usr/%_lib subconfig
cd capiinit
./configure --sbindir=/sbin --mandir=/usr/share/man --libdir=/usr/%_lib
cd ..
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fgnu89-inline -DUSE_INTERP_RESULT -DUSE_INTERP_ERRORLINE"
# build destination database with all available data
pushd isdnlog/tools/dest
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fgnu89-inline" alldata
popd
cd ant-phone 
./configure --prefix=/usr --mandir=/usr/share/man --libdir=/usr/%_lib
make
cd ..
#divactrl
cd ../divactrl_2.1
./configure --sbindir=/sbin --bindir=/usr/bin \
        --with-sbin=/sbin --mandir=/usr/share/man \
        --with-datas=/lib/firmware/isdn --libdir=/usr/%_lib
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fgnu89-inline"

%install
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,bin,share,include}
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/sbin/conf.d
mkdir -p $RPM_BUILD_ROOT/lib/firmware/isdn
mkdir -p $RPM_BUILD_ROOT/usr/lib/isdn
mkdir -p $RPM_BUILD_ROOT/etc/isdn
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/isdn/scripts
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/network/scripts
mkdir -p $RPM_BUILD_ROOT/etc/xinetd.d
mkdir -p $RPM_BUILD_ROOT/dev
touch isdnctrl_conf_timru
grep CONFIG_ISDNCTRL_ .config | \
while read line ; do
    case "$line" in
        CONFIG_ISDNCTRL_CONF=y)
            echo /usr/share/man/man8/.isdnctrl_conf.8.gz > isdnctrl_conf_timru
            ;;
        CONFIG_ISDNCTRL_TIMRU=y)
            echo /usr/share/man/man8/.isdnctrl_timru.8.gz > isdnctrl_conf_timru
            ;;
    esac
done
make DESTDIR=$RPM_BUILD_ROOT install INSTALL_PROGRAM='install -m 0755' \
     INSTALL_DATA='install -m 0644' INSTALL_MAN='install -m 0644' \
     INSTALL_DIR='install -m 0755 -d' INSTALL_SBIN='install -m 0755' \
     INSTALL_BIN='install -m 0755'
ls -l $RPM_BUILD_ROOT/usr/%_lib
cd ant-phone
make DESTDIR=$RPM_BUILD_ROOT install
cd ..
# hack for lib64 platforms
#if [ "%_lib" != "lib" ] ; then
#  mkdir -p $RPM_BUILD_ROOT/usr/%_lib
#  mv -v $RPM_BUILD_ROOT/usr/lib/lib* $RPM_BUILD_ROOT/usr/%_lib
#fi
# now we have libcapi20 needed for this :( ugly
export CFLAGS="$RPM_OPT_FLAGS"
pushd capiinfo
./configure --with-man=/usr/share/man --libdir=/usr/%_lib
make CFLAGS="$RPM_OPT_FLAGS"
make DESTDIR=$RPM_BUILD_ROOT install
popd
# we need the V2 libversion too
pushd capi20
make clean
make distclean
./configure --enable-V2 --libdir=/usr/%_lib
make CFLAGS="$RPM_OPT_FLAGS"
make DESTDIR=$RPM_BUILD_ROOT install
make clean
make distclean
./configure --libdir=/usr/%_lib
make CFLAGS="$RPM_OPT_FLAGS"
make DESTDIR=$RPM_BUILD_ROOT install
popd
# hack for lib64 platforms
#if [ "%_lib" != "lib" ] ; then
#  mkdir -p $RPM_BUILD_ROOT/usr/%_lib
#  mv -v $RPM_BUILD_ROOT/usr/lib/lib* $RPM_BUILD_ROOT/usr/%_lib
#fi
#divactrl 
cd ../divactrl_2.1
make DESTDIR=$RPM_BUILD_ROOT install-data
make DESTDIR=$RPM_BUILD_ROOT install-bin
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/divas
make DESTDIR=$RPM_BUILD_ROOT DATA_DIR=%{_defaultdocdir}/%{name}/divas install-extra
chmod a-x $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/divas/*
# i4l_suse.tar.bz2
cd ../i4l_suse
install -d $RPM_BUILD_ROOT%{_fillupdir}
install -m 755 %{S:9} $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.i4l-base
install -d $RPM_BUILD_ROOT/etc/xinetd.d
install -m 644 etc/xinetd.d/i4l-vbox $RPM_BUILD_ROOT/etc/xinetd.d
install -p -m 755 bin/isdnmon $RPM_BUILD_ROOT/usr/bin
install -p -m 755 bin/isdnmonp $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
cp -a doc/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
cp -a doc.isdnlog/* $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
# take newest docs from the kernel
# cp -a /usr/src/linux/Documentation/isdn/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
chmod -R og+r $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
cp -a etc/isdn/* $RPM_BUILD_ROOT/etc/isdn
chmod 755 $RPM_BUILD_ROOT/etc/isdn/stop
install -d $RPM_BUILD_ROOT/etc/ppp
install -d $RPM_BUILD_ROOT/etc/ppp/peers
cp -a etc/ppp/* $RPM_BUILD_ROOT/etc/ppp/
cp  etc/ppp/peers/capi-isdn $RPM_BUILD_ROOT/etc/ppp/peers/
cp  etc/ppp/peers/capi-adsl $RPM_BUILD_ROOT/etc/ppp/peers/
cp -p firm/* $RPM_BUILD_ROOT/lib/firmware/isdn
chmod a+r $RPM_BUILD_ROOT/lib/firmware/isdn/*
install -d $RPM_BUILD_ROOT/%{_datadir}/i4l-base/scripts
install -p -m 755 rc/isdn $RPM_BUILD_ROOT/%{_datadir}/i4l-base/scripts
install -d $RPM_BUILD_ROOT/%_unitdir
install -p -m 644 system/isdn.service $RPM_BUILD_ROOT/%_unitdir
install -p -m 755 etc/sysconfig/isdn/scripts/* $RPM_BUILD_ROOT/etc/sysconfig/isdn/scripts
install -p -m 755 etc/sysconfig/network/scripts/* $RPM_BUILD_ROOT/etc/sysconfig/network/scripts
######## /etc/logrotate.d ############
install -d $RPM_BUILD_ROOT/etc/logrotate.d
install -p -m 644 etc/logrotate.d/* $RPM_BUILD_ROOT/etc/logrotate.d
######## postprocess.isdn #############
install -p -m 755 %{S:8} $RPM_BUILD_ROOT/etc/sysconfig/isdn/scripts/postprocess.isdn
###### rc links ######
ln -sf /usr/sbin/service $RPM_BUILD_ROOT/usr/sbin/rcisdn
###### sysconfig links ######
ln -sf ifup-isdn $RPM_BUILD_ROOT/etc/sysconfig/network/scripts/ifdown-isdn
ln -sf ifup-isdn $RPM_BUILD_ROOT/etc/sysconfig/network/scripts/ifstatus-isdn
#################################
# special isdnlog to copy files for at,ch,nl ... too
cp ../isdn4k-utils/isdnlog/*.dat $RPM_BUILD_ROOT/usr/lib/isdn
cp ../isdn4k-utils/isdnlog/*.cdb $RPM_BUILD_ROOT/usr/lib/isdn
#################################
#########################################################
# extra docu nach %{_defaultdocdir}/%{name}
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/faq
cd ../isdn4k-utils/FAQ
cp -a _example $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/faq/example
cp -a _howto $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/howto
cp -a tutorial $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/
cd ../
#########################################################
# extra docu nach %{_defaultdocdir}/%{name}/*
### isdnlog
cp -p isdnlog/BUGS $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
cp -p isdnlog/FAQ $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
cp -p isdnlog/Isdn $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
cp -p isdnlog/NEWS $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
cp -p isdnlog/README $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
cp -p isdnlog/README.* $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog
cp -a isdnlog/contrib $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog/
pushd isdnlog/samples
for i in isdn.conf.* ; do
       sed -f ../../../i4l_suse/isdn.conf.sed ${i} >$RPM_BUILD_ROOT/etc/isdn/${i}
done
sed -f ../../../i4l_suse/isdn.conf.sed isdn.conf >$RPM_BUILD_ROOT/etc/isdn/isdn.conf.unknown
sed -f ../../../i4l_suse/isdn.conf.sed isdn.conf.de >$RPM_BUILD_ROOT/etc/isdn/isdn.conf
cp -a rate.conf* $RPM_BUILD_ROOT/etc/isdn/
popd
### ipppd
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/ipppd
cp -p ipppd/NOTES.IPPPD $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/ipppd
cp -p ipppd/README $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/ipppd
cp -p ipppd/README.RADIUS $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/ipppd
cp -p ipppd/README.linux.ORIG $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/ipppd
cp -p ipppd/README.mschap80.ORIG $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/ipppd
cp -p ipppd/TODO.4.MP $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/ipppd
### pcbit
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/pcbit
cp -p pcbit/README.pt $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/pcbit
### rcapid
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/capi4linux/rcapid
cp -p rcapid/README $RPM_BUILD_ROOT%{_defaultdocdir}/capi4linux/rcapid
### capi4linux
cp -p capi20/README $RPM_BUILD_ROOT%{_defaultdocdir}/capi4linux
### vbox
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-vbox/examples
cp -p vbox/README $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-vbox
cp -a vbox/examples/ $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-vbox
### vbox3
#install -d $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/i4l-vbox/vbox3
#cp -a vbox3/examples/ $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-vbox/vbox3
#cp -a vbox3/doc/ $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-vbox/vbox3
### areacode
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog/areacode
cp -p areacode/areacode.doc $RPM_BUILD_ROOT%{_defaultdocdir}/i4l-isdnlog/areacode/
### pppdcapiplugin
install -m 600 pppdcapiplugin/peers/t-dsl $RPM_BUILD_ROOT/etc/ppp/peers/t-dsl
if test "%_lib" = "lib64"; then
   mv %buildroot/usr/lib/pppd %buildroot/usr/lib64
fi
###########################################################
### some man pages are installed with wrong permissions ###
chmod 0644 $RPM_BUILD_ROOT/usr/share/man/*/*
###########################################################
### clean up some unneeded files                        ###
# part of fcdsl package
rm -rf $RPM_BUILD_ROOT/etc/drdsl
# not longer used by SL
rm -f $RPM_BUILD_ROOT/etc/isdn/isdnlog.isdnctrl0.options
rm -rf $RPM_BUILD_ROOT/usr/man
rm -rf $RPM_BUILD_ROOT/usr/X11R6/man
# udev/hotplug stuff
install -m644 -D %{S:4} $RPM_BUILD_ROOT/usr/lib/udev/rules.d/45-isdn.rules
install -m755 -D %{S:5} $RPM_BUILD_ROOT/usr/lib/udev/isdn.sh
mkdir -p  $RPM_BUILD_ROOT/usr/lib/tmpfiles.d
install -m644 %{S:7} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d
rm -f $RPM_BUILD_ROOT/dev/isdnctrl
rm -f "%buildroot/%_libdir"/*.la
%find_lang ant-phone

%pre -n i4l-base
%service_add_pre isdn.service

%post -p /bin/bash
%service_add_post isdn.service
# install/doinst.sh - to be done after extraction
#
#
# dank an werner für diesen code ;)))
#
if [ -f etc/SuSE-release ] ; then
  while read line ; do
    case "$line" in
        VERSION*) break ;;
        *)              ;;
    esac
  done < etc/SuSE-release
else
  # use 5.3 for anything older
  line="VERSION = 5.3"
fi
line=${line##*=}
major=${line%%.*}
minor=${line##*.}
#
# create missing legacy devices
systemd-tmpfiles --create /usr/lib/tmpfiles.d/i4l.conf 
#
# Move MODIFY_SECRETS from /etc/sysconfig/suseconfig
# to /etc/sysconfig/i4l-base
#
SC=/etc/sysconfig/suseconfig
FT=%{_fillupdir}/sysconfig.i4l-base
if test -f $SC; then
    fillup -i $SC $FT /etc/sysconfig/i4l-base
    fillup -r $SC $FT $SC
    mv $SC.new $SC
fi

%fillup_only

%set_permissions /sbin/isdnctrl
exit 0

%post -n i4l-vbox
%set_permissions /usr/bin/vboxbeep

%post -n libcapi20-2 -p /sbin/ldconfig

%post -n libcapi20-3 -p /sbin/ldconfig

%post -n capi4linux -p /sbin/ldconfig

%preun
%service_del_preun isdn.service
%stop_on_removal isdn

%postun -n libcapi20-2 -p /sbin/ldconfig

%postun -n libcapi20-3 -p /sbin/ldconfig

%postun -n capi4linux -p /sbin/ldconfig

%postun -n i4l-base
%service_del_postun isdn.service

%verifyscript
%verify_permissions -e /sbin/isdnctrl

%verifyscript -n i4l-vbox
%verify_permissions -e /usr/bin/vboxbeep

%files -f isdnctrl_conf_timru
%defattr(-,root,root)
%{_fillupdir}/sysconfig.i4l-base
### /etc/isdn 
%dir /etc/isdn
### /etc/ppp
%config /etc/ppp/auth-down
%config /etc/ppp/auth-up
%config /etc/ppp/ioptions
### /sbin
/sbin/actctrl
/sbin/divactrl
#/sbin/divaload
#/sbin/eiconctrl
/sbin/hisaxctrl
/sbin/icnctrl
/sbin/pcbitctl
### /usr/sbin
#/usr/sbin/divalog
#/usr/sbin/divalogd
/usr/sbin/divertctrl
/usr/sbin/imon
/usr/sbin/imontty
/usr/sbin/ipppd
/usr/sbin/ipppstats
/usr/sbin/iprofd
%verify(not mode) %attr(4750,root,dialout)/sbin/isdnctrl
/usr/sbin/loopctrl
/usr/sbin/rcisdn
### /usr/bin
/usr/bin/isdnmon
/usr/bin/isdnmonp
/usr/bin/xisdnload
/usr/bin/xmonisdn
### /lib/firmware/isdn
%dir /lib/firmware/isdn
/lib/firmware/isdn/ISAR.BIN
### udev devices
%if 0%{?suse_version} < 1230
%dir /usr/lib/udev
%dir /usr/lib/udev/rules.d
%endif
/usr/lib/udev/rules.d/45-isdn.rules
/usr/lib/udev/isdn.sh
/usr/lib/tmpfiles.d/i4l.conf
### init scripts
%{_datadir}/i4l-base
%{_datadir}/i4l-base/scripts
%{_datadir}/i4l-base/scripts/isdn
%_unitdir/isdn.service
### sysconfig ###
%dir /etc/sysconfig/isdn
%dir /etc/sysconfig/isdn/scripts
/etc/sysconfig/isdn/scripts/*
/etc/sysconfig/network/scripts/*
### postprocess ###
/etc/sysconfig/isdn/scripts/postprocess.isdn
### for x11
%{_xorg7_prefix}/include/X11/bitmaps/netactive
%{_xorg7_prefix}/include/X11/bitmaps/netactiveout
%{_xorg7_prefix}/include/X11/bitmaps/netinactive
%{_xorg7_prefix}/include/X11/bitmaps/netstart
%{_xorg7_prefix}/include/X11/bitmaps/netstop
%{_xorg7_prefix}/include/X11/bitmaps/netwaiting
%config %{_xorg7_app}/X11/app-defaults/XISDNLoad
### man pages
%doc /usr/share/man/man1/xisdnload.1x.gz
%doc /usr/share/man/man1/xmonisdn.1x.gz
%doc /usr/share/man/man4/isdn_audio.4.gz
%doc /usr/share/man/man4/isdnctrl.4.gz
%doc /usr/share/man/man4/isdninfo.4.gz
%doc /usr/share/man/man4/ttyI.4.gz
%doc /usr/share/man/man7/isdn_cause.7.gz
%doc /usr/share/man/man8/actctrl.8.gz
%doc /usr/share/man/man8/divertctrl.8.gz
%doc /usr/share/man/man8/hisaxctrl.8.gz
%doc /usr/share/man/man8/icnctrl.8.gz
%doc /usr/share/man/man8/imon.8.gz
%doc /usr/share/man/man8/imontty.8.gz
%doc /usr/share/man/man8/ipppd.8.gz
%doc /usr/share/man/man8/ipppstats.8.gz
%doc /usr/share/man/man8/iprofd.8.gz
%doc /usr/share/man/man8/isdnctrl.8.gz
%doc /usr/share/man/man8/loopctrl.8.gz
%doc /usr/share/man/man8/pcbitctl.8.gz
%doc %{_defaultdocdir}/%{name}

%files -n i4l-isdnlog
%defattr(-,root,root)
### /etc/isdn
%dir /etc/isdn
%config(noreplace) /etc/isdn/callerid.conf
%config            /etc/isdn/isdn.conf
%config            /etc/isdn/isdn.conf.*
%config            /etc/isdn/stop
%config(noreplace) /etc/isdn/isdnlog.options.templ
%config            /etc/isdn/rate.conf*
%config(noreplace) /etc/isdn/isdnlog.users
%config(noreplace) /etc/logrotate.d/i4l-isdnlog
### /usr/sbin
/usr/sbin/isdnlog
/usr/sbin/mkzonedb
### /usr/bin
/usr/bin/isdnconf
/usr/bin/isdnrate
/usr/bin/isdnrep
/usr/bin/isdnbill
### /usr/lib
%dir /usr/lib/isdn/
/usr/lib/isdn/*.dat
/usr/lib/isdn/*.cdb
### man pages
%doc /usr/share/man/man1/isdnbill.1.gz
%doc /usr/share/man/man1/isdnconf.1.gz
%doc /usr/share/man/man1/isdnrate.1.gz
%doc /usr/share/man/man1/isdnrep.1.gz
%doc /usr/share/man/man5/callerid.conf.5.gz
%doc /usr/share/man/man5/isdnlog.5.gz
%doc /usr/share/man/man5/isdnlog.users.5.gz
%doc /usr/share/man/man8/isdnlog.8.gz
%doc /usr/share/man/man5/isdnformat.5.gz
%doc /usr/share/man/man5/rate.conf.5.gz
%doc /usr/share/man/man5/rate-files.5.gz
%doc /usr/share/man/man5/isdn.conf.5.gz
%doc /usr/share/man/man8/mkzonedb.8.gz
%doc %{_defaultdocdir}/i4l-isdnlog

%files -n libcapi20-2
%defattr(-,root,root)
%_libdir/libcapi20.so.2*

%files -n libcapi20-3
%defattr(-,root,root)
%_libdir/libcapi20.so.3*

%files -n capi4linux
%defattr(-,root,root)
### /etc/ppp
%dir /etc/ppp/peers
%dir /etc/ppp/peers/isdn
%config /etc/ppp/peers/isdn/*
%config /etc/ppp/peers/t-dsl
%config /etc/ppp/peers/capi-isdn
%config /etc/ppp/peers/capi-adsl
### /sbin
/sbin/avmcapictrl
/sbin/capiinit
### /usr/sbin
/usr/sbin/rcapid
### /usr/bin
/usr/bin/capiinfo
/usr/bin/capifax
/usr/bin/capifaxrcvd
### /usr/lib
%_libdir/capi/
%_libdir/pppd/%ppp_version_short/capiplugin.so
### /lib/firmware/isdn
%dir /lib/firmware/isdn
/lib/firmware/isdn/*.frm
### doc
%doc /usr/share/man/man8/avmcapictrl.8.gz
%doc /usr/share/man/man8/capiinfo.8.gz
%doc /usr/share/man/man8/capiplugin.8.gz
%doc %{_defaultdocdir}/capi4linux

%files -n ppp-userpass
%defattr(-,root,root)
%_libdir/pppd/%ppp_version_short/userpass.so

%files -n capi4linux-devel
%defattr(-,root,root)
### /usr/include
/usr/include/capi20.h
/usr/include/capicmd.h
/usr/include/capiutils.h
/usr/include/capi_debug.h
/usr/include/capi_mod.h
/usr/%_lib/libcapi20.so
/usr/%_lib/libcapi20.a
/usr/%_lib/libcapi20dyn.a
/usr/%_lib/pkgconfig/capi20.pc

%files -n i4l-vbox
%defattr(-,root,root)
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) /etc/xinetd.d/i4l-vbox
### /usr/bin
/usr/bin/autovbox
/usr/bin/rmdtovbox
/usr/bin/vbox
%verify(not mode) %attr(0755,root,trusted) /usr/bin/vboxbeep
/usr/bin/vboxcnvt
/usr/bin/vboxctrl
/usr/bin/vboxmail
/usr/bin/vboxmode
/usr/bin/vboxplay
/usr/bin/vboxtoau
### /usr/sbin
/usr/sbin/vboxd
/usr/sbin/vboxgetty
/usr/sbin/vboxputty
### config
%dir /etc/vbox
%config(noreplace) /etc/vbox/vboxd.conf
%config(noreplace) /etc/vbox/vboxgetty.conf
%config(noreplace) /etc/logrotate.d/i4l-vbox
%dir /var/spool/vbox
%dir /var/log/vbox
# manual
%doc /usr/share/man/man1/autovbox.1.gz
%doc /usr/share/man/man1/rmdtovbox.1.gz
%doc /usr/share/man/man1/vboxbeep.1.gz
%doc /usr/share/man/man1/vboxconvert.1.gz
%doc /usr/share/man/man1/vboxctrl.1.gz
%doc /usr/share/man/man1/vboxmode.1.gz
%doc /usr/share/man/man1/vboxplay.1.gz
%doc /usr/share/man/man1/vboxtoau.1.gz
%doc /usr/share/man/man1/vbox.1.gz
%doc /usr/share/man/man5/vbox_file.5.gz
%doc /usr/share/man/man5/vbox.conf.5.gz
%doc /usr/share/man/man5/vboxd.conf.5.gz
%doc /usr/share/man/man5/vboxgetty.conf.5.gz
%doc /usr/share/man/man5/vboxrc.5.gz
%doc /usr/share/man/man5/vboxtcl.5.gz
%doc /usr/share/man/man8/vboxd.8.gz
%doc /usr/share/man/man8/vboxgetty.8.gz
%doc /usr/share/man/man8/vboxputty.8.gz
%doc /usr/share/man/man8/vboxmail.8.gz
### /usr/share/doc/packages/*
%doc %{_defaultdocdir}/i4l-vbox

%files -n ant-phone -f ant-phone.lang
%defattr(-,root,root)
/usr/bin/ant-phone
%doc /usr/share/man/man1/ant-phone.1.gz

%files -n i4lfirm
%defattr(-,root,root)
%dir /lib/firmware/isdn
/lib/firmware/isdn/*.t4
/lib/firmware/isdn/*.bin
/lib/firmware/isdn/*.bit
/lib/firmware/isdn/bip1120.btl
/lib/firmware/isdn/te*.p*
/lib/firmware/isdn/te*.s*
/lib/firmware/isdn/te*.qm*

%changelog
