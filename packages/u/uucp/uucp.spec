#
# spec file for package uucp
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


Name:           uucp
Version:        1.07
Release:        0
Summary:        Taylor Unix-to-Unix copy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://www.gnu.org/software/uucp/
Source0:        http://ftp.gnu.org/gnu/uucp/%{name}-%{version}.tar.gz
Source1:        uucpcfg.tar.bz2
Source3:        suucp.service
Source4:        uucpman.sh
Source5:        uucp@.service
Source6:        uucp.socket
Source7:        uucp.pam
Source8:        xinetd.uucp
Source9:        uucp-rpmlintrc
Source10:       uucp.bashrc
Source11:       uucp.tmpfiles
Patch0:         uucp-1.07.dif
Patch1:         uucp-1.07-contrib.dif
Patch2:         uucp-1.07-grade.patch
Patch3:         uucp-1.07-cu.patch
Patch4:         uucp-1.07-lockdev.patch
Patch5:         drop_ftime.patch
Patch6:         uucp-texinfo-5.0.patch
Patch7:         address-wildcard-in-port.patch
Patch8:         fix-proty-gcc33.patch
Patch9:         uucp-1.07-lfs.patch
Patch10:        uucp-1.07-sigfpe2.patch
Patch11:        uucp-1.07-initgroups.patch
Patch12:        uucp-1.07-configure.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  lockdev-devel
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
Requires:       ca-certificates
Requires:       filesystem
Requires:       logrotate
Requires:       netcfg
Requires:       openssl
Requires:       rmail
Requires:       stunnel
%if 0%{?suse_version} >= 1330
Requires(pre):  user(uucp) group(uucp)
%else
Requires(pre):  shadow
%endif
Requires(post): %{install_info_prereq}
Requires(post): fileutils
Requires(post): permissions
Requires(preun):%{install_info_prereq}
Requires(verify):permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
Ian Taylor's Unix to Unix copy: mail and news over modem lines. This is
the standard UUCP package from the Free Software Foundation. It is
configured to use HoneyDanBer or Taylor configuration files. With
version 6.0 of SuSE Linux, the configuration directory has been moved
to %{_sysconfdir}/uucp.

Exactly:
Taylor config:	 %{_sysconfdir}/uucp
HoneyDanBer config: %{_sysconfdir}/uucp/hdb_config

If you have your own setup under {_localstatedir}/lib/uucp, please
%move it to %{_sysconfdir}/uucp.
Example configurations can be found in %{_docdir}/uucp.

We did not include a uucp guest account. If you want to create a guest
account, make sure the directory %{_localstatedir}/spool/uucppublic exists.

%package xinetd
Summary:        Taylor UUCP using xinetd
Group:          Productivity/Networking/Other
Requires:       uucp = %version-%release
Requires:       xinetd

%description xinetd
Unix to Unix copy with xinetd setup instead of using modern systemd
service units.

%prep
%setup -q
%patch1 -p0 -b .cont
%patch2 -p0 -b .grad
%patch3 -p0 -b .cu
%patch4 -p0 -b .lockdev
%patch0 -p0 -b .p0
%patch5 -p1 -b .p5
%patch6 -p1 -b .p6
%patch7 -p1 -b .p7
%patch8 -p0 -b .p8
%patch9 -p1 -b .p9
%patch10 -p1 -b .p10
%patch11 -p0 -b .p11
%patch12 -p0 -b .p12

%build
autoreconf -fvi
export CFLAGS="%{optflags} -fno-strict-aliasing -fPIE -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE"
%configure \
	--with-newconfigdir=%{_sysconfdir}/uucp \
	--with-oldconfigdir=%{_sysconfdir}/uucp/hdb_config
make %{?_smp_mflags} LDFLAGS="-pie" MAKEINFO="makeinfo --force"

%install
%make_install install-info
# oldconfig
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/uucp/hdb_config
# logrotate
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 logrotate %{buildroot}%{_sysconfdir}/logrotate.d/uucp
# systemd services
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE3} %{buildroot}%{_unitdir}
install -m644 %{SOURCE5} %{buildroot}%{_unitdir}
install -m644 %{SOURCE6} %{buildroot}%{_unitdir}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
install -m644 %{SOURCE7} %{buildroot}%{_pam_vendordir}/uucp
%else
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m644 %{SOURCE7} %{buildroot}%{_sysconfdir}/pam.d/uucp
%endif
mkdir -p %{buildroot}%{_sysconfdir}/xinetd.d
install -m644 %{SOURCE8} %{buildroot}%{_sysconfdir}/xinetd.d/uucp
# move to libexec
mkdir -p -m 755 %{buildroot}%{_libexecdir}/uucp/
mv %{buildroot}%{_sbindir}/uu* %{buildroot}%{_libexecdir}/uucp/
for x in %{buildroot}%{_libexecdir}/uucp/* ; do
    echo ${x##*/}
    ln -fs %{_libexecdir}/uucp/${x##*/} %{buildroot}%{_sbindir}/
done
# readme
mkdir -p -m 755 %{buildroot}%{_localstatedir}/spool/uucp %{buildroot}%{_localstatedir}/spool/uucppublic
install -m 644 README.suse %{buildroot}%{_localstatedir}/spool/uucppublic/README
# docs
rm -rf %{buildroot}%{_defaultdocdir}/uucp
mkdir -p %{buildroot}%{_defaultdocdir}/uucp
mkdir -p %{buildroot}%{_localstatedir}/log/uucp
chmod 1755      %{buildroot}%{_localstatedir}/log/uucp
tar -jxvpf %{SOURCE1} -C %{buildroot}%{_defaultdocdir}/uucp
chmod -R uog+r %{buildroot}%{_defaultdocdir}/uucp/
cp %{buildroot}%{_defaultdocdir}/uucp/cfg_example/taylor_config/suucp-server.conf.systemd \
   %{buildroot}%{_sysconfdir}/uucp/suucp-server.conf.systemd
cp %{buildroot}%{_defaultdocdir}/uucp/cfg_example/taylor_config/suucp-server.conf.xinetd \
   %{buildroot}%{_sysconfdir}/uucp/suucp-server.conf.xinetd
cp %{buildroot}%{_defaultdocdir}/uucp/cfg_example/taylor_config/suucp-client.conf \
   %{buildroot}%{_sysconfdir}/uucp/suucp-client.conf.example
install -m 0640 %{SOURCE10} %{buildroot}%{_sysconfdir}/uucp/.bashrc
mkdir %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE11} %{buildroot}%{_tmpfilesdir}/uucp.conf
> list.files
if ! tmp=$(rpm -qf %{_tmpfilesdir} 2>/dev/null)
then
    echo %%dir %%{_tmpfilesdir} > list.files
fi
# rcbla compat symlink
ln -fs service %{buildroot}/%{_sbindir}/rcs%{name}
# manual pages
for man in uulog uuto uuname uupick
do
    test -e ${man}.1 || continue
    install -m 0644 ${man}.1 %{buildroot}%{_mandir}/man1/
done

%verifyscript
%verify_permissions -e %{_localstatedir}/spool/uucp/
%verify_permissions -e %{_localstatedir}/spool/uucppublic/
%verify_permissions -e %{_bindir}/uucp
%verify_permissions -e %{_bindir}/uuname
%verify_permissions -e %{_bindir}/uustat
%verify_permissions -e %{_bindir}/uux
%verify_permissions -e %{_libexecdir}/uucp/uucico
%verify_permissions -e %{_libexecdir}/uucp/uuxqt
%if 0
%verify_permissions -e %{_bindir}/uulog
%verify_permissions -e %{_bindir}/uupick
%endif

%pre
%service_add_pre s%{name}.service %{name}.socket
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/uucp ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/uucp ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%install_info --info-dir=%{_infodir} %{_infodir}/uucp.info%{ext_info}
%service_add_post s%{name}.service %{name}.socket
for log in Log Stats Debug ; do
    if test -e %{_localstatedir}/log/uucp/$log ; then
    	continue
    fi
    touch %{_localstatedir}/log/uucp/$log
    chown uucp:uucp %{_localstatedir}/log/uucp/$log
    chmod 0640      %{_localstatedir}/log/uucp/$log
done
chown root:root %{_localstatedir}/log/uucp
chmod 1755      %{_localstatedir}/log/uucp
%set_permissions %{_localstatedir}/spool/uucp/
%set_permissions %{_localstatedir}/spool/uucppublic/
%set_permissions %{_bindir}/uucp
%set_permissions %{_bindir}/uuname
%set_permissions %{_bindir}/uustat
%set_permissions %{_bindir}/uux
%set_permissions %{_libexecdir}/uucp/uucico
%set_permissions %{_libexecdir}/uucp/uuxqt
%if 0
%set_permissions %{_bindir}/uulog
%set_permissions %{_bindir}/uupick
%endif
%if %{defined tmpfiles_create}
%tmpfiles_create %{_tmpfilesdir}/uucp.conf
%else
test -x /usr/bin/systemd-tmpfiles && /usr/bin/systemd-tmpfiles --create %{_tmpfilesdir}/uucp.conf || :
%endif

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/uucp.info%{ext_info}
%service_del_preun s%{name}.service %{name}.socket

%postun
%service_del_postun s%{name}.service %{name}.socket

%files -f list.files
%defattr(-,root,root)
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.socket
%{_unitdir}/s%{name}.service
%{_sbindir}/rcs%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/uucp
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/uucp
%else
%config %{_sysconfdir}/pam.d/uucp
%endif
%dir %attr(0750,uucp,uucp) %{_sysconfdir}/%{name}/
%config %attr(0640,uucp,uucp) %{_sysconfdir}/%{name}/suucp-server.conf.systemd
%config %attr(0640,uucp,uucp) %{_sysconfdir}/%{name}/suucp-client.conf.example
%config(noreplace) %attr(0640,uucp,uucp) %{_sysconfdir}/%{name}/.bashrc
%dir %attr(0750,uucp,uucp) %{_sysconfdir}/uucp/hdb_config
%dir %{_libexecdir}/uucp
%dir %attr(1755,root,root) %{_localstatedir}/log/uucp
%verify(not mode group) %dir %attr(1770,root,uucp) %{_localstatedir}/spool/uucppublic
%attr(755,root,root) %{_bindir}/cu
%verify(not mode) %attr(6555,uucp,uucp) %{_bindir}/uucp
%verify(not mode) %attr(6555,uucp,uucp) %{_bindir}/uuname
%verify(not mode) %attr(6555,uucp,uucp) %{_bindir}/uustat
%verify(not mode) %attr(6555,uucp,uucp) %{_bindir}/uux
%if 0
%verify(not mode) %attr(6555,uucp,uucp) %{_bindir}/uulog
%verify(not mode) %attr(6555,uucp,uucp) %{_bindir}/uupick
%else
%{_bindir}/uulog
%{_bindir}/uupick
%endif
%verify(not mode) %attr(6555,uucp,uucp) %{_libexecdir}/uucp/uucico
%verify(not mode) %attr(6555,uucp,uucp) %{_libexecdir}/uucp/uuxqt
%{_bindir}/uuto
%{_infodir}/uucp.info*%{ext_info}
%{_libexecdir}/uucp/uuchk
%{_libexecdir}/uucp/uuconv
%{_libexecdir}/uucp/uusched
%{_sbindir}/uuchk
%{_sbindir}/uucico
%{_sbindir}/uuconv
%{_sbindir}/uusched
%{_sbindir}/uuxqt
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
%{_localstatedir}/spool/uucppublic/README
%doc %{_defaultdocdir}/uucp
%attr(0640,root,uucp) %{_defaultdocdir}/uucp/cfg_example/taylor_config/call
%attr(0640,root,uucp) %{_defaultdocdir}/uucp/cfg_example/taylor_config/passwd
%{_tmpfilesdir}/uucp.conf

%files xinetd
%defattr(-,root,root)
%config %attr(0640,uucp,uucp) %{_sysconfdir}/%{name}/suucp-server.conf.xinetd
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/uucp

%changelog
