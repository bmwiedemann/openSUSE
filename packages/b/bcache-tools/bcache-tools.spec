#
# spec file for package bcache-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bcache-tools
Summary:        Configuration utilities for bcache
License:        GPL-2.0-only
Group:          System/Base
Version:        1.0.8+suse5
Release:        0
Url:            http://bcache.evilpiepirate.org/

#Git-Clone:	http://evilpiepirate.org/git/bcache-tools.git
Source:         %name-%version.tar.xz
Patch1:         1001-udev-do-not-rely-on-DRIVER-variable.patch
BuildRequires:  libblkid-devel
BuildRequires:  libsmartcols-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkg-config
BuildRequires:  xz

%description
This package contains utilities for configuring the bcache Module.

%prep
%autosetup -p1

%build
export SUSE_ASNEEDED=0
make all CFLAGS="%optflags $(pkg-config blkid uuid smartcols --cflags) -std=gnu99" \
	LDFLAGS="$(pkg-config blkid uuid smartcols --libs)" %{?_smp_mflags}

%install
b="%buildroot"
# Without these existing, make install would fail
mkdir -p "$b"/{sbin,%_sbindir,%_mandir/man8,/lib/udev/rules.d}
mkdir -p "$b/%_sysconfdir/initramfs-tools/scripts/init-premount"
mkdir -p "$b/%_sysconfdir/initramfs-tools/hooks"
make install DESTDIR="$b" DRACUTLIBDIR="%_libexecdir/dracut"
# Not used in openSUSE
rm -Rf "$b/%_sysconfdir/initramfs-tools" "$b/%_prefix/lib/initcpio" \
	"$b/%_datadir/initramfs-tools"
mkdir -p "$b/%_prefix/lib"
mv "$b/lib/udev" "$b/%_prefix/lib/"

%files
%_sbindir/bcache-super-show
%_sbindir/make-bcache
%_sbindir/bcache
%_prefix/lib/udev
%_libexecdir/dracut/
%_mandir/man8/*.8*
%license COPYING

%changelog
