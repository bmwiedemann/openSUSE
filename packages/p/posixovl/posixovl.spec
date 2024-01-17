#
# spec file for package posixovl
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


Name:           posixovl
Version:        1.4
Release:        0
Summary:        POSIX overlay filesystem
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            http://posixovl.sf.net/

Source:         https://inai.de/files/posixovl/%name-%version.tar.xz
Source2:        https://inai.de/files/posixovl/%name-%version.tar.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(fuse) >= 2.6.5

%description
A FUSE filesystem that provides POSIX functionality - UNIX-style permissions,
ownership, special files - for filesystems that do not have such, e.g. vfat. It
can be seen as a contemporary equivalent of the UMSDOS fs.

%prep
%autosetup

%build
%configure
%make_build

%install
b="%buildroot"
%make_install
mkdir -p "$b/%_mandir/man8"
ln -s ../man1/posixovl.1 "$b/%_mandir/man8/mount.posixovl.8"

%files
%_sbindir/*
%_mandir/man*/*

%changelog
