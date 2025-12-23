#
# spec file for package dovecot
#
# Copyright (c) 2025 SUSE LLC
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


Name:           dovecot
Version:        2.4
Release:        0
Summary:        IMAP and POP3 Server Written Primarily with Security in Mind
License:        BSD-3-Clause AND LGPL-2.1-or-later AND MIT
Group:          Productivity/Networking/Email/Servers
URL:            http://www.dovecot.org/
PreReq:         dovecot-implementation
PreReq:         shadow
%sysusers_requires
Recommends:     %{name}24
#!BuildIgnore: dovecot-implementation
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Source0:        %{name}-2.0.configfiles
Source1:        %{name}-2.1.configfiles
Source2:        %{name}-2.2.configfiles
Source4:        %{name}.pam
Source5:        %{name}.README.SUSE
Source7:        %{name}.tmpfiles.d
Source8:        %{name}.service
Source9:        %{name}.socket
Source10:       %{name}-2.1-pigeonhole.configfiles
Source11:       %{name}-2.2-pigeonhole.configfiles
Source12:       %{name}-2.3.configfiles
Source13:       %{name}-2.3-pigeonhole.configfiles
Source14:       %{name}-2.4.configfiles
Source15:       %{name}-user.conf
BuildRequires:  pam-devel
BuildRequires:  sysuser-tools


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
%sysusers_generate_pre %{S:15} %{name}-user

%install
for i in $RPM_SOURCE_DIR/*.configfiles ; do
  echo "Creating ghost files for '$i'"
  for j in $(<$i) ; do
    install -D -m 0644 /dev/null %{buildroot}$j
  done
done

%{__install} -D -p -m 0644 %{S:4} %{buildroot}/%{_pam_vendordir}/%{name}
%{__install} -D -p -m 0644 %{S:5} %{buildroot}%{_datadir}/doc/packages/%{name}/README.SUSE
%{__install} -d %{buildroot}%{_sbindir}
%{__install} -D -m 644 %{S:7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%{__install} -D -p -m 0644 %{S:8} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -D -p -m 0644 %{S:9} %{buildroot}%{_unitdir}/%{name}.socket
%{__install} -D -m 0644 %{S:15} %{buildroot}%{_sysusersdir}/dovecot.conf

%pre -f %{name}-user.pre
# try to copy the default configuration.
#
# we fail silently if the dovecot-implementation package is not
# installed yet. This allows us to break a little build loop between
# dovecot and dovecotXY.
if [ ! -e %{_sysconfdir}/%{name}/%{name}.conf -a -e %{_datadir}/%{name}/example-config/%{name}.conf ] ; then
  # install default config
  echo "Did not find a /etc/dovecot/dovecot.conf. copying default configuration"
  cp -na %{_datadir}/%{name}/example-config/* %{_sysconfdir}/%{name}/
  # the chmod breaks the lda. lets use the more open permissions
fi
%service_add_pre %{name}.service %{name}.socket

%preun
%service_del_preun %{name}.service %{name}.socket

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service %{name}.socket

%postun
%service_del_postun %{name}.service %{name}.socket

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/packages/%{name}/
# conf
%dir /etc/%{name}/
%ghost %config(noreplace) /etc/%{name}/*
%ghost %dir %attr(0755,root,root) /run/dovecot/
%ghost %dir %attr(0755,root,dovecot) /run/dovecot/login/
%ghost %dir %attr(0750,root,root) %{_localstatedir}/lib/%{name}
%config(noreplace) /%{_pam_vendordir}/%{name}
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket

%changelog
