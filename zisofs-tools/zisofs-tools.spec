#
# spec file for package zisofs-tools
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           zisofs-tools
Version:        1.0.8
Release:        0
Summary:        User tools for zisofs
License:        GPL-2.0+
Group:          System/Filesystems
Url:            http://www.kernel.org/pub/linux/utils/fs/zisofs/

#DL-URL:	http://mirror.linux.org.au/linux/utils/fs/zisofs/
Source:         http://mirror.linux.org.au/linux/utils/fs/zisofs/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  zlib-devel
Requires:       /usr/bin/mkisofs

%description
Zisofs-tools, in conjunction with a zisofs-enabled system, allows the
creation of an ISO-9660 filesystem that can be decompressed "live" on a
file-by-file basis, while still being readable by systems without
zisofs support. This package contains the tools necessary to create
such a filesystem and read compressed files on a system without zisofs
support.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --mandir=%{_mandir}
make %{?_smp_mflags}

%install
make INSTALLROOT=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc CHANGES COPYING INSTALL README
%{_bindir}/mkzftree
%doc %{_mandir}/man1/mkzftree.1*

%changelog
