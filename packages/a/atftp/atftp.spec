#
# spec file for package atftp
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


#
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           atftp
Version:        0.8.0
Release:        0
Summary:        Advanced TFTP Server and Client
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://sourceforge.net/projects/atftp/
Source:         https://sourceforge.net/projects/atftp/files/%{name}-%{version}.tar.gz
Source2:        atftpd.sysconfig
Source3:        atftpd.logrotate
Source5:        atftpd.service
Source6:        atftpd.socket
Patch1:         atftp-0.7-default_user_man.patch
# PATCH-FIX-SUSE update default directory in man (bnc#507011)
Patch2:         atftp-0.7-default_dir_man.patch
Patch3:         atftp-drop_privileges_non-daemon.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  readline-devel
BuildRequires:  tcpd-devel
Requires(pre):  %fillup_prereq
Requires(pre):  user(tftp) group(tftp)
Recommends:     logrotate
Conflicts:      tftp
Provides:       tftp(client)
Provides:       tftp(server)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  systemd-rpm-macros

%description
atftp stands for Advanced Trivial File Transfer Protocol. It is called
"advanced", in contrast to others TFTP servers, for two reasons. First,
it is intended to be fully compliant with all related RFCs. This
includes RFC1350, RFC2090, RFC2347, RFC2348, and RFC2349. Second, atftp
is intended for serving boot files to large clusters. It is
multithreaded and will eventually support multicast, allowing faster
boot of hundreds of machines simultaneously.

%prep
%autosetup -p1

%build
autoreconf -fi
CFLAGS="%optflags -fgnu89-inline"
%configure
make %{?_smp_mflags}

%install
%make_install
# SuSE rc
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_unitdir}/atftpd.service
install -D -m 0644 %{SOURCE6} %{buildroot}/%{_unitdir}/atftpd.socket
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcatftpd
install -D -m 0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.atftpd
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -D -m 0644 %{SOURCE3} %{buildroot}%{_distconfdir}/logrotate.d/%{name}
%else
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%endif
install -d -m 0755 %{buildroot}/srv/tftpboot
install -d -m 0750 %{buildroot}%{_localstatedir}/log/atftpd

%pre
# fix sysconfig to get new defaults on Update
if [ -f %{_sysconfdir}/sysconfig/atftpd ]; then
  sed -i -e "s@^\(ATFTPD_OPTIONS=\"--daemon \"\)@#\1@" %{_sysconfdir}/sysconfig/atftpd
  sed -i -e "s@^\(ATFTPD_DIRECTORY=\"/tftpboot\"\)@#\1@" %{_sysconfdir}/sysconfig/atftpd
fi
%service_add_pre atftpd.service atftpd.socket
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/%{name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%preun
%service_del_preun atftpd.service atftpd.socket

%post
%service_add_post atftpd.service atftpd.socket
%{fillup_only -n atftpd}

%postun
%service_del_postun atftpd.service atftpd.socket

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/%{name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%defattr(-,root,root)
%license LICENSE
%doc BUGS FAQ README README.MCAST README.PCRE TODO
%{_bindir}/atftp
%{_sbindir}/atftpd
%{_sbindir}/in.tftpd
%{_sbindir}/rcatftpd
%{_unitdir}/atftpd.service
%{_unitdir}/atftpd.socket
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/%{name}
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%endif
%{_fillupdir}/sysconfig.atftpd
%{_mandir}/man1/atftp.1.gz
%{_mandir}/man8/atftpd.8.gz
%{_mandir}/man8/in.tftpd.8.gz

%dir %attr(0755,tftp,tftp) /srv/tftpboot
%dir %attr(0750,tftp,tftp) %{_localstatedir}/log/atftpd/

%changelog
