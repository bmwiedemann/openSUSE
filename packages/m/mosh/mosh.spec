#
# spec file for package mosh
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Flavio Castelli.
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


Name:           mosh
Version:        1.4.0
Release:        0
Summary:        The mobile shell
License:        GPL-3.0-or-later
Group:          Productivity/Networking/SSH
URL:            https://mosh.org/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  utempter-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(zlib)
Requires:       openssh
Requires:       perl(IO::Socket::IP)
Requires:       perl(IO::Tty)

%description
Remote terminal application that allows roaming, supports
intermittent connectivity, and provides intelligent local echo and
line editing of user keystrokes.

Mosh is a replacement for SSH. It's more robust and responsive,
especially over Wi-Fi, cellular, and long-distance links.

%prep
%setup -q

sed -i '1s@^#!.*env perl@#!/usr/bin/perl@' scripts/mosh.pl

%build
%if 0%{?suse_version} >= 1500
export CPPFLAGS=-std=c++17
%endif
autoreconf -fi
%configure \
  --enable-completion \
  --enable-client     \
  --enable-server     \
  --enable-hardening  \
  --enable-ufw        \
  --disable-examples
make %{?_smp_mflags} V=1

%install
%make_install

%check
make %{?_smp_mflags} check

%files
%dir %{_sysconfdir}/ufw/
%dir %{_sysconfdir}/ufw/applications.d/
%config %{_sysconfdir}/ufw/applications.d/mosh
%{_bindir}/mosh
%{_bindir}/mosh-client
%{_bindir}/mosh-server
%{_datadir}/bash-completion
%{_mandir}/man1/mosh.1%{?ext_man}
%{_mandir}/man1/mosh-client.1%{?ext_man}
%{_mandir}/man1/mosh-server.1%{?ext_man}

%changelog
