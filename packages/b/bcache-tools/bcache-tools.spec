#
# spec file for package bcache-tools
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


Name:           bcache-tools
Version:        1.1+git37.a5e3753
Release:        0
Summary:        Configuration utilities for bcache
License:        GPL-2.0-only
Group:          System/Base
URL:            http://bcache.evilpiepirate.org/
Source:         %name-%version.tar.xz
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)

%description
This package contains utilities for creating and inspecting
bcache filesystems.

%prep
%autosetup -p1

%build
export SUSE_ASNEEDED=0
%make_build all \
	CFLAGS="%optflags $(pkg-config blkid uuid --cflags) -std=gnu99" \
	LDFLAGS="$(pkg-config blkid uuid --libs)"
perl -i -lpe 's{^#!/usr/bin/env python\b}{#!/usr/bin/python3}' bcache-status

%install
b="%buildroot"
# Without these existing, make install would fail
mkdir -p "$b/%_sbindir" "$b/%_mandir/man8" "$b/lib/udev/rules.d"
%make_install DRACUTLIBDIR="%_prefix/lib/dracut"
# Not used in openSUSE
rm -Rf "$b/%_sysconfdir/initramfs-tools" "$b/%_prefix/lib/initcpio" \
	"$b/%_datadir/initramfs-tools"
mkdir -p "$b/%_prefix/lib"
mv "$b/lib/udev" "$b/%_prefix/lib/"

%files
%_sbindir/bcache-super-show
%_sbindir/make-bcache
%_sbindir/bcache
%_sbindir/bcache-status
%_prefix/lib/dracut/
%_prefix/lib/udev
%_mandir/man8/*.8*
%license COPYING

%changelog
