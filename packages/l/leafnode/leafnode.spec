#
# spec file
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


%define spooldir    %{_localstatedir}/spool/news
%define confdir     %{_sysconfdir}/leafnode
%define runas_user  news
%define runas_group news
%define admin_user  newsadmin
%define admin_group newsadmin
%define upname leafnode
Name:           %{upname}
Version:        2.0.0+git.1677927696.44d2783
Release:        0
Summary:        Leaf site NNTP server
License:        MIT
Summary(de):    Ein offline-Newsserver
URL:            http://www.dt.e-technik.uni-dortmund.de/~ma/leafnode/beta/
# Use checkout from the git repo at
# https://gitlab.com/leafnode-2/leafnode-2/
Source0:        %{name}-%{version}.tar.xz
Source1:        README-SUSE.rst
Patch1:         harden_leafnode@.service.patch
BuildRequires:  autoconf >= 2.68
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pcre-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  shadow
BuildRequires:  pkgconfig(systemd)
Requires(post): coreutils
Requires(post): systemd
Requires(postun):systemd
Requires(pre):  permissions
Requires(pre):  shadow
Requires(preun):systemd
# Because of moderators(5) manpage, and really these two
# shouldn't be on one system at once.
Conflicts:      inn
Obsoletes:      leafnode < %{version}
Provides:       leafnode = %{version}-%{release}
#
Provides:       user(%runas_user)
Provides:       group(%admin_group)
Provides:       group(%runas_group)
Provides:       user(%admin_user)
# For postfix
Requires(pre):  (group(maildrop) and postfix)

%description
Leafnode is a small NNTP server for leaf sites without permanent
connection to the internet. It supports a subset of NNTP and is able to
automatically fetch the newsgroups the user reads regularly from the
newsserver of the ISP and additionally offer local (site-specific)
groups to a LAN.

%description -l de
Leafnode ist ein offline-Newsserver, der vor allem für den typischen
Einzelnutzer-Rechner ohne permanente Internetanbindung geeignet ist.
Leafnode bezieht automatisch die Newsgroups, die der oder die Nutzer
regelmäßig lesen, vom Newsserver des Providers. Weiter erlaubt es, lokale
(Standort-spezifische) Newsgruppen im LAN anzubieten.

%prep
%autosetup -p1 -n %{name}-%{version}

autoreconf -v -i

cp -p %{SOURCE1} .

%build
%configure \
 --disable-silent-rules \
 --enable-spooldir=%{spooldir} \
 --enable-runas-user=$(id -un) \
 --sysconfdir=%{_sysconfdir}/%{upname} --with-pam
%make_build

%check
%make_build check

%install
# first clean out any prior aborted runs
%make_install

# We actually do not want filters to be installed in /etc/leafnode
rm %{buildroot}/%{_sysconfdir}/leafnode/filters*

# install systemd units
install -D -m 644 -t %{buildroot}%{_unitdir} systemd/*

for file in %{buildroot}/%{_sysconfdir}/leafnode/*.example ; do
   NEWFN=$(basename $file .example);
   mv $file %{buildroot}/%{_sysconfdir}/leafnode/$NEWFN
done

# When building without runas_user, then we need to set this
# parameter explicitly.
sed -i -e "s/^#\s*run_as_user.*\$/run_as_user = %{runas_user}/" \
    %{buildroot}/%{_sysconfdir}/leafnode/config

cat >%{buildroot}/%{_sysconfdir}/leafnode/local.groups << EOS
# List of all local groups
# The format of the file containing the local groups is
# news.group.name[tab]status[tab]Description
# where
# status could be y, n, or m letter, where
# y - "Local postings are allowed",
# m - "The group is moderated and all postings must be approved.",
# n - "No local postings are allowed, only articles from peers."
EOS

# Droplet for sudoers
install -d -m 750 %{buildroot}/%{_sysconfdir}/sudoers.d
echo "%"%{admin_group}"  ALL = (%{runas_user}) NOPASSWD:/usr/sbin/fetchnews" \
    > %{buildroot}%{_sysconfdir}/sudoers.d/leafnode

%pre
%service_add_pre leafnode.service leafnode.socket leafnode@.service leafnode-daily.service leafnode-hourly.service leafnode-daily.timer leafnode-hourly.timer

# create daemon group, if not existing
getent group %{runas_group} >/dev/null || groupadd -r %{runas_group}  2>/dev/null || :
getent group %{admin_group} >/dev/null || groupadd -r %{admin_group}  2>/dev/null || :
# create daemon user, if not existing
getent passwd %{runas_user} >/dev/null || \
    useradd -r -g %{runas_group} -s /bin/false -c "leafnode daemon" \
        -d %{spooldir} %{runas_user}  2>/dev/null || :
getent passwd %{admin_user} >/dev/null || \
    useradd -r -g %{admin_group} -s /bin/false -c "leafnode administration" \
        -d %{spooldir} %{admin_user}  2>/dev/null || :
# if postfix is installed
test -x /sbin/postdrop && usermod -a -G maildrop %{runas_user}
exit 0

%post
%set_permissions %{spooldir}/leaf.node
%service_add_post leafnode.service leafnode.socket leafnode@.service leafnode-daily.service leafnode-hourly.service leafnode-daily.timer leafnode-hourly.timer

%preun
%service_del_preun leafnode.service leafnode.socket leafnode@.service leafnode-daily.service leafnode-hourly.service leafnode-daily.timer leafnode-hourly.timer

%postun
%service_del_postun leafnode.service leafnode.socket leafnode@.service leafnode-daily.service leafnode-hourly.service leafnode-daily.timer leafnode-hourly.timer

%files
%license COPYING COPYING.LGPL
%doc config.example filters.example CREDITS README-SUSE.rst
%doc DEBUGGING ENVIRONMENT FAQ.tex CHANGES-FROM-LEAFNODE-1 NEWS
%doc README-FQDN.tex TODO ChangeLog AUTHORS README-leaf.node README.html
%attr(644,root,root) %{_unitdir}/%{upname}*
%dir %{_sysconfdir}/leafnode/
%config(noreplace) %attr(640,root,news) %{_sysconfdir}/leafnode/config
%config(noreplace) %attr(640,root,news) %{_sysconfdir}/leafnode/uucp
%config(noreplace) %attr(640,root,news) %{_sysconfdir}/leafnode/local.groups
%dir %{_sysconfdir}/sudoers.d
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/sudoers.d/leafnode
%attr(755,root,root) %{_bindir}/leafnode-version
%attr(755,root,root) %{_bindir}/lsmac.pl
%attr(755,root,root) %{_bindir}/newsq
%attr(755,root,root) %{_sbindir}/applyfilter
%attr(755,root,root) %{_sbindir}/checkgroups
%attr(755,root,root) %{_sbindir}/fetchnews
%attr(755,root,root) %{_sbindir}/leafnode
%attr(755,root,root) %{_sbindir}/rnews
%attr(755,root,root) %{_sbindir}/sendbatch.bash
%attr(755,root,root) %{_sbindir}/texpire
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%attr(775,%{runas_user},%{runas_group}) %{spooldir}

%changelog
