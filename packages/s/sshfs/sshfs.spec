#
# spec file for package sshfs
#
# Copyright (c) 2025 SUSE LLC
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


Name:           sshfs
Version:        3.7.4a
Release:        0
Summary:        Filesystem client based on SSH file transfer protocol
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/deadbeefsociety/sshfs
Source0:        https://github.com/deadbeefsociety/sshfs/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/deadbeefsociety/sshfs/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:        sshfs.keyring
BuildRequires:  fuse3-devel >= 3.1.0
BuildRequires:  meson
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(glib-2.0)
Requires:       fuse3 >= 3.1.0

%description
SSHFS is a filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy to
set up: i.e. on the server side there's nothing to do.	On the client
side mounting the filesystem is as easy as logging into the server with
openssh (ssh).

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS
%{_bindir}/sshfs
%{_sbindir}/mount.fuse.sshfs
%{_sbindir}/mount.sshfs
%{_mandir}/man1/sshfs.1%{?ext_man}

%changelog
