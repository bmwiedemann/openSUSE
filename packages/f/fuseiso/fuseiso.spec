#
# spec file for package fuseiso
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


Name:           fuseiso
Version:        20070708
Release:        0
Summary:        FUSE module to mount CD-ROM images with ISO9660 filesystems in them
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://sourceforge.net/projects/fuseiso/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-fuse3.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)
Requires:       fuse3

%description
Fuseiso is a FUSE filesystem module which allows to mount many ISO9660
filesystem images (for CD-ROMs) as a non-root user using fuse.

It supports plain ISO9660 Level 1 and 2, with Rock Ridge, Joliet and
zisofs extensions and also supports the CD-ROM image types img, bin,
mdf and nrg.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}

%changelog
