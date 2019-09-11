#
# spec file for package bindfs
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


Name:           bindfs
Version:        1.13.9
Release:        0
Summary:        Mount Directories to other Locations and alter Permission Bits
License:        GPL-2.0+
Group:          System/Filesystems
Url:            http://bindfs.org/
#Git-Clone:	git://github.com/mpartel/bindfs
Source:         http://bindfs.org/downloads/%name-%version.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse) >= 2.6.0

%description
bindfs is a FUSE filesystem for mounting a directory to another
location, similarly to mount --bind. The permissions inside the
mountpoint can be altered using various rules.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc ChangeLog COPYING
%_bindir/%name
%_mandir/man1/%name.1%ext_man

%changelog
