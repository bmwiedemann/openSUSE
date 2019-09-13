#
# spec file for package makebootfat
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           makebootfat
Version:        1.4
Release:        0
Summary:        Create Bootable FAT File Systems
License:        GPL-2.0+
Group:          System/Boot
Url:            http://advancemame.sourceforge.net
Source:         http://sourceforge.net/projects/advancemame/files/advanceboot/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  nasm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86

%description
Create bootable FAT file systems, mainly for USB disks.

%prep
%setup -q
  rm -f mbrfat.bin

%build
  %configure
  make mbrfat.bin %{?_smp_mflags}
  make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
  mkdir -p %{buildroot}/%{_libexecdir}/makebootfat
  install -m 644 mbrfat.bin %{buildroot}/%{_libexecdir}/makebootfat

%files
%defattr(-,root,root)
%{_bindir}/makebootfat
%{_libexecdir}/makebootfat
%{_mandir}/man1/makebootfat.1.gz
%doc README COPYING HISTORY

%changelog
