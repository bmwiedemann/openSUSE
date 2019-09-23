#
# spec file for package links
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           links
Version:        2.20.1
Release:        0
Summary:        Text-Based WWW Browser
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            http://links.twibright.com/
Source:         http://links.twibright.com/download/links-%{version}.tar.bz2
Patch2:         configure.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gpm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires: 	pkgconfig(libzstd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
Provides:       web_browser

%description
Links is like Lynx--an easy-to-use browser for HTML documents and other
Internet services, like FTP, telnet, and news. Links provides a
graphical interface besides the text interface. It has good support for
frames, supports ssl, and has a little bit of JavaScript support.

%prep
%setup -q
%patch2 -p1

%build
autoreconf -ifv
CFLAGS="%{optflags} -DOPENSSL_NO_SSL_INTERN"
%configure \
        --with-ipv6 \
        --with-zlib \
        --with-bzip2 \
        --with-lzma \
        --with-fb \
        --without-directfb \
        --with-libjpeg \
        --with-libtiff \
        --with-ssl \
        --with-x \
        --enable-graphics
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc README NEWS ChangeLog BRAILLE_HOWTO AUTHORS KEYS SITES
%doc doc/links_cal
%{_bindir}/links
%{_mandir}/man1/links.1%{?ext_man}

%changelog
