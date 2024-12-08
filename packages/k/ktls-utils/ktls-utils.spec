#
# spec file for package ktls-utils
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


Name:           ktls-utils
Version:        0.10+33.g311d943
Release:        0
Summary:        Agent for performing handshakes for kernel TLS sockets
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/oracle/ktls-utils
Source:         ktls-utils-%{version}.tar
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(glib-2.0) >= 2.6
BuildRequires:  pkgconfig(gnutls) >= 3.3.0
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1
BuildRequires:  pkgconfig(systemd)

%description
In-kernel TLS consumers need a mechanism to perform TLS handshakes on a
connected socket to negotiate TLS session parameters that can then be
programmed into the kernel's TLS record protocol engine.

This package of software provides a TLS handshake user agent that listens for
kernel requests and then materializes a user space socket endpoint on which to
perform these handshakes. The resulting negotiated session parameters are
passed back to the kernel via standard kTLS socket options.

%prep
%setup -q -n ktls-utils-%{version}

%build
./autogen.sh
%{configure} --with-systemd
%{make_build} CFLAGS="%{optflags}"

%install
%{make_install}

%pre
%service_add_pre tlshd.service

%post
%service_add_post tlshd.service

%preun
%service_del_preun tlshd.service

%postun
%service_del_postun tlshd.service

%files
%doc README.md
%license LICENSE.txt
%{_sbindir}/tlshd
%{_unitdir}/tlshd.service
%config(noreplace) %{_sysconfdir}/tlshd.conf
%{_mandir}/man8/tlshd.8*
%{_mandir}/man5/tlshd.conf.5*

%changelog
