#
# spec file for package darkhttpd
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


%define pkg_home %{_localstatedir}/lib/%{name}
Name:           darkhttpd
Version:        1.15
Release:        0
Summary:        When you need a web server in a hurry
License:        ISC
Group:          Productivity/Networking/Web/Servers
URL:            https://unix4lyfe.org/darkhttpd
Source:         https://github.com/emikulic/darkhttpd/archive/v%{version}.tar.gz
Source1:        %{name}.sysconfig
Source2:        %{name}.service
BuildRequires:  gcc
BuildRequires:  make
Requires(post): %fillup_prereq
Provides:       http_daemon
Provides:       httpd

%description
Features:
    Simple to set up:
        Single binary, no other files, no installation needed.
        Standalone, doesn't need inetd or ucspi-tcp.
        No messing around with config files - all you have to specify is the www root.
    Written in C - efficient and portable.
    Small memory footprint.
    Event loop, single threaded - no fork() or pthreads.
    Generates directory listings.
    Supports HTTP GET and HEAD requests.
    Supports Range / partial content. (try streaming music files or resuming a download)
    Supports If-Modified-Since.
    Supports Keep-Alive connections.
    Supports IPv6.
    Can serve 301 redirects based on Host header.
    Uses sendfile() on FreeBSD, Solaris and Linux.
    Can use acceptfilter on FreeBSD.
    At some point worked on FreeBSD, Linux, OpenBSD, Solaris.
    ISC license.
    suckless.org says darkhttpd sucks less.
    Small Docker image (<100KB)

Security:
    Can log accesses, including Referer and User-Agent.
    Can chroot.
    Can drop privileges.
    Impervious to /../ sniffing.
    Times out idle connections.
    Drops overly long requests.

Limitations:
    Only serves static content - no CGI.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
%make_build

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/system/%{name}.service
mkdir -p %{buildroot}%{_sbindir}
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%{_sbindir}/groupadd -r %{name} >/dev/null 2>&1 ||:
%{_sbindir}/useradd  -g %{name} -s %{_sbindir}/nologin -r -c "user for %{name}" -d %{pkg_home} %{name} >/dev/null 2>&1 ||:
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only -n darkhttpd}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license COPYING
%{_fillupdir}/sysconfig.%{name}
%{_prefix}/lib/systemd/system/%{name}.service
%{_bindir}/%{name}
%{_sbindir}/rcdarkhttpd

%changelog
