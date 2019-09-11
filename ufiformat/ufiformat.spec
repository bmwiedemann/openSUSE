#
# spec file for package ufiformat
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ufiformat
Version:        0.9.9
Release:        0
Summary:        Low-level format tool for USB floppy drives under Linux
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://github.com/tedigh/ufiformat
Source:         https://github.com/tedigh/ufiformat/archive/v%version.tar.gz
Patch1:         ufiformat-headers.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libext2fs-devel
BuildRequires:  xz

%description
ufiformat is a tool to low-level format USB floppy disks.

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc ChangeLog NEWS README
%license COPYING
%_bindir/ufiformat
%_mandir/man8/ufiformat.8.gz

%changelog
