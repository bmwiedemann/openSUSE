#
# spec file for package fatsort
#
# Copyright (c) 2023 SUSE LLC
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


Name:           fatsort
Version:        1.6.5.640
Release:        0
Summary:        FAT Filesystem Sorting Utility
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://fatsort.sourceforge.io/
Source0:        https://sourceforge.net/projects/fatsort/files/fatsort-%{version}.tar.xz
BuildRequires:  help2man

%description
FATsort sorts directory structures of FAT filesystems. Many MP3 hardware
players don't sort files automatically but play them in the order they were
transmitted to the device. FATSort can help here.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
install -Dpm 0755 -p src/%{name}   %{buildroot}%{_sbindir}/%{name}
install -Dpm 0644 -p man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE.txt
%doc CHANGES.md README
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
