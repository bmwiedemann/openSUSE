#
# spec file for package obexfs
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           obexfs
BuildRequires:  automake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(obexftp)
Requires:       fuse
Summary:        FUSE based filesystem using ObexFTP
License:        GPL-2.0+
Group:          System/Filesystems
Version:        0.12
Release:        0
Source:         %{name}-%{version}.tar.bz2
Url:            http://openobex.triq.net/obexfs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ObexFS is a fuse (FUSE-based filesystem) using obexftp (ObexFTP) to
access files on mobile phones.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS README*
%{_bindir}/*

%changelog
