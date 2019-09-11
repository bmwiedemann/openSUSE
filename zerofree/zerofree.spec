#
# spec file for package zerofree
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           zerofree
Version:        1.1.1
Release:        0
Summary:        Utility for ext2,ext3,ext4 filesystems that zeroes out unallocated blocks
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            http://frippery.org/uml/
Source0:        http://frippery.org/uml/%{name}-%{version}.tgz
Source1:        http://frippery.org/uml/sparsify.c
Source2:        zerofree.8
BuildRequires:  libext2fs-devel

%description
zerofree is a utility for ext2,ext3 and ext4 filesystems that
will scan the list of free blocks in a filesystem and fill with
zeroes any blocks that do not already contain zeroes.

This RPM also includes the sparsify utility, which will scan all
files in a filesystem and ensure that they are maximally sparse.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}
gcc %{optflags} -o sparsify %{SOURCE1} -lext2fs

%install
mkdir -p %{buildroot}%{_bindir}
install -s -m 0755 zerofree %{buildroot}%{_bindir}/
install -s -m 0755 sparsify %{buildroot}%{_bindir}/
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/zerofree.8

%files
%license COPYING
%{_bindir}/sparsify
%{_bindir}/zerofree
%{_mandir}/man8/zerofree.8%{?ext_man}

%changelog
