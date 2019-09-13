#
# spec file for package brlemu
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


BuildRequires:  ncurses-devel

Name:           brlemu
License:        GPL-2.0
Group:          Development/Tools/Other
Summary:        Emulates a braille display
Version:        0.1
Release:        37
Url:            http://sourceforge.net/
Source:         brlemu-0.1.tgz
Patch:          brlemu-fakeport.diff
Patch1:         brlemu-0.1-gcc7.diff
Patch2:         brlemu-0.1-nostrip.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Brlemu emulates a braille display. It is intended for testing braille
support without needing to acquire expensive hardware devices.

%prep
%setup -n brlemu-0.1
%patch -p1
%patch1 -p1
%patch2 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} CC="%{__cc}"

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
/usr/bin/brlemu
%doc README
%doc COPYING

%changelog
