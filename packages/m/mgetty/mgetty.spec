#
# spec file for package mgetty
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


Name:           mgetty
Version:        1.2.1
Release:        0
Summary:        Mgetty Listens for Data, Fax, or Voice Calls on a Serial Line
License:        GPL-2.0-or-later
Group:          Hardware/Fax
URL:            http://mgetty.greenie.net/
Source0:        ftp://mgetty.greenie.net/pub/mgetty/source/1.2/mgetty-%{version}.tar.gz
Source2:        logrotate
Source3:        mgetty@.service
Source4:        vgetty@.service
Patch0:         mgetty-1.1.37-makefile.patch
Patch1:         mgetty-1.1.36-local.patch
Patch2:         mgetty-1.1.36-tempfile.patch
Patch3:         mgetty-1.1.37-callback.patch
Patch4:         mgetty-1.1.36-specialdigits.patch
Patch5:         mgetty-1.1.36-implicit-fortify-decl.patch
Patch6:         mgetty-1.1.36-no-date-time.patch
Patch7:         bug646280.patch
Patch8:         fixpie.patch
Patch9:         lp64.patch
Patch10:        mgetty-1.1.36-fix-bashisms.patch
Patch12:        mgetty-noroot.patch
Patch13:        mgetty-mkdir-p.patch
Patch14:        mgetty-fix-errlist.patch
Patch15:        faxq-libexec.patch
BuildRequires:  groff
BuildRequires:  makeinfo
BuildRequires:  netpbm
BuildRequires:  systemd-rpm-macros
Requires:       g3utils
Requires(post): %{install_info_prereq}
Requires(postun):%{install_info_prereq}
Recommends:     logrotate
%systemd_requires

%description
This package turns your computer into a fax machine. With some voice
modems (Zyxel, Rockwell, and USR), you can even use your computer as an
answering machine.

Mgetty recognizes what kind of call it is receiving and does everything
else automatically. It is able to accept data (login/PPP), fax, and
(depending on your modem) voice calls. Find the documentation in
%{_docdir}/mgetty and TeX Info files in %{_datadir}/info.

The configuration files are in %{_sysconfdir}/mgetty+sendfax.

%package -n sendfax
Summary:        A Tool for Sending Fax Documents
Group:          Hardware/Fax
Requires:       g3utils
Requires:       mgetty
Requires(pre):  group(uucp)
Requires(pre):  permissions
Requires(pre):  shadow
Conflicts:      hylafax
Provides:       fax_daemon

%description -n sendfax
The sendfax part of mgetty. You can use it instead of hylafax for
sending faxes. The sources are included in the mgetty source package.

%package -n g3utils
Summary:        Tools for the G3 (Fax) Graphics Format
Group:          Productivity/Graphics/Convertors

%description -n g3utils
These utilities convert graphics files from the G3 format into the
general- purpose PBM format and back, so you can print or manipulate
them. G3 is used by fax modems and machines.

The g3utils are included in the mgetty source package.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1
%patch4
%patch5
%patch6
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
chmod +x mkidirs

%build
ln -s policy.h-dist policy.h
%make_build -j1 CFLAGS="%{optflags} -fPIE -DAUTO_PPP" LDFLAGS="-pie" CC="gcc"
%make_build -j1 -C voice CFLAGS="%{optflags} -fPIE -DAUTO_PPP" LDFLAGS="-pie" CC="gcc"

%install
%make_install
install samples/new_fax.mail %{buildroot}%{_sysconfdir}/mgetty+sendfax/new_fax
ln -sf ../../..%{_sysconfdir}/mgetty+sendfax/new_fax %{buildroot}%{_prefix}/lib/mgetty+sendfax/
make install -C voice DESTDIR=%{buildroot}
install -m 644 voice/voice.conf-dist %{buildroot}%{_sysconfdir}/mgetty+sendfax/voice.conf
mkdir -p %{buildroot}%{_localstatedir}/spool/voice/{incoming,messages} %{buildroot}%{_docdir}/mgetty/voice
install -m 644 [BFRT]* doc/ttyS-cua.txt %{buildroot}%{_docdir}/mgetty/
install -m 644 voice/[ART]* voice/doc/* %{buildroot}%{_docdir}/mgetty/voice/
mkdir -p %{buildroot}%{_docdir}/mgetty/samples
for name in samples/*; do if test ! -d $name; then install -m644 $name %{buildroot}%{_docdir}/mgetty/samples; fi; done
mkdir -p %{buildroot}%{_docdir}/mgetty/samples/new_fax.all
install -m 644 samples/new_fax.all/* %{buildroot}%{_docdir}/mgetty/samples/new_fax.all/
cd voice && cp -R scripts %{buildroot}%{_docdir}/mgetty/voice/
chmod 644 %{buildroot}%{_docdir}/mgetty/voice/scripts/*
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/mgetty
install -D -m 0644  %{SOURCE3} %{buildroot}/%{_unitdir}/mgetty@.service
install -D -m 0644  %{SOURCE4} %{buildroot}/%{_unitdir}/vgetty@.service

%pre -n sendfax
%{_sbindir}/useradd -r -o -g uucp -u 33 -s /bin/bash -c "Facsimile agent" -d %{_localstatedir}/spool/fax fax 2> /dev/null || :
/bin/touch %{_localstatedir}/log/sendfax.log
chown fax:uucp %{_localstatedir}/log/sendfax.log
chmod 664 %{_localstatedir}/log/sendfax.log

%post -n sendfax
%set_permissions  %{_localstatedir}/spool/fax/outgoing %{_libexecdir}/mgetty+sendfax/faxq-helper

%verifyscript -n sendfax
%verify_permissions -e %{_localstatedir}/spool/fax/outgoing -e %{_libexecdir}/mgetty+sendfax/faxq-helper

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%dir %{_sysconfdir}/mgetty+sendfax
%doc %{_docdir}/mgetty
%dir %{_localstatedir}/spool/voice
%dir %{_localstatedir}/spool/voice/incoming
%dir %{_localstatedir}/spool/voice/messages
%{_unitdir}/mgetty@.service
%{_unitdir}/vgetty@.service
%config(noreplace) %{_sysconfdir}/logrotate.d/mgetty
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/dialin.config
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/login.config
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/mgetty.config
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/voice.conf
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/callback.config
%{_bindir}/autopvf
%{_bindir}/basictopvf
%{_bindir}/lintopvf
%{_bindir}/newslock
%{_bindir}/pvfamp
%{_bindir}/pvfcut
%{_bindir}/pvfecho
%{_bindir}/pvffft
%{_bindir}/pvffile
%{_bindir}/pvffilter
%{_bindir}/pvfmix
%{_bindir}/pvfnoise
%{_bindir}/pvfreverse
%{_bindir}/pvfsine
%{_bindir}/pvfspeed
%{_bindir}/pvftoau
%{_bindir}/pvftobasic
%{_bindir}/pvftolin
%{_bindir}/pvftormd
%{_bindir}/pvftovoc
%{_bindir}/pvftowav
%{_bindir}/rmdfile
%{_bindir}/rmdtopvf
%{_bindir}/sff2g3
%{_bindir}/vm
%{_bindir}/voctopvf
%{_bindir}/wavtopvf
%{_infodir}/mgetty.info*%{ext_info}
%{_mandir}/man1/autopvf.1%{?ext_man}
%{_mandir}/man1/basictopvf.1%{?ext_man}
%{_mandir}/man1/lintopvf.1%{?ext_man}
%{_mandir}/man1/pvf.1%{?ext_man}
%{_mandir}/man1/pvfamp.1%{?ext_man}
%{_mandir}/man1/pvfcut.1%{?ext_man}
%{_mandir}/man1/pvfecho.1%{?ext_man}
%{_mandir}/man1/pvffft.1%{?ext_man}
%{_mandir}/man1/pvffile.1%{?ext_man}
%{_mandir}/man1/pvffilter.1%{?ext_man}
%{_mandir}/man1/pvfmix.1%{?ext_man}
%{_mandir}/man1/pvfnoise.1%{?ext_man}
%{_mandir}/man1/pvfreverse.1%{?ext_man}
%{_mandir}/man1/pvfsine.1%{?ext_man}
%{_mandir}/man1/pvfspeed.1%{?ext_man}
%{_mandir}/man1/pvftoau.1%{?ext_man}
%{_mandir}/man1/pvftobasic.1%{?ext_man}
%{_mandir}/man1/pvftolin.1%{?ext_man}
%{_mandir}/man1/pvftormd.1%{?ext_man}
%{_mandir}/man1/pvftovoc.1%{?ext_man}
%{_mandir}/man1/pvftowav.1%{?ext_man}
%{_mandir}/man1/sff2g3.1%{?ext_man}
%{_mandir}/man1/rmdfile.1%{?ext_man}
%{_mandir}/man1/rmdtopvf.1%{?ext_man}
%{_mandir}/man1/voctopvf.1%{?ext_man}
%{_mandir}/man1/wavtopvf.1%{?ext_man}
%{_mandir}/man1/zplay.1%{?ext_man}
%{_mandir}/man4/mgettydefs.4%{?ext_man}
%{_mandir}/man8/callback.8%{?ext_man}
%{_mandir}/man8/faxq-helper.8%{?ext_man}
%{_mandir}/man8/mgetty.8%{?ext_man}
%{_mandir}/man8/vgetty.8%{?ext_man}
%{_sbindir}/mgetty
%{_sbindir}/vgetty
%{_sbindir}/callback
# Note: This was erroneously in sendfax subpackage and the %config was missing
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/new_fax
%config %{_prefix}/lib/mgetty+sendfax/new_fax

%files -n g3utils
%{_bindir}/g32pbm
%{_bindir}/g3cat
%{_bindir}/g3topbm
%{_bindir}/pbm2g3
%{_mandir}/man1/g32pbm.1%{?ext_man}
%{_mandir}/man1/g3cat.1%{?ext_man}
%{_mandir}/man1/pbm2g3.1%{?ext_man}

%files -n sendfax
%dir %{_sysconfdir}/mgetty+sendfax
%dir %{_prefix}/lib/mgetty+sendfax
%{_libexecdir}/mgetty+sendfax
%attr(755,fax,root) %dir %{_localstatedir}/spool/fax
%dir %{_localstatedir}/spool/fax/incoming
%attr(755,fax,root) %verify(not mode) %dir %{_localstatedir}/spool/fax/outgoing
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/faxheader
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/faxrunq.config
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/sendfax.config
%config %{_sysconfdir}/mgetty+sendfax/faxspool.rules.sample
%{_bindir}/faxq
%{_bindir}/faxrm
%{_bindir}/faxrunq
%{_bindir}/faxspool
%{_sbindir}/faxrunqd
%{_sbindir}/sendfax
%attr(4750,fax,trusted) %verify(not mode group) %{_libexecdir}/mgetty+sendfax/faxq-helper
%{_prefix}/lib/mgetty+sendfax/cour25.pbm
%{_prefix}/lib/mgetty+sendfax/cour25n.pbm
%{_mandir}/man1/fax.1%{?ext_man}
%{_mandir}/man1/faxq.1%{?ext_man}
%{_mandir}/man1/faxrm.1%{?ext_man}
%{_mandir}/man1/faxrunq.1%{?ext_man}
%{_mandir}/man1/faxspool.1%{?ext_man}
%{_mandir}/man1/coverpg.1%{?ext_man}
%{_mandir}/man5/faxqueue.5%{?ext_man}
%{_mandir}/man8/faxrunqd.8%{?ext_man}
%{_mandir}/man8/sendfax.8%{?ext_man}

%changelog
