#
# spec file for package talk
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


%global         ncursesw_config %(set -- %{_bindir}/ncursesw*-config; echo ${1})
Name:           talk
Version:        0.17
Release:        0
Summary:        Talk Client for Chatting with Another User
License:        BSD-3-Clause
Group:          Productivity/Networking/Talk/Clients
Url:            ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/
Source:         netkit-ntalk-%{version}.tar.bz2
Source4:        ntalk.service
Source5:        ntalk.socket
Patch0:         netkit-ntalk-%{version}.dif
Patch1:         netkit-ntalk-multibyte.diff
Patch2:         netkit-ntalk-%{version}-alt-talkd.patch
Patch3:         netkit-ntalk-%{version}-strip.diff
Patch4:         netkit-ntalk-%{version}-dont-resolve.patch
Patch5:         netkit-n%{name}-0.17-dots_in_usernames.patch
# PATCH-FIX-UPSTREAM netkit-ntalk-0.17-close_file_on_failure.patch
Patch6:         netkit-ntalk-0.17-close_file_on_failure.patch
Patch7:         netkit-ntalk-curses-lvalue.patch
BuildRequires:  ncurses-devel
Provides:       nkitb:%{_bindir}/talk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  systemd-rpm-macros

%description
This package contains the talk client, which allows you to chat with
another user on a different system. Talk is a communication program
which copies lines from one terminal to that of another user.

%package server
Version:        0.17
Release:        0
Summary:        Talk Daemon to Chat with Another User
Group:          Productivity/Networking/Talk/Servers
Requires:       net-tools
Requires:       netcfg
Provides:       nkitserv:%{_sbindir}/in.talkd
%{?systemd_requires}

%description server
This package contains the talk daemon, which allows you to chat with
another user on a different system. Talk is a communication program
which copies lines from one terminal to the terminal of another user.

%prep
%setup -q -n netkit-ntalk-%{version}
%patch0
%patch1 -p1 -b .mb
%patch2 -p1
%patch3
%patch4
%patch5
%patch6
%patch7 -p1

%build
# Not autotools configure macro
CFLAGS="%{optflags}" ./configure
cat <<-EOF >> MCONFIG
	LIBCURSES=$(%{ncursesw_config} --libs)
	CFLAGS += -D_GNU_SOURCE -fPIE  $(%{ncursesw_config} --cflags)
	LDFLAGS += -pie
EOF
make %{?_smp_mflags}

%install
install -d -m 755 %{buildroot}%{_prefix}/{bin,sbin}
install -d -m 755 %{buildroot}%{_mandir}/man{1,8}
make install INSTALLROOT=%{buildroot}
install -D -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}/ntalk.service
install -D -m 644 %{SOURCE5} %{buildroot}/%{_unitdir}/ntalk.socket

%files
%defattr(-,root,root)
%doc BUGS ChangeLog
%{_bindir}/talk
%{_mandir}/man1/*

%pre server
%service_add_pre ntalk.socket

%post server
%service_add_post ntalk.socket

%preun server
%service_del_preun ntalk.socket

%postun server
%service_del_postun ntalk.socket

%files server
%defattr(-,root,root)
%doc BUGS ChangeLog
%{_mandir}/man8/*
%{_sbindir}/in.ntalkd
%{_sbindir}/in.talkd
%{_unitdir}/ntalk.socket
%{_unitdir}/ntalk.service

%changelog
