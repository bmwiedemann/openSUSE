#
# spec file for package atftp
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


#
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           atftp
Version:        0.7.2
Release:        0
Summary:        Advanced TFTP Server and Client
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://sourceforge.net/projects/atftp/
Source:         %{name}-%{version}.tar.gz
Source2:        atftpd.sysconfig
Source3:        atftpd.logrotate
Source5:        atftpd.service
Source6:        atftpd.socket
# PATCH-FIX-SUSE sorcerer's apprentice syndrom (bnc#727843)
Patch1:         atftp-0.7-sorcerers_apprentice.patch
# PATCH-FIX-SUSE server receive thread race (bnc#599856)
Patch2:         atftp-0.7-server_receive_race.patch
# PATCH-FIX-SUSE drop one duplicated ACK each round (bnc#774376)
Patch3:         atftp-0.7-ack_heuristic.patch
Patch4:         atftp-0.7-default_user_man.patch
# PATCH-FIX-SUSE update default directory in man (bnc#507011)
Patch5:         atftp-0.7-default_dir_man.patch
Patch6:         atftp-drop_privileges_non-daemon.patch
# PATCH-FIX-UPSTREAM bsc#1176437 CVE-2020-6097 Fix for DoS issue
Patch7:         atftp-CVE-2020-6097.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  readline-devel
BuildRequires:  tcpd-devel
Requires(pre):  %fillup_prereq
Requires(pre):  pwdutils
Recommends:     logrotate
Conflicts:      tftp
Provides:       tftp(client)
Provides:       tftp(server)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
atftp stands for Advanced Trivial File Transfer Protocol. It is called
"advanced", in contrast to others TFTP servers, for two reasons. First,
it is intended to be fully compliant with all related RFCs. This
includes RFC1350, RFC2090, RFC2347, RFC2348, and RFC2349. Second, atftp
is intended for serving boot files to large clusters. It is
multithreaded and will eventually support multicast, allowing faster
boot of hundreds of machines simultaneously.

%prep
%setup -q -n %{name}-%{version}
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6 -p1
%patch7 -p1

%build
autoreconf -fi
CFLAGS="%optflags -fgnu89-inline"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# SuSE rc
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_unitdir}/atftpd.service
install -D -m 0644 %{SOURCE6} %{buildroot}/%{_unitdir}/atftpd.socket
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcatftpd
install -D -m 0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.atftpd
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -d -m 0755 %{buildroot}/srv/tftpboot
install -d -m 0750 %{buildroot}%{_localstatedir}/log/atftpd

%pre
# This group/user is shared with tftp, so please
# keep this in sync with tftp.spec
# add group
%{_sbindir}/groupadd -r tftp 2>/dev/null || :
# add user
%{_sbindir}/useradd -c "TFTP account" -d /srv/tftpboot -G tftp -g tftp \
  -r -s /bin/false tftp 2>/dev/null || :
# fix sysconfig to get new defaults on Update
if [ -f %{_sysconfdir}/sysconfig/atftpd ]; then
  sed -i -e "s@^\(ATFTPD_OPTIONS=\"--daemon \"\)@#\1@" %{_sysconfdir}/sysconfig/atftpd
  sed -i -e "s@^\(ATFTPD_DIRECTORY=\"/tftpboot\"\)@#\1@" %{_sysconfdir}/sysconfig/atftpd
fi
%service_add_pre atftpd.service atftpd.socket

%preun
%service_del_preun atftpd.service atftpd.socket

%post
%service_add_post atftpd.service atftpd.socket
%{fillup_only -n atftpd}

%postun
%service_del_postun atftpd.service atftpd.socket

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
%config %{_sysconfdir}/logrotate.d/%{name}
%{_fillupdir}/sysconfig.atftpd
%{_mandir}/man1/atftp.1.gz
%{_mandir}/man8/atftpd.8.gz
%{_mandir}/man8/in.tftpd.8.gz

%dir %attr(0755,tftp,tftp) /srv/tftpboot
%dir %attr(0750,tftp,tftp) %{_localstatedir}/log/atftpd/

%changelog
