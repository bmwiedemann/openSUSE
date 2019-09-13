#
# spec file for package mbuffer
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mbuffer
Version:        20180505
Release:        0
Summary:        Replacement for "buffer" with many more Features
License:        GPL-3.0+
Group:          Productivity/Text/Utilities
Url:            http://www.maier-komor.de/mbuffer.html
Source:         http://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

make %{?_smp_mflags} SHELL=/bin/sh

%install
install -D -m 0755 mbuffer "%{buildroot}%{_bindir}/mbuffer"
install -D -m 0644 mbuffer.1 "%{buildroot}%{_mandir}/man1/mbuffer.1"

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog LICENSE NEWS README
%{_bindir}/mbuffer
%{_mandir}/man1/mbuffer.1*

%changelog
