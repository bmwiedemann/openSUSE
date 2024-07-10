#
# spec file for package fsarchiver
#
# Copyright (c) 2023 SUSE LLC
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


Name:           fsarchiver
Version:        0.8.7
Release:        0
Summary:        Filesystem Archiver
License:        GPL-2.0-only
Group:          Productivity/Archiving/Backup
URL:            http://www.fsarchiver.org
Source0:        https://github.com/fdupoux/fsarchiver/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        HOWTO
# PATCH-FIX-UPSTREAM Remove conflicting uses of reserved identifiers
Patch0:         fsarchiver-types.patch
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
FSArchiver is a system tool that allows you to save the contents of
a file-system to a compressed archive file. The file-system can be
restored on a partition which has a different size and it can be
restored on a different file-system. Unlike tar/dar, FSArchiver also
creates the file-system when it extracts the data to partitions.
Everything is checksummed in the archive in order to protect the data.
If the archive is corrupt, you just loose the current file, not
the whole archive.

%prep
%autosetup -p1

cp -p %{SOURCE1} .

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%license COPYING
%doc ChangeLog HOWTO NEWS README THANKS internals/
%{_sbindir}/%{name}
%{_mandir}/man?/*

%changelog
