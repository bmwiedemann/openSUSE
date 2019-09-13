#
# spec file for package ncompress
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ncompress
Version:        4.2.4.4
Release:        0
Summary:        LZW compression and decompression utilities
License:        SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
URL:            http://ncompress.sourceforge.net/
Source:         https://github.com/vapier/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-4.2.4-make.patch
Patch1:         %{name}-4.2.4.4-lfs2.patch
Patch2:         %{name}-4.2.4.4-filenamelen.patch
Patch3:         %{name}-2GB.patch
Patch6:         %{name}-4.2.4-endians.patch
# PATCH-FIX-UPSTREAM -- drop date to fix build-compare (boo#1047218)
Patch7:         ncompress-4.2.4.4-drop-datestamp.patch
# gzip provides the uncompress tool in /usr/bin
# we don't provide a link here as this conflicts with gzip
Requires:       gzip

%description
The ncompress package contains the "compress" and "uncompress"
utilities which are compatible with the original UNIX compress
utility (.Z file extensions).

Install ncompress if you need compression/decompression utilities
which are compatible with the original UNIX compress utility. gzip is
also able to decompress .Z files, though ncompress will not recognize
.gz files at all.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .lfs
%patch2 -p1 -b .filenamelen
%patch3 -p1 -b .2GB
%patch6 -p1 -b .endians
%patch7 -p1

%build
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
%ifarch sparc m68k armv4l ppc s390 s390x ppc64 sparc64
export ENDIAN=1234
%else
export ENDIAN=4321
%endif
make %{?_smp_mflags} Makefile # avoid build time race
make %{?_smp_mflags} ENDIAN="$ENDIAN"

%install
install -D -p -m 0755 compress \
  %{buildroot}%{_bindir}/compress
install -D -p -m 0644 compress.1 \
  %{buildroot}%{_mandir}/man1/compress.1

%files
%doc LZW.INFO README
%{_bindir}/compress
%{_mandir}/man1/compress.1%{?ext_man}

%changelog
