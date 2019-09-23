#
# spec file for package pdisk
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pdisk
Summary:        Partitioning tool for PPC Macs
License:        MIT
Group:          System/Base
Version:        0.8a
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://www.cfcl.com/~eryk/linux/pdisk/
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



Authors:
--------
    Eryk Vershen <eryk@apple.com>

%prep
%setup -q -n pdisk
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall -D_FILE_OFFSET_BITS=64" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -m755 pdisk $RPM_BUILD_ROOT/sbin/pdisk
install -m444 pdisk.8 $RPM_BUILD_ROOT%{_mandir}/man8/pdisk.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/pdisk
%{_mandir}/man8/pdisk.8.gz
%doc README pdisk.html

%changelog
