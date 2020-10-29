#
# spec file for package canutils
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           canutils
Summary:        Utilities for Controller Area Networks from the Linux-CAN project
License:        GPL-2.0-only AND BSD-3-Clause
Group:          Hardware/Other
Version:        2020.02.04.g192
Release:        0
URL:            https://github.com/linux-can/can-utils

Source:         can-utils-%version.tar.xz
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
Obsoletes:      canutils-linuxcan
Provides:       canutils-linuxcan

%description
SocketCAN userspace utilities and tools.

CAN is a message-based network protocol designed for vehicles
originally initially created by Robert Bosch GmbH. SocketCAN is a set
of CAN drivers and a networking stack contributed by Volkswagen
Research to the Linux kernel.

This package contains some userspace utilities for the Linux
SocketCAN subsystem: asc2log, bcmserver, canbusload,
can-calc-bit-timing, candump, canfdtest, cangen, cangw, canlogserver,
canplayer, cansend, cansniffer, isotpdump, isotprecv, isotpperf,
isotpsend, isotpserver, isotpsniffer, isotptun, log2asc, log2long,
slcan_attach, slcand and slcanpty.

%prep
%autosetup -n can-utils-%version -p1

%build
./autogen.sh
# Avoid overlap with other canutils
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%_bindir/*

%changelog
