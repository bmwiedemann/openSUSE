#
# spec file for package fuse-exfat
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 Sidlovsky, Yaroslav <zawertun@gmail.com>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           fuse-exfat
Version:        1.4.0
Release:        0
Summary:        exFAT file system implementation
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/relan/exfat
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3)
Recommends:     exfat-utils

%description
This driver is an exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is
intended to replace FAT32, removing some of its limitations. exFAT is
a standard FS for SDXC memory cards.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc ChangeLog README
%{_sbindir}/mount.exfat
%{_sbindir}/mount.exfat-fuse
%{_mandir}/man8/mount.exfat-fuse.8%{?ext_man}

%changelog
