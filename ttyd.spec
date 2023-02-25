#
# spec file for package ttyd
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2017-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           ttyd
Version:        1.7.3
Release:        0
Summary:        Share your terminal over the web
License:        MIT
Group:          System/Monitoring
URL:            https://tsl0922.github.io/ttyd/
#Git-Clone:     https://github.com/tsl0922/ttyd.git
Source:         https://github.com/tsl0922/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
# required vim for xxd
BuildRequires:  vim
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libwebsockets)
BuildRequires:  pkgconfig(zlib)

%description
Ttyd is a simple command-line tool for sharing terminal over the web, inspired
by GoTTY.

Features include:
 * Built on top of Libwebsockets with C for speed
 * Fully-featured terminal based on Xterm.js with CJK and IME support
 * SSL support based on OpenSSL
 * Run any custom command with options
 * Basic authentication support and many other custom options
 * Cross platform: macOS, Linux, FreeBSD, OpenWrt/LEDE, Windows

%prep
%setup -q

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install

%files
%doc LICENSE README.md
%{_bindir}/ttyd
%{_mandir}/man1/ttyd.1%{ext_man}

%changelog
