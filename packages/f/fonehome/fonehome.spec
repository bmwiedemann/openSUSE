#
# spec file for package fonehome
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Archie L. Cobbs <archie@dellroad.org>
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


# client side
%define clientdir   %{_datadir}/%{name}
%define scriptfile  %{_bindir}/%{name}
%define systemdsvc  %{_usr}/lib/systemd/system
%define servicefile %{name}.service
%define confdir     %{_sysconfdir}/%{name}
%define conffile    %{confdir}/%{name}.conf
%define keyfile     %{confdir}/%{name}.key
%define hostsfile   %{confdir}/%{name}.hosts
%define retrydelay  30
%define syslogfac   daemon

# server side
%define username    %{name}
%define usergroup   %{name}
%define serverdir   %{_var}/lib/%{name}-server
%define portsfile   %{_sysconfdir}/%{name}-ports.conf
%define servprikey  %{serverdir}/.ssh/id_rsa
%define servpubkey  %{servprikey}.pub
%define authkeys    %{serverdir}/.ssh/authorized_keys

%define authkeys_comment    restrict what %{username} user can do
%define authkeys_options    no-X11-forwarding,no-agent-forwarding,no-pty,permitopen="0.0.0.0:9",command="sleep 99999d"

Name:           fonehome
Version:        1.1.1
Release:        0
Summary:        Remote access to machines behind firewalls
License:        Apache-2.0
Group:          System/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Source:         %{name}-%{version}.tar.gz
Source1:        %{servicefile}.in
URL:            https://github.com/archiecobbs/%{name}/
Requires:       bc
Requires:       findutils
Requires:       openssh
Requires:       sed
%systemd_requires

%description
fonehome allows remote access to machines behind firewalls using SSH
port forwarding.

The fonehome client is a daemon that runs on remote client machines that
are behind some firewall that you either do not control or do not want
to reconfigure, but which does allow normal outgoing TCP connections. The
clients use SSH to connect to a fonehome server to which you have direct
access. The SSH connections include reverse-forwarded TCP ports which
in turn allow you to connect back to the remote machine.

This setup is useful in situations where you have several machines
deployed in the field and want to maintain access to them from a central
operations server.

%prep
%setup

%build
subst()
{
    sed -r \
      -e 's|@fonehomename@|%{name}|g' \
      -e 's|@fonehomeuser@|%{username}|g' \
      -e 's|@fonehomeconf@|%{conffile}|g' \
      -e 's|@fonehomeports@|%{portsfile}|g' \
      -e 's|@fonehomekey@|%{keyfile}|g' \
      -e 's|@fonehomehosts@|%{hostsfile}|g' \
      -e 's|@fonehomeretry@|%{retrydelay}|g' \
      -e 's|@fonehomeinit@|%{initfile}|g' \
      -e 's|@fonehomescript@|%{scriptfile}|g' \
      -e 's|@fonehomelogfac@|%{syslogfac}|g'
}
subst < %{_sourcedir}/%{servicefile}.in > %{servicefile}
subst < src/conf/fonehome.conf.sample > fonehome.conf.sample
subst < src/conf/fonehome-ports.conf.sample > fonehome-ports.conf.sample
subst < src/scripts/fonehome-init.sh > fonehome-init
subst < src/scripts/fonehome.sh > fonehome
subst < src/scripts/fhshow.sh > fhshow
subst < src/scripts/fhssh.sh > fhssh
subst < src/man/fhssh.1 > fhssh.1
subst < src/man/fhscp.1 > fhscp.1
subst < src/man/fhshow.1 > fhshow.1
subst < src/man/fonehome.1 > fonehome.1

%install

# systemd service script
install -d %{buildroot}%{systemdsvc}
install %{servicefile} %{buildroot}%{systemdsvc}/

# man pages
install -d %{buildroot}%{_mandir}/man1
install *.1 %{buildroot}%{_mandir}/man1/

# docs
install -d %{buildroot}%{_datadir}/doc/packages/%{name}
install -d %{buildroot}%{_datadir}/doc/packages/%{name}-server
install CHANGES README COPYING %{buildroot}%{_datadir}/doc/packages/%{name}/
install CHANGES README COPYING %{buildroot}%{_datadir}/doc/packages/%{name}-server/

# script files
install -d %{buildroot}%{_bindir}
install fonehome fhs{sh,how} %{buildroot}/%{_bindir}/
ln %{buildroot}/%{_bindir}/fhs{sh,cp}

# config files
install -d %{buildroot}%{confdir}
install -d %{buildroot}%{clientdir}
install fonehome.conf.sample %{buildroot}%{clientdir}/
install fonehome.conf.sample %{buildroot}%{conffile}
install fonehome-ports.conf.sample %{buildroot}%{portsfile}

# fonehome user
install -d %{buildroot}%{serverdir}/.ssh

# Create ghost files
install /dev/null %{buildroot}%{hostsfile}
install /dev/null %{buildroot}%{keyfile}
install /dev/null %{buildroot}%{servprikey}
install /dev/null %{buildroot}%{servpubkey}
install /dev/null %{buildroot}%{authkeys}

%preun
%service_del_preun %{name}.service

%postun
# No restart_on_update - don't kill the connection we might be using to update this RPM with!
%service_del_postun_without_restart %{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%files
%defattr(644,root,root,755)
%dir %attr(700,root,root) %{confdir}
%config(noreplace) %{conffile}
%ghost %attr(644,root,root) %{hostsfile}
%ghost %attr(600,root,root) %{keyfile}
%{systemdsvc}/%{servicefile}
%attr(755,root,root) %{scriptfile}
%doc %{_datadir}/doc/packages/%{name}
%{_mandir}/man1/fonehome.1*
%{clientdir}

%package server
Summary:        Server for %{name} SSH connections
Group:          System/Daemons
Requires(pre):  pwdutils
Requires(post): openssh

%description server
fonehome allows remote access to machines behind firewalls using SSH
port forwarding. This package is installed on the machine that you
want to be the fonehome server.

%pre server

# Create user and group
if ! getent group '%{usergroup}' >/dev/null 2>&1; then
    groupadd -r '%{usergroup}'
fi
if ! id '%{username}' >/dev/null 2>&1; then
    useradd -r -p '*' -d '%{serverdir}' -g '%{usergroup}' -c 'Fonehome User' -s /bin/false '%{username}'
fi

%post server

# Generate ssh key pair for user fonehome
if ! [ -e %{servprikey} ]; then

    # Generate key
    echo "creating SSH public key pair for user '%{username}'"
    rm -f %{servpubkey}
    ssh-keygen -t rsa -N '' -C '%{username}' -f %{servprikey}
    chmod 600 %{servprikey}
    chmod 644 %{servpubkey}
    chown root:root %{servprikey}
    chown %{username}:%{usergroup} %{servpubkey}

    # Allow incoming ssh connections using key, but with lots of restrictions
    sed -r 's/^((ssh|ecdsa)-[^[:space:]]+[[:space:]].*)$/# %{authkeys_comment}\n%{authkeys_options} \1/g' \
      < %{servpubkey}> %{authkeys}
    chmod 644 %{authkeys}
    chown %{username}:%{usergroup} %{authkeys}
fi

%files server
%defattr(644,root,root,755)
%{_mandir}/man1/fhssh.1*
%{_mandir}/man1/fhscp.1*
%{_mandir}/man1/fhshow.1*
%doc %{_datadir}/doc/packages/%{name}-server
%attr(755,root,root) %{_bindir}/fhshow
%attr(755,root,root) %{_bindir}/fhssh
%attr(755,root,root) %{_bindir}/fhscp
%config(noreplace missingok) %{portsfile}
%dir %attr(755,%{username},%{usergroup}) %{serverdir}
%dir %attr(700,%{username},%{usergroup}) %{serverdir}/.ssh
%ghost %verify(not size md5 mtime) %attr(600,root,root) %{servprikey}
%ghost %verify(not size md5 mtime) %attr(644,%{username},%{usergroup}) %{servpubkey}
%ghost %verify(not size md5 mtime) %attr(644,%{username},%{usergroup}) %{authkeys}

%changelog
