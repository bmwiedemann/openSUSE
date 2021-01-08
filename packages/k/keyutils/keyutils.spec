#
# spec file for package keyutils
#
# Copyright (c) 2021 SUSE LLC
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


%define lname	libkeyutils1
Name:           keyutils
Version:        1.6.3
Release:        0
Summary:        Linux Key Management Utilities
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Kernel
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/snapshot/keyutils-%{version}.tar.gz
Source1:        baselibs.conf
Source3:        %{name}.keyring
Patch1:         request-key-cifs.patch
Patch2:         request-key-nfs4.patch
Patch3:         keyutils-nodate.patch
Patch4:         keyutils-usr-move.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(krb5)

%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel can call back to user space to get a
key instantiated.

%package -n %{lname}
Summary:        Key utilities library
License:        LGPL-2.1-or-later
Group:          System/Kernel
Obsoletes:      keyutils-libs < %{version}-%{release}
Provides:       keyutils-libs = %{version}-%{release}

%description -n %{lname}
This package provides a wrapper library for the key management facility
system calls.

%package devel
Summary:        Development package for building linux key management utilities
License:        LGPL-2.1-or-later
Group:          System/Kernel
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
This package provides headers and libraries for building key utilities.

%prep
%setup -q
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build NO_ARLIB=1 CFLAGS="%{optflags}" CC="gcc"

%install
make install NO_ARLIB=1 DESTDIR=%{buildroot} BINDIR=/%{_bindir} SBINDIR=/%{_sbindir} LIBDIR=/%{_libdir} USRLIBDIR=%{_libdir}
%if !0%{?usrmerged}
mkdir -p %{buildroot}/bin %{buildroot}/sbin
ln -s /%{_bindir}/keyctl %{buildroot}/bin
ln -s /%{_sbindir}/key.dns_resolver %{buildroot}/sbin
ln -s /%{_sbindir}/request-key %{buildroot}/sbin
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENCE.GPL
%doc README
%if !0%{?usrmerged}
/sbin/*
/bin/*
%endif
/%{_sbindir}/*
/%{_bindir}/*
%{_datadir}/keyutils
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/request-key.conf
%dir %{_sysconfdir}/request-key.d/

%files -n %{lname}
%license LICENCE.LGPL
/%{_libdir}/libkeyutils.so.*

%files devel
%{_libdir}/libkeyutils.so
%{_includedir}/*
%attr(0644, root, root) %{_libdir}/pkgconfig/libkeyutils.pc

%changelog
