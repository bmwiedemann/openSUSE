#
# spec file for package mbuffer
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           mbuffer
Version:        20230301
Release:        0
Summary:        Replacement for "buffer" with many more Features
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.maier-komor.de/mbuffer.html
Source:         https://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz
BuildRequires:  libtool
BuildRequires:  openssl-devel

%description
mbuffer is a raplacement for buffer with additional functionality:
- display of I/O speed
- optional use of memory mapped I/O for huge buffers
- multithreaded instead of sharedmemory ipc
- multi volume support
- autoloader support
- networking support
- compatible command-line options

%prep
%setup -q

%build
%configure \
    --enable-md5 \
    --disable-debug

%make_build SHELL=/bin/sh

%install
install -D -m 0755 mbuffer "%{buildroot}%{_bindir}/mbuffer"
install -D -m 0644 mbuffer.1 "%{buildroot}%{_mandir}/man1/mbuffer.1"

%files
%license LICENSE
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/mbuffer
%{_mandir}/man1/mbuffer.1%{?ext_man}

%changelog
