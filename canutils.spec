#
# spec file for package canutils
#
# Copyright (c) 2020 SUSE LLC
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


Name:           canutils
Summary:        Utilities for Controller Area Networks from the Linux-CAN project
License:        GPL-2.0-only AND BSD-3-Clause
Group:          Hardware/Other
Version:        2020.12.0
Release:        0
URL:            https://github.com/linux-can/can-utils
Source:         https://github.com/linux-can/can-utils/archive/v%version.tar.gz
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
Obsoletes:      canutils-linuxcan
Provides:       canutils-linuxcan
Provides:       can-utils = %version-%release

%description
SocketCAN userspace utilities and tools.

CAN is a message-based network protocol designed for vehicles
originally initially created by Robert Bosch GmbH. SocketCAN is a set
of CAN drivers and a networking stack contributed by Volkswagen
Research to the Linux kernel.

This package contains some userspace utilities for the Linux
SocketCAN subsystem.

%prep
%autosetup -n can-utils-%version -p1

%build
if test ! -e configure; then ./autogen.sh; fi
%configure --disable-static
%make_build

%install
%make_install

%files
%_bindir/*
%doc *.md
%license LICENSES/*

%changelog
