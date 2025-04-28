#
# spec file for package encfs
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           encfs
Version:        1.9.5
Release:        0
Summary:        Userspace Encrypted File System
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Filesystems
URL:            https://vgough.github.io/encfs/
Source:         https://github.com/vgough/encfs/releases/download/v%{version}/encfs-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fuse
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(easyloggingpp)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(tinyxml2)
Requires:       fuse
Recommends:     %{name}-lang = %{version}

%description
EncFS provides an encrypted file system, layered on top of a normal
directory tree and encrypts individual files which are stored in the
hosting directory tree.

This has several advantages over the loopback encryption which
provided by the Linux kernel:
- No space is and has to be reserved, encrypted files only
  take the space that they really occupy
- Backups: encrypted files can be individually backed-up on the host
  filesystem
- Layering: Since it's hosted on a normal filesystem, encfs can be
  used on filesystems which normally have no support encryption,
  like NFS or other userspace filesystems.

EncFS is implemented as a userspace filesystem in an unprivileged
application using fuse (FUSE (Filesystem in USErspace)).

%lang_package

%prep
%autosetup -p1

%build
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
 	-DUSE_INTERNAL_TINYXML:BOOL=OFF \
	-DINSTALL_LIBENCFS:BOOL=ON \
	-DBUILD_UNIT_TESTS:BOOL=OFF \
	%{nil}
%cmake_build

%install
%cmake_install
%find_lang %{name}

%ldconfig_scriptlets

%files
%license COPYING*
%doc AUTHORS ChangeLog DESIGN.md PERFORMANCE.md README*
%{_bindir}/encfs*
%{_mandir}/man1/*.1%{?ext_man}
%{_libdir}/libencfs.so*

%files lang -f %{name}.lang
%license COPYING*

%changelog
