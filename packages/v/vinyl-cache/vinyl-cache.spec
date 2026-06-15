#
# spec file for package vinyl-cache
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define library_name libvinylapi3
%define pkg_home     %_localstatedir/lib/%name
%define pkg_logdir   %_localstatedir/log/%name
%define pkg_cachedir %_localstatedir/cache/%name
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if !0%{?_fillupdir:1}
%define _fillupdir %_localstatedir/adm/fillup-templates
%endif
Name:           vinyl-cache
Version:        9.0.1
Release:        0
Summary:        Accelerator for HTTP services
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://vinyl-cache.org/
#Git-Clone:	https://code.vinyl-cache.org/vinyl-cache/vinyl-cache
Source:         https://vinyl-cache.org/downloads/%name-%version.tgz
Source3:        vinyl-cache.sysconfig
Source5:        vinyl-cache.logrotate
Source7:        vinyl-cache.service
Source8:        vinyl-cachelog.service
Source9:        vinyl-cache_reload_vcl
Patch1:         0001-Fix-DESTDIR-builds.patch
Patch2:         uninit.patch
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libxslt-devel
BuildRequires:  netcfg
BuildRequires:  ncurses-devel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-docutils
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xz
BuildRequires:  pkgconfig(libpcre2-8)
# Manpage file vmod_cookie.3.gz is offered by both varnish-8 and vinyl-9
Conflicts:      varnish
Requires:       c_compiler
%sysusers_requires
Recommends:     logrotate
%{?systemd_ordering}

%description
Vinyl Cache is an HTTP accelerator. Often called Reverse Proxy, it is an
application that stores (caches) documents that have been requested
over the HTTP protocol.

Based on certain criteria, the next client requesting the document is
either given the cached document, or a "fresh" document requested
from a backend server. The purpose of this is to minimize the
requests going to the backend server(s) by serving the same document
to potentially many users.

%package -n %library_name
Summary:        Shared libraries for Vinyl Cache
Group:          Productivity/Networking/Web/Proxy

%description -n %library_name
Vinyl Cache is an HTTP accelerator. Often called Reverse Proxy, it is
an application that stores (caches) documents that have been
requested over the HTTP protocol.

Based on certain criteria, the next client requesting the document is
either given the cached document, or a "fresh" document requested
from a backend server. The purpose of this is to minimize the
requests going to the backend server(s) by serving the same document
to potentially many users.

This package holds the shared libraries for Vinyl Cache.

%package devel
Summary:        Development files for Vinyl Cache
Group:          Development/Libraries/C and C++
Requires:       %name = %version

%description devel
Vinyl Cache is an HTTP accelerator. Often called Reverse Proxy, it is
an application that stores (caches) documents that have been
requested over the HTTP protocol.

This package holds the development files for vinyl-cache.

%prep
%autosetup -p1

%build
%define _lto_cflags %nil
export CFLAGS="%optflags -fcommon -fstack-protector"
%ifarch %ix86
export CFLAGS="$CFLAGS -ffloat-store -fexcess-precision=standard"
%endif
autoreconf -fiv
%configure --disable-static --docdir="%_docdir/%name"
%make_build V=1

%install
b="%buildroot"
%make_install
# There is no use for them to normal users
mv "$b/%_bindir"/* "$b/%_sbindir/"
#
##missing directories
install -dm 0755 "$b"/{%pkg_logdir,%pkg_home}
install -Dpm 0644 "%SOURCE5" "$b/%_sysconfdir/logrotate.d/vinyl-cache"
#
##init scripts
install -Dpm 0644 "%SOURCE3" "$b/%_fillupdir/sysconfig.%name"
install -Dpm 0644 "%SOURCE7" "$b/%_unitdir/vinyl-cache.service"
install -Dpm 0644 "%SOURCE8" "$b/%_unitdir/vinyl-cachelog.service"
install -Dpm 0755 "%SOURCE9" "$b/%_sbindir/vinyl-cache_reload_vcl"
#
##config files
mkdir -p "$b/%_sysconfdir/%name"
cp "$b/%_docdir/%name/example.vcl" "$b/%_sysconfdir/%name/vcl.conf"

find "$b" -type f -name "*.la" -delete -print
mkdir -p "$b/%pkg_logdir" "$b/%_docdir/%name" "$b/%pkg_cachedir" "$b/%_sysusersdir"
cp -a doc/changes.rst LICENSE README.md "$b/%_docdir/%name/"

perl -i -pe 's{^#!/usr/bin/env python}{#!/usr/bin/python}g' \
	"$b/%_datadir/vinyl-cache/vmodtool.py" "$b/%_datadir/vinyl-cache/vsctool.py"
echo 'u vinyl-cache - "user for Vinyl Cache" %pkg_home' >system-user-vinyl-cache.conf
cp -a system-user-vinyl-cache.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-vinyl-cache.conf random system-user-vinyl-cache.conf

%check
# This needs a sensible (/usr)/etc/services [netcfg package]
if ! %make_build check; then
	x="$?"
	cat bin/vinyl-cachetest/test-suite.log
	#exit "$x"
fi

%pre -f random.pre
%service_add_pre vinyl-cache.service vinyl-cachelog.service

%post
%fillup_only
%service_add_post vinyl-cache.service vinyl-cachelog.service

%preun
%service_del_preun vinyl-cache.service vinyl-cachelog.service

%postun
%service_del_postun vinyl-cache.service vinyl-cachelog.service

%ldconfig_scriptlets -n %library_name

%files
%_unitdir/*.service
%config(noreplace) %_sysconfdir/logrotate.d/vinyl-cache
%dir %attr(0750,root,vinyl-cache) %_sysconfdir/%name/
%config(noreplace) %attr(0640,root,vinyl-cache) %_sysconfdir/%name/vcl.conf
%_libdir/vinyl-cache
%_sbindir/vinyl*
%_sbindir/vtest
%_mandir/man*/*
%_docdir/%name/
%_datadir/%name/
%dir %attr(0750,vinyl-cache,vinyl-cache) %pkg_home
%dir %attr(0750,vinyl-cache,vinyl-cache) %pkg_cachedir
%dir %attr(0750,vinyl-cache,vinyl-cache) %pkg_logdir
%_fillupdir/sysconfig.%name
%_sysusersdir/*

%files -n %library_name
%_libdir/libvinylapi.so.*

%files devel
%_includedir/vinyl-cache/
%_datadir/aclocal/
%_libdir/pkgconfig/*
%_libdir/libvinylapi.so

%changelog
