#
# spec file for package canutils
#
# Copyright (c) 2025 SUSE LLC
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
%define lname   libisobusfs-suse0
Version:        2025.01
Release:        0
Summary:        Utilities for Controller Area Networks from the Linux-CAN project
License:        BSD-3-Clause AND GPL-2.0-only AND LGPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/linux-can/can-utils
Source:         https://github.com/linux-can/can-utils/archive/refs/tags/v%version.tar.gz
Patch1:         0001-build-give-libisobusfs-a-version.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  pkg-config
BuildRequires:  xz
Obsoletes:      canutils-linuxcan
Provides:       can-utils = %version-%release
Provides:       canutils-linuxcan

%description
SocketCAN userspace utilities and tools.

CAN is a message-based network protocol designed for vehicles
originally initially created by Robert Bosch GmbH. SocketCAN is a set
of CAN drivers and a networking stack contributed by Volkswagen
Research to the Linux kernel.

This package contains some userspace utilities for the Linux
SocketCAN subsystem.

%package -n libisobusfs0
Summary:        Component library for can-utils
Group:          System/Libraries
License:        LGPL-2.0-only

%description -n libisobusfs0
Component library for the CAN utilities.

%prep
%autosetup -n can-utils-%version -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# headers are useless at present - https://github.com/linux-can/can-utils/issues/578
rm -Rf "%buildroot/%_includedir" "%buildroot/%_libdir/libisobusfs.so"

%ldconfig_scriptlets -n libisobusfs0

%files
%doc *.md
%license LICENSES/*
%_bindir/*

%files -n libisobusfs0
%_libdir/libisobusfs.so.*

%changelog
