#
# spec file for package curl
#
# Copyright (c) 2024 SUSE LLC
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
# need ssl always for python-pycurl
%bcond_without openssl
%define target @BUILD_FLAVOR@%{nil}
%if "%{target}" == "mini"
%bcond_without mini
%global psuffix -mini
%else
%bcond_with mini
%global psuffix %{nil}
%endif

Name:           curl%{?psuffix}
Version:        8.8.0
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
#PATCH-FIX-UPSTREAM Fix make install for curl-config.1 github.com/curl/curl/pull/13741
Patch4:         curl-make-install-curl-config.patch
BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libidn2)
# Disable metalink [bsc#1188218, CVE-2021-22923][bsc#1188217, CVE-2021-22922]
# BuildRequires:  pkgconfig(libmetalink)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Requires:       libcurl4 = %{version}
%if %{with openssl}
BuildRequires:  pkgconfig(libssl)
%endif
%if !%{with mini}
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libssh)
%endif
%if 0%{?_with_stunnel:1}
# used by the testsuite
BuildRequires:  stunnel
%endif

%description
Curl is a client to get documents and files from or send documents to a
server using any of the supported protocols (HTTP, HTTPS, FTP, FTPS,
TFTP, DICT, TELNET, LDAP, or FILE). The command is designed to work
without user interaction or any kind of interactivity.

%package -n libcurl%{?psuffix}4
Summary:        Library for transferring data from URLs
%if %{with mini}
Provides:       libcurl4 = %{version}
%else
Obsoletes:      libcurl-mini4 <= %{version}
%endif

%description -n libcurl%{?psuffix}4
The cURL shared library for accessing data using different
network protocols.

%if !%{with mini}
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

%package -n libcurl-devel-doc
Summary:        Manual pages for libcurl
Provides:       libcurl-devel:%{_mandir}/man1/curl-config.1%{?ext_man}
BuildArch:      noarch

%description -n libcurl-devel-doc
Manual pages for the libcurl C API.

%package        fish-completion
Summary:        Fish completion for curl
Group:          System/Shells
Requires:       fish
Supplements:    (curl and fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %name.

%package        zsh-completion
Summary:        Zsh Completion for %name
Group:          System/Shells
Requires:       zsh
Supplements:    (curl and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %name.
%endif

%prep
%autosetup -p1 -n curl-%{version}

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
    --enable-hsts \
    --enable-ipv6 \
%if %{with openssl}
    --with-openssl \
    --with-ca-fallback \
    --without-ca-path \
    --without-ca-bundle \
%else
    --without-openssl \
%endif
    --with-libidn2 \
    --with-nghttp2 \
    --enable-docs \
%if %{with mini}
    --disable-dict \
    --disable-ftp \
    --disable-gopher \
    --disable-imap \
    --disable-mqtt \
    --disable-ntlm \
    --disable-ntlm-wb \
    --disable-pop3 \
    --disable-rtsp \
    --disable-smtp \
    --disable-telnet \
    --disable-tftp \
    --disable-tls-srp \
    --disable-websockets \
    --without-brotli \
    --without-libssh \
%else
    --with-gssapi=$(krb5-config --prefix) \
    --with-brotli \
    --with-libssh \
%endif
    --enable-symbol-hiding \
    --disable-static \
    --enable-threaded-resolver \
    --with-zsh-functions-dir=%{_datadir}/zsh/site-functions/ \
    --with-fish-functions-dir=%{_datadir}/fish/vendor_completions.d

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
%if %{with mini}
rm -rv %{buildroot}%{_includedir}/curl %{buildroot}/%{_libdir}/pkgconfig %{buildroot}%{_datadir}
rm -v %{buildroot}%{_bindir}/curl %{buildroot}%{_bindir}/curl-config %{buildroot}%{_libdir}/libcurl.so
%else
install -Dm 0644 docs/libcurl/libcurl.m4 %{buildroot}%{_datadir}/aclocal/libcurl.m4
pushd scripts
%make_install
popd
%endif

%ldconfig_scriptlets -n libcurl%{?psuffix}4

%files -n libcurl%{?psuffix}4
%license COPYING
%{_libdir}/libcurl.so.4*

%if !%{with mini}
%files
%doc README RELEASE-NOTES CHANGES
%doc docs/{BUGS.md,FAQ,FEATURES.md,TODO,TheArtOfHttpScripting.md}
%{_bindir}/curl
%{_mandir}/man1/curl.1%{?ext_man}

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_curl

%files fish-completion
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/curl.fish

%files -n libcurl-devel
%{_bindir}/curl-config
%{_includedir}/curl
%dir %{_datadir}/aclocal/
%{_datadir}/aclocal/libcurl.m4
%{_libdir}/libcurl.so
%{_libdir}/pkgconfig/libcurl.pc

%files -n libcurl-devel-doc
%{_mandir}/man1/curl-config.1%{?ext_man}
%{_mandir}/man3/*
%doc docs/libcurl/symbols-in-versions
%endif

%changelog
