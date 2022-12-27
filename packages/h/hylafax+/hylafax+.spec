#
# spec file for package hylafax+
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


%global faxspool    %{_localstatedir}/spool/hylafax
%define lib_version %(echo %{version} | tr \. _)
Name:           hylafax+
Version:        7.0.6
Release:        0
Summary:        A fax server
License:        BSD-3-Clause
Group:          Productivity/Telephony/Servers
URL:            https://hylafax.sourceforge.io
Source0:        https://prdownloads.sourceforge.net/hylafax/hylafax-%{version}.tar.gz
Source4:        hylafax-hfaxd.service
Source5:        hylafax-faxq.service
Source6:        hylafax-faxgetty@.service
Source7:        hylafax.target
Source8:        README.openSUSE
Source9:        sendonly.conf
# systemd-timer
Source10:       hylafax-usage.timer
Source11:       hylafax-usage.service
Source12:       hylafax-faxqclean.timer
Source13:       hylafax-faxqclean.service
Source14:       hylafax-faxmodem@.service
Source15:       hylafax-service.xml
Source16:       hylafax-helper.xml

BuildRequires:  firewalld
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libjbig-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
# needed together with devel for proper configure detection
BuildRequires:  tiff
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Requires:       gawk
Requires:       ghostscript
Requires:       ghostscript-fonts
# Server checks for existence of sendfax
Requires:       hylafax+-client
Requires:       mailx
Requires:       sharutils
Requires:       tiff
Conflicts:      hylafax < 30.0.0
Conflicts:      mgetty-sendfax
Provides:       hylafax = 30.0.0
%{?systemd_requires}
%if 0%{?suse_version} >= 1500
Requires(pre):  group(uucp)
Requires(pre):  user(uucp)
%else
Requires(pre):  aaa_base
%endif

%description
HylaFAX is a fax server supporting Class 1 and 2 fax modems on UNIX
systems. It provides spooling services and numerous supporting fax
management tools. The fax clients may reside on machines different
from the server, and client implementations exist for a number of
platforms, including Windows.

%package -n libfaxutil%{lib_version}
Summary:        Runtime library needed by both fax server and client
Group:          System/Libraries

%description -n libfaxutil%{lib_version}
This runtime lib is needed by both the fax server and the client.

%package client
Summary:        Client package for the Hylafax server
Group:          Hardware/Fax
Conflicts:      hylafax-client < 30.0.0
Conflicts:      sendfax
Provides:       hylafax-client = 30.0.0

%description client
This is client part of the Hylafax fax server. If the Hylafax fax
server is already running on another machine, this package can be
used to access the server.

%prep
%setup -q -n hylafax-%{version}

cp %{SOURCE8} .
cp %{SOURCE9} .

%build
# - Can't use the configure macro because HylaFAX configure script does
#   not understand the config options used by that macro
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" \
STRIP=':' \
./configure \
        --with-DIR_BIN=%{_bindir} \
        --with-DIR_SBIN=%{_sbindir} \
        --with-DIR_LIB=%{_libdir} \
        --with-DIR_LIBEXEC=%{_sbindir} \
        --with-DIR_LIBDATA=%{_sysconfdir}/hylafax \
        --with-DIR_LOCKS=%{_localstatedir}/lock \
        --with-LIBDIR=%{_libdir} \
        --with-TIFFBIN=%{_bindir} \
        --with-DIR_MAN=%{_mandir} \
        --with-PATH_GSRIP=%{_bindir}/gs \
        --with-TIFFINC=-L%{_includedir} \
        --with-LIBTIFF="-ltiff" \
        --with-DIR_SPOOL=%{faxspool} \
        --with-AFM=no \
        --with-AWK=%{_bindir}/gawk \
        --with-PATH_VGETTY=/sbin/vgetty \
        --with-PATH_GETTY=/sbin/mgetty \
        --with-PAGESIZE=A4 \
        --with-PATH_DPSRIP=%{faxspool}/bin/ps2fax \
        --with-PATH_IMPRIP="" \
        --with-SYSVINIT=%{_initddir}/hylafax+ \
        --with-INTERACTIVE=no \
        --with-JBIGTIFF=yes
# can't use _smp_mflags because it breaks libfaxutil dso building
make -j1

%install
# install: make some dirs...
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/hylafax
mkdir -p -m 755 %{buildroot}%{_unitdir}
mkdir -p -m 755 %{buildroot}%{_initddir}
mkdir -p -m 755 %{buildroot}%{_bindir}
mkdir -p -m 755 %{buildroot}%{_sbindir}
mkdir -p -m 755 %{buildroot}%{_libdir}
mkdir -p -m 755 %{buildroot}%{_mandir}
mkdir -p -m 755 %{buildroot}%{faxspool}/config

# install: binaries and man pages
# FAXUSER, FAXGROUP, SYSUSER and SYSGROUP are set to the current user to
# avoid warnings about chown/chgrp if the user building the SRPM is not root;
# they are set to the correct values with the RPM attr macro
make install -e \
        FAXUSER=`id -u` \
        FAXGROUP=`id -g` \
        SYSUSER=`id -u` \
        SYSGROUP=`id -g` \
        BIN=%{buildroot}%{_bindir} \
        SBIN=%{buildroot}%{_sbindir} \
        LIBDIR=%{buildroot}%{_libdir} \
        LIBDATA=%{buildroot}%{_sysconfdir}/hylafax \
        LIBEXEC=%{buildroot}%{_sbindir} \
        SPOOL=%{buildroot}%{faxspool} \
        MAN=%{buildroot}%{_mandir} \
        INSTALL_ROOT=%{buildroot}

install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/hylafax-hfaxd.service
install -p -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/hylafax-faxq.service
install -p -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/hylafax-faxgetty@.service
install -p -m 644 %{SOURCE7} %{buildroot}%{_unitdir}/hylafax.target
install -D -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/hylafax-usage.timer
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/hylafax-usage.service
install -D -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/hylafax-faxqclean.timer
install -D -m 0644 %{SOURCE13} %{buildroot}%{_unitdir}/hylafax-faxqclean.service
install -D -m 0644 %{SOURCE14} %{buildroot}%{_unitdir}/hylafax-faxmodem@.service
install -D -m 0644 %{SOURCE15} %{buildroot}%{_prefix}/lib/firewalld/services/hylafax.xml
install -D -m 0644 %{SOURCE16} %{buildroot}%{_prefix}/lib/firewalld/helpers/hylafax.xml

for lnk in hylafax-hfaxd hylafax-faxq; do
    ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc$lnk
done
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rchylafax

# not being executable is rather unconvenient
chmod +x %{buildroot}%{_sbindir}/edit-faxcover

# Prepare docdir by removing non-doc files
# Remove files that are not needed on Linux
rm -f %{buildroot}%{_sbindir}/{faxsetup.irix,faxsetup.bsdi}
rm -f %{buildroot}%{faxspool}/bin/{ps2fax.imp,ps2fax.dps}

rm -f %{buildroot}%{faxspool}/COPYRIGHT

%pre
%service_add_pre hylafax-faxq.service hylafax-hfaxd.service hylafax-usage.service hylafax-faxqclean.service hylafax-usage.timer hylafax-faxqclean.timer hylafax.target hylafax-faxgetty@.service hylafax-faxmodem@.service

%post
/sbin/ldconfig
%service_add_post hylafax-faxq.service hylafax-hfaxd.service hylafax-usage.service hylafax-faxqclean.service hylafax-usage.timer hylafax-faxqclean.timer hylafax.target hylafax-faxgetty@.service hylafax-faxmodem@.service

%preun
%service_del_preun hylafax-faxq.service hylafax-hfaxd.service hylafax-usage.service hylafax-faxqclean.service hylafax-usage.timer hylafax-faxqclean.timer hylafax.target hylafax-faxgetty@.service hylafax-faxmodem@.service

%postun
/sbin/ldconfig
%service_del_postun hylafax-faxq.service hylafax-hfaxd.service hylafax-usage.service hylafax-faxqclean.service hylafax-usage.timer hylafax-faxqclean.timer hylafax.target hylafax-faxgetty@.service hylafax-faxmodem@.service

%post -n libfaxutil%{lib_version} -p /sbin/ldconfig
%postun -n libfaxutil%{lib_version} -p /sbin/ldconfig

%files
%{_unitdir}/hylafax-hfaxd.service
%{_unitdir}/hylafax-faxq.service
%{_unitdir}/hylafax-faxgetty@.service
%{_unitdir}/hylafax.target
%{_unitdir}/hylafax-usage.timer
%{_unitdir}/hylafax-usage.service
%{_unitdir}/hylafax-faxqclean.timer
%{_unitdir}/hylafax-faxmodem@.service
%{_unitdir}/hylafax-faxqclean.service
%{_prefix}/lib/firewalld/services/hylafax.xml
%{_prefix}/lib/firewalld/helpers/hylafax.xml
%{_sbindir}/rchylafax-faxq
%{_sbindir}/rchylafax-hfaxd
%{_sbindir}/rchylafax
%defattr(-,root,root)
%doc CHANGES CONTRIBUTORS COPYRIGHT README TODO VERSION README.openSUSE sendonly.conf
%exclude %{_libdir}/libfaxutil*
%{_libdir}/libfax*
%{_mandir}/man5/hylafax-config.5f%{ext_man}
%{_mandir}/man5/doneq.5f%{ext_man}
%{_mandir}/man5/dialrules.5f%{ext_man}
%{_mandir}/man5/hosts.hfaxd.5f%{ext_man}
%{_mandir}/man5/hylafax-server.5f%{ext_man}
%{_mandir}/man5/hylafax-info.5f%{ext_man}
%{_mandir}/man5/hylafax-log.5f%{ext_man}
%{_mandir}/man5/pagermap.5f%{ext_man}
%{_mandir}/man5/pagesizes.5f%{ext_man}
%{_mandir}/man5/recvq.5f%{ext_man}
%{_mandir}/man5/sendq.5f%{ext_man}
%{_mandir}/man5/hylafax-shutdown.5f%{ext_man}
%{_mandir}/man5/status.5f%{ext_man}
%{_mandir}/man5/tsi.5f%{ext_man}
%{_mandir}/man5/typerules.5f%{ext_man}
%{_mandir}/man5/xferfaxlog.5f%{ext_man}
%{_mandir}/man8/choptest.8c%{ext_man}
%{_mandir}/man8/cqtest.8c%{ext_man}
%{_mandir}/man8/dialtest.8c%{ext_man}
%{_mandir}/man8/faxabort.8c%{ext_man}
%{_mandir}/man8/faxaddmodem.8c%{ext_man}
%{_mandir}/man8/faxadduser.8c%{ext_man}
%{_mandir}/man8/faxanswer.8c%{ext_man}
%{_mandir}/man8/faxconfig.8c%{ext_man}
%{_mandir}/man8/faxcron.8c%{ext_man}
%{_mandir}/man8/faxdeluser.8c%{ext_man}
%{_mandir}/man8/faxgetty.8c%{ext_man}
%{_mandir}/man8/faxinfo.8c%{ext_man}
%{_mandir}/man8/faxlock.8c%{ext_man}
%{_mandir}/man8/faxmodem.8c%{ext_man}
%{_mandir}/man8/faxq.8c%{ext_man}
%{_mandir}/man8/faxqclean.8c%{ext_man}
%{_mandir}/man8/faxquit.8c%{ext_man}
%{_mandir}/man8/faxrcvd.8c%{ext_man}
%{_mandir}/man8/faxsend.8c%{ext_man}
%{_mandir}/man8/faxsetup.8c%{ext_man}
%{_mandir}/man8/faxstate.8c%{ext_man}
%{_mandir}/man8/faxwatch.8c%{ext_man}
%{_mandir}/man8/hfaxd.8c%{ext_man}
%{_mandir}/man8/jobcontrol.8c%{ext_man}
%{_mandir}/man8/mkcover.8c%{ext_man}
%{_mandir}/man8/notify.8c%{ext_man}
%{_mandir}/man8/pagesend.8c%{ext_man}
%{_mandir}/man8/pollrcvd.8c%{ext_man}
%{_mandir}/man8/pdf2fax.8c%{ext_man}
%{_mandir}/man8/ps2fax.8c%{ext_man}
%{_mandir}/man8/recvstats.8c%{ext_man}
%{_mandir}/man8/tagtest.8c%{ext_man}
%{_mandir}/man8/tiff2fax.8c%{ext_man}
%{_mandir}/man8/tiffcheck.8c%{ext_man}
%{_mandir}/man8/tsitest.8c%{ext_man}
%{_mandir}/man8/wedged.8c%{ext_man}
%{_mandir}/man8/xferfaxstats.8c%{ext_man}
%{_mandir}/man8/faxfetch.8c%{ext_man}
%{_mandir}/man8/faxmsg.8c%{ext_man}
%{_mandir}/man8/faxsetup.linux.8c%{ext_man}
%{_mandir}/man8/hylafax.8c%{ext_man}
%{_mandir}/man8/lockname.8c%{ext_man}
%{_mandir}/man8/ondelay.8c%{ext_man}
%{_mandir}/man8/probemodem.8c%{ext_man}
%{_mandir}/man8/typetest.8c%{ext_man}
%{faxspool}/config/*
%{faxspool}/bin/dict/*
%{faxspool}/bin/genfontmap.ps
%{faxspool}/bin/auto-rotate.ps
%{faxspool}%{_sysconfdir}/dpsprinter.ps
%{faxspool}%{_sysconfdir}/cover.templ
%{faxspool}%{_sysconfdir}/lutRS18.pcf
%{faxspool}%{_sysconfdir}/LiberationSans-25.pcf
%config(noreplace) %{faxspool}%{_sysconfdir}/dialrules*
%defattr(755,root,root,-)
%dir %{_sysconfdir}/hylafax
%dir %{_sysconfdir}/hylafax/faxmail
%dir %{_sysconfdir}/hylafax/faxmail/application
%dir %{_sysconfdir}/hylafax/faxmail/image
%dir %{faxspool}/bin
%dir %{faxspool}%{_sysconfdir}
%dir %{faxspool}/config
%dir %{faxspool}/bin/dict
%config(noreplace) %{_sysconfdir}/hylafax/hfaxd.conf
%{_sbindir}/choptest
%{_sbindir}/cqtest
%{_sbindir}/dialtest
%{_sbindir}/faxabort
%{_sbindir}/faxaddmodem
%{_sbindir}/faxadduser
%{_sbindir}/faxanswer
%{_sbindir}/faxconfig
%{_sbindir}/faxcron
%{_sbindir}/faxdeluser
%{_sbindir}/faxinfo
%{_sbindir}/faxlock
%{_sbindir}/faxmodem
%{_sbindir}/faxmsg
%{_sbindir}/faxq
%{_sbindir}/faxqclean
%{_sbindir}/faxquit
%{_sbindir}/faxsetup
%{_sbindir}/faxsetup.linux
%{_sbindir}/faxstate
%{_sbindir}/faxwatch
%{_sbindir}/probemodem
%{_sbindir}/recvstats
%{_sbindir}/tagtest
%{_sbindir}/tiffcheck
%{_sbindir}/tsitest
%{_sbindir}/typetest
%{_sbindir}/xferfaxstats
%{_sbindir}/faxfetch
%{_sbindir}/faxgetty
%{_sbindir}/faxsend
%{_sbindir}/hfaxd
%{_sbindir}/hylafax
%{_sbindir}/lockname
%{_sbindir}/ondelay
%{_sbindir}/pagesend
%{faxspool}/bin/archive
%{faxspool}/bin/common-functions
%{faxspool}/bin/dictionary
%{faxspool}/bin/faxrcvd
%{faxspool}/bin/mkcover
%{faxspool}/bin/notify
%{faxspool}/bin/pcl2fax
%{faxspool}/bin/pdf2fax.gs
%{faxspool}/bin/pollrcvd
%{faxspool}/bin/ps2fax.gs
%{faxspool}/bin/qp-encode.awk
%{faxspool}/bin/rfc2047-encode.awk
%{faxspool}/bin/tiff2fax
%{faxspool}/bin/tiff2pdf
%{faxspool}/bin/wedged
%{_sysconfdir}/hylafax/faxmail/application/pdf
%{_sysconfdir}/hylafax/faxmail/application/octet-stream
%{_sysconfdir}/hylafax/faxmail/application/binary
%{_sysconfdir}/hylafax/faxmail/image/tiff
%defattr(-,uucp,uucp,-)
%dir %{faxspool}
%dir %{faxspool}/client
%dir %{faxspool}/info
%dir %{faxspool}/log
%dir %{faxspool}/recvq
%dir %{faxspool}/status
%dir %{faxspool}/config
%dir %{faxspool}/dev
%config(noreplace) %{faxspool}%{_sysconfdir}/xferfaxlog
%defattr(700,uucp,uucp)
%dir %{faxspool}/docq
%dir %{faxspool}/doneq
%dir %{faxspool}/archive
%dir %{faxspool}/sendq
%dir %{faxspool}/tmp
%dir %{faxspool}/pollq
%defattr(600,uucp,uucp,-)
%config(noreplace) %{faxspool}%{_sysconfdir}/hosts.hfaxd

%files -n libfaxutil%{lib_version}
%defattr(-,root,root,-)
%{_libdir}/libfaxutil*

%files client
%config(noreplace) %{_sysconfdir}/hylafax/faxcover.ps
%config(noreplace) %{_sysconfdir}/hylafax/faxmail.ps
%config(noreplace) %{_sysconfdir}/hylafax/pagesizes
%config(noreplace) %{_sysconfdir}/hylafax/typerules
%{_bindir}/faxalter
%{_bindir}/faxcover
%{_bindir}/faxmail
%{_bindir}/faxrm
%{_bindir}/faxstat
%{_bindir}/sendfax
%{_bindir}/sendpage
%{_sbindir}/edit-faxcover
%{_sbindir}/textfmt
%{_mandir}/man1/edit-faxcover.1%{?ext_man}
%{_mandir}/man1/faxalter.1%{?ext_man}
%{_mandir}/man1/faxcover.1%{?ext_man}
%{_mandir}/man1/faxmail.1%{?ext_man}
%{_mandir}/man1/faxrm.1%{?ext_man}
%{_mandir}/man1/faxstat.1%{?ext_man}
%{_mandir}/man1/hylafax-client.1%{?ext_man}
%{_mandir}/man1/sendfax.1%{?ext_man}
%{_mandir}/man1/sendpage.1%{?ext_man}
%{_mandir}/man1/sgi2fax.1%{?ext_man}
%{_mandir}/man1/textfmt.1%{?ext_man}

%changelog
