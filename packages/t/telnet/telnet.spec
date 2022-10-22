#
# spec file for package telnet
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


Name:           telnet
Version:        1.2
Release:        0
Summary:        A client program for the telnet remote login protocol
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            https://svnweb.freebsd.org/base/head/contrib/telnet/
Source:         http://distfiles.gentoo.org/distfiles/f3/telnet-bsd-%{version}.tar.bz2
Source3:        telnet.socket
Source4:        telnet@.service
Source5:        telnet.target
Patch1:         telnet-bsd-1.2-suppress_hostname.patch
Patch2:         telnet-bsd-1.2-man-page.patch
Patch3:         telnet-bsd-1.2-no_gethostbyname.patch
#PATCH-FIX-UPSTREAM fix crash when using -b option bnc#700229
Patch4:         telnet-bsd-1.2-hostalias.patch
#PATCH-FIX-UPSTREAM bnc#898481 kstreitova@suse.com -- fix the infinite loop consumes an entire CPU
Patch5:         telnet-bsd-1.2-fix-infinite-loop.patch
# PATCH-FIX-SECURITY bsc#1203759 danilo.spinella@suse.com CVE-2022-39028
# NULL pointer dereference in telnetd
Patch6:         CVE-2022-39028.patch
BuildRequires:  ncurses-devel
BuildRequires:  systemd-rpm-macros
Provides:       nkitb:%{_bindir}/telnet

%description
Telnet is an old protocol for logging into remote systems.  It is
rarely used, since the transfer is not encrypted (ssh is mostly used
these days).  The telnet client is often used for debugging other
network services. The command

telnet localhost 25

connects to the local smtp server, for example.

%package server
Summary:        A Server Program for the Telnet Remote Login Protocol
Group:          Productivity/Networking/Other
Requires:       netcfg
Provides:       nkitserv:%{_sbindir}/in.telnetd
Obsoletes:      nkitserv
%{?systemd_requires}

%description server
Telnet is a popular protocol for logging into remote systems. This
package provides the telnet daemon, which will allow remote logins into
this machine.

%prep
%setup -q -n telnet-bsd-%{version}
%patch1
%patch2
%patch3
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export CFLAGS="%{optflags} -fpie $(ncurses6-config --cflags)"
export LDFLAGS="-pie $(ncurses6-config --libs)"
%configure
%make_build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{_mandir}/man5
install -d -m 755 %{buildroot}%{_mandir}/man8
%make_install
install -D -m 644 %{SOURCE3} %{buildroot}/%{_unitdir}/telnet.socket
install -D -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}/telnet@.service
install -D -m 644 %{SOURCE5} %{buildroot}/%{_unitdir}/telnet.target

%files
%defattr(644,root,root,755)
%license COPYING
%doc ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1%{?ext_man}

%files server
%defattr(644,root,root,755)
%license COPYING
%doc ChangeLog README NEWS
%{_mandir}/man8/in.telnetd.8%{?ext_man}
%{_mandir}/man8/telnetd.8%{?ext_man}
%{_mandir}/man5/issue.net.5%{?ext_man}
%attr(755,root,root) %{_sbindir}/in.telnetd
%{_unitdir}/telnet@.service
%{_unitdir}/telnet.socket
%{_unitdir}/telnet.target

%pre server
%service_add_pre telnet.socket

%post server
%service_add_post telnet.socket

%preun server
%service_del_preun telnet.target

%postun server
%service_del_postun telnet.target

%changelog
