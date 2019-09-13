#
# spec file for package sdparm
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sdparm
Version:        1.10
Release:        0
Summary:        List or change SCSI disk parameters
License:        BSD-3-Clause
Group:          Hardware/Other
Url:            http://sg.danny.cz/sg/sdparm.html

#Freecode-URL:	http://freecode.com/projects/sdparm
Source:         http://sg.danny.cz/sg/p/%name-%version.tar.xz
BuildRequires:  libsgutils-devel
BuildRequires:  xz
Provides:       scsi:/sbin/sdparm

%description
SCSI disk parameters are held in mode pages. This utility lists or
changes those parameters. Other SCSI devices (or devices that use the
SCSI command set) such as CD/DVD and tape drives may also find parts of
sdparm useful. Requires the linux kernel 2.4 series or later. In the
2.6 series any device node the understands a SCSI command set may be
used (e.g. /dev/sda). In the 2.4 series SCSI device node may be used.

Warning: It is possible (but unlikely) to change SCSI disk settings
such that the disk stops operating or is slowed down. Use with care.

%prep
%setup -q

%build
# None of these is performance-critical, so use -Os rather than -O2:
CFLAGS=$(echo "%optflags" | sed 's/\-O2/-Os/')
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot" bindir="/sbin"

%files
%defattr(-,root,root)
/sbin/sas_disk_blink
/sbin/scsi_ch_swp
/sbin/sdparm
%_mandir/man8/*.8*
%doc README ChangeLog

%changelog
