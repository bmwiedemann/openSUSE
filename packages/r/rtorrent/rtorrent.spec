#
# spec file for package rtorrent
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           rtorrent
Version:        0.16.5
Release:        0
Summary:        Console-based BitTorrent client
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/rakshasa/rtorrent
Source:         https://github.com/rakshasa/rtorrent/releases/download/v%version/%name-%version.tar.gz
Source2:        rtorrent.desktop
# This manpage copied from the 0.9.2 tarball as it was missing in later versions
Source3:        rtorrent.1
Source4:        rtorrent.service
BuildRequires:  autoconf-archive
BuildRequires:  automake
%if 0%{?suse_version} && 0%{?suse_version} < 1600
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  sysuser-tools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cppunit) >= 1.9.6
BuildRequires:  pkgconfig(libtorrent) >= %version
Provides:       bundled(tinyxml2) = 10.0.0
%sysusers_requires

%description
rTorrent is a text-based BitTorrent client written in C++ and with
ncurses. It supports fast resume and session management, and can be
run in the background with the help of e.g. GNU screen.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1600
export CXX=g++-13
%endif
# It's full of type pun violations
export CFLAGS="%optflags -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
autoreconf -fiv
%configure --with-xmlrpc-tinyxml2 --enable-ipv6
%make_build

%install
b="%buildroot"
%make_install
install -Dm0644 "%{S:2}" "$b/%_datadir/applications/%name.desktop"
mkdir -p "$b/%_mandir/man1"
install -pm0644 "%{S:3}" "$b/%_mandir/man1/"
%suse_update_desktop_file -r "%name" Network P2P
install -Dm0644 "%{S:4}" "$b/%_unitdir/rtorrent.service"

echo 'u rtorrent - "rtorrent daemon"' >system-user-rtorrent.conf
mkdir -p "$b/%_sysusersdir"
cp -a system-user-rtorrent.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-rtorrent.conf random system-user-rtorrent.conf

%pre -f random.pre
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
%_datadir/%name/
%_mandir/man1/rtorrent.1*
%_unitdir/rtorrent.service
%_sysusersdir/*

%changelog
