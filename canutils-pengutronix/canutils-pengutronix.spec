#
# spec file for package canutils
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           canutils-pengutronix
Summary:        Utilities for Controller Area Networks from the Pengutronix project
License:        GPL-2.0
Group:          Hardware/Other
Version:        4.0.6
Release:        0
Url:            http://pengutronix.de/software/socket-can/download/

#Git-Clone:	git://git.pengutronix.de/git/tools/canutils
Source:         http://pengutronix.de/software/socket-can/download/canutils/v4.0/canutils-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libsocketcan) >= 0.0.8
Obsoletes:      canutils <= 4.0.6

%description
SocketCAN userspace utilities and tools from Pengutronix.

CAN is a message-based network protocol designed for vehicles
originally initially created by Robert Bosch GmbH. SocketCAN is a set
of CAN drivers and a networking stack contributed by Volkswagen
Research to the Linux kernel.

This package contains some userspace utilities for the Linux
SocketCAN subsystem: canconfig candump canecho cansend cansequence.

%prep
%setup -qn canutils-%version

%build
%configure --disable-static --program-prefix="pgt-"
make %{?_smp_mflags}

%install
%make_install
# There are no development files here..
rm -Rf "%buildroot/%_libdir/pkgconfig"

%files
%defattr(-,root,root)
%_bindir/*
%_sbindir/*
%_mandir/man8/*.8*
%license COPYING

%changelog
