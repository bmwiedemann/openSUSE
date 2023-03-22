#
# spec file for package amanda
#
# Copyright (c) 2023 SUSE LLC
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


%define amanda_group amanda
%define upstreamver tag-community-%{version}
Name:           amanda
Version:        3.5.3
Release:        0
Summary:        Network Disk Archiver
License:        GPL-3.0-or-later
URL:            http://www.amanda.org/
Source:         https://github.com/zmanda/amanda/archive/%{upstreamver}/%{name}-%{version}.tar.gz
#amanda-SUSE.tar.bz2 contains init scripts, config examples
Source1:        amanda-SUSE.tar.bz2
Source2:        amanda-howto-collection.pdf.tar.bz2
Patch1:         amanda-2.6.1p1-shellbang.patch
Patch2:         amanda-2.6.1p1-return_val.patch
Patch3:         amanda-2.6.1p1-avoid-perl-provides.patch
Patch4:         amanda-3.3.2-returnvalues.patch
Patch6:         amanda-3.5-no_return_in_nonvoid_fnc.patch
Patch7:         amanda-libnsl.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cups-client
BuildRequires:  dump
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnuplot
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  mailx
BuildRequires:  mtx
BuildRequires:  openssh
BuildRequires:  openssl-devel
BuildRequires:  perl-base
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  procps
BuildRequires:  readline-devel
BuildRequires:  rpcgen
BuildRequires:  samba-client
BuildRequires:  sendmail
BuildRequires:  swig
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(Test::Simple)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(smbclient)
Requires:       %{_bindir}/smbclient
Requires:       dump
Requires:       grep
Requires:       perl = %{perl_version}
Requires:       tar
Requires(post): permissions
Requires(pre):  shadow

%description
AMANDA, the Advanced Maryland Automatic Network Disk Archiver, is a backup
solution that allows the IT administrator to set up a single master backup
server to back up multiple hosts over network to tape drives/changers or
disks or optical media. Amanda uses native utilities and formats (e.g. dump
and/or GNU tar) and can back up a large number of servers and workstations
running multiple versions of Linux or Unix.

%prep
%setup -q -n %{name}-%{upstreamver} -a 1 -a 2
%patch1
%patch2
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1

%build
./autogen

export CFLAGS="%{optflags} -fno-strict-aliasing -fPIC -fPIE"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -fPIC -fPIE"
export LDFLAGS="-pie"
%configure --with-bsdtcp-security \
           --with-bsdudp-security \
           --with-ssh-security \
           --with-rsh-security \
           --with-krb5-security \
           --with-index-server=localhost \
           --with-gnutar-listdir=%{_localstatedir}/lib/amanda/gnutar-lists \
           --with-smbclient=%{_bindir}/smbclient \
           --with-amperldir=%{perl_vendorlib} \
           --with-user=amanda \
           --with-group=%{amanda_group} \
           --with-gnutar=/bin/tar \
           --disable-libtool \
           --with-amandahosts \
           --disable-installperms
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}/
install -d %{buildroot}/%{_sysconfdir}/amanda \
           %{buildroot}%{_localstatedir}/lib/amanda/index \
           %{buildroot}%{_localstatedir}/lib/amanda/gnutar-lists \
           %{buildroot}%{_localstatedir}/lib/amanda/disklist \
           %{buildroot}%{_localstatedir}/lib/amanda/DailySet1 \
           %{buildroot}%{_localstatedir}/lib/amanda/lbl-templ \
           %{buildroot}/%{_docdir}/%{name} \
           %{buildroot}/%{_sysconfdir}/xinetd.d
install NEWS README.md README.SUSE example/{amanda.conf,chg-multi.conf,disklist} %{buildroot}/%{_docdir}/%{name}
install -m 644 %{buildroot}%{_sysconfdir}/amanda/amanda-security.conf %{buildroot}%{_sysconfdir}/amanda-security.conf
chmod 644 %{buildroot}/%{_docdir}/%{name}/* %{buildroot}/%{_mandir}/*/*
cp -a SUSE/* %{buildroot}

# pdf doc
cp amanda-howto-collection.pdf %{buildroot}/%{_docdir}/%{name}/

# label templates
cp -a example/*.ps %{buildroot}%{_localstatedir}/lib/amanda/lbl-templ

# contain docs, examples which are already included
rm -rf %{buildroot}%{_datadir}/amanda

# bnc#412636
touch %{buildroot}/%{_libexecdir}/amanda/exclude.gtar

# delete all static linking remnats
find %{buildroot} \( -name "*.a" -o -name "*.la" \) -delete

# create a list of binaries to be checked externally
cat << EOF > %{buildroot}%{_libexecdir}/amanda/suidlist
%{_libexecdir}/amanda/ambind
%{_libexecdir}/amanda/application/ambsdtar
%{_libexecdir}/amanda/application/amgtar
%{_libexecdir}/amanda/application/amstar
%{_libexecdir}/amanda/calcsize
%{_libexecdir}/amanda/killpgrp
%{_libexecdir}/amanda/rundump
%{_libexecdir}/amanda/runtar
EOF

# create a symlink for amoldrecover manpage
ln -s amrecover.8.gz %{buildroot}%{_mandir}/man8/amoldrecover.8

%pre
# since 11.2 we use group "tape" instead of "disk" for tape devices /dev/nst*,
# so we must check group for "amanda" user
# create primary group for amanda user
%{_sbindir}/groupadd -r amanda 2>/dev/null || :
# if user already exists and has effective group "disk", we have to change this group
# to "amanda" group and also add supplementary "tape" group see bnc#523006
# else - move amanda to group amanda unconditionally (ignore failures if amanda doesn't exist)
%{_bindir}/id -n -g amanda 2>&1 | grep "disk" >/dev/null \
    && %{_sbindir}/usermod -g amanda -G tape amanda \
    || %{_sbindir}/usermod -g amanda amanda 2>&1 \
    || :
# this is ugly but just simple add user with "tape" and "amanda" groups regardless of existing user
%{_sbindir}/useradd -r -o -g amanda -G tape -u 37 -s /bin/bash \
    -c "Amanda admin" -d %{_localstatedir}/lib/amanda amanda >/dev/null 2>&1 || :

%post
%if 0%{?set_permissions:1}
%set_permissions %{_libexecdir}/amanda/ambind %{_libexecdir}/amanda/application/ambsdtar %{_libexecdir}/amanda/application/amgtar %{_libexecdir}/amanda/application/amstar %{_libexecdir}/amanda/calcsize %{_libexecdir}/amanda/killpgrp %{_libexecdir}/amanda/rundump %{_libexecdir}/amanda/runtar
%else
%run_permissions
%endif

%verifyscript
%verify_permissions -f %{_libexecdir}/amanda/suidlist

%files
%doc amanda-howto-collection.pdf ChangeLog NEWS AUTHORS COPYRIGHT README.md ReleaseNotes README.SUSE
%doc %attr(755,root,root) %dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man*/*
%config %{_libexecdir}/amanda/exclude.gtar
%attr(755,root,root) %dir %{_libexecdir}/amanda
%attr(664,amanda,%{amanda_group}) %config(noreplace) %{_sysconfdir}/dumpdates
%attr(664,amanda,%{amanda_group}) %config(noreplace) %{_sysconfdir}/amandates
%attr(755,amanda,%{amanda_group}) %dir %{_sysconfdir}/amanda
%attr(755,amanda,%{amanda_group}) %dir %{_sysconfdir}/amanda/example
%attr(755,amanda,%{amanda_group}) %dir %{_localstatedir}/lib/amanda/
%attr(755,amanda,%{amanda_group}) %dir %{_localstatedir}/lib/amanda/disklist
%attr(755,amanda,%{amanda_group}) %dir %{_localstatedir}/lib/amanda/gnutar-lists/
%attr(755,amanda,%{amanda_group}) %dir %{_localstatedir}/lib/amanda/index/
%attr(755,amanda,%{amanda_group}) %dir %{_localstatedir}/lib/amanda/DailySet1
%attr(755,amanda,%{amanda_group}) %dir %{_localstatedir}/lib/amanda/lbl-templ
%attr(644,amanda,%{amanda_group}) %{_localstatedir}/lib/amanda/lbl-templ/*
%config %attr(644,amanda,%{amanda_group}) %{_localstatedir}/lib/amanda/.bashrc
%config %attr(644,amanda,%{amanda_group}) %{_localstatedir}/lib/amanda/.profile
# bnc#412636 file permissions of .amandahosts should be 600
%config %attr(600,amanda,%{amanda_group}) %{_localstatedir}/lib/amanda/.amandahosts
%config %attr(644,amanda,%{amanda_group}) %{_sysconfdir}/amanda/example/amanda.conf
# amanda-security.conf must be installed at %%{_sysconfdir} and only root must be able to write it
# an example file should be installed at %%{_sysconfdir}/amanda/
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/amanda-security.conf
%{_sysconfdir}/amanda/amanda-security.conf
%config %attr(644,amanda,%{amanda_group}) %{_sysconfdir}/amanda/example/disklist
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/*
# perl scripts
%dir %{perl_vendorlib}/Amanda/
%dir %{perl_vendorlib}/Amanda/Application
%dir %{perl_vendorlib}/Amanda/Changer
%dir %{perl_vendorlib}/Amanda/Config
%dir %{perl_vendorlib}/Amanda/Curinfo
%dir %{perl_vendorlib}/Amanda/DB
%dir %{perl_vendorlib}/Amanda/FetchDump
%dir %{perl_vendorlib}/Amanda/Chunker
%dir %{perl_vendorlib}/Amanda/Interactivity
%dir %{perl_vendorlib}/Amanda/IPC
%dir %{perl_vendorlib}/Amanda/Recovery
%dir %{perl_vendorlib}/Amanda/Report
%dir %{perl_vendorlib}/Amanda/Rest
%dir %{perl_vendorlib}/Amanda/Rest/Storages
%dir %{perl_vendorlib}/Amanda/Service
%dir %{perl_vendorlib}/Amanda/Taper
%dir %{perl_vendorlib}/Amanda/Taper/Scan
%dir %{perl_vendorlib}/auto/Amanda/
%dir %{perl_vendorlib}/auto/Amanda/Application
%dir %{perl_vendorlib}/auto/Amanda/Archive
%dir %{perl_vendorlib}/auto/Amanda/Cmdline
%dir %{perl_vendorlib}/auto/Amanda/Cmdfile
%dir %{perl_vendorlib}/auto/Amanda/Config
%dir %{perl_vendorlib}/auto/Amanda/Debug
%dir %{perl_vendorlib}/auto/Amanda/Device
%dir %{perl_vendorlib}/auto/Amanda/Disklist
%dir %{perl_vendorlib}/auto/Amanda/Feature
%dir %{perl_vendorlib}/auto/Amanda/Header
%dir %{perl_vendorlib}/auto/Amanda/IPC
%dir %{perl_vendorlib}/auto/Amanda/IPC/Binary
%dir %{perl_vendorlib}/auto/Amanda/Logfile
%dir %{perl_vendorlib}/auto/Amanda/MainLoop
%dir %{perl_vendorlib}/auto/Amanda/NDMP
%dir %{perl_vendorlib}/auto/Amanda/Tapelist
%dir %{perl_vendorlib}/auto/Amanda/Tests
%dir %{perl_vendorlib}/auto/Amanda/Util
%dir %{perl_vendorlib}/auto/Amanda/Xfer
%dir %{perl_vendorlib}/auto/Amanda/XferServer
%{perl_vendorlib}/Amanda/*/*/*.pm
%{perl_vendorlib}/Amanda/*/*.pm
%{perl_vendorlib}/Amanda/*.pm
%{perl_vendorlib}/auto/Amanda/*/*.so
%{perl_vendorlib}/auto/Amanda/*/*/*.so
%defattr(755,amanda,%{amanda_group})
%{_sbindir}/amadmin
%{_sbindir}/ambackup
%{_sbindir}/amreindex
%{_sbindir}/amssl
%{_sbindir}/amanda-rest-server
%{_sbindir}/amcheckdb
%{_sbindir}/amcleanup
%{_sbindir}/amdump
%{_sbindir}/amflush
%{_sbindir}/amgetconf
%{_sbindir}/amlabel
%{_sbindir}/amoverview
%{_sbindir}/amplot
%{_sbindir}/amcheck
%attr(0750,amanda,%{amanda_group}) %{_sbindir}/amrecover
%{_sbindir}/amreport
%{_sbindir}/amrestore
%{_sbindir}/amrmtape
%{_sbindir}/amstatus
%{_sbindir}/amtape
%{_sbindir}/amtapetype
%{_sbindir}/amtoc
%{_sbindir}/amcrypt-ossl
%{_sbindir}/amcrypt-ossl-asym
%{_sbindir}/amoldrecover
%{_sbindir}/amgpgcrypt
%{_sbindir}/amaespipe
%{_sbindir}/amcrypt
%{_sbindir}/amfetchdump
%{_sbindir}/amaddclient
%{_sbindir}/amarchiver
%{_sbindir}/amcheckdump
%{_sbindir}/amcryptsimple
%{_sbindir}/amdevcheck
%{_sbindir}/amdump_client
%{_sbindir}/amserverconfig
%{_sbindir}/amservice
%{_sbindir}/amvault
%{_sbindir}/activate-devpay
%defattr(644,amanda,%{amanda_group})
%{_libexecdir}/amanda/suidlist
%{_libexecdir}/amanda/amcat.awk
%{_libexecdir}/amanda/amplot.awk
%{_libexecdir}/amanda/amplot.g
%{_libexecdir}/amanda/amplot.gp
%defattr(755,amanda,%{amanda_group})
%{_libexecdir}/amanda/amandad
%{_libexecdir}/amanda/amdumpd
%{_libexecdir}/amanda/amidxtaped
%{_libexecdir}/amanda/amindexd
%{_libexecdir}/amanda/amtrmidx
%{_libexecdir}/amanda/driver
%{_libexecdir}/amanda/amadmin_perl
%{_libexecdir}/amanda/ambackupd
%{_libexecdir}/amanda/rest-server/
%{_libexecdir}/amanda/amcheck-device
%{_sbindir}/amcleanupdisk
%{_libexecdir}/amanda/amlogroll
%{_libexecdir}/amanda/amndmjob
%{_libexecdir}/amanda/amtrmlog
%{_libexecdir}/amanda/patch-system
%{_libexecdir}/amanda/selfcheck
%{_libexecdir}/amanda/sendbackup
%{_libexecdir}/amanda/sendsize
%{_libexecdir}/amanda/taper
%{_libexecdir}/amanda/chunker
%{_libexecdir}/amanda/noop
%{_libexecdir}/amanda/ndmjob
%{_libexecdir}/amanda/amanda-sh-lib.sh
%{_libexecdir}/amanda/teecount
%{_libexecdir}/amanda/restore
%{_libexecdir}/amanda/senddiscover
%{_libexecdir}/amanda/dumper
%{_libexecdir}/amanda/planner
%attr(0755 root root) %dir %{_libexecdir}/amanda/application/
%{_libexecdir}/amanda/application/amlog-script
%{_libexecdir}/amanda/application/ampgsql
%{_libexecdir}/amanda/application/amrandom
%{_libexecdir}/amanda/application/amraw
%{_libexecdir}/amanda/application/amsamba
%{_libexecdir}/amanda/application/amsuntar
%{_libexecdir}/amanda/application/amzfs-sendrecv
%{_libexecdir}/amanda/application/amzfs-snapshot
%{_libexecdir}/amanda/application/script-email
%{_libexecdir}/amanda/application/script-fail
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/ambind
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/application/ambsdtar
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/application/amgtar
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/application/amstar
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/calcsize
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/killpgrp
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/rundump
%verify(not mode) %attr(0750,root,%{amanda_group})%{_libexecdir}/amanda/runtar
# include shared libs
%dir %{_libdir}/amanda/
%{_libdir}/amanda/lib*

%check
make %{?_smp_mflags} check

%changelog
