#
# spec file for package dovecot
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?suse_version} > 1230
%bcond_without systemd
%else
%bcond_with    systemd
%endif

Name:           dovecot
Version:        2.3
Release:        0
Summary:        IMAP and POP3 Server Written Primarily with Security in Mind
License:        BSD-3-Clause AND LGPL-2.1-or-later AND MIT
Group:          Productivity/Networking/Email/Servers
Url:            http://www.dovecot.org/
PreReq:         dovecot-implementation
Recommends:     dovecot23
#!BuildIgnore: dovecot-implementation
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define has_systemd 1
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Source0:        dovecot-2.0.configfiles
Source1:        dovecot-2.1.configfiles
Source2:        dovecot-2.2.configfiles
Source3:        %{name}.init
Source4:        %{name}.pam
Source5:        %{name}.README.SUSE
Source7:        dovecot.tmpfiles.d
Source8:        dovecot.service
Source9:        dovecot.socket
Source10:       dovecot-2.1-pigeonhole.configfiles
Source11:       dovecot-2.2-pigeonhole.configfiles
Source12:       dovecot-2.3.configfiles
Source13:       dovecot-2.3-pigeonhole.configfiles

%description
Dovecot is an IMAP and POP3 server for Linux and UNIX-like systems,
written primarily with security in mind. Although it is written in C,
it uses several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and is fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

This is a wrapper package that will just handle common things for all
versioned dovecot packages.

%prep

%build

%install
for i in $RPM_SOURCE_DIR/*.configfiles ; do
  echo "Creating ghost files for '$i'"
  for j in $(<$i) ; do
    install -D -m 0644 /dev/null %{buildroot}$j
  done
done

install -D -m 0644 %{S:5} %{buildroot}%{_datadir}/doc/packages/dovecot/README.SUSE
install -d %{buildroot}%{_sbindir}
# install the init script
%if %{with systemd}
%{__install} -D -m 644 %{S:7} %{buildroot}/usr/lib/tmpfiles.d/dovecot.conf
%{__ln_s} -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D -m 0644 %{S:8} %{buildroot}%{_unitdir}/dovecot.service
install -D -m 0644 %{S:9} %{buildroot}%{_unitdir}/dovecot.socket
%else
%{__install} -D -m 0755 %{S:3} %{buildroot}%{_sysconfdir}/init.d/%{name}
%{__ln_s} -f %{_sysconfdir}/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif

# install pam config
%{__install} -D -m 0644 %{S:4} %{buildroot}%{_sysconfdir}/pam.d/%{name}
# create /var directories
%{__install} -m 0755 -Dd \
  %{buildroot}%{_var}/run/%{name}/login/ \
  %{buildroot}%{_var}/lib/%{name}/

%pre
/usr/sbin/groupadd -r %{name} >/dev/null 2>&1 || :
/usr/sbin/useradd -g %{name} -s /bin/false -r -c "User for Dovecot imapd" -d %{_var}/run/%{name} %{name} >/dev/null 2>&1 || :
/usr/sbin/useradd -g %{name} -s /bin/false -r -c "User for Dovecot login" -d %{_var}/run/%{name} dovenull >/dev/null 2>&1 || :
# try to copy the default configuration.
#
# we fail silently if the dovecot-implementation package is not
# installed yet. This allows us to break a little build loop between
# dovecot and dovecotXY.
if [ ! -e %{_sysconfdir}/%{name}/dovecot.conf -a -e %{_datadir}/%{name}/example-config/dovecot.conf ] ; then
  # install default config
  echo "Did not find a /etc/dovecot/dovecot.conf. copying default configuration"
  cp -na %{_datadir}/%{name}/example-config/* %{_sysconfdir}/%{name}/
  # the chmod breaks the lda. lets use the more open permissions
  #chmod -Rv o= %{_sysconfdir}/%{name}/
fi
%if %{with systemd}
%service_add_pre %{name}.service %{name}.socket
%endif

%preun
%if %{with systemd}
%service_del_preun %{name}.service %{name}.socket
%else
%stop_on_removal %{name}
%endif

%if %{with systemd}
%post
systemd-tmpfiles --create /usr/lib/tmpfiles.d/dovecot.conf || true
%service_add_post %{name}.service %{name}.socket
%endif

%postun
%if %{with systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/packages/dovecot/
# conf
%dir /etc/dovecot/
%ghost %config(noreplace) /etc/dovecot/*
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_sbindir}/rc%{name}
%if %{with systemd}
/usr/lib/tmpfiles.d/dovecot.conf
%{_unitdir}/dovecot.service
%{_unitdir}/dovecot.socket
%else
%{_sysconfdir}/init.d/%{name}
%endif
# setting up permissions
%if ! %{with systemd}
%dir %attr(0755,root,root)        %ghost %{_var}/run/%{name}/
%dir %attr(0750,root,%{name}) %ghost %{_var}/run/%{name}/login/
%endif
%dir %attr(0750,root,root)        %{_var}/lib/%{name}/

%changelog
