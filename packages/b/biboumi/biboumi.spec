#
# spec file for package biboumi
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Tomáš Čech <sleep_walker@opensuse.org>
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


Name:           biboumi
Version:        8.3
Release:        0
Summary:        XMPP to IRC gateway
License:        Zlib
Group:          Productivity/Networking/IRC
URL:            https://biboumi.louiz.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  udns-devel
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)

%description
Biboumi is an XMPP gateway that connects to IRC servers and
translates between the two protocols. XMPP users can take part in IRC
discussions, using their favourite XMPP client.

It provides the following features:

 * Connection from an unlimited number of XMPP users to an unlimited number of IRC servers
 * Persistent connections to a configured list of channels, making it behave as an IRC bouncer
 * Basic channel features: join, part, view and set the topic, view and set channel or user modes, kick, nick change…
 * Private conversations
 * Notices
 * Invitations
 * IRC colors (receive only)
 * TLS connections to IRC servers
 * Channel listing
 * CTCP version and ping
 * Dynamic per-user, per-server configuration using XMPP ad-hoc commands and data-forms
 * Automatic sending of a command on connection (mostly used to send an identify message to NickServ or other authentication services)
 * Support for sending arbitrary IRC commands to a server
 * Embedded identd server
 * Message Archive Management support

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
install -m 0755 -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc CHANGELOG.rst README.rst CONTRIBUTING.rst
%dir %{_sysconfdir}/biboumi
%config %{_sysconfdir}/biboumi/*
%{_unitdir}/%{name}.service
%{_bindir}/biboumi
%{_sbindir}/rc%{name}

%changelog
