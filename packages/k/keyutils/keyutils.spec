#
# spec file for package keyutils
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


Name:           keyutils
%define lname	libkeyutils1
Url:            http://people.redhat.com/~dhowells/keyutils/
Summary:        Linux Key Management Utilities
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Kernel
Version:        1.6
Release:        0
Source0:        https://people.redhat.com/~dhowells/keyutils/%name-%version.tar.bz2
Source1:        baselibs.conf
Source3:        %name.keyring
Patch1:         request-key-cifs.patch
Patch2:         request-key-nfs4.patch
Patch3:         keyutils-nodate.patch
Patch4:         keyutils-usr-move.patch
BuildRequires:  pkgconfig(krb5)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel can call back to user space to get a
key instantiated.

%package -n %lname
Summary:        Key utilities library
Group:          System/Kernel
Obsoletes:      keyutils-libs < %version-%release
Provides:       keyutils-libs = %version-%release

%description -n %lname
This package provides a wrapper library for the key management facility
system calls.

%package devel
Summary:        Development package for building linux key management utilities
Group:          System/Kernel
Requires:       %lname = %version
Requires:       glibc-devel

%description devel
This package provides headers and libraries for building key utilities.

%prep
%setup -q
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make %{?_smp_mflags} NO_ARLIB=1 CFLAGS="%{optflags}" CC="%__cc"

%install
make install NO_ARLIB=1 DESTDIR=%{buildroot} BINDIR=/%{_bindir} SBINDIR=/%{_sbindir} LIBDIR=/%{_libdir} USRLIBDIR=%{_libdir}
mkdir -p %{buildroot}/bin %{buildroot}/sbin
ln -s /%{_bindir}/keyctl %{buildroot}/bin
ln -s /%{_sbindir}/key.dns_resolver %{buildroot}/sbin
ln -s /%{_sbindir}/request-key %{buildroot}/sbin

%post -n %lname -p /sbin/ldconfig 

%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENCE.GPL
%doc README
/sbin/*
/bin/*
/%{_sbindir}/*
/%{_bindir}/*
%{_datadir}/keyutils
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/request-key.conf
%dir %{_sysconfdir}/request-key.d/

%files -n %lname
%defattr(-,root,root,-)
%license LICENCE.LGPL
/%{_libdir}/libkeyutils.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libkeyutils.so
%{_includedir}/*
%attr(0644, root, root) %{_libdir}/pkgconfig/libkeyutils.pc

%changelog
