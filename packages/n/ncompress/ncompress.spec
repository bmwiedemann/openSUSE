#
# spec file for package ncompress
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.2.4.6
Release:        0
Summary:        LZW compression and decompression utilities
License:        SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
URL:            https://github.com/vapier/ncompress
Source:         https://github.com/vapier/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
%autosetup

%build
export CFLAGS="%{optflags}"
%make_build

%install
install -Dpm 0755 compress \
  %{buildroot}%{_bindir}/compress
install -Dpm 0644 compress.1 \
  %{buildroot}%{_mandir}/man1/compress.1

%check
make %{?_smp_mflags} check

%files
%license UNLICENSE
%doc LZW.INFO README.md
%{_bindir}/compress
%{_mandir}/man1/compress.1%{?ext_man}

%changelog
