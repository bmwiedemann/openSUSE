#
# spec file for package kbdsniffd
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


Name:           kbdsniffd
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
Version:        0.6
Release:        0
Source:         http://www.openblinux.de/download/kbdsniffd-%{version}.tgz
Source1:        kbdsniffd.service
Url:            http://www.openblinux.de/de/index.php?page=download
Patch0:         %name-fixes.patch
Summary:        Keyboard Grabber Daemon
License:        GPL-2.0-or-later
Group:          Hardware/Other
BuildRequires:  systemd-rpm-macros
%systemd_requires
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
kbdsniffd is a keyboard grabber daemon applications like screenreaders
(sbl) can connect via network socket to the daemon and set a modifier
key to enable the grabbing mode if the modifier key is pressed all
key-strokes are send to the connected application this is useful if a
blind user wants to use a screenreader without a braille display the
grabbed keys can be used to trigger special screenreader functions

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="%{optflags} -D_POSIX_C_SOURCE=2 -D_BSD_SOURCE" LIB_CFLAGS="%{optflags} -D_POSIX_C_SOURCE=2 -D_BSD_SOURCE -fPIC" CC="%{__cc}" LD="%{__cc}"

%install 
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/etc/init.d
%make_install LIBINSTPATH=%{_libdir}
rm -rf %{buildroot}/etc/init.d
ln -sf service %{buildroot}/usr/sbin/rckbdsniffd
mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}

%post
%service_add_post %{name}.service

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr (-,root,root,755)
%doc COPYING Changelog
/usr/sbin/kbdsniffd
%{_unitdir}/%{name}.service
/usr/sbin/rckbdsniffd
%_mandir/man8/*
%config /etc/kbdsniffd.conf

%changelog
