#
# spec file for package curl
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


%bcond_without testsuite
%bcond_with mozilla_nss
# need ssl always for python-pycurl
%bcond_without openssl
Name:           curl
Version:        7.73.0
Release:        0
Summary:        A Tool for Transferring Data from URLs
License:        curl
URL:            https://curl.haxx.se/
Source:         https://curl.haxx.se/download/curl-%{version}.tar.xz
Source2:        https://curl.haxx.se/download/curl-%{version}.tar.xz.asc
Source3:        baselibs.conf
Source4:        https://daniel.haxx.se/mykey.asc#/curl.keyring
Patch0:         libcurl-ocloexec.patch
Patch1:         dont-mess-with-rpmoptflags.diff
Patch2:         curl-secure-getenv.patch
# PATCH-FIX-OPENSUSE bsc#1076446 protocol redirection not supported or disabled
Patch4:         curl-disabled-redirect-protocol-message.patch
Patch5:         curl-use_OPENSSL_config.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       libcurl4 = %{version}
BuildRequires:  groff
BuildRequires:  lzma
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libmetalink)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libssh)
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
%patch0 -p1
%patch1
%patch2
%patch4 -p1
%patch5 -p1

# disable new failing test 1165
echo "1165" >> tests/data/DISABLED

%build
# curl complains if macro definition is contained in CFLAGS
# see m4/xc-val-flgs.m4
CPPFLAGS="-D_FORTIFY_SOURCE=2"
CFLAGS=$(echo "%{optflags}" | sed -e 's/-D_FORTIFY_SOURCE=2//')
export CPPFLAGS CFLAGS
export CFLAGS="$CFLAGS -fPIE"
export LDFLAGS="$LDFLAGS -pie"
autoreconf -fiv
# local hack to make curl-config --libs stop printing libraries it depends on
# (currently, libtool sets link_all_deplibs=(yes|unknown) everywhere,
# will hopefully change in the future)
sed -i 's/\(link_all_deplibs=\)unknown/\1no/' configure
%configure \
    --enable-ipv6 \
%if %{with openssl}
    --with-ssl \
    --with-ca-fallback \
    --without-ca-path \
    --without-ca-bundle \
%else
    --without-ssl \
%if %{with mozilla_nss}
    --with-nss \
%endif
%endif
    --with-gssapi=$(krb5-config --prefix) \
    --with-libidn2 \
    --with-libssh \
    --with-libmetalink \
    --enable-hidden-symbols \
    --disable-static \
    --enable-threaded-resolver

# if this fails, the above sed hack did not work
./libtool --config | grep -q link_all_deplibs=no
# enable-hidden-symbols needs gcc4 and causes that curl exports only its API
make %{?_smp_mflags} V=1

%if %{with testsuite}
%check
pushd tests
make %{?_smp_mflags} V=1
# make sure the testsuite runs don't race on MP machines in autobuild
if test -z "$BUILD_INCARNATION" -a -r /.buildenv; then
	. /.buildenv
fi
if test -z "$BUILD_INCARNATION"; then
	BUILD_INCARNATION=0
fi

base=$((8990 + $BUILD_INCARNATION * 20))
# bug940009 do not run flaky tests for any architecture
# at least test 1510 do fail for i586 and ppc64le
perl ./runtests.pl -a -v -p -b$base '!flaky' || exit

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
%doc docs/{BUGS.md,FAQ,FEATURES,TODO,TheArtOfHttpScripting.md}
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
