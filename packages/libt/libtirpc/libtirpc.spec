#
# spec file for package libtirpc
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


Name:           libtirpc
# src/crypt_client.c and tirpc/rpcsvc/crypt.x have the BSD advertising clause
Version:        1.0.3
Release:        0
Summary:        Transport Independent RPC Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
%if 0%{suse_version} >= 1300
BuildRequires:  krb5-mini-devel
%else
BuildRequires:  krb5-devel
%endif
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkg-config
Url:            https://sourceforge.net/projects/libtirpc/
Source:         %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         000-bindresvport_blacklist.patch
# only needed on openSUSE >= 13.1, SLE >= 12
Patch1:         001-new-rpcbindsock-path.patch
# Revert upstream change until tirpc 1.0.4 with a final solutions comes out
Patch2:         002-revert-binddynport.patch
Patch3:         0001-Fix-regression-introduced-by-change-rpc-version-orde.patch
Patch16:        0001-xdrstdio_create-buffers-do-not-output-encoded-values.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define debug_package_requires libtirpc3 = %{version}-%{release}

%description
The Transport Independent RPC library (TI-RPC) is a replacement for the
standard SunRPC library in glibc which does not support IPv6 addresses.
This implementation allows the support of other transports than UDP and
TCP over IPv4.

%package -n libtirpc3
Summary:        Transport Independent RPC Library
Group:          System/Libraries
Requires:       libtirpc-netconfig >= %{version}

%description -n libtirpc3
The Transport Independent RPC library (TI-RPC) is a replacement for the
standard SunRPC library in glibc which does not support IPv6 addresses.
This implementation allows the support of other transports than UDP and
TCP over IPv4.

%package netconfig
Summary:        Netconfig configuration file for TI-RPC Library
Group:          System/Base

%description netconfig
This RPM contains the netconfig configuration file and manual page for
the TI-RPC Library.

%package devel
# src/crypt_client.c tirpc/spinlock.h and tirpc/rpcsvc/crypt.x have the BSD
# advertising clause
Summary:        Development files for the Transport Independent RPC Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libtirpc3 = %{version}

%description devel
The Transport Independent RPC library (TI-RPC) is a replacement for the
standard SunRPC library in glibc which does not support IPv6 addresses.
This implementation allows the support of other transports than UDP and
TCP over IPv4.

%prep
%setup -q -n %name-%version
%patch0 -p0
%if 0%{suse_version} >= 1310
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch16 -p1

%build
sed -i -e 's|@includedir@/tirpc|@includedir@|g' libtirpc.pc.in
/bin/sh autogen.sh
%configure --disable-static \
%if 0%{suse_version} < 1200
		--disable-gssapi \
%endif
		--libdir=/%{_lib}
make %{?_smp_mflags}

%install
# Don't strip .symtab to allow debugging
export STRIP_KEEP_SYMTAB=libtirpc*.so*
# NO_BRP_CHECK_ROOTFS is for SLES11 only, but does not harm for Factory
export NO_BRP_CHECK_ROOTFS=true
%make_install
# move devel so link to _libdir
mkdir -p %{buildroot}/%{_libdir}
ln -sv /%{_lib}/$(readlink %{buildroot}/%{_lib}/%{name}.so) %{buildroot}%{_libdir}/%{name}.so
rm -v %{buildroot}/%{_lib}/%{name}.{la,so}
mv -v %{buildroot}/%{_lib}/pkgconfig %{buildroot}/%{_libdir}
# Move RPC headers from tirpc subdirectory into main directory,
# they are now default
mv -v %{buildroot}%{_includedir}/tirpc/* %{buildroot}%{_includedir}
rmdir %{buildroot}%{_includedir}/tirpc

%post -n libtirpc3 -p /sbin/ldconfig

%postun -n libtirpc3 -p /sbin/ldconfig

%files -n libtirpc3
%defattr(-,root,root)
%license COPYING
/%{_lib}/libtirpc.so.3*

%files netconfig
%defattr(-,root,root)
%config %{_sysconfdir}/netconfig
%{_mandir}/man5/netconfig.5.gz

%files devel
%defattr(-,root,root)
%{_libdir}/libtirpc.so
/usr/include/*
/usr/%{_lib}/pkgconfig/*
%{_mandir}/man3/*

%changelog
