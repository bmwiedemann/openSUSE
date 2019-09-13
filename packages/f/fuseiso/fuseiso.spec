#
# spec file for package fuseiso
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fuseiso
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
Requires:       fuse
Summary:        FUSE module to mount CD-ROM images with ISO9660 filesystems in them
License:        GPL-2.0+
Group:          System/Filesystems
Version:        20070708
Release:        0
Source:         %{name}-%{version}.tar.bz2
Patch:          fuseiso-20061017.patch
Url:            http://apps.sourceforge.net/mediawiki/fuse/index.php?title=FuseIso
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fuseiso is a FUSE filesystem module which allows to mount many ISO9660
filesystem images (for CD-ROMs) as a non-root user using fuse.

It supports plain ISO9660 Level 1 and 2, with Rock Ridge, Joliet and
zisofs extensions and also supports the CD-ROM image types img, bin,
mdf and nrg.

%prep
%setup -q
%patch

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS README*
%{_bindir}/*

%changelog
