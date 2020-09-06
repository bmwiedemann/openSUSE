#
# spec file for package libssh2_org
#
# Copyright (c) 2020 SUSE LLC
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


%define pkg_name libssh2
Name:           libssh2_org
Version:        1.9.0
Release:        0
Summary:        A library implementing the SSH2 protocol
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.libssh2.org/
Source0:        https://www.libssh2.org/download/%{pkg_name}-%{version}.tar.gz
Source1:        https://www.libssh2.org/download/%{pkg_name}-%{version}.tar.gz.asc
Source2:        baselibs.conf
Source3:        libssh2_org.keyring
Patch0:         libssh2-ocloexec.patch
# PATCH-FIX-UPSTREAM bsc#1154862 CVE-2019-17498
Patch1:         libssh2_org-CVE-2019-17498.patch
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
# drops build cycle in Factory
#!BuildIgnore:  groff-full

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION,
SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and
SECSH-PUBLICKEY.

%package -n libssh2-1
Summary:        A library implementing the SSH2 protocol
Group:          Development/Libraries/C and C++

%description -n libssh2-1
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION,
SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and
SECSH-PUBLICKEY.

%package -n libssh2-devel
Summary:        A library implementing the SSH2 protocol
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libssh2-1 = %{version}

%description -n libssh2-devel
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION,
SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and
SECSH-PUBLICKEY.

%prep
%setup -q -n %{pkg_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
sed -i -e 's@AM_CONFIG_HEADER@AC_CONFIG_HEADERS@g' configure.ac
cp src/libssh2_config.h.in example/libssh2_config.h
# remove m4 macro files for libtool as they should be picked up by
rm -v m4/libtool.m4 m4/lt*
autoreconf -fiv
export CFLAGS="%{optflags} -DOPENSSL_LOAD_CONF"
%configure \
    --disable-silent_rules \
    --disable-static \
    --disable-rpath \
    --with-libz=%{_prefix} \
    --with-openssl=%{_prefix}
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
rm -f  %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a

%post -n libssh2-1 -p /sbin/ldconfig
%postun -n libssh2-1 -p /sbin/ldconfig

%files -n libssh2-1
%defattr(-,root,root)
%{_libdir}/libssh2.so.1*

%files -n libssh2-devel
%defattr(-,root,root)
%doc NEWS
%{_libdir}/libssh2.so
%{_includedir}/*.h
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libssh2.pc

%changelog
