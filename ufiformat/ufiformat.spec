#
# spec file for package ufiformat
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ufiformat
Version:        0.9.9
Release:        0
Summary:        Low-level format tool for USB floppy drives under Linux
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://www.geocities.jp/tedi_world/format_usbfdd_e.html
Source:         %name-%version.tar.xz
Patch1:         ufiformat-headers.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libext2fs-devel
BuildRequires:  xz

%description
ufiformat is a tool to low-level format USB floppy disks.

%prep
%setup -q
%patch -P 1 -p1

%build
%configure 
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README 
%_bindir/ufiformat
%_mandir/man8/ufiformat.8.gz

%changelog
