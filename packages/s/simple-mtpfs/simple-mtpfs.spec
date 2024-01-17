#
# spec file for package simple-mtpfs
#
# Copyright (c) 2023 SUSE LLC
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


Name:           simple-mtpfs
Version:        0.4.0
Release:        0
Summary:        Simple MTP fuse filesystem driver
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://github.com/phatina/simple-mtpfs
Source:         https://github.com/phatina/simple-mtpfs/archive/v%{version}.tar.gz
Patch1:         disable-partial-support.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libmtp)

%description
SIMPLE-MTPFS (Simple Media Transfer Protocol FileSystem) is a file system for
Linux (and other operating systems with a FUSE implementation, such as Mac OS X
or FreeBSD) capable of operating on files on MTP devices attached via USB to
local machine. On the local computer where the SIMPLE-MTPFS is mounted, the
implementation makes use of the FUSE (Filesystem in Userspace) kernel module.
The practical effect of this is that the end user can seamlessly interact with
MTP device files.

%prep
%autosetup -p1

%build
autoreconf -fvi
%configure \
    --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
