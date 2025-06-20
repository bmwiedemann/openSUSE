#
# spec file for package ifuse
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ifuse
Version:        1.1.4
Release:        0
Summary:        Filesystem access for Apple devices
License:        LGPL-2.0-or-later
Group:          System/Filesystems
URL:            https://www.libimobiledevice.org
Source:         https://github.com/libimobiledevice/ifuse/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch0:         ifuse-1.1.4-fuse3.patch
# for ifuse-1.1.4-fuse3.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libimobiledevice-devel >= 1.3.0
BuildRequires:  libplist-2_0-devel >= 2.2.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3)

%description
iFuse is a FUSE filesystem driver which uses `libimobiledevice` to connect to
devices without the need for a jailbreak.
It is using the native Apple "AFC" protocol, over the normal USB cable in order
to access the iPhone's, iPod Touch's or iPad's media files under Linux.

%prep
%autosetup -p1

%build
export CPPFLAGS=-D_FILE_OFFSET_BITS=64
# for ifuse-1.1.4-fuse3.patch
autoreconf -fiv
%configure
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README.md NEWS
%{_bindir}/ifuse
%{_mandir}/man1/ifuse.1%{?ext_man}

%changelog
