#
# spec file for package cyrus-sasl
#
# Copyright (c) 2022 SUSE LLC
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


%define lname	libsasl2-3
Name:           cyrus-sasl
Version:        2.1.28
Release:        0
Summary:        Implementation of Cyrus SASL API
License:        BSD-4-Clause
Group:          Productivity/Networking/Other
URL:            https://github.com/cyrusimap/cyrus-sasl/
Source:         https://github.com/cyrusimap/cyrus-sasl/releases/download/cyrus-sasl-%{version}/cyrus-sasl-%{version}.tar.gz
Source1:        cyrus-sasl-rc.tar.bz2
Source2:        README.Source
Source3:        baselibs.conf
Patch0:         cyrus-sasl.dif
Patch5:         cyrus-sasl-no_rpath.patch
Patch6:         cyrus-sasl-lfs.patch
Patch7:         fix_libpq-fe_include.diff
BuildRequires:  gdbm-devel
BuildRequires:  krb5-mini-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  opie
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
Conflicts:      cyrus-sasl-bdb
%ifarch ppc64
# bug437293
Obsoletes:      cyrus-sasl-64bit
%endif

%description
This is the Cyrus SASL API. It can be used on the client or server side
to provide authentication. See RFC 2222 for more information.

%package gssapi
Summary:        Plugin for the GSSAPI SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-gssapi

%description gssapi
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%package crammd5
Summary:        Plugin for the CRAMMD5 SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-crammd5

%description crammd5
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%package digestmd5
Summary:        Plugin for the DIGESTMD5 SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-digestmd5

%description digestmd5
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%package otp
Summary:        Plugin for the OTP SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-otp

%description otp
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%package plain
Summary:        Plugin for the PLAIN SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-plain

%description plain
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%package ntlm
Summary:        Plugin for the NTLM SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-ntlm

%description ntlm
This is the Cyrus SASL API. It can be used on the client or server side
to provide authentication. See RFC 2222 for more information.

%package gs2
Summary:        Plugin for the GS2 SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-ntlm

%description gs2
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%package scram
Summary:        Plugin for the SCRAM SASL mechanism
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      cyrus-sasl-bdb-scram

%description scram
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 5802 for more
information.

%package devel
Summary:        Cyrus SASL API Implementation, Libraries and Header Files
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel
Conflicts:      cyrus-sasl-devel-bdb
# bug437293
%ifarch ppc64
Obsoletes:      cyrus-sasl-devel-64bit
%endif

%description devel
This is the Cyrus SASL API. It can be used on the client or server side
to provide authentication. See RFC 2222 for more information.

%package -n libsasl2-3
Summary:        Simple Authentication and Security Layer (SASL) library
Group:          System/Libraries

%description -n libsasl2-3
Simple Authentication and Security Layer (SASL) is a framework for
authentication and data security in Internet protocols.

This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%prep
%setup -q -n cyrus-sasl-%{version} -a 1
if [ -e %{_builddir}/%{name}-%{version}/dlcompat-*/ ]
then
    echo "dlcompat contains potential legal risks."
    rm -rf %{_builddir}/%{name}-%{version}/dlcompat-*
fi
%patch0
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
find . -name "*.cvsignore" -exec rm -fv "{}" "+"
autoreconf -f
export CFLAGS="%optflags -fno-strict-aliasing"
%configure --with-pic \
            --with-plugindir=%{_libdir}/sasl2 \
            --with-configdir=%{_sysconfdir}/sasl2/:%{_libdir}/sasl2 \
	    --with-saslauthd=/run/sasl2/ \
	    --with-dblib=gdbm \
	    --enable-pam \
	    --enable-sample \
	    --enable-login \
	    --enable-gssapi \
	    --enable-ntlm \
	    --enable-krb4=no \
            --enable-sql=no \
	    --with-devrandom=/dev/urandom
%make_build sasldir=%{_libdir}/sasl2

%install
make DESTDIR=%{buildroot} sasldir=%{_libdir}/sasl2 install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
install -m 755 sample/.libs/client %{buildroot}%{_bindir}/cyrus_sasl_sample_client
install -m 755 sample/.libs/server %{buildroot}%{_bindir}/cyrus_sasl_sample_server
find doc -type f -exec chmod 0644 {} \;
rm -f doc/Makefile*
rm -f %{buildroot}/%{_mandir}/cat?/*
rm -f %{buildroot}/%{_mandir}/man8/saslauthd*
rm -f %{buildroot}/%{_mandir}/man8/testsaslauthd*
rm -f %{buildroot}%{_sbindir}/saslauthd
rm -f %{buildroot}%{_sbindir}/testsaslauthd
find %{buildroot} -type f -name "*.la" -delete -print

%pre
#Convert password file from berkely into gdbm
#In %pre the existing file will be dumped out

if test -x %{_bindir}/db_verify && %{_bindir}/db_verify %{_sysconfdir}/sasldb2 >/dev/null 2>&1 ; then
cat > %{_localstatedir}/adm/update-scripts/saslpw.awk <<EOF
{
        split(\$0,b,/\\\00/)
        if( b[3] == "userPassword" ) {
                user=b[1]
                domain=b[2]
        } else {
                if( user != "" ) {
                        printf("echo '%s' | saslpasswd2 -p -u %s %s\n",substr(b[1],2),user,domain)
                        user = ""
                        domain = ""
                }
        }
}
EOF
db_dump -p %{_sysconfdir}/sasldb2 | gawk -f %{_localstatedir}/adm/update-scripts/saslpw.awk > %{_localstatedir}/adm/update-scripts/saslpwd
rm -f %{_localstatedir}/adm/update-scripts/saslpw.awk
mv %{_sysconfdir}/sasldb2 %{_sysconfdir}/sasldb2-back
fi

%post
if [ -e %{_localstatedir}/adm/update-scripts/saslpwd ]; then
        chmod 755 %{_localstatedir}/adm/update-scripts/saslpwd
        %{_localstatedir}/adm/update-scripts/saslpwd
	rm -f %{_localstatedir}/adm/update-scripts/saslpwd
fi

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%{_libdir}/libsasl2.so.3*

%files
%license COPYING
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/libanonymous.so*
%{_libdir}/sasl2/liblogin.so*
%{_libdir}/sasl2/libsasldb.so*
%dir %{_sysconfdir}/sasl2/
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man3/sasl.*.gz
%{_mandir}/man8/*.gz

%files gssapi
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libgssapiv2.so*

%files crammd5
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libcrammd5.so*

%files digestmd5
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libdigestmd5.so*

%files otp
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libotp.so*

%files plain
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libplain.so*

%files ntlm
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libntlm.so*

%files gs2
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libgs2.so*

%files scram
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libscram.so*

%files devel
%license COPYING
%doc AUTHORS ChangeLog README doc
%_includedir/sasl/
%{_mandir}/man3/sasl_*.gz
%{_libdir}/libsasl2.so
%{_libdir}/pkgconfig/*

%changelog
