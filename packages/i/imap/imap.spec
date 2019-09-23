#
# spec file for package imap
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


Name:           imap
Version:        2007f_suse
Release:        0
Summary:        IMAP4, POP2, and POP3 Mail Server
License:        Apache-2.0
Group:          Productivity/Networking/Email/Servers
Url:            http://www.washington.edu/imap/
Source0:        %{name}-2007f.tar.bz2
Source1:        README.SUSE
# pam config
Source2:        %{name}.pamd
Source3:        pop.pamd
# xinetd config
Source4:        %{name}.xinetd
# c-client config
Source5:        c-client.cf
Source100:      %{name}.rpmlintrc
Patch0:         %{name}-2001a-include.diff
Patch1:         %{name}-2004a-doc.diff
Patch2:         %{name}-2002e-ssl.diff
Patch3:         %{name}-2004-cflags.diff
Patch4:         %{name}-2001a-overflow.diff
Patch5:         %{name}-2007e-c++.patch
Patch6:         %{name}-2007e.patch
Patch7:         imap-openssl.patch
Patch8:         imap-implicit-decls.patch
Patch9:         imap-2007e-poll.patch
Patch10:        imap-2007f-format-security.patch
Patch11:        imap-openssl-1.1.patch
BuildRequires:  fdupes
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
Requires:       inet-daemon
Requires(post): openssl
Requires:       pam

%description
This package contains IMAP4, POP2, and POP3 mail servers.

After installation, activate the servers in the file %{_sysconfdir}/inetd.conf.

%package -n libc-client2007f_suse
Summary:        IMAP4rev1/c-client Development Environment
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++

%description -n libc-client2007f_suse
This package contains the libraries for IMAP client programs.

%package devel
Summary:        IMAP4rev1/c-client Development Environment
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Provides:       libc-client-devel = %{version}
Requires:       libc-client2007f_suse = %{version}

%description devel
This package contains the libraries and header files for IMAP client
programs.

%prep
%setup -q -n %{name}-2007f
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

#K & R declarations of errno won't work anymore..
#it a no longer an integer but a macro that expands to a function  call
find -type f -name "*.[h,c]" -exec sed -i -e '/extern int errno;/d' {} +

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
test -f %{_sysconfdir}/profile.d/krb5.sh && . %{_sysconfdir}/profile.d/krb5.sh
GSSDIR="$(krb5-config --prefix 2>/dev/null)"
EXTRACFLAGS="$(pkg-config --cflags openssl 2>/dev/null) -DOPENSSL_NO_DEPRECATED -DOPENSSL_NO_SSL_INTERN"
EXTRACFLAGS="$EXTRACFLAGS -DDISABLE_POP_PROXY=1 %{optflags} -fno-strict-aliasing -fstack-protector"
EXTRALDFLAGS="-L $PWD/c-client"
make %{?_smp_mflags} lnp IP=6 SSLTYPE=nopwd CC=gcc \
    MYCFLAGS="$EXTRACFLAGS" \
    EXTRACFLAGS="$EXTRACFLAGS" EXTRALDFLAGS="$EXTRALDFLAGS" \
    SPECIALS="GSSDIR=${GSSDIR} SSLLIB=%{_libdir} LOCKPGM=%{_sbindir}/mlock" \
    CCLIENTLIB=-lc-client \
    SHLIBBASE=libc-client.so \
    SHLIBNAME=libc-client.so.%{version}

%install
mkdir -p %{buildroot}%{_prefix}/{sbin,share/man/man8,share/doc/packages/imap}
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m 755 imapd/imapd ipopd/ipop2d ipopd/ipop3d mtest/mtest mlock/mlock %{buildroot}%{_sbindir}/
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/%{name}
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/pop
install -m 644 -D %{SOURCE4} %{buildroot}%{_sysconfdir}/xinetd.d/%{name}
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/c-client.cf
install -m 644 src/imapd/imapd.8 %{buildroot}%{_mandir}/man8/imapd.8
install -m 644 src/ipopd/ipopd.8 %{buildroot}%{_mandir}/man8/ipopd.8
install -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/
install -m 644 CONTENTS README docs/RELNOTES %{buildroot}%{_docdir}/%{name}/
install -m 644 docs/{FAQ,bugs,imaprc,md5,naming,drivers}.txt %{buildroot}%{_docdir}/%{name}/
mkdir -p %{buildroot}/%{_includedir}/%{name}
cp src/osdep/tops-20/*.h %{buildroot}/%{_includedir}/%{name}
cp src/osdep/unix/*.h %{buildroot}/%{_includedir}/%{name}
cp src/c-client/*.h %{buildroot}/%{_includedir}/%{name}
cp c-client/linkage.{h,c} %{buildroot}/%{_includedir}/%{name}
cp c-client/osdep.h %{buildroot}/%{_includedir}/%{name}
mkdir -p %{buildroot}/%{_libdir}
install -m 644 c-client/c-client.a %{buildroot}/%{_libdir}/libc-client.a
ln -sf libc-client.a %{buildroot}/%{_libdir}/c-client.a
install -m 755 c-client/libc-client.so.%{version} %{buildroot}/%{_libdir}/
ln -sf libc-client.so.%{version} %{buildroot}/%{_libdir}/libc-client.so
ln -sf ..%{_sbindir}/imapd %{buildroot}%{_sysconfdir}/rimapd
ln -sf ..%{_sbindir}/ipop3d %{buildroot}%{_sysconfdir}/rpop3d
ln -sf ..%{_sbindir}/ipop2d %{buildroot}%{_sysconfdir}/rpop2d
%fdupes %{buildroot}%{_includedir}

%post
if [ -f %{_datadir}/ssl/certs/imapd.pem ] ; then
    if [ ! -f %{_sysconfdir}/ssl/certs/imapd.pem ] ; then
	echo "moving imapd certificate to %{_sysconfdir}/ssl/certs"
	mv %{_datadir}/ssl/certs/imapd.pem %{_sysconfdir}/ssl/certs/
    fi
fi
if [ -f %{_datadir}/ssl/certs/ipop3d.pem ] ; then
    if [ ! -f %{_sysconfdir}/ssl/certs/ipop3d.pem ] ; then
	echo "moving ipop3d certificate to %{_sysconfdir}/ssl/certs"
	mv %{_datadir}/ssl/certs/ipop3d.pem %{_sysconfdir}/ssl/certs/
    fi
fi

%post -n libc-client2007f_suse -p /sbin/ldconfig
%postun -n libc-client2007f_suse -p /sbin/ldconfig

%files
%{_sbindir}/*
%{_mandir}/man8/*
%config %{_sysconfdir}/pam.d/*
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}
%{_sysconfdir}/rimapd
%{_sysconfdir}/rpop3d
%{_sysconfdir}/rpop2d
%doc %{_docdir}/%{name}

%files -n libc-client2007f_suse
%config(noreplace) %{_sysconfdir}/c-client.cf
%{_libdir}/*.so
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.a
%{_includedir}/%{name}

%changelog
