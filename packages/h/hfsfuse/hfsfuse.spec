#
# spec file for package hfsfuse
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           hfsfuse
Version:        0.400
Release:        0
Summary:        FUSE driver for HFS+ filesystems
License:        BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND MIT
Group:          System/Filesystems
URL:            https://github.com/0x09/hfsfuse
Source:         https://github.com/0x09/hfsfuse/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch:          no-incompatible-pointer-types.patch
BuildRequires:  fuse3-devel
BuildRequires:  libarchive-devel
BuildRequires:  lzfse-devel
BuildRequires:  utf8proc-devel
BuildRequires:  zlib-devel

%description
FUSE driver for HFS+ filesystems, based on NetBSD's kernel driver with modifications.

hfsfuse embeds and extends NetBSD's HFS+ kernel driver into a portable library for use
with FUSE and other userspace tools. hfsfuse was created for use on FreeBSD and other
Unix-like systems that lack a native HFS+ driver, but can also be used on Linux and
macOS as an alternative to their kernel drivers.

hfsfuse also includes two standalone tools, hfsdump and hfstar, which can be used
without FUSE.

This driver is read-only and cannot write to or alter the target filesystem.

Supported

 * Journaled and non-journaled HFS+
 * Unicode normalization for pathnames via utf8proc
 * Hard links, including directory hard links (i.e. Time Machine backups)
 * Resource fork, Finder info, and creation/backup time access via extended attributes
 * birthtime (with compatible FUSE)
 * User-defined extended attributes
 * HFS+ compression with zlib and lzfse

Not supported

 * HFS without the "+", aka "Mac OS Standard" volumes. For these, try hfsutils.
 * Writing

%prep
%autosetup -p1

%build
%make_build WITH_UBILIO=local WITH_UTF8PROC=system

%install
%make_install WITH_UBILIO=local WITH_UTF8PROC=system PREFIX=%{_prefix}

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/hfsdump
%{_bindir}/hfsfuse
%{_bindir}/hfstar

%changelog
