#
# spec file for package pounce
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           pounce
Version:        3.1
Release:        0
Summary:        IRC bouncer
License:        GPL-3.0-or-later
URL:            https://git.causal.agency/pounce/about/
Source:         https://git.causal.agency/pounce/snapshot/%{name}-%{version}.tar.gz
BuildRequires:  ctags
# libtls is implemented by both libressl and libretls
BuildRequires:  libretls-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libtls)

%description
Pounce is a multi-client, TLS-only IRC bouncer. It maintains a persistent
connection to an IRC server, acting as a proxy and buffer for a number of
clients. When a client connects, any messages received since it last
disconnected will be relayed to it. Unlike some other bouncers, pounce uses a
single buffer for all IRC messages, which acts as a queue from which each
client reads messages independently. Pounce speaks regular modern IRC to both
servers and clients, using the server-time extension to indicate when messages
originally occurred.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc QUIRKS.7 README.7
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
