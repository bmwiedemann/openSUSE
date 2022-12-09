#
# spec file for package bindfs
#
# Copyright (c) 2022 SUSE LLC
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


Name:           bindfs
Version:        1.17.1
Release:        0
Summary:        Filesystem for mapping directories with alternate permissions
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://bindfs.org/

#Git-Clone:	https://github.com/mpartel/bindfs
Source:         https://bindfs.org/downloads/%name-%version.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse3) >= 3.10.2

%description
bindfs is a FUSE filesystem for mounting a directory to another
location, similarly to mount --bind. The permissions inside the
mountpoint can be altered using various rules.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc ChangeLog
%license COPYING
%_bindir/%name
%_mandir/man1/%name.1%ext_man

%changelog
