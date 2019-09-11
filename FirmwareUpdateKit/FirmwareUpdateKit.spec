#
# spec file for package FirmwareUpdateKit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2008 Steffen Winterfeldt
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


Name:           FirmwareUpdateKit
Version:        2.0
Release:        0
Summary:        Tool for assisting with DOS-based firmware updates
License:        GPL-3.0-only
Group:          System/Boot
Source:         %{name}-%{version}.tar.xz
Requires:       dosfstools
%if 0%{suse_version} >= 1500
Requires:       mkisofs
%else
Requires:       genisoimage
%endif
Requires:       mtools
Requires:       syslinux
Obsoletes:      dosbootdisk
Provides:       dosbootdisk
ExclusiveArch:  %{ix86} x86_64

%description
This tool creates a bootable mini-DOS system and adds files to it.
It may be useful if one has to do firmware updates from a real-mode environment.

%prep
%setup -q

%build

%install
%make_install

%files
%{_bindir}/fuk
%{_datadir}/FirmwareUpdateKit
%license doc/COPYING

%changelog
