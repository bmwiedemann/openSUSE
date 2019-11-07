#
# spec file for package leafnode
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           leafnode
Version:        1.11.11
Release:        0
Summary:        A Leaf Site NNTP Server
License:        LGPL-2.1-or-later AND SUSE-Public-Domain AND MIT
Group:          Productivity/Networking/News/Servers
Url:            http://sourceforge.net/projects/leafnode/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        README.SUSE
Source2:        leafnode.cron.daily
Source3:        filters
Source4:        leafnode@.service
Source5:        leafnode-fetch.cron
Source6:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
# https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/pgpkeys-developers.html#pgpkey-mandree
Source7:        leafnode.keyring
Source8:        leafnode.socket
Patch0:         leafnode-1.11.6-spooldir-permissions.diff
Patch1:         fix_overflow.diff
BuildRequires:  cron
BuildRequires:  pcre-devel >= 2.06
BuildRequires:  systemd-rpm-macros
Requires:       cron
Conflicts:      cnews
Conflicts:      inn
Provides:       nntp_daemon
%{?systemd_requires}
%if 0%{?suse_version} >= 1330
Requires(pre):  group(news)
%endif

%description
Leafnode is a small NNTP server for leaf sites without permanent
connections to the Internet. It supports a subset of NNTP and is able
to automatically fetch the newsgroups the user reads regularly from the
ISP's news server.

%prep
%setup -q
%patch0
%patch1 -p1

%build
%configure\
  --with-ipv6 \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --with-spooldir=%{_localstatedir}/spool/news \
  --with-lockfile=%{_localstatedir}/spool/news/leaf.node/lock.file
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
mkdir -p %{buildroot}/%{_sysconfdir}/cron.daily
install -m 755 %{SOURCE2} %{buildroot}/%{_sysconfdir}/cron.daily/%{name}
mv %{buildroot}/%{_sysconfdir}/%{name}/config.example %{buildroot}/%{_sysconfdir}/%{name}/config
install -m 644 %{SOURCE1} .
install -m 640 %{SOURCE3} %{buildroot}/%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_mandir}/de/man1
install -d -m 755 %{buildroot}%{_mandir}/de/man8
install -D -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}/leafnode@.service
install -D -m 644 %{SOURCE8} %{buildroot}/%{_unitdir}/leafnode.socket

# Get rid of files we don't want to package or package with doc below
rm -f %{buildroot}/%{_sysconfdir}/%{name}/*.dist
rm -f %{buildroot}/%{_sysconfdir}/%{name}/UNINSTALL-daemontools
rm -f %{buildroot}/%{_sysconfdir}/%{name}/filters.example
mkdir examples
cp -a update.sh tools examples
cp %{SOURCE5} examples

%pre
%service_add_pre leafnode@.service leafnode.socket

%post
%service_add_post leafnode@.service leafnode.socket

%preun
%service_del_preun leafnode@.service leafnode.socket

%postun
%service_del_postun leafnode@.service leafnode.socket

%files
%defattr(-,root,root)
%attr(640,root,news) %config(noreplace) %{_sysconfdir}/%{name}/config
%attr(640,root,news) %config(noreplace) %{_sysconfdir}/%{name}/filters
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/cron.daily/%{name}
%attr(750,root,news) %dir %{_sysconfdir}/%{name}
%license COPYING
%doc ChangeLog CREDITS NEWS FAQ.txt FAQ.pdf
%doc README README.SUSE README-FQDN
%doc filters.example
%doc ADD-ONS KNOWNBUGS
%doc doc_german/INSTALL_de
%doc doc_german/LIESMICH-daemontools
%doc doc_german/README
%doc doc_german/README_de
%doc examples/
%{_mandir}/man1/newsq.1%{ext_man}
%{_mandir}/man1/leafnode-version.1%{ext_man}
%{_mandir}/man8/applyfilter.8%{ext_man}
%{_mandir}/man8/checkgroups.8%{ext_man}
%{_mandir}/man8/fetchnews.8%{ext_man}
%{_mandir}/man8/leafnode.8%{ext_man}
%{_mandir}/man8/texpire.8%{ext_man}
%{_bindir}/newsq
%{_bindir}/leafnode-version
%{_sbindir}/applyfilter
%{_sbindir}/checkgroups
%{_sbindir}/fetchnews
%{_sbindir}/leafnode
%{_sbindir}/texpire
%attr(775,news,news) %{_localstatedir}/spool/news
%{_unitdir}/leafnode.socket
%{_unitdir}/leafnode@.service

%changelog
