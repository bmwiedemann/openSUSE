#
# spec file for package abootimg
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           abootimg
Version:        0.6
Release:        0
Summary:        Android boot image manipulator
License:        GPL-2.0+ and Apache-2.0
Group:          System/Boot
Url:            http://gitorious.org/ac100/abootimg
Source:         %{name}.tar.bz2
BuildRequires:  pkgconfig(blkid)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Android boot image manipulator. It can create/update/unpack boot.img - boot
file used by Android OS.

%prep
%setup -q -n %{name}

%build
# First make clean as a binary already exists in the tarball
make %{?_smp_mflags} clean
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -D -m 0755 abootimg %{buildroot}/%{_bindir}/abootimg
install -D -m 0755 abootimg-unpack-initrd %{buildroot}/%{_bindir}/abootimg-unpack-initrd
install -D -m 0755 abootimg-pack-initrd %{buildroot}/%{_bindir}/abootimg-pack-initrd
install -D -m 0644 debian/abootimg.1 %{buildroot}/%{_mandir}/man1/abootimg.1

%files
%defattr(-,root,root)
%{_bindir}/abootimg
%{_bindir}/abootimg-pack-initrd
%{_bindir}/abootimg-unpack-initrd
%{_mandir}/man1/abootimg.1%{ext_man}

%changelog
