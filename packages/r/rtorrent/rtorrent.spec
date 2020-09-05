#
# spec file for package rtorrent
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rtorrent
Version:        0.9.8
Release:        0
Summary:        Console-based BitTorrent Client
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/rakshasa/rtorrent

Source:         https://github.com/rakshasa/rtorrent/releases/download/v%version/%name-%version.tar.gz
Source2:        rtorrent.desktop
# This manpage copied from the 0.9.2 tarball as it was missing in later versions
Source3:        rtorrent.1
Source4:        rtorrent.service
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cppunit) >= 1.9.6
BuildRequires:  pkgconfig(libcurl) >= 7.15.4
BuildRequires:  pkgconfig(libtorrent) >= 0.13.8
BuildRequires:  pkgconfig(xmlrpc)
Requires(pre):  shadow

%description
rTorrent is a console-based BitTorrent client. It aims to be a
fully-featured and efficient client with the ability to run in the
background using screen. It supports fast-resume and session
management.

%prep
%setup -q

%build
# It's full of type pun violations
export CFLAGS="%optflags -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
export CXXFLAGS="$CXXFLAGS -std=gnu++11"
autoreconf -fiv
%configure \
	--with-xmlrpc-c="%_bindir/xmlrpc-c-config" \
	--enable-ipv6
%make_build

%install
b="%buildroot"
%make_install
install -Dm0644 "%{S:2}" "$b/%_datadir/applications/%name.desktop"
mkdir -p "$b/%_mandir/man1"
install -pm0644 "%{S:3}" "$b/%_mandir/man1/"
%suse_update_desktop_file -r "%name" Network P2P
install -Dm0644 "%{S:4}" "$b/%_unitdir/rtorrent.service"

%pre
getent passwd rtorrent >/dev/null || useradd -r rtorrent
%service_add_pre rtorrent.service

%post
%service_add_post rtorrent.service

%preun
%service_del_preun rtorrent.service

%postun
%service_del_postun rtorrent.service

%files
%doc doc/rtorrent.rc
%license COPYING
%_bindir/rtorrent
%_datadir/applications/%name.desktop
%_mandir/man1/rtorrent.1*
%_unitdir/rtorrent.service

%changelog
