#
# spec file for package dds2tar
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dds2tar
Version:        2.5.2
Release:        0
Summary:        DDS2 Tape Streamer Utilities
License:        GPL-2.0+
Group:          Productivity/Archiving/Backup
Url:            http://www.eulesoft.de/
Source:         http://www.eulesoft.de/dds2tar-%{version}.tar.gz
Patch0:         dds2tar-%{version}.dif
Patch1:         %{name}-%{version}-without-kernel-header.diff

%description
A tool for quick extraction of individual files from a DDS2 streamer.
dds2tar can control data compression for HP DAT streamers.

%prep
%setup -q
%patch0
%patch1

%build
make CC="cc %{optflags} -fno-strict-aliasing" %{?_smp_mflags}

%install
%make_install MANDIR=%{_mandir}

%files
%doc README COPYING Changes
%{_bindir}/dds-dd
%{_bindir}/dds2index
%{_bindir}/dds2tar
%{_bindir}/ddstool
%{_bindir}/mt-dds
%{_bindir}/scsi_vendor
%{_mandir}/man1/dds-dd.1%{ext_man}
%{_mandir}/man1/dds2index.1%{ext_man}
%{_mandir}/man1/dds2tar.1%{ext_man}
%{_mandir}/man1/mt-dds.1%{ext_man}

%changelog
