#
# spec file for package nmh
#
# Copyright (c) 2024 SUSE LLC
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


Name:           nmh
BuildRequires:  gdbm-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  postfix
Requires:       less
Requires:       smtp_daemon
Provides:       mh
Obsoletes:      mh <= 6.8.4
Version:        1.8
Release:        0
Summary:        Unix Mail Handler
License:        BSD-3-Clause
Group:          Productivity/Networking/Email/Clients
URL:            https://www.nongnu.org/nmh/
Source0:        https://download.savannah.nongnu.org/releases/nmh/%{name}-%{version}.tar.gz
Source1:        https://download.savannah.nongnu.org/releases/nmh/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM bmwiedemann https://savannah.nongnu.org/support/?109535
Patch0:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
nmh (new MH) is a powerful electronic mail handling system. It was
originally based on version 6.8.3 of the MH message system developed by
the RAND Corporation and the University of California. It is intended
to be a (mostly) compatible drop-in replacement for MH.

nmh consists of a collection of fairly simple single-purpose programs
to send, receive, save, retrieve, and manipulate e-mail messages.
Because nmh is a suite rather than a single monolithic program, you may
freely intersperse nmh commands with other commands at your shell
prompt or write custom scripts that use these commands in flexible
ways.

%prep
%autosetup -p0

%build
export HOSTNAME=OBS # for boo#1084909
%configure  --libdir=%{_libexecdir}/%name \
            --docdir=%_defaultdocdir/%name \
            --sysconfdir=%{_sysconfdir}/nmh \
	        --enable-pop \
            --with-pager=/usr/bin/less
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libexecdir}/%name
%dir %{_sysconfdir}/nmh
%config %{_sysconfdir}/nmh/*
%{_mandir}/man*/*
%_defaultdocdir/%name

%changelog
