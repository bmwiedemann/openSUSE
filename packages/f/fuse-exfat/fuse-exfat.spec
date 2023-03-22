#
# spec file for package fuse-exfat
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013 Sidlovsky, Yaroslav <zawertun@gmail.com>
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


Name:           fuse-exfat
Version:        1.4.0
Release:        0
Summary:        exFAT file system implementation
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/relan/exfat
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse-devel >= 2.6
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       fuse >= 2.6
Recommends:     exfat-utils

%description
This driver is an exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is
intended to replace FAT32, removing some of its limitations. exFAT is
a standard FS for SDXC memory cards.

%prep
%setup -q

%build
# force installation of manual pages
sed -i -e 's/no-installman//' configure.ac
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%post
if ! grep -q -e '^exfat$' %{_sysconfdir}/filesystems ; then
    sed -i 's/*/exfat\n*/g' %{_sysconfdir}/filesystems
    echo "Added 'exfat' to the file %{_sysconfdir}/filesystems"
fi

if ! grep -q exfat_fuse %{_sysconfdir}/filesystems ; then
    sed -i 's/*/exfat_fuse\n*/g' %{_sysconfdir}/filesystems
    echo "Added 'exfat_fuse' to the file %{_sysconfdir}/filesystems"
fi

%postun
if [ "$1" = "0" ]; then
    sed -i -e '/exfat_fuse/d' -e '/^exfat$/d' %{_sysconfdir}/filesystems
    echo "Deleted 'exfat' and 'exfat_fuse' from the file %{_sysconfdir}/filesystems"
fi

%files
%license COPYING
%doc ChangeLog README
%{_sbindir}/mount.exfat
%{_sbindir}/mount.exfat-fuse
%{_mandir}/man8/mount.exfat-fuse.8%{?ext_man}

%changelog
