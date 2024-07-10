#
# spec file for package gptfdisk
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gptfdisk
Version:        1.0.10
Release:        0
Summary:        GPT partitioning and MBR repair software
License:        GPL-2.0-only
Group:          System/Base
URL:            http://rodsbooks.com/gdisk
#Git-Clone:     https://git.code.sf.net/p/gptfdisk/code gptfdisk-code
#Git-Web:       https://sourceforge.net/p/gptfdisk/code/ci/master/tree/
Source:         https://downloads.sf.net/%name/%name-%version.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(uuid)
Obsoletes:      gdisk < %version-%release
Provides:       gdisk = %version-%release

%description
Partitioning software for GPT disks and to repair MBR disks. The
gdisk, cgdisk, and sgdisk utilities (in the gdisk package) are
GPT-enabled partitioning tools; the fixparts utility (in the fixparts
package) fixes some problems with MBR disks that can be created by
buggy partitioning software.

%package fixparts
Summary:        A tool for repairing certain types of damage to MBR disks
Group:          System/Base

%description fixparts
A program that corrects errors that can creep into MBR-partitioned
disks. Removes stray GPT data, fixes mis-sized extended partitions,
and enables changing primary vs. logical partition status. Also
provides a few additional partition manipulation features.

%prep
%autosetup -p1

%build
CFLAGS="%optflags" CXXFLAGS="%optflags" %make_build

%install
b="%buildroot"
mkdir -p "$b/%_sbindir" "$b/%_mandir/man8"
install -pm0755 fixparts {,c,s}gdisk "$b/%_sbindir/"
install -pm0644 *.8 "$b/%_mandir/man8/"

%check
./gdisk_test.sh

%files
%license COPYING
%doc NEWS README
%_sbindir/gdisk
%_sbindir/sgdisk
%_sbindir/cgdisk
%_mandir/man8/gdisk.8*
%_mandir/man8/cgdisk.8*
%_mandir/man8/sgdisk.8*

%files fixparts
%_sbindir/fixparts
%_mandir/man8/fixparts.8*

%changelog
