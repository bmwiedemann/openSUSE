#
# spec file for package varnish
#
# Copyright (c) 2025 SUSE LLC
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


%define library_name libvarnishapi3
%define pkg_home     %_localstatedir/lib/%name
%define pkg_logdir   %_localstatedir/log/%name
%define pkg_cachedir %_localstatedir/cache/%name
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if !0%{?_fillupdir:1}
%define _fillupdir %_localstatedir/adm/fillup-templates
%endif
Name:           varnish
Version:        7.7.1
Release:        0
Summary:        Accelerator for HTTP services
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://varnish-cache.org/
#Git-Web:	https://github.com/varnishcache/varnish-cache
Source:         https://varnish-cache.org/_downloads/%name-%version.tgz
Source3:        varnish.sysconfig
Source5:        varnish.logrotate
Source7:        varnish.service
Source8:        varnishlog.service
Source9:        varnish_reload_vcl
Patch2:         uninit.patch
BuildRequires:  libxslt-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-docutils
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xz
BuildRequires:  pkgconfig(libpcre2-8)
Requires:       c_compiler
%sysusers_requires
Recommends:     logrotate
%{?systemd_ordering}

%description
Varnish is an HTTP accelerator. Often called Reverse Proxy, it is an
application that stores (caches) documents that have been requested
over the HTTP protocol.

Based on certain criteria, the next client requesting the document is either
given the cached document, or a "fresh" document requested from a backend
server. The purpose of this is to minimize the requests going to the backend
server(s) by serving the same document to potentially many users.

%package -n %library_name
Summary:        Shared libraries for Varnish
Group:          Productivity/Networking/Web/Proxy

%description -n %library_name
Varnish is an HTTP accelerator. Often called Reverse Proxy, it is an
application that stores (caches) documents that have been requested
over the HTTP protocol.

Based on certain criteria, the next client requesting the document is either
given the cached document, or a "fresh" document requested from a backend
server. The purpose of this is to minimize the requests going to the backend
server(s) by serving the same document to potentially many users.

This package holds the shared libraries for varnish.

%package devel
Summary:        Development files for Varnish
Group:          Development/Libraries/C and C++
Requires:       %name = %version

%description devel
Varnish is an HTTP accelerator. Often called Reverse Proxy, it is an
application that stores (caches) documents that have been requested
over the HTTP protocol.

This package holds the development files for varnish.

%prep
%autosetup -p1

%build
%define _lto_cflags %nil
export CFLAGS="%optflags -fcommon -fstack-protector"
%ifarch %ix86
export CFLAGS="$CFLAGS -ffloat-store -fexcess-precision=standard"
%endif
%configure --disable-static --docdir="%_docdir/%name" \
           --localstatedir="%_localstatedir/cache/"
%make_build V=1

%install
b="%buildroot"
%make_install
# There is no use for them to normal users
mv "$b/%_bindir"/* "$b/%_sbindir/"
#
##missing directories
install -dm 0755 "$b"/{%pkg_logdir,%pkg_home}
install -Dpm 0644 "%SOURCE5" "$b/%_sysconfdir/logrotate.d/varnish"
#
##init scripts
install -Dpm 0644 "%SOURCE3" "$b/%_fillupdir/sysconfig.%name"
install -Dpm 0644 "%SOURCE7" "$b/%_unitdir/varnish.service"
install -Dpm 0644 "%SOURCE8" "$b/%_unitdir/varnishlog.service"
mkdir -p "$b/%_sbindir"
ln -s service "$b/%_sbindir/rcvarnish"
ln -s service "$b/%_sbindir/rcvarnishlog"
install -Dpm 0755 "%SOURCE9" "$b/%_sbindir/varnish_reload_vcl"
#
##config files
mkdir -p "$b/%_sysconfdir/%name"
cp "$b/%_docdir/%name/example.vcl" "$b/%_sysconfdir/%name/vcl.conf"

find "$b" -type f -name "*.la" -delete -print
mkdir -p "$b/%pkg_logdir"
mkdir -p "$b/%_docdir/%name"
cp -a doc/changes.rst LICENSE README.rst "$b/%_docdir/%name/"

perl -i -pe 's{^#!/usr/bin/env python}{#!/usr/bin/python}g' \
	"$b/%_datadir/varnish/vmodtool.py" "$b/%_datadir/varnish/vsctool.py"

mkdir -p "$b/%_sysusersdir"
echo 'u varnish - "user for Varnish" %pkg_home' >system-user-varnish.conf
cp -a system-user-varnish.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-varnish.conf random system-user-varnish.conf

%check
if ! %make_build check; then
	x="$?"
	cat bin/varnishtest/test-suite.log
	exit "$x"
fi

%pre -f random.pre
%service_add_pre varnish.service varnishlog.service

%post
%fillup_only
%service_add_post varnish.service varnishlog.service

%preun
%service_del_preun varnish.service varnishlog.service

%postun
%service_del_postun varnish.service varnishlog.service

%ldconfig_scriptlets -n %library_name

%files
%_unitdir/*.service
%config(noreplace) %_sysconfdir/logrotate.d/varnish
%dir %attr(0750,root,varnish) %_sysconfdir/%name/
%config(noreplace) %attr(0640,root,varnish) %_sysconfdir/%name/vcl.conf
%_libdir/varnish
%_sbindir/varnish*
%_sbindir/rcvarnish*
%_mandir/man*/*
%_docdir/%name/
%_datadir/%name/
%dir %attr(0750,varnish,varnish) %pkg_home
%dir %attr(0750,varnish,varnish) %pkg_cachedir
%dir %attr(0750,varnish,varnish) %pkg_logdir
%_fillupdir/sysconfig.%name
%_sysusersdir/*

%files -n %library_name
%_libdir/libvarnishapi.so.3*

%files devel
%_includedir/varnish/
%_datadir/aclocal/
%_libdir/pkgconfig/*
%_libdir/libvarnishapi.so

%changelog
