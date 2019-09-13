#
# spec file for package posixovl
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           posixovl
Version:        1.3
Release:        0
Summary:        POSIX overlay filesystem
License:        GPL-2.0-or-later
Group:          System/Filesystems
Url:            http://posixovl.sf.net/

Source:         http://downloads.sf.net/posixovl/%name-%version.tar.xz
Source2:        http://downloads.sf.net/posixovl/%name-%version.tar.asc
Source3:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake >= 1.9
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(fuse) >= 2.6.5

%description
A FUSE filesystem that provides POSIX functionality - UNIX-style permissions,
ownership, special files - for filesystems that do not have such, e.g. vfat. It
can be seen as a contemporary equivalent of the UMSDOS fs.

%prep
%setup -q

%build
if [ ! -e configure ]; then
	autoreconf -fiv
fi
%configure
make %{?_smp_mflags}

%install
b="%buildroot"
%make_install
mkdir -p "$b/%_mandir/man8"
ln -s ../man1/posixovl.1 "$b/%_mandir/man8/mount.posixovl.8"

%files
%defattr(-,root,root)
%_sbindir/*
%_mandir/man*/*

%changelog
