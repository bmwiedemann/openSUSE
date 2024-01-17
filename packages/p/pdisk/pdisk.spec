#
# spec file for package pdisk
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pdisk
Version:        0.8a
Release:        0
Summary:        Partitioning tool for PPC Macs
License:        MIT
Group:          System/Base
URL:            http://www.cfcl.com/~eryk/linux/pdisk/
#Ftp: ftp://cfcl.com/pub/ev/
Source:         pdisk.tar.gz
Patch1:         pdisk.makefile-gcc.patch
Patch2:         pdisk.makefile-deps.patch
Patch3:         pdisk.llseek.patch
Patch4:         pdisk.sys_errlist.patch
Patch5:         pdisk.edit-map-segfault.patch
Patch6:         pdisk.compute_block_size.patch
Patch7:         pdisk.default-type.patch
Patch8:         pdisk.linux-fs_h.patch
Patch9:         pdisk.type-punning.patch
Patch10:        pdisk.hfs-dump-format.patch
Patch11:        pdisk-strlen-check.patch
Patch12:        pdisk-dump_block-typepunning.patch
Patch13:        pdisk-write_partition_map-unused-result.patch
Patch14:        pdisk-print_range_list-unused-string.patch
Patch15:        pdisk.64bit.patch
Patch16:        pdisk-no-strnlen-needed.patch
ExclusiveArch:  ppc ppc64 ppc64le

%description
This tool allows you to edit Mac partition tables.

%prep
%autosetup -n pdisk -p1

%build
%make_build CFLAGS="%{optflags} -Wall -D_FILE_OFFSET_BITS=64"

%install
install -Dpm 0755 pdisk \
  %{buildroot}/sbin/pdisk
install -Dpm 0444 pdisk.8 \
  %{buildroot}%{_mandir}/man8/pdisk.8

%files
%doc README pdisk.html
/sbin/pdisk
%{_mandir}/man8/pdisk.8%{?ext_man}

%changelog
