#
# spec file for package ftp
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


Name:           ftp
URL:            ftp://ftp.uk.linux.org/pub/linux/Networking/netkit
Prefix:         /usr
License:        BSD-3-Clause
BuildRequires:  ncurses-devel
Group:          Productivity/Networking/Ftp/Clients
Conflicts:      lukemftp
Version:        0.17
Release:        0
Summary:        The Standard UNIX FTP Client
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         netkit-ftp-%{version}.tar.bz2
Patch0:         netkit-ftp-%{version}.dif
Patch1:         ipv6-usagi-20010122.diff
Patch2:         netkit-ftp-0.17-glibc28.patch

%description
This package provides the standard UNIX command line FTP client. FTP is
the file transfer protocol, which is a widely used Internet protocol
for transferring files.

%prep
%setup -n netkit-ftp-%{version}
%patch -P 0
%patch -P 1 -p2
%patch -P 2

%build
CFLAGS="$RPM_OPT_FLAGS -std=gnu11" CC="%__cc" ./configure --without-readline
make

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make INSTALLROOT=$RPM_BUILD_ROOT install
#ln -sf ftp $RPM_BUILD_ROOT/usr/bin/pftp
#echo ".so man1/ftp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS README
%{_bindir}/ftp
%{_bindir}/pftp
%doc %{_mandir}/man1/ftp.1.gz
%doc %{_mandir}/man1/pftp.1.gz
%doc %{_mandir}/man5/netrc.5.gz

%changelog
