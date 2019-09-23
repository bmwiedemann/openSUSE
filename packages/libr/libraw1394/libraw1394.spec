#
# spec file for package libraw1394
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


Name:           libraw1394
Version:        2.1.1
Release:        0
Summary:        A Firewire Interface library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.dennedy.org/libraw1394/

#Git-Web:	https://git.kernel.org/cgit/libs/ieee1394/libraw1394.git/
#Git-Clone:	git://git.kernel.org/pub/scm/libs/ieee1394/libraw1394
Source:         https://www.kernel.org/pub/linux/libs/ieee1394/%name-%version.tar.xz
Source2:        https://www.kernel.org/pub/linux/libs/ieee1394/%name-%version.tar.sign
Source3:        %name.keyring
Source4:        baselibs.conf
Patch0:         libraw1394.no-isodump.patch
Patch1:         libraw1394-exports.patch
BuildRequires:  libtool
BuildRequires:  openjade-devel
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libraw1394 provides direct access to the connected 1394 buses to
userspace. Through this library, applications can directly send to
and receive from other nodes without requiring a kernel driver for
the protocol in question.

%package 11
Summary:        A Firewire Interface library
Group:          System/Libraries

%description 11
libraw1394 provides direct access to the connected 1394 buses to
userspace. Through this library, applications can directly send to
and receive from other nodes without requiring a kernel driver for
the protocol in question.

libraw1394 abstracts the interface that is used to communicate with
the kernel. It works with both the Juju stack (firewire-core.ko;
/dev/fw*; present since Linux kernel 2.6.22) and the old Linux1394
(raw1394.ko; /dev/raw1394; present until 2.6.36).

%package devel
Summary:        Development files for libraw1394
Group:          Development/Libraries/C and C++
Summary(pt_BR): Arquivos de desenvolvimento e cabeçalhos para o libraw1394
Requires:       %{name}-11 = %{version}
Requires:       glibc-devel

%description devel
libraw1394 provides direct access to the connected 1394 buses to
userspace. Through this library, applications can directly send to
and receive from other nodes without requiring a kernel driver for
the protocol in question.

This subpackage contains the library links and headers for
libraw1394.

%package tools
Summary:        Command-line utilties to manipulate IEEE1394 devices
Group:          Hardware/Other
# added on 2015-11-14
Obsoletes:      %name < %version-%release
Provides:       %name = %version-%release

%description tools
Command-line utilities to inspect and send IEEE 1394 isochronous
packets, and to test the basic functionality of raw1394.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf --force --install
%configure --disable-static
make %{?_smp_mflags} all

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# empty dependency libs
rm -f %{buildroot}%{_libdir}/libraw1394.la

%post 11 -p /sbin/ldconfig

%postun 11 -p /sbin/ldconfig

%files tools
%defattr(-,root,root)
%doc AUTHORS COPYING* NEWS README
%{_bindir}/testlibraw
%{_bindir}/dumpiso
%{_bindir}/sendiso
%{_mandir}/man1/*

%files 11
%defattr(-,root,root)
%{_libdir}/libraw1394.so.11*

%files devel
%defattr(-,root,root)
%{_includedir}/libraw1394
%{_libdir}/libraw1394.so
%{_libdir}/pkgconfig/libraw1394.pc

%changelog
