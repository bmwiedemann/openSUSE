#
# spec file for package curl
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


%bcond_without testsuite
%bcond_with mozilla_nss
# need ssl always for python-pycurl
%bcond_without openssl
Name:           curl
Version:        7.87.0
Release:        0
Summary:        A Tool for Transferring Data from URLs
License:        curl
URL:            https://curl.se
Source:         https://curl.se/download/curl-%{version}.tar.xz
Source2:        https://curl.se/download/curl-%{version}.tar.xz.asc
Source3:        baselibs.conf
Source4:        https://daniel.haxx.se/mykey.asc#/curl.keyring
Patch0:         libcurl-ocloexec.patch
Patch1:         dont-mess-with-rpmoptflags.patch
Patch2:         curl-secure-getenv.patch
#PATCH-FIX-OPENSUSE bsc#1076446 protocol redirection not supported or disabled
Patch3:         curl-disabled-redirect-protocol-message.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       libcurl4 = %{version}
BuildRequires:  groff
BuildRequires:  lzma
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libidn2)
# Disable metalink [bsc#1188218, CVE-2021-22923][bsc#1188217, CVE-2021-22922]
# BuildRequires:  pkgconfig(libmetalink)
#
# The 7.86.0 cURL release introduced the use of
# nghttp2_option_set_no_rfc9113_leading_and_trailing_ws_validation,
# a function introduced by the 1.50.0 nghttp2 release.
#
# This is a bandaid, as cURL didn't provide a function/version check
# in their build scripts. Without this some users my end up with a broken
# Zypper/cURL if they have a libnghttp2 < 1.50.0 yet in their system,
# and do some Zypper transaction that updates cURL, but not libnghttp2.
#
BuildRequires:  pkgconfig(libnghttp2) >= 1.50.0
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
%if %{with openssl}
BuildRequires:  pkgconfig(libssl)
%endif
%if %{with mozilla_nss}
BuildRequires:  mozilla-nss-devel
%endif
#BuildRequires:  openssh
%if 0%{?_with_stunnel:1}
# used by the testsuite
BuildRequires:  stunnel
%endif

%description
Curl is a client to get documents and files from or send documents to a
server using any of the supported protocols (HTTP, HTTPS, FTP, FTPS,
TFTP, DICT, TELNET, LDAP, or FILE). The command is designed to work
without user interaction or any kind of interactivity.

%package -n libcurl4
Summary:        Library for transferring data from URLs

%description -n libcurl4
The cURL shared library for accessing data using different
network protocols.

%package -n libcurl-devel
Summary:        Development files for the curl library
Requires:       glibc-devel
Requires:       libcurl4 = %{version}
Provides:       curl-devel = %{version}
Obsoletes:      curl-devel < %{version}

%description -n libcurl-devel
Curl is a client to get documents and files from or send documents to a
server using any of the supported protocols (HTTP, HTTPS, FTP, GOPHER,
DICT, TELNET, LDAP, or FILE). The command is designed to work without
user interaction or any kind of interactivity.

%prep
%setup -q -n curl-%{version}
%autopatch -p1

%build
# curl complains if macro definition is contained in CFLAGS
# see m4/xc-val-flgs.m4
CPPFLAGS="-D_FORTIFY_SOURCE=2"
CFLAGS=$(echo "%{optflags}" | sed -e 's/-D_FORTIFY_SOURCE=2//')
export CPPFLAGS
export CFLAGS="$CFLAGS -fPIE"
export LDFLAGS="$LDFLAGS -Wl,-z,defs,-z,now,-z,relro -pie"
autoreconf -fiv
# local hack to make curl-config --libs stop printing libraries it depends on
# (currently, libtool sets link_all_deplibs=(yes|unknown) everywhere,
# will hopefully change in the future)
sed -i 's/\(link_all_deplibs=\)unknown/\1no/' configure
%configure \
    --enable-ipv6 \
%if %{with openssl}
    --with-openssl \
    --with-ca-fallback \
    --without-ca-path \
    --without-ca-bundle \
%else
    --without-openssl \
%if %{with mozilla_nss}
    --with-nss \
%endif
%endif
    --with-gssapi=$(krb5-config --prefix) \
    --with-libidn2 \
    --with-libssh \
    --enable-symbol-hiding \
    --disable-static \
    --enable-threaded-resolver

# if this fails, the above sed hack did not work
./libtool --config | grep -q link_all_deplibs=no
# enable-hidden-symbols needs gcc4 and causes that curl exports only its API
%make_build

%if %{with testsuite}
%check
pushd tests
%make_build

find -type f -name "*.pl" -exec sed -i 's|#!.*/usr/bin/env perl|#!/usr/bin/perl|' "{}" +
find -type f -name "*.py" -exec sed -i 's|#!.*/usr/bin/env python.*|#!/usr/bin/python3|' "{}" +

perl ./runtests.pl -a -v -p '!flaky' || exit
popd
%endif

%install
%make_install
rm -f %{buildroot}%{_libdir}/libcurl.la
install -Dm 0644 docs/libcurl/libcurl.m4 %{buildroot}%{_datadir}/aclocal/libcurl.m4
pushd scripts
%make_install
popd

%post -n libcurl4 -p /sbin/ldconfig
%postun -n libcurl4 -p /sbin/ldconfig

%files
%doc README RELEASE-NOTES CHANGES
%doc docs/{BUGS.md,FAQ,FEATURES.md,TODO,TheArtOfHttpScripting.md}
%{_bindir}/curl
%{_datadir}/zsh/site-functions/_curl
%{_mandir}/man1/curl.1%{?ext_man}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/curl.fish

%files -n libcurl4
%license COPYING
%{_libdir}/libcurl.so.4*

%files -n libcurl-devel
%{_bindir}/curl-config
%{_includedir}/curl
%dir %{_datadir}/aclocal/
%{_datadir}/aclocal/libcurl.m4
%{_libdir}/libcurl.so
%{_libdir}/pkgconfig/libcurl.pc
%{_mandir}/man1/curl-config.1%{?ext_man}
%{_mandir}/man3/*
%doc docs/libcurl/symbols-in-versions

%changelog
