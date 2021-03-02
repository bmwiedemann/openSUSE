#
# spec file for package cyrus-sasl-bdb
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


Name:           cyrus-sasl-bdb
%define lname   libsasl2-3
Version:        2.1.27
Release:        0
URL:            http://asg.web.cmu.edu/sasl/
Summary:        Implementation of Cyrus SASL API
License:        BSD-4-Clause
Group:          Productivity/Networking/Other

Source:         cyrus-sasl-%{version}.tar.gz
Source1:        cyrus-sasl-rc.tar.bz2
Source2:        README.Source
Source3:        baselibs.conf
Patch:          cyrus-sasl.dif
# see https://github.com/cyrusimap/cyrus-sasl/issues/587
Patch1:         cyrus-sasl-bug587.patch
Patch5:         cyrus-sasl-no_rpath.patch
Patch6:         cyrus-sasl-lfs.patch
Patch7:         fix_libpq-fe_include.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libsasl2-3
BuildRequires:  db-devel
BuildRequires:  krb5-mini-devel
BuildRequires:  libsasl2-3
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  opie
BuildRequires:  pam-devel
BuildRequires:  pkg-config
%ifarch ppc64
# bug437293
Obsoletes:      cyrus-sasl-64bit
%endif
Conflicts:      cyrus-sasl

%package      gssapi
Summary:        Plugin for the GSSAPI SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-gssapi

%package      crammd5
Summary:        Plugin for the CRAMMD5 SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-crammd5

%package      digestmd5
Summary:        Plugin for the DIGESTMD5 SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-digestmd5

%package      otp
Summary:        Plugin for the OTP SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-otp

%package      plain
Summary:        Plugin for the PLAIN SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-plain

%package      ntlm
Summary:        Plugin for the NTLM SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-ntlm

%package      gs2
Summary:        Plugin for the GS2 SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-gs2

%package      scram
Summary:        Plugin for the SCRAM SASL mechanism
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl-bdb = %{version}
Conflicts:      cyrus-sasl-scram

%package      devel
# bug437293
%ifarch ppc64
Obsoletes:      cyrus-sasl-devel-64bit
%endif
#
Summary:        Cyrus SASL API Implementation, Libraries and Header Files
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel
Conflicts:      cyrus-sasl-devel

%description
This is the Cyrus SASL API. It can be used on the client or server side
to provide authentication. See RFC 2222 for more information.

%description gssapi
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%description devel
This is the Cyrus SASL API. It can be used on the client or server side
to provide authentication. See RFC 2222 for more information.

%description digestmd5
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%description crammd5
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%description otp
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%description plain
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%description ntlm
This is the Cyrus SASL API. It can be used on the client or server side
to provide authentication. See RFC 2222 for more information.

%description gs2
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%description scram
This is the Cyrus SASL API implementation. It can be used on the client
or server side to provide authentication. See RFC 5802 for more
information.

%prep
%setup -q -n cyrus-sasl-%{version} -a 1
if [ -e %{_builddir}/cyrus-sasl-%{version}/dlcompat-*/ ]
then
    echo "dlcompat contains potential legal risks."
    rm -rf %{_builddir}/cyrus-sasl-%{version}/dlcompat-*
fi
%patch
%patch1 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
find . -name "*.cvsignore" -exec rm -fv "{}" "+"
autoreconf -f
export CFLAGS="%optflags -fno-strict-aliasing"
%configure --with-pic \
            --with-plugindir=%{_libdir}/sasl2 \
            --with-configdir=/etc/sasl2/:%{_libdir}/sasl2 \
	    --with-saslauthd=/run/sasl2/ \
	    --enable-pam \
	    --enable-sample \
	    --enable-login \
	    --enable-gssapi \
	    --enable-ntlm \
	    --enable-krb4=no \
            --enable-sql=no \
	    --with-devrandom=/dev/urandom
%{__make} %{?_smp_mflags} sasldir=%{_libdir}/sasl2

%install
make DESTDIR=$RPM_BUILD_ROOT sasldir=%{_libdir}/sasl2 install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/sasl2
install -m 755 sample/.libs/client $RPM_BUILD_ROOT/usr/bin/cyrus_sasl_sample_client
install -m 755 sample/.libs/server $RPM_BUILD_ROOT/usr/bin/cyrus_sasl_sample_server
chmod 0644 doc/*
rm -f doc/Makefile*
rm -f $RPM_BUILD_ROOT/%{_mandir}/cat?/*
rm -f $RPM_BUILD_ROOT/%{_mandir}/man8/saslauthd*
rm -f $RPM_BUILD_ROOT/usr/sbin/saslauthd
rm -f $RPM_BUILD_ROOT/usr/sbin/testsaslauthd
rm -r $RPM_BUILD_ROOT%{_libdir}/libsasl2.so.3*
find "%buildroot" -type f -name "*.la" -print -delete

%files
%defattr(-,root,root)
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/libanonymous.so*
%{_libdir}/sasl2/liblogin.so*
%{_libdir}/sasl2/libsasldb.so*
%dir /etc/sasl2/
/usr/sbin/*
/usr/bin/*
%doc %{_mandir}/man3/sasl.*.gz
%doc %{_mandir}/man8/*.gz
%doc COPYING

%files gssapi
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libgssapiv2.so*

%files crammd5
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libcrammd5.so*

%files digestmd5
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libdigestmd5.so*

%files otp
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libotp.so*

%files plain
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libplain.so*

%files ntlm
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libntlm.so*

%files gs2
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libgs2.so*

%files scram
%defattr(-,root,root)
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libscram.so*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README doc
%_includedir/sasl/
%doc %{_mandir}/man3/sasl_*.gz
%{_libdir}/libsasl2.so
%{_libdir}/pkgconfig/*

%changelog
