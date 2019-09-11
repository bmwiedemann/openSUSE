#
# spec file for package fusesmb
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


Name:           fusesmb
BuildRequires:  automake
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  samba-client
Requires:       fuse
Summary:        SMB for FUSE
License:        GPL-2.0+
Group:          System/Filesystems
Version:        0.8.7
Release:        0
Source:         %{name}-%{version}.tar.bz2
Patch:          search_path_fix.patch
Patch1:         single_thread.patch
Url:            http://www.ricardis.tudelft.nl/~vincent/fusesmb/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SMB for fuse (FUSE) is a filesystem which allows to mount a full
Network Neighborhood with samba (Samba) and other SMB shares. It works
like smbfs, but instead of accessing one share at a time, all computers
and workgroups are accessible at once from a single filesystem mount,
making network browsing just as easy as it is on Windows.

%prep
%setup
%patch -p1
%patch1 -p1

%build
autoreconf -fi
CFLAGS="%{optflags} `pkg-config --cflags smbclient`"
%configure
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog README* TODO
%{_bindir}/*
%{_mandir}/*/fusesmb*

%changelog
